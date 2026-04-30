import argparse
import base64
import json
import os
import sys
from pathlib import Path
from urllib import error, parse, request


DEFAULT_MODEL = "eleven_multilingual_v2"
DEFAULT_OUTPUT_FORMAT = "mp3_44100_128"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate ElevenLabs narration and convert timestamp alignment into word timings."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text", help="Narration text.")
    source.add_argument("--text-file", help="Path to a UTF-8 text file.")
    parser.add_argument(
        "--env-file",
        default=r"C:\Users\mario\Desktop\Creator Canon Social Content\.env",
        help="Path to .env file.",
    )
    parser.add_argument("--api-key-env", default="ELEVENLABS_API_KEY")
    parser.add_argument("--voice-id-env", default="ELEVENLABS_VOICE_ID")
    parser.add_argument("--api-key", help="ElevenLabs API key. Prefer .env/env var.")
    parser.add_argument("--voice-id", help="ElevenLabs voice id. Prefer .env/env var.")
    parser.add_argument("--model-id", default=DEFAULT_MODEL)
    parser.add_argument("--output-format", default=DEFAULT_OUTPUT_FORMAT)
    parser.add_argument("--stability", type=float, default=0.45)
    parser.add_argument("--similarity-boost", type=float, default=0.85)
    parser.add_argument("--style", type=float)
    parser.add_argument("--speaker-boost", action="store_true", default=True)
    parser.add_argument("--no-speaker-boost", dest="speaker_boost", action="store_false")
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--write-media", required=True, help="Output audio path.")
    parser.add_argument("--write-words", required=True, help="Output word JSON path.")
    parser.add_argument("--write-manifest", help="Optional output manifest JSON path.")
    parser.add_argument("--write-alignment", help="Optional raw alignment JSON path.")
    return parser.parse_args()


def find_env_file(path):
    env_path = Path(path)
    if env_path.is_absolute() or env_path.exists():
        return env_path if env_path.exists() else None

    for folder in (Path.cwd(), *Path.cwd().parents):
        candidate = folder / env_path
        if candidate.exists():
            return candidate

    return None


def load_env_file(path):
    env_path = find_env_file(path)
    if not env_path:
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def resolve_secret(cli_value, env_name, label):
    value = cli_value or os.environ.get(env_name)
    if not value:
        raise SystemExit(
            f"Missing {label}. Set {env_name} in .env/environment or pass the matching CLI flag."
        )
    return value


def build_payload(text, args):
    voice_settings = {
        "stability": args.stability,
        "similarity_boost": args.similarity_boost,
        "use_speaker_boost": args.speaker_boost,
    }
    if args.style is not None:
        voice_settings["style"] = args.style

    return {
        "text": text,
        "model_id": args.model_id,
        "voice_settings": voice_settings,
    }


def post_elevenlabs_timestamps(api_key, voice_id, payload, output_format):
    query = parse.urlencode({"output_format": output_format})
    url = (
        f"https://api.elevenlabs.io/v1/text-to-speech/"
        f"{parse.quote(voice_id)}/with-timestamps?{query}"
    )
    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "xi-api-key": api_key,
        },
    )

    try:
        with request.urlopen(req, timeout=120) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(
            f"ElevenLabs request failed with HTTP {exc.code}: {details}"
        ) from exc


def get_alignment(response):
    alignment = response.get("normalized_alignment") or response.get("alignment")
    if not alignment:
        raise SystemExit("ElevenLabs response did not include timestamp alignment.")

    chars = alignment.get("characters") or []
    starts = alignment.get("character_start_times_seconds") or []
    ends = alignment.get("character_end_times_seconds") or []

    if not chars or len(chars) != len(starts) or len(chars) != len(ends):
        raise SystemExit("ElevenLabs alignment arrays are missing or have mismatched lengths.")

    return chars, starts, ends


def alignment_to_words(chars, starts, ends, fps):
    words = []
    active_chars = []
    active_start = None
    active_end = None

    def flush():
        nonlocal active_chars, active_start, active_end
        text = "".join(active_chars).strip()
        if text and active_start is not None and active_end is not None:
            words.append(
                {
                    "text": text,
                    "start": active_start,
                    "end": active_end,
                    "from": round(active_start * fps),
                    "to": max(round(active_end * fps), round(active_start * fps) + 1),
                }
            )
        active_chars = []
        active_start = None
        active_end = None

    for char, start, end in zip(chars, starts, ends):
        if char.isspace():
            flush()
            continue

        if active_start is None:
            active_start = start
        active_end = end
        active_chars.append(char)

    flush()
    return words


def main():
    args = parse_args()
    load_env_file(args.env_file)

    text = args.text
    if args.text_file:
        text = Path(args.text_file).read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("No narration text provided.")

    api_key = resolve_secret(args.api_key, args.api_key_env, "ElevenLabs API key")
    voice_id = resolve_secret(args.voice_id, args.voice_id_env, "ElevenLabs voice id")

    payload = build_payload(text, args)
    response = post_elevenlabs_timestamps(
        api_key=api_key,
        voice_id=voice_id,
        payload=payload,
        output_format=args.output_format,
    )

    audio_base64 = response.get("audio_base64")
    if not audio_base64:
        raise SystemExit("ElevenLabs response did not include audio_base64.")

    media_path = Path(args.write_media)
    words_path = Path(args.write_words)
    media_path.parent.mkdir(parents=True, exist_ok=True)
    words_path.parent.mkdir(parents=True, exist_ok=True)

    media_path.write_bytes(base64.b64decode(audio_base64))

    chars, starts, ends = get_alignment(response)
    words = alignment_to_words(chars, starts, ends, args.fps)
    words_path.write_text(json.dumps(words, indent=2), encoding="utf-8")

    if args.write_alignment:
        alignment_path = Path(args.write_alignment)
        alignment_path.parent.mkdir(parents=True, exist_ok=True)
        alignment_path.write_text(
            json.dumps(
                {
                    "normalized_alignment": response.get("normalized_alignment"),
                    "alignment": response.get("alignment"),
                },
                indent=2,
            ),
            encoding="utf-8",
        )

    if args.write_manifest:
        manifest_path = Path(args.write_manifest)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        duration = max((word["end"] for word in words), default=0)
        manifest = {
            "provider": "elevenlabs",
            "voiceIdEnv": args.voice_id_env,
            "modelId": args.model_id,
            "audio": str(media_path).replace("\\", "/"),
            "fps": args.fps,
            "duration": duration,
            "totalFrames": round(duration * args.fps),
            "words": words,
        }
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(
        json.dumps(
            {
                "provider": "elevenlabs",
                "audio": str(media_path),
                "words": str(words_path),
                "manifest": args.write_manifest,
                "wordCount": len(words),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
