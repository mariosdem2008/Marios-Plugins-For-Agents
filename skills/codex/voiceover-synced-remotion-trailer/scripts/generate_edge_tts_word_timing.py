import argparse
import asyncio
import json
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate Edge TTS narration and exact word-boundary timing."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text", help="Narration text.")
    source.add_argument("--text-file", help="Path to a UTF-8 text file.")
    parser.add_argument("--voice", default="en-US-AndrewNeural")
    parser.add_argument("--rate", default="+0%")
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--write-media", required=True, help="Output audio path.")
    parser.add_argument("--write-words", required=True, help="Output word JSON path.")
    parser.add_argument("--write-manifest", help="Optional output manifest JSON path.")
    return parser.parse_args()


async def main():
    args = parse_args()

    try:
        import edge_tts
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: edge-tts. Install with `python -m pip install edge-tts`."
        ) from exc

    text = args.text
    if args.text_file:
        text = Path(args.text_file).read_text(encoding="utf-8")

    media_path = Path(args.write_media)
    words_path = Path(args.write_words)
    media_path.parent.mkdir(parents=True, exist_ok=True)
    words_path.parent.mkdir(parents=True, exist_ok=True)

    communicate = edge_tts.Communicate(
        text,
        args.voice,
        rate=args.rate,
        boundary="WordBoundary",
    )
    words = []

    with media_path.open("wb") as media:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                media.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / 10_000_000
                duration = chunk["duration"] / 10_000_000
                end = start + duration
                words.append(
                    {
                        "text": chunk["text"],
                        "start": start,
                        "end": end,
                        "from": round(start * args.fps),
                        "to": round(end * args.fps),
                    }
                )

    words_path.write_text(json.dumps(words, indent=2), encoding="utf-8")

    if args.write_manifest:
        manifest_path = Path(args.write_manifest)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        duration = max((word["end"] for word in words), default=0)
        manifest = {
            "audio": str(media_path).replace("\\", "/"),
            "fps": args.fps,
            "duration": duration,
            "totalFrames": round(duration * args.fps),
            "words": words,
        }
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")


if __name__ == "__main__":
    asyncio.run(main())
