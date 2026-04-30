---
name: voiceover-synced-remotion-trailer
description: Build or revise premium voiceover-synced Remotion trailers, reels, shorts, and launch videos from a script plus visual references. Use when Codex needs to generate or import narration first, extract exact word and phrase timings, animate bottom subtitles in sync with the voiceover, map visuals to spoken words, use the official CreatorCanon logo from universal assets, recreate or crop supplied visuals into programmatic animated components instead of static slides, vary scene transitions, render the final MP4, and verify timing/quality.
---

# Voiceover-Synced Remotion Trailer

## Core Rule

Treat the voiceover timing as the edit timeline. Do not build the video from guessed scene durations when narration audio exists or can be generated.

Every important visual element must answer: "What spoken word or phrase causes this to appear?"

## CreatorCanon Defaults

For CreatorCanon reels, apply these defaults unless the user explicitly provides a different audio file, voice, background, or brand system:

- Generate narration with ElevenLabs using `ELEVENLABS_API_KEY` and `ELEVENLABS_VOICE_ID` from `C:\Users\mario\Desktop\Creator Canon Social Content\.env` whenever those variables exist. Do not print or expose secret values.
- If ElevenLabs credentials are missing and the user still wants generated narration, fall back to Edge TTS voice `en-US-AndrewNeural`.
- Do not use `C:\Users\mario\Desktop\Creator Canon Social Content\universal assets\creatorcanon-simple-universal-reel-background.png` as the default background. Only use it if the user explicitly requests that exact asset.
- Search `C:\Users\mario\Desktop\Creator Canon Social Content\universal assets\` recursively for reusable assets. Copy or reference relevant assets as needed, but do not move or delete originals.
- Always use the official CreatorCanon logo from `C:\Users\mario\Desktop\Creator Canon Social Content\universal assets\`. Search that folder recursively and use the currently available official logo asset. Prefer `creatorcanon_logo_transparent.svg` when present; otherwise use the active `logo.png`/`.svg` or other explicit CreatorCanon logo file that exists in universal assets. Do not generate, redraw, trace, typeset, approximate, recolor, or recreate the CreatorCanon logo. If no official logo asset is available, report the blocker instead of rendering a recreated logo.
- Include the official logo asset in CreatorCanon videos, normally in the final CTA/end frame and any explicit brand/signature moment. Preserve its aspect ratio and use scale/position/opacity only; do not distort it or rebuild it as text.
- Treat `C:\Users\mario\Desktop\Creator Canon Social Content\Brand Guidelines.md` as the CreatorCanon visual source of truth. Read it before styling CreatorCanon reels, prioritizing color system, typography, visual identity, layout/composition, motion style, and do/don't rules.
- Use the current CreatorCanon brand colors from `Brand Guidelines.md`: default cream editorial surfaces with Paper `#F5F1EA`, Paper Deep `#EFEAE0`, Card White `#FFFFFF`, Canon Ink `#1C1C1E`, Soft Ink `#6B6B70`, Canon Amber `#D97706` for citations/markers, and Canon Sage `#7C9A7E` only for light-mode verified/outcome moments. Use Night `#0B0B0D`, Night Raised `#111114`, Night Surface `#1A1A1D`, Paper on Night `#F4F1EA`, and Insight Purple `#8B5CF6` only for dark cinematic insight beats.
- Preserve the new CreatorCanon visual system: warm cream paper backgrounds, ink-black editorial typography, white cards with hairline borders, archive/source/citation motifs, restrained amber structure, sage verified outcomes, and near-black cinematic scenes only for problem, insight, or CTA moments. Avoid emerald, electric blue, decay red, neon SaaS palettes, pure black, pure white page backgrounds, and mixing sage with insight purple in one frame.

## Vertical Reel Canvas And Safe Areas

For CreatorCanon reels, default to full-screen vertical Reels specs unless the user explicitly requests a different platform export:

- Composition: `1080x1920`, `9:16`, `30fps`.
- Full-bleed backgrounds, textures, particles, and non-critical video cards may extend to the canvas edges.
- Critical content must stay inside the safe layout: captions, hooks, logos, CTA text, product UI labels, faces, key numbers, play buttons, citation chips, and any visual proof the viewer must read.

Use these 1080x1920 layout constants in Remotion:

```ts
const REEL = { width: 1080, height: 1920, fps: 30 };

const REEL_SAFE = {
  top: 270,
  bottom: 670,
  left: 80,
  right: 160,
  x: 80,
  y: 270,
  width: 840,
  height: 980,
  maxCriticalY: 1250,
};

const REEL_CAPTIONS = {
  x: 96,
  y: 1030,
  width: 808,
  height: 210,
  maxBottom: 1250,
};
```

Placement rules:

- Keep all critical text and key visual information inside `REEL_SAFE`.
- Keep subtitles inside `REEL_CAPTIONS`; the bottom of the caption surface must never pass `y = 1250`.
- Do not place captions in the native app UI area near the bottom of the reel. If a caption needs two lines, move the caption surface upward, not downward.
- Keep right-side key content clear of the Reels engagement rail; use `right: 160` even though the minimum side margin is smaller.
- Reserve the top `270px` for platform UI and breathing room. Do not put a logo, headline, or main subject flush to the top edge.
- Use the center/middle safe zone for hooks, count-up numbers, product panels, and CTA cards. For final CTAs, place the official logo and CTA panel above the bottom UI zone, not at the bottom edge.
- Use a debug safe-zone overlay during development or audit stills whenever layout is being adjusted.

## Workflow

1. Inspect the repo.
   - Detect package manager and Remotion entry points.
   - Locate the script, visual references, existing assets, `.env`, audio files, render scripts, CreatorCanon universal assets, the official CreatorCanon logo file, and Brand Guidelines sections relevant to the reel.
   - Use existing project patterns before adding new structure.

2. Generate or import narration before animation.
   - If the user provides audio, analyze that audio.
   - If the user provides only a script and `C:\Users\mario\Desktop\Creator Canon Social Content\.env` contains ElevenLabs credentials, generate narration first with `scripts/generate_elevenlabs_word_timing.py --env-file "C:\Users\mario\Desktop\Creator Canon Social Content\.env"`.
   - If ElevenLabs is unavailable, generate narration with Edge TTS voice `en-US-AndrewNeural` unless the user explicitly asks for another voice.
   - Extract word timings. Prefer ElevenLabs timestamp alignment or provider word-boundary data; otherwise use transcription/alignment.
   - Save a timing manifest with words, phrase ranges, fps frame numbers, audio path, and total duration.
   - Use `scripts/generate_elevenlabs_word_timing.py` as the preferred CreatorCanon helper. It reads `ELEVENLABS_API_KEY` and `ELEVENLABS_VOICE_ID`, writes audio, word timings, and a Remotion-ready manifest.
   - Use `scripts/generate_edge_tts_word_timing.py --voice en-US-AndrewNeural` as a reusable helper when Edge TTS is appropriate.

3. Build a phrase map.
   - Split narration into semantic beats, not arbitrary equal scenes.
   - Convert each phrase and word into frames at the composition FPS.
   - Keep overlaps short. Avoid end-of-scene pauses unless the audio has intentional silence.
   - Make transitions begin before the previous scene fully ends so momentum is continuous.

4. Analyze visual references by meaning.
   - Inspect all visual files recursively.
   - Include all relevant files from the CreatorCanon universal assets folder in the asset inventory.
   - Treat the official logo file from universal assets as a required brand asset, not a reference to regenerate.
   - Do not use `creatorcanon-simple-universal-reel-background.png` as a default base layer. Build scene backgrounds from the current Brand Guidelines instead, using cream paper surfaces by default and dark cinematic surfaces only for suitable problem, insight, or CTA beats.
   - Rename copied/generated assets descriptively when useful, without moving or deleting originals.
   - Categorize by what each visual communicates, not by filename.
   - Use visuals as references, ingredients, or crops. Avoid showing whole pages/posters as static slides.
   - Skip any visual that does not match the narration beat.

5. Rebuild visuals as animated systems.
   - Recreate repeated UI cards, arrows, badges, video tiles, phones, dashboards, lists, search bars, and diagrams in React/CSS/SVG.
   - Crop or mask supplied visuals only when the crop is a meaningful component.
   - Define and use shared safe-area constants from `Vertical Reel Canvas And Safe Areas` for every text, caption, CTA, logo, and key visual component.
   - Layer base camera movement, scene-specific UI animation, and detail motion in every scene.
   - Use Remotion frame math: `useCurrentFrame`, `useVideoConfig`, `interpolate`, `spring`, `Easing`, `Sequence`, `Audio`, `Img`, and `staticFile`.

6. Synchronize visuals to narration.
   - Trigger components from exact word timings, e.g. "audience" creates the Audience card, "business" creates the Business card, "CANON" highlights the CTA text.
   - Do not place a full sentence on screen before it is spoken.
   - Build utility helpers such as `wordAt('audience')`, `phraseFrames('useful-again')`, and `delayFromWord('business', -6)`.
   - Audit stills at trigger frames and 6-12 frames later.

7. Put subtitles at the bottom.
   - Use word-by-word or phrase-by-phrase subtitles synchronized to timing data.
   - Keep subtitles in `REEL_CAPTIONS`, above the native Reels bottom UI area. Captions should feel bottom-anchored but must not sit at the physical bottom of the 1080x1920 canvas.
   - Keep caption surfaces to one or two lines. If text wraps beyond two lines, shorten the phrase window or split the subtitle into a new timed beat.
   - Use a legible caption surface when backgrounds vary.
   - Highlight only the currently spoken or recently spoken emphasis words.
   - Never use the top of the frame for subtitles unless the user explicitly asks.

8. Vary transitions and motion language.
   - Avoid repeating fade-out/fade-in for every scene.
   - Mix directional wipes, push-throughs, match cuts, object carries, split-screen slides, card gathers, masked reveals, and camera moves.
   - Vary component entrances: bottom-up, left-right, right-left, top-down, center pop, masked draw, and line-following.
   - Ensure the chosen direction matches the story logic. For example, scattered ideas can fly outward; organized assets can align inward.
   - No dead holds longer than roughly 20 frames unless the voiceover needs readability.

9. Render and verify.
   - Run typecheck or project validation.
   - Keep the render output folder canonical: `out/` should contain only the final deliverable MP4, normally `out/final-video.mp4`. Put contact sheets, frame stills, JSON reports, CSV metrics, and any other audit artifacts in a sibling `audit/` folder, never inside `out/`.
   - Render timing audit stills at the key spoken-word frames into `audit/`, not `out/`.
   - Render the MP4.
   - Use `ffprobe` or equivalent to confirm dimensions, fps, duration, frame count, and audio stream.
   - Create a contact sheet from the final MP4 and visually inspect subtitle placement, scene variety, and sync-critical moments, but do not treat a contact sheet as sufficient verification.
   - Run a frame-by-frame pixel audit against the final MP4. Downscale each frame to a small fixed raster, compute per-frame luminance and adjacent-frame pixel differences, and write CSV/JSON metrics under `audit/frame-audit-final/`.
   - The frame audit must report total frames scanned, max/average adjacent-frame difference, long freeze runs, hard-cut frames, and repeated fade/pulse windows. Repeated fade/pulse flags inside a scene are blockers unless there is a specific intentional reason tied to narration.
   - Inspect flagged frames and 6-12 frames around each flag. If components fade in/out repeatedly, oscillate opacity, or re-trigger without a spoken-word cause, fix the animation and rerender before final response.
   - Rerun the pixel audit after fixes. The final audit should have no unexplained repeated fade/pulse windows and no unexpected freeze runs.

## Remotion Implementation Standards

- Register CreatorCanon reel compositions as `1080x1920`, `9:16`, `30fps` unless the user explicitly requests a different export. Register the requested duration exactly.
- For CreatorCanon reels, build backgrounds from the current Brand Guidelines color system and visual motifs. Do not import or copy `creatorcanon-simple-universal-reel-background.png` as the default scene background.
- For CreatorCanon reels, import/copy the official logo from universal assets and render it with `Img`/`staticFile` or the project's established asset pattern. Never recreate the logo with text, SVG paths, CSS, image generation, or screenshots.
- Keep all critical text, captions, logos, CTA panels, product labels, faces, and key visual proof inside the `REEL_SAFE` and `REEL_CAPTIONS` rectangles.
- Use reusable components for caption text, timed words, UI cards, arrows, video tiles, phones, product panels, and transitions.
- Prefer programmatic UI over screenshots when components need independent animation.
- When using image assets, animate camera/crop/mask/parallax and add independent overlays.
- Include optional audio loading so a render does not crash when audio is temporarily missing.
- Keep final render scripts explicit about output path and codec.
- Keep reveal animations monotonic after they complete. Avoid looping opacity, repeated scene-wide fade overlays, or pulsing components unless the pulse is brief, intentional, and tied to a specific spoken beat.
- Keep audit and render outputs separated: `out/` is for the final MP4 only; `audit/` is for screenshots, contact sheets, frame metrics, and review reports.

## Quality Checklist

Before final response:

- Narration audio exists or the render intentionally handles missing audio.
- Generated CreatorCanon narration uses ElevenLabs from `C:\Users\mario\Desktop\Creator Canon Social Content\.env` unless user-provided audio or an explicit override exists.
- If ElevenLabs was unavailable, the response reports the fallback and never exposes secret values.
- Timing manifest maps spoken words to frames.
- `creatorcanon-simple-universal-reel-background.png` is not used as the default background.
- Official CreatorCanon logo from `universal assets` is used in the video and was not recreated, generated, traced, or typeset.
- Current Brand Guidelines colors and visual rules are applied.
- Relevant assets from `universal assets` were considered.
- Brand Guidelines were applied selectively without loading unnecessary sections.
- Bottom subtitles reveal in sync and do not appear early.
- Captions stay inside `REEL_CAPTIONS` and never extend below `y = 1250` on a 1080x1920 reel.
- Critical text, logos, CTA panels, faces, key numbers, and product UI labels stay inside `REEL_SAFE`.
- Audit stills were checked with a safe-zone overlay or equivalent visual inspection.
- Each scene has at least three motion layers.
- Visual objects appear when the matching words are spoken.
- Scene transitions are varied and continuous.
- Frame-by-frame pixel audit was run on the final MP4, not on a stale render.
- Repeated fade/pulse windows from the pixel audit were investigated and resolved, or explicitly justified as intentional narration-tied transitions.
- No long frozen segments are present unless intentionally held for readability.
- `out/` contains exactly one deliverable MP4, normally `final-video.mp4`.
- Audit screenshots, contact sheets, JSON reports, and CSV metrics are outside `out/`.
- No full-page visual is used as a lazy static slide.
- Final MP4 exists at the requested path.
- Video specs and audio stream are verified.
- The response reports changed files, commands, output path, and any missing env vars.

## References

- Read `references/workflow.md` when planning or auditing a full trailer build.
- Use `scripts/generate_elevenlabs_word_timing.py` for CreatorCanon ElevenLabs narration with timestamp-derived word timings.
- Use `scripts/generate_edge_tts_word_timing.py` when a free Edge TTS voiceover with word timings is appropriate.
