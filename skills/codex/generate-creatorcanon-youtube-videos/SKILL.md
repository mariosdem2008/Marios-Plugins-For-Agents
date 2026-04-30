---
name: generate-creatorcanon-youtube-videos
description: Use when the user asks to generate, batch-produce, create, render, or make one or more long-form CreatorCanon YouTube videos end to end from a requested count or topic. Orchestrates YouTube script generation, YouTube visual asset planning/generation, voiceover-synced Remotion production, horizontal MP4 rendering, and verification inside the CreatorCanon YouTube Drafts folder.
---

# Generate CreatorCanon YouTube Videos

## Core Mission

Run the full CreatorCanon long-form YouTube pipeline from one user command:

1. Generate distinct strategic YouTube scripts.
2. Create isolated YouTube draft folders.
3. Generate YouTube-specific visual systems and assets.
4. Build and render each voiceover-synced horizontal Remotion video.
5. Verify every final MP4.

This is an orchestration skill. It does not replace the downstream skills; it loads and follows them in the right order while preserving the YouTube-specific workflow.

## Required Sub-Skills

Use these skills in this order:

1. `generate-creatorcanon-youtube-scripts` for long-form YouTube scripts, outlines, titles, thumbnails, descriptions, and CTAs.
2. `generate-creatorcanon-youtube-visuals` for thumbnail concepts, visual systems, image prompts, generated source plates, reusable components, and Remotion handoff notes.
3. `voiceover-synced-remotion-youtube-video` for narration, timing, captions, chaptered animation, horizontal render, and MP4 verification.

Do not substitute the reel-oriented skills:

- Do not use `generate-creatorcanon-scripts`.
- Do not use `generate-script-visuals` unless explicitly asked to create short-form assets.
- Do not use `voiceover-synced-remotion-trailer` unless explicitly asked for a reel/trailer/Short.

When the request asks for multiple videos and subagents are explicitly authorized by the user or permitted by the active runtime policy, use one worker per video folder. Otherwise process videos sequentially while keeping the same folder isolation rules.

## Fixed Project Paths

Use these paths unless the user explicitly overrides them:

- Project root: `C:\Users\mario\Desktop\Creator Canon Social Content\Youtube`
- YouTube drafts root: `C:\Users\mario\Desktop\Creator Canon Social Content\Youtube\Drafts`
- Shared CreatorCanon root: `C:\Users\mario\Desktop\Creator Canon Social Content`
- Brand guidelines: `C:\Users\mario\Desktop\Creator Canon Social Content\Brand Guidelines.md`
- Universal assets: `C:\Users\mario\Desktop\Creator Canon Social Content\universal assets`
- Script skill: `C:\Users\mario\.codex\skills\generate-creatorcanon-youtube-scripts\SKILL.md`
- Visual skill: `C:\Users\mario\.codex\skills\generate-creatorcanon-youtube-visuals\SKILL.md`
- Remotion skill: `C:\Users\mario\.codex\skills\voiceover-synced-remotion-youtube-video\SKILL.md`

All generated YouTube video drafts must sit under:

```text
C:\Users\mario\Desktop\Creator Canon Social Content\Youtube\Drafts
```

## Input Rules

- Extract `X` from the user's request.
- If `X` is missing, ask for the count before starting because this workflow creates files, may spend image-generation credits, and renders videos.
- If the user gives topics, title ideas, themes, archive sources, target length, CTA, voice, pacing, or visual constraints, pass them through every stage.
- Default each video to 6-9 minutes unless the user asks for a different range.
- Keep videos horizontal 16:9 YouTube videos unless the user explicitly asks for Shorts.
- If the user asks for a batch but gives only one theme, generate distinct angles under that theme instead of repeating the same thesis.

## Preflight

Before generating anything:

1. Confirm the YouTube drafts root exists or create it.
2. Confirm the three required YouTube sub-skill files exist.
3. Confirm `Brand Guidelines.md` exists and read it before visual or Remotion work.
4. Inspect `C:\Users\mario\Desktop\Creator Canon Social Content\Youtube` for existing project patterns, Remotion entry points, package manager, assets, and prior drafts.
5. Check whether image generation is available through the active `imagegen` route. If only a local route is available and it requires `OPENAI_API_KEY`, stop before image generation if the key is missing.
6. Check whether `C:\Users\mario\Desktop\Creator Canon Social Content\.env` exists for ElevenLabs. Do not print secrets. If ElevenLabs credentials are missing, the Remotion skill may use its Edge TTS fallback.
7. Inspect existing draft folders to avoid name collisions.

## Execution Model

The controller handles shared setup:

1. Preflight.
2. Generate all scripts.
3. Create all draft folders.
4. Write each folder's `script.md`.
5. Write each folder's `production-brief.md`.
6. Run each video's visual generation and Remotion rendering in an isolated folder.
7. Collect results and verify final outputs.

For multiple videos:

- Use parallel workers only when user/runtime policy permits subagents.
- If workers are not permitted, process one draft folder at a time.
- Whether parallel or sequential, never mix files across draft folders.

Folder ownership rule:

```text
One video owns:
<draft folder>\script.md
<draft folder>\production-brief.md
<draft folder>\assets\
<draft folder>\remotion\
<draft folder>\out\
```

Shared read-only resources are allowed:

- `Brand Guidelines.md`
- `universal assets`
- required skill files
- shared package templates or existing Remotion project files when copied intentionally into the owned folder

## Stage 1 - Generate X YouTube Scripts

Use `generate-creatorcanon-youtube-scripts`.

Generate exactly `X` complete, distinct CreatorCanon YouTube scripts. Require each script to include:

- title options
- thumbnail text options
- video premise
- timed YouTube script
- visual/animation direction by section
- full voiceover script
- description
- pinned comment
- CTA options
- a short slug suitable for folder naming

Variation rules:

- Rotate the main belief, false belief, video type, visual metaphor, title packaging, and CTA phrasing.
- Do not generate small rewrites of the same idea.
- Keep every video aligned with CreatorCanon's ICP: serious creators with real archives and proof of work.
- Keep each script focused on one primary belief.
- Avoid 20+ minute scripts unless the user explicitly asks.

After script generation, create a script index:

| Video # | Working title | Target length | Primary belief | False belief attacked | Video type | Folder slug |
| --- | --- | --- | --- | --- | --- | --- |

## Stage 2 - Create YouTube Draft Folders

For each script, create this isolated structure:

```text
C:\Users\mario\Desktop\Creator Canon Social Content\Youtube\Drafts\
  YYYY-MM-DD-youtube-##-short-slug\
    script.md
    production-brief.md
    assets\
      generated-youtube-visuals\
      thumbnails\
    remotion\
    out\
```

Folder rules:

- Use the current date, a two-digit video number, and a short lowercase slug.
- Example: `2026-04-29-youtube-01-playlists-are-not-products`.
- If a folder exists, append `-v2`, `-v3`, etc. Do not overwrite existing drafts.
- Write only that video's script into that folder's `script.md`.
- Write a concise production brief into `production-brief.md`.
- Create asset, thumbnail, Remotion, and output folders before production.

`script.md` must contain the complete script, not just the voiceover.

`production-brief.md` should include:

- working title
- target length
- primary belief
- false belief attacked
- video type
- visual thesis
- CTA
- output target path
- downstream skills to use

## Stage 3 - Generate YouTube Visuals

For each folder, use `generate-creatorcanon-youtube-visuals` with:

```text
Create a motion-ready CreatorCanon YouTube visual system.

Script: <current video folder>\script.md
Production brief: <current video folder>\production-brief.md
Assets output: <current video folder>\assets
Thumbnail output: <current video folder>\assets\thumbnails
Brand guidelines: C:\Users\mario\Desktop\Creator Canon Social Content\Brand Guidelines.md
Universal assets: C:\Users\mario\Desktop\Creator Canon Social Content\universal assets

Requirements:
- Plan for a horizontal 16:9 long-form YouTube video.
- Include thumbnail concepts.
- Include section-level visual systems.
- Separate generated image assets from Remotion rebuild components.
- Generate or prepare assets inside this folder only.
- Preserve CreatorCanon brand rules.
```

Visual requirements:

- Create a visual thesis for the whole video.
- Include one thumbnail concept set.
- Include 8-12 section visual systems for a 6-9 minute video.
- Include reusable component plans: archive tiles, source cards, citation chips, search rows, framework nodes, chapter markers, CTA panels.
- Generate live images when requested and available.
- Save all generated visual files under the current folder's `assets\`.
- Do not put short-form 9:16 assets in this folder unless explicitly requested.

## Stage 4 - Build And Render Remotion YouTube Video

For each folder, use `voiceover-synced-remotion-youtube-video` with:

```text
Build a horizontal 16:9 Remotion YouTube video.

Script: <current video folder>\script.md
Production brief: <current video folder>\production-brief.md
Visual references: <current video folder>\assets
Remotion workspace: <current video folder>\remotion
Output: <current video folder>\out\final-youtube-video.mp4
Brand guidelines: C:\Users\mario\Desktop\Creator Canon Social Content\Brand Guidelines.md

Requirements:
- Generate or import the voiceover first.
- Extract exact word and phrase timings.
- Derive duration from the final audio/timing manifest.
- Build a 1920x1080, 30 fps composition unless overridden.
- Structure the video by chapters/sections, not reel-style cuts.
- Use captions selectively and keep them synced.
- Match major visuals to narration phrase timing.
- Use generated assets as plates/components, not static slides.
- Rebuild text-heavy diagrams and source citations programmatically.
- Render and verify the final MP4.
```

Render requirements:

- Output file must be `<current video folder>\out\final-youtube-video.mp4`.
- Include audio.
- Verify dimensions are 16:9 horizontal, normally 1920x1080.
- Verify fps, duration, frame count, and audio stream with `ffprobe` or equivalent.
- Create audit stills or a contact sheet when possible.

## Parallel Worker Prompt

When worker subagents are permitted, dispatch one worker per draft folder with this prompt:

```text
You are worker youtube-## for CreatorCanon YouTube production.

Owned folder: <current video folder>
Script: <current video folder>\script.md
Production brief: <current video folder>\production-brief.md
Assets output: <current video folder>\assets
Remotion workspace: <current video folder>\remotion
Video output: <current video folder>\out\final-youtube-video.mp4
Brand guidelines: C:\Users\mario\Desktop\Creator Canon Social Content\Brand Guidelines.md
Universal assets: C:\Users\mario\Desktop\Creator Canon Social Content\universal assets

You are not alone in the workspace. Other workers may own other video folders. Do not read from, write to, move, delete, or reuse files from any other draft folder.

First use generate-creatorcanon-youtube-visuals for this script and save all assets inside this folder's assets folder.

Then use voiceover-synced-remotion-youtube-video for this same folder only:
- Generate or import the voiceover first.
- Extract exact word and phrase timings.
- Build a horizontal 16:9 YouTube composition.
- Use chaptered long-form pacing, not reel-style pacing.
- Use visual assets as motion-ready plates/components.
- Rebuild exact text, diagrams, and citations programmatically.
- Render and verify <current video folder>\out\final-youtube-video.mp4.

Return:
- status: DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT, or BLOCKED
- generated asset count
- thumbnail asset count
- timing manifest path
- final MP4 path
- verification evidence
- any fallback voice or missing environment variable
- changed/created files inside your owned folder
```

## Controller Review And Batch Summary

After every video finishes:

1. Read every status.
2. If a video reports `NEEDS_CONTEXT`, provide the missing context and continue that same folder.
3. If a video reports `BLOCKED`, determine whether the blocker is credentials, image generation, missing files, package setup, or render failure.
4. If a video reports `DONE_WITH_CONCERNS`, inspect the concerns before marking it successful.
5. Verify independently that each successful folder contains assets and `out\final-youtube-video.mp4`.
6. Run or inspect MP4 verification evidence for every successful video.

Final report table:

| Video # | Folder | Script | Visual assets | Thumbnail assets | Final MP4 | Verification status |
| --- | --- | --- | --- | --- | --- | --- |

Also report:

- commands or major tools run
- any missing environment variables
- any fallback voice used
- any videos that failed and why
- exact paths to successful final videos

## Failure Handling

- If script generation fails, stop before creating draft folders.
- If the YouTube drafts root cannot be created, stop before generating scripts.
- If image generation is blocked, preserve `script.md` and `production-brief.md`, then report the blocker.
- If visual generation fails for one video, do not render that video. Other independent videos may continue.
- If Remotion rendering fails, keep the script, production brief, assets, timing files, and render workspace intact.
- Never delete successful folders or assets because a later video fails.
- Never overwrite an existing draft folder or final MP4 unless the user explicitly asks.

## Quality Gate

Before final response, verify:

- Exactly `X` scripts were generated.
- Exactly `X` draft folders were created under `C:\Users\mario\Desktop\Creator Canon Social Content\Youtube\Drafts`.
- Each folder contains `script.md`, `production-brief.md`, `assets\`, `remotion\`, and `out\`.
- Each `script.md` contains only the matching YouTube script.
- Each video used `generate-creatorcanon-youtube-visuals`.
- Each successful video used `voiceover-synced-remotion-youtube-video`.
- No reel-oriented skill was used unless explicitly requested.
- Each successful output is horizontal 16:9.
- Each successful video has `out\final-youtube-video.mp4`.
- MP4 specs and audio stream were verified for every successful video.
- No video used another video's script, assets, audio, timing manifest, Remotion workspace, or render output.
