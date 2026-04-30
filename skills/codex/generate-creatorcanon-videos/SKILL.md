---
name: generate-creatorcanon-videos
description: Use when the user asks to generate, batch-produce, create, render, or make one or more CreatorCanon videos, reels, shorts, TikToks, YouTube Shorts, or Remotion videos end to end from a requested count such as "generate 3 CreatorCanon videos" or "make X videos for CreatorCanon," especially when each video can run in its own draft folder.
---

# Generate CreatorCanon Videos

## Core Mission

Run the full CreatorCanon video pipeline from one user command:

1. Generate distinct CreatorCanon scripts.
2. Create isolated draft folders.
3. Generate visual assets for each script.
4. Build and render each voiceover-synced Remotion video.
5. Verify every final MP4.

This is an orchestration skill. It does not replace the downstream skills; it loads and follows them in the right order while using one worker subagent per video folder for parallel production.

## Required Sub-Skills

Use these skills in this order:

1. `generate-creatorcanon-scripts` for script generation.
2. `generate-script-visuals` for per-script visual asset packs. That skill uses `imagegen`.
3. `voiceover-synced-remotion-trailer` for narration, timing, subtitles, animation, render, and MP4 verification.

Also use these Superpowers workflow skills when `X >= 2`:

- `superpowers:subagent-driven-development` for fresh focused worker agents, explicit ownership, status handling, and review discipline.
- `superpowers:dispatching-parallel-agents` because each video folder is an independent work domain that can run concurrently.

Do not skip a sub-skill because the workflow feels obvious. Each stage has domain rules that matter.

## Fixed Project Paths

Use these paths unless the user explicitly overrides them:

- Project root: `C:\Users\mario\Desktop\Creator Canon Social Content`
- Drafts root: `C:\Users\mario\Desktop\Creator Canon Social Content\Drafts`
- Brand guidelines: `C:\Users\mario\Desktop\Creator Canon Social Content\Brand Guidelines.md`
- Script skill: `C:\Users\mario\.codex\skills\generate-creatorcanon-scripts\SKILL.md`
- Visual skill: `C:\Users\mario\.codex\skills\generate-script-visuals\SKILL.md`
- Remotion skill: `C:\Users\mario\.codex\skills\voiceover-synced-remotion-trailer\SKILL.md`

## Input Rules

- Extract `X` from the user's request.
- If `X` is missing, ask for the count before starting because this workflow creates files, spends image-generation credits, and renders videos.
- If `X` is large, still use one worker agent per video by default. If the environment or API limits make that unsafe, process workers in small waves while preserving one agent per video.
- If the user gives themes, angles, target length, CTA, voice, or platform constraints, pass them into the script stage and preserve them through visuals and rendering.

## Preflight

Before generating anything:

1. Confirm the Drafts root exists or create it.
2. Confirm the three required sub-skill files exist.
3. Read `Brand Guidelines.md`.
4. Check whether `OPENAI_API_KEY` is available before visual generation. If missing, stop before creating assets and tell the user image generation is blocked.
5. Check whether `C:\Users\mario\Desktop\Creator Canon Social Content\.env` exists for ElevenLabs. Do not print secrets. If ElevenLabs credentials are missing, the Remotion skill may use its Edge TTS fallback.
6. Inspect existing draft folders to avoid name collisions.

## Parallel Execution Model

The controller handles only shared setup:

1. Preflight.
2. Generate all scripts.
3. Create all draft folders.
4. Write each folder's `script.md`.
5. Dispatch one worker subagent per video folder.
6. Collect worker results and verify final outputs.

Each worker owns exactly one folder. The worker performs that video's visual generation and Remotion rendering sequentially inside the folder it owns.

Worker ownership rule:

```text
Worker video-## owns:
<draft folder>\script.md
<draft folder>\assets\
<draft folder>\out\
```

Workers must not read, edit, copy from, or write into any other video draft folder. Shared read-only resources are allowed: `Brand Guidelines.md`, universal assets, and required skill files.

Dispatch all video workers concurrently when the tool environment supports parallel agents. Do not make two workers share a video folder.

## Stage 1 — Generate X Scripts

Use `generate-creatorcanon-scripts`.

Generate exactly `X` complete, distinct CreatorCanon scripts. Require each script to include:

- timed scene-by-scene script
- full voiceover script
- best on-screen text only version
- strong caption
- a short title or slug suitable for folder naming

Variation rules:

- Rotate the main belief, false belief, hook style, visual metaphor, and CTA phrasing.
- Do not generate small rewrites of the same idea.
- Keep every script aligned with CreatorCanon's ICP: serious creators with real archives and proof of work.

After script generation, create a simple script index with:

| Video # | Working title | Primary belief | False belief attacked | Folder slug |
| --- | --- | --- | --- | --- |

## Stage 2 — Create Draft Folders

For each script, create this isolated structure:

```text
C:\Users\mario\Desktop\Creator Canon Social Content\Drafts\
  YYYY-MM-DD-video-##-short-slug\
    script.md
    assets\
    out\
```

Folder rules:

- Use the current date, a two-digit video number, and a short lowercase slug.
- Example: `2026-04-29-video-01-playlists-are-not-products`.
- If a folder exists, append `-v2`, `-v3`, etc. Do not overwrite an existing draft.
- Write only that video's script into that folder's `script.md`.
- Create an empty `assets` folder before visual generation.
- Create an `out` folder for render output.

`script.md` must contain the complete script, not just the voiceover. Include the title, timed scenes, full voiceover, on-screen text version, and caption.

## Stage 3 — Dispatch One Worker Agent Per Video

After all draft folders exist, dispatch one worker subagent per video folder.

Each worker receives only:

- its assigned draft folder path
- the path to that folder's `script.md`
- the path to that folder's `assets\`
- the path to that folder's `out\final-video.mp4`
- the CreatorCanon brand guidelines path
- the required downstream skill names

Worker prompt template:

```text
You are worker video-## for CreatorCanon batch production.

Owned folder: <current video folder>
Script: <current video folder>\script.md
Assets output: <current video folder>\assets
Video output: <current video folder>\out\final-video.mp4
Brand guidelines: C:\Users\mario\Desktop\Creator Canon Social Content\Brand Guidelines.md

You are not alone in the workspace. Other workers own other video folders. Do not read from, write to, move, delete, or reuse files from any other draft folder.

First use generate-script-visuals for this script and save all generated visuals inside this folder's assets folder. Generate at least 10 visuals and target 20-30+ when useful.

Then use voiceover-synced-remotion-trailer for this same folder only:
- Generate the voiceover first.
- Extract exact word timings.
- Put subtitles at the bottom, synced word by word.
- Recreate/crop visual references into animated components, not static slides.
- Match every major visual to the narration timing.
- Vary transitions and remove dead pauses.
- Render and verify <current video folder>\out\final-video.mp4.

Return:
- status: DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT, or BLOCKED
- generated asset count
- final MP4 path
- verification evidence
- any fallback voice or missing environment variable
- changed/created files inside your owned folder
```

Worker requirements:

- Use `generate-script-visuals` before Remotion rendering.
- Keep all generated visuals inside the owned `assets\` folder.
- Include scene plates and reusable motion components, not only finished poster frames.
- Apply CreatorCanon brand rules from `Brand Guidelines.md`.
- Do not begin Remotion work until visual generation has produced and verified assets in the owned folder.

## Stage 4 — Worker Render Step

Inside each worker, use `voiceover-synced-remotion-trailer` with:

```text
Build a vertical Remotion trailer.

Script: <current video folder>\script.md
Visual references: <current video folder>\assets
Output: <current video folder>\out\final-video.mp4

Requirements:
- Generate the voiceover first.
- Extract exact word timings.
- Put subtitles at the bottom, synced word by word.
- Recreate/crop visual references into animated components, not static slides.
- Match every major visual to the narration timing.
- Vary transitions and remove dead pauses.
- Render and verify the final MP4.
```

Isolation rules:

- Work only from the current folder's `script.md` and `assets\`.
- Save output only to the current folder's `out\`.
- Do not use another draft's assets, timing manifests, audio, or output files.
- A worker may render while other workers render their own videos, because each worker owns a separate folder.

## Stage 5 — Controller Review And Batch Summary

After workers return:

1. Read every worker status.
2. If a worker reports `NEEDS_CONTEXT`, provide the missing context and re-dispatch that same video worker.
3. If a worker reports `BLOCKED`, assess whether the blocker is credentials, tool failure, missing files, or render failure. Do not silently mark it complete.
4. If a worker reports `DONE_WITH_CONCERNS`, inspect the concerns before marking the video successful.
5. Verify independently that each successful folder has assets and `out\final-video.mp4`.
6. Run or inspect MP4 verification evidence for every successful video.

After all videos finish, report:

| Video # | Folder | Script | Assets count | Final MP4 | Verification status |
| --- | --- | --- | --- | --- | --- |

Also report:

- commands or major tools run
- any missing environment variables
- any fallback voice used
- any videos that failed and why
- exact paths to successful final videos

## Failure Handling

- If script generation fails, stop before creating draft folders.
- If visual generation is blocked by missing `OPENAI_API_KEY`, stop before image generation and explain the blocker.
- If visual generation fails for one video, that worker must not render that video. Report the failure. Other workers may continue in their own folders.
- If Remotion rendering fails, keep the script and assets folder intact and report the failing command/output summary.
- Never delete successful folders or assets because a later video fails.

## Quality Gate

Before final response, verify:

- Exactly `X` scripts were generated.
- Exactly `X` draft folders were created under `Drafts`.
- Each folder contains `script.md`, `assets\`, and `out\`.
- Each `script.md` contains only the matching video script.
- One worker subagent was assigned per video folder when `X >= 2`.
- Each worker owned exactly one video folder.
- Each video used `generate-script-visuals` separately inside its worker.
- Each assets folder contains generated visuals for that video.
- Each video used `voiceover-synced-remotion-trailer` separately inside its worker.
- Each successful video has `out\final-video.mp4`.
- MP4 specs and audio stream were verified for every successful video.
- No video used another video's script, assets, audio, timing manifest, or render output.
