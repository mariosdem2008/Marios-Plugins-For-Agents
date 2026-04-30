---
name: voiceover-synced-remotion-youtube-video
description: Build or revise long-form horizontal YouTube videos in Remotion from scripts, narration, audio, transcripts, timing manifests, and visual references. Use when Codex needs to generate or import voiceover, extract exact word/phrase timings, create 16:9 chaptered YouTube explainers, video essays, authority videos, or animated educational videos, synchronize visuals and captions to spoken words, use the official CreatorCanon logo from universal assets, render the final MP4, and verify timing, audio, pacing, and visual quality.
---

# Voiceover-Synced Remotion YouTube Video

## Core Rule

Treat the final voiceover as the edit timeline. Do not build a YouTube video from guessed scene durations when narration audio exists or can be generated.

Every meaningful visual decision should answer: "Which spoken phrase, chapter beat, or key word causes this to appear?"

## Long-Form YouTube Defaults

Use these defaults unless the user gives different specs:

- Format: horizontal 16:9 YouTube video.
- Composition: 1920x1080, 30 fps.
- Default length: 6-9 minutes when the script allows it.
- Extended length: 9-12 minutes for deeper breakdowns.
- Tutorial length: 10-15 minutes only when requested.
- Avoid vertical 9:16 reel composition unless the user explicitly asks for Shorts.
- Build around chapters, sections, proof beats, diagrams, and visual explanations rather than rapid reel-style scene churn.

Long-form pacing should feel deliberate, watchable, and premium. Use motion to support comprehension, not to create constant interruption.

## CreatorCanon Defaults

For CreatorCanon YouTube videos, apply these defaults unless the user explicitly provides a different audio file, voice, background, or brand system:

- Generate narration with ElevenLabs using `ELEVENLABS_API_KEY` and `ELEVENLABS_VOICE_ID` from `C:\Users\mario\Desktop\Creator Canon Social Content\.env` whenever those variables exist. Do not print or expose secret values.
- If ElevenLabs credentials are missing and the user still wants generated narration, fall back to Edge TTS voice `en-US-AndrewNeural`.
- Search `C:\Users\mario\Desktop\Creator Canon Social Content\universal assets\` recursively for reusable assets. Copy or reference relevant assets as needed, but do not move or delete originals.
- Always use the official CreatorCanon logo from `C:\Users\mario\Desktop\Creator Canon Social Content\universal assets\`. Prefer `creatorcanon_logo_transparent.svg`; fall back to `creatorcanon_logo_transparent.png` if the SVG cannot be used; use `creatorcanon_logo_secondary.png` only when that variant is clearly the better fit. Do not generate, redraw, trace, typeset, approximate, recolor, or recreate the CreatorCanon logo. If no official logo asset is available, report the blocker instead of rendering a recreated logo.
- Include the official logo asset in CreatorCanon YouTube videos, normally in the intro signature, final CTA/end frame, channel/package mockup when relevant, and any explicit brand moment. Preserve its aspect ratio and use scale/position/opacity only; do not distort it or rebuild it as text.
- Treat `C:\Users\mario\Desktop\Creator Canon Social Content\Brand Guidelines.md` as the CreatorCanon visual source of truth. Read it before styling CreatorCanon videos, prioritizing color system, typography, visual identity, layout/composition, motion style, and do/don't rules.
- Use the current CreatorCanon colors from `Brand Guidelines.md`: default cream editorial surfaces with Paper `#F5F1EA`, Paper Deep `#EFEAE0`, Card White `#FFFFFF`, Canon Ink `#1C1C1E`, Soft Ink `#6B6B70`, Canon Amber `#D97706` for citations/markers, and Canon Sage `#7C9A7E` only for light-mode verified/outcome moments. Use Night `#0B0B0D`, Night Raised `#111114`, Night Surface `#1A1A1D`, Paper on Night `#F4F1EA`, and Insight Purple `#8B5CF6` only for dark cinematic insight beats.
- Preserve the CreatorCanon visual system: warm cream paper backgrounds, ink-black editorial typography, white cards with hairline borders, archive/source/citation motifs, restrained amber structure, sage verified outcomes, and near-black cinematic scenes only for problem, insight, or CTA moments.
- Avoid emerald, electric blue, decay red, neon SaaS palettes, pure black, pure white page backgrounds, and mixing sage with insight purple in one frame.

## YouTube-Specific Creative Direction

Think in sections, not just scenes.

Use a long-form structure such as:

1. Cold open / pattern interrupt
2. ICP identification
3. Big promise
4. Surface problem
5. Deeper diagnosis
6. False solution
7. Strategic reframe
8. New model or framework
9. Practical breakdown
10. Future-state vision
11. Calm CTA

For each section, create a visual system that can evolve over 30-90 seconds:

- archive grids turning into structured maps
- video tiles opening into extracted lessons
- timestamp/citation chips attaching to claims
- search bars, indexes, and knowledge maps
- side-by-side "feed vs system" comparisons
- chapter cards and progress markers
- evidence/source panels
- simple framework diagrams
- productized hub mockups

Do not make the video a sequence of static slides. Rebuild visuals as animated React/CSS/SVG systems that can respond to the narration.

## Workflow

1. Inspect the repo.
   - Detect the package manager and Remotion entry points.
   - Locate scripts, voiceover files, timing manifests, render scripts, visual references, CreatorCanon assets, the official CreatorCanon logo file, `.env`, and brand guidelines.
   - Use existing project patterns before adding new structure.

2. Create or import the final narration first.
   - If the user provides audio, analyze that audio.
   - If the user provides only a script and CreatorCanon ElevenLabs credentials exist, generate narration with `scripts/generate_elevenlabs_word_timing.py --env-file "C:\Users\mario\Desktop\Creator Canon Social Content\.env"`.
   - If ElevenLabs is unavailable, generate narration with `scripts/generate_edge_tts_word_timing.py --voice en-US-AndrewNeural` unless the user requests another voice.
   - Save audio, word timings, and a Remotion-ready manifest.

3. Build the timing model.
   - Convert words into frames at the composition FPS.
   - Group words into semantic phrase beats.
   - Group phrase beats into YouTube sections or chapters.
   - Derive the composition duration from the final audio/timing manifest, not from an estimate.

4. Build a chapter map.
   - Create section ids, title cards, visual goals, key claims, and transition points.
   - Use progress markers or subtle chapter labels where helpful.
   - Put the strongest visual changes at belief-shift moments, not arbitrary intervals.

5. Map visuals to narration.
   - Trigger key components from exact words or phrases.
   - Use phrase-level timing for diagrams, chapter cards, and section transitions.
   - Use word-level timing for emphasis words, citation pings, highlight strokes, and CTA text.
   - Do not place a full sentence, framework, or CTA on screen before the voiceover earns it.

6. Build long-form visual systems.
   - Use Remotion frame math: `useCurrentFrame`, `useVideoConfig`, `interpolate`, `spring`, `Easing`, `Sequence`, `Audio`, `Img`, and `staticFile`.
   - Create reusable components for chapters, captions, citation chips, video tiles, archive grids, search bars, source cards, framework diagrams, and CTA panels.
   - Use the official logo file from universal assets as an image asset in brand/signature components. Do not recreate it as editable text, SVG paths, CSS, generated imagery, or a cropped screenshot.
   - Prefer programmatic UI over screenshots when elements need independent animation.
   - When using image assets, animate camera/crop/mask/parallax and add independent overlays.

7. Add captions intentionally.
   - Long-form YouTube does not need huge kinetic captions on every word.
   - Use bottom subtitles or phrase captions when they improve clarity, accessibility, or retention.
   - Keep captions in the lower safe area with generous margins.
   - Keep a stable caption container so layout does not jump.
   - Highlight only currently spoken or strategically important words.

8. Design transitions for comprehension.
   - Use chapter transitions, camera moves, object carries, masked reveals, card gathers, framework builds, source pings, and match cuts.
   - Avoid repeating fade-out/fade-in across the whole video.
   - Allow calm holds for reading complex visuals, but keep background motion alive.
   - Avoid reel-style jumpiness in diagnostic or explanatory sections.

9. Render and verify.
   - Run typecheck or project validation.
   - Render audit stills at chapter starts, key claim moments, diagram reveals, subtitle states, and the final CTA.
   - Render the MP4.
   - Use `ffprobe` or equivalent to confirm dimensions, fps, duration, frame count, and audio stream.
   - Create a contact sheet from the final MP4 and inspect readability, sync, pacing, scene variety, and safe margins.

## Remotion Implementation Standards

- Register the requested composition id, width, height, fps, and duration exactly.
- Default to `1920x1080`, 30 fps, horizontal YouTube composition.
- Derive `durationInFrames` from the timing manifest or audio duration.
- Include optional audio loading so a render does not crash while audio is temporarily missing.
- Keep all text inside title-safe/action-safe margins.
- Use section-aware components instead of hundreds of disconnected one-off scenes.
- Keep charts, cards, and diagrams readable on desktop, TV, and mobile playback.
- Avoid tiny text. If a source screenshot or archive panel contains small text, crop into a readable region or rebuild it programmatically.
- For CreatorCanon videos, import/copy the official logo from universal assets and render it with `Img`/`staticFile` or the project's established asset pattern. Never recreate the logo with text, SVG paths, CSS, image generation, or screenshots.
- Use motion layers per section: base camera drift, section-level layout movement, and beat-level component triggers.
- Keep final render scripts explicit about output path, codec, composition id, and props.

## Timing Helpers

Use the bundled scripts when narration needs to be generated or aligned:

- `scripts/generate_elevenlabs_word_timing.py`: Generate ElevenLabs narration, word timings, and a manifest from text.
- `scripts/generate_edge_tts_word_timing.py`: Generate Edge TTS narration with word-boundary timings when ElevenLabs is unavailable or inappropriate.

The timing manifest should include:

```ts
type TimedWord = {
  text: string;
  start: number;
  end: number;
  from: number;
  to: number;
};

type TimingManifest = {
  audio: string;
  fps: number;
  duration: number;
  totalFrames: number;
  words: TimedWord[];
};
```

Build helper utilities in the Remotion project when useful:

- `wordAt("archive")`
- `firstWordFrame("CANON")`
- `phraseFrames("structured knowledge")`
- `sectionFrames("strategic-reframe")`
- `delayFromWord("business", -8)`

## Quality Checklist

Before final response, verify:

- Final narration audio exists or the render intentionally handles missing audio.
- Generated CreatorCanon narration uses ElevenLabs from `C:\Users\mario\Desktop\Creator Canon Social Content\.env` unless user-provided audio or an explicit override exists.
- If ElevenLabs was unavailable, the response reports the fallback and never exposes secret values.
- Timing manifest maps spoken words to frames.
- Composition is horizontal 16:9 unless the user requested otherwise.
- Duration comes from audio/timing, not guessed scene lengths.
- Brand Guidelines were applied for CreatorCanon work.
- Relevant assets from `universal assets` were considered.
- Official CreatorCanon logo from `universal assets` is used in the video and was not recreated, generated, traced, or typeset.
- Captions/subtitles do not appear before the spoken words.
- Key visuals trigger from phrase or word timing.
- Long-form pacing is readable and section-based, not reel-style.
- No full-page visual is used as a lazy static slide.
- Rendered MP4 exists at the requested path.
- Video specs and audio stream are verified.
- Contact sheet or audit stills were inspected.
- Final response reports changed files, commands run, output path, and any missing environment variables.

## References

- Read `references/workflow.md` when planning or auditing a full YouTube build.
- Use `scripts/generate_elevenlabs_word_timing.py` for CreatorCanon ElevenLabs narration with timestamp-derived word timings.
- Use `scripts/generate_edge_tts_word_timing.py` when a free Edge TTS voiceover with word timings is appropriate.
