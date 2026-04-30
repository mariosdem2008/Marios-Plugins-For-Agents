---
name: generate-script-visuals
description: Use when a user wants realistic visual assets, image prompts, image generation, scene plates, motion-ready frames, YouTube-style thumbnails, channel mockups, professional UI/product visuals, or a complete asset pack generated from any script, voiceover, reel, trailer, ad, short, TikTok, YouTube Short, Remotion video, or scene-by-scene script.
---

# Generate Script Visuals

## Core Principle

Turn any script into a complete motion-ready visual asset pack. Do not assume the script is a specific previous script. Treat the script path, pasted script, or active file as the source label only.

This skill creates source visuals for animation, not finished static slides. Every generated visual should have a clear job in the edit: establish, explain, dramatize, transition, provide texture, isolate a component, or support a timed narration beat.

**REQUIRED SUB-SKILL:** Use `imagegen` for live image generation. Load it before running image generation. When the runtime exposes a callable `imagegen` / `image_gen` tool, call that tool directly when the prompts are ready; do not treat `OPENAI_API_KEY` as required for that hosted tool route. If the only available imagegen route is the local bundled CLI, follow the `imagegen` skill's CLI, environment, output, and validation rules.

## Realism Standard

Make generated visuals look production-ready, believable, and professionally art-directed. Avoid the common AI-image look: glossy generic gradients, impossible screens, fake tiny text, plastic people, over-smoothed hands, cluttered dashboards, random icons, and vague "futuristic" compositions.

When a visual is meant to look real:

- Use plausible camera language: real lens choices, natural depth of field, editorial lighting, controlled shadows, realistic texture, and believable scale.
- Use real-world compositions: desk setups, screens, documents, archive cards, channel pages, creator workspaces, product surfaces, and practical UI closeups.
- Make UI assets feel designed by a real product team: consistent spacing, aligned typography, restrained shadows, clear hierarchy, and no random filler widgets.
- Keep text short and intentional. For exact headlines, captions, citations, or UI labels, leave the text for Remotion or a design tool unless the user explicitly wants baked-in text.
- Use fictional but coherent brands, channels, avatars, thumbnails, and dashboards when source details are not supplied. Do not invent factual metrics, testimonials, citations, creator names, or platform claims.

For thumbnails and channel/package visuals, the output should feel like something a real YouTube channel could publish today, not a generic marketing graphic.

## Output Target

Generate enough visuals for a full editor or Remotion build:

- Minimum: 10 generated visuals for any usable script.
- Target: 20-30 generated visuals for most 35-90 second scripts.
- More than 30 is acceptable when the script has many distinct beats, recurring UI components, thumbnails, transitions, or alternate crops.

Do not stop at exactly 10 unless the script is short or the user explicitly limits the count.

## Workflow

1. Resolve the script source.
   - Use the path the user gives first, then the active/obvious `script.md`, then pasted text.
   - If multiple scripts are plausible, choose the one closest to the user's requested folder or active file.
   - Label the script source in the asset plan, but do not hard-code that script into the skill.

2. Inspect context.
   - Read the script fully.
   - Check nearby `assets/`, `visual references/`, `Brand Guidelines.md`, and project-specific visual docs when present.
   - For CreatorCanon projects, read `Brand Guidelines.md` and preserve the current cream editorial, source-backed, knowledge-system visual identity.
   - For CreatorCanon assets intended for Remotion trailers, reels, or shorts, read `references/creatorcanon-remotion-visual-system.md` before writing prompts.
   - Inventory existing references by meaning, not filename.
   - If the user asks for thumbnails, channel visuals, or YouTube packaging, inspect any provided channel references, prior thumbnails, avatar/logo files, titles, and brand examples before inventing a look.

3. Break the script into visual beats.
   - Split by scene headings, timestamps, paragraphs, or narration beats.
   - Identify hook, problem, proof, reframe, mechanism, transformation, payoff, and CTA when present.
   - Create visual moments for narration shifts, not arbitrary equal intervals.

4. Plan the asset pack before generation.
   - Create an asset plan with at least 10 rows and preferably 20+ rows.
   - Include scene plates, reusable graphics, UI components, texture/background plates, transition elements, CTA backgrounds, and optional alternate crops.
   - Mark which assets are primary required assets and which are supporting/optional if the count exceeds the minimum.
   - For Remotion, plan assets as motion ingredients: scene plates, isolated components, crop sources, UI rebuild references, and poster references. Avoid relying on full static posters as the main edit.

5. Write generation prompts.
   - Write one prompt per asset.
   - Use imagegen's structured prompt style and classify each as `ui-mockup`, `infographic-diagram`, `stylized-concept`, `product-mockup`, or another imagegen taxonomy slug.
   - Include aspect ratio, composition, allowed text, text to leave for Remotion, palette, visual style, negative prompt, and filename.
   - Avoid long baked-in subtitles. Prefer clean plates with negative space for kinetic text.
   - Add realism details when appropriate: lens, lighting, surface materials, believable screen content density, real platform thumbnail conventions, and professional production finish.
   - Add negative prompts against AI artifacts: distorted hands, unreadable tiny text, fake logos, warped UI, random glyphs, over-polished plastic faces, cluttered panels, impossible reflections, and generic stock-photo posing.

6. Generate images end to end.
   - Use `imagegen` for live generation as soon as the asset plan and prompts are ready.
   - Prefer the callable `imagegen` / `image_gen` tool when available in the session, especially when the user asks not to use a local API key.
   - For each asset, pass the structured prompt, aspect ratio, style constraints, allowed in-image text, and negative prompt to `imagegen`.
   - Prefer batch generation for 10+ assets when the active imagegen route supports it; otherwise generate assets one by one until the pack is complete.
   - Use the bundled CLI only when no callable imagegen tool is available or when the user specifically asks for local reproducible CLI generation.
   - Save outputs under the script/project folder, usually `assets/generated-visuals/` or `assets/<script-label>-visuals/`.
   - Use descriptive, stable filenames such as `scene-01-pattern-interrupt-archive-map.png`, not timestamps.
   - For Remotion jobs, also write `asset-manifest.json` beside the generated images with each asset's role, visual world, script beat, trigger words, motion intent, text policy, and what should be rebuilt programmatically.
   - Do not move or delete the user's original visual references.

7. Validate and iterate.
   - Inspect generated images, especially text, brand consistency, composition, and safe area.
   - Regenerate any image that is off-brand, illegible, too generic, overstuffed, or not useful for animation.
   - Prefer a targeted prompt correction over reworking the whole pack.

8. Return a production handoff.
   - List the generated files.
   - Include the asset plan summary.
   - Mention any missing API key, skipped generation, or assets that need manual review.
   - If this is for Remotion, include the `asset-manifest.json` path and identify which assets are scene plates, components, crop sources, UI rebuild references, poster references, and CTA plates.

## Asset Plan Schema

Use this table before generation:

| # | Filename | Script beat / timestamp | Asset type | Purpose in edit | What to show | Animate on top |
| --- | --- | --- | --- | --- | --- | --- |

Asset types:
- full scene plate
- reusable graphic
- UI component
- product/mockup component
- realistic thumbnail
- channel/page mockup
- publish-ready hero image
- transition element
- texture/background
- CTA background
- alternate crop/detail

For Remotion requests, extend the plan with:
- Remotion role: `scene_plate`, `component_source`, `crop_source`, `ui_rebuild_reference`, `poster_reference`, `texture_plate`, or `cta_plate`
- Visual world: brand/style mode, such as `cream_editorial`, `dark_cinematic_archive`, `product_ui`, or `photoreal_cta`
- Trigger words: spoken words or phrases that cause the asset or component to appear
- Rebuild in Remotion: text, logo, counters, badges, connectors, or UI details that should be animated programmatically

## Remotion Handoff Manifest

For Remotion jobs, write `asset-manifest.json` beside the image outputs:

```json
[
  {
    "id": "scene-01-archive-scale-dark",
    "file": "assets/generated-visuals/scene-01-archive-scale-dark.png",
    "role": "scene_plate",
    "visual_world": "dark_cinematic_archive",
    "script_beat": "creator has a large video archive",
    "trigger_words": ["50+", "videos", "archive"],
    "remotion_use": "background plate with parallax cards and animated count-up overlay",
    "text_policy": "no baked headline; Remotion adds kinetic text",
    "motion_layers": ["camera push", "floating card parallax", "source-line draw"],
    "rebuild_in_remotion": ["headline", "count number", "category labels", "official logo"]
  }
]
```

Do not include the official CreatorCanon logo in generated images. For CreatorCanon videos, reserve logo placement for Remotion using the official asset from universal assets.

## Prompt Template

Write prompts in this form:

```text
Filename: <stable-file-name.png>
Use case: <imagegen taxonomy slug>
Asset type: <scene plate/component/etc.>
Aspect ratio: 9:16 vertical, 1080x1920 unless another format is requested
Script beat: <short label or timestamp>
Main composition: <what the viewer sees>
Key objects: <objects/UI/diagrams/cards/people if needed>
Style: <brand/style system>
Palette: <brand colors or visual palette>
Text allowed inside image: <short UI labels only, or none>
Text to leave for Remotion: <subtitles/headlines/long copy>
Motion intent: <how the asset will be animated later>
Constraints: <safe area, negative space, no clutter, source-plate requirements>
Realism notes: <camera/lens, lighting, material, UI fidelity, platform authenticity>
Avoid: <negative prompt, including AI artifacts and fake platform/brand claims>
```

## YouTube Thumbnail And Channel Realism

When creating thumbnails or channel visuals:

- Use 16:9, usually 1920x1080 or 1280x720, unless the user asks for a vertical format.
- Make the thumbnail readable at phone size: one focal object, one core tension, 2-5 words, large shape contrast, and no tiny UI details as the main hook.
- Make thumbnails feel YouTube-native: bold but not tacky, clear title/thumbnail tension, realistic subject lighting, credible product/channel context, and strong edge separation.
- For creator-led expert channels, use authority cues: clean studio or desk context, premium channel identity, organized archives, source cards, research boards, productized knowledge maps, and polished educational packaging.
- For channel mockups, create a coherent fictional channel ecosystem: avatar, banner, video grid, recurring thumbnail style, playlist rows, credible upload titles, consistent colors, and realistic spacing.
- Do not fake real YouTube analytics, subscriber counts, views, endorsements, or verified badges unless the user provides exact values. Use placeholders or clearly fictional generic values for mockups.
- Avoid shock faces, money stacks, red arrows, fake viral graphs, screenshot clutter, and low-quality clickbait unless the user specifically asks for that style.

Professional thumbnail prompt direction:

```text
Realistic YouTube thumbnail for a serious educational creator channel, 16:9 horizontal. One premium focal object: a messy grid of old video thumbnails transforming into a clean knowledge-library interface. Large readable blank area for 3-word headline, realistic screen glow, editorial lighting, warm cream and ink palette, subtle amber source markers, sharp mobile-readable contrast, polished creator-economy documentary style. No fake YouTube logos, no tiny unreadable text, no shock face, no money stacks, no red arrows, no random UI glyphs.
```

Professional channel mockup prompt direction:

```text
Believable fictional YouTube channel page for a serious expert creator, 16:9 horizontal browser view. Cohesive avatar, clean banner, premium educational thumbnails in a grid, realistic spacing and modern platform layout, titles represented as short clean placeholder lines, warm editorial brand palette, source-backed knowledge-system motifs, professional SaaS-quality UI polish. No real platform trademarks as focal points, no fake verified badge, no real subscriber claims, no distorted UI, no unreadable microtext.
```

## CreatorCanon Defaults

When the script or project is CreatorCanon:

- If the asset pack is for a Remotion trailer or reel, follow `references/creatorcanon-remotion-visual-system.md`.
- Use cream paper as the default surface: `#F5F1EA`, `#EFEAE0`, white cards, `#1C1C1E` ink, `#6B6B70` muted text.
- Use `#D97706` only for citations, step markers, small structural labels, and source accents.
- Use sage green only for verified/outcome moments in light scenes.
- Use near-black scenes only for problem, insight, or CTA beats, with insight purple as the single accent.
- Make visuals feel like a premium knowledge operating system: archive cards, timestamps, citations, search, framework maps, source libraries, dashboards, and Knowledge Hub UI.
- Make thumbnails feel like a real premium educational YouTube channel: confident, readable, high-contrast, strategically tense, and visually tied to archives becoming assets.
- Make CreatorCanon channel/page mockups feel consistent: recurring thumbnail system, serious creator-facing titles, clean banner treatment, restrained avatar/logo placement, and believable content rows.
- Do not use neon SaaS gradients, generic AI robots, stock creators pointing at laptops, loud YouTube aesthetics, fake platform stats, or long baked-in copy.

## Visual Coverage Rules

For every script, cover these categories when possible:

- 3-5 primary scene plates for the main story arc.
- 4-8 reusable component assets: cards, nodes, diagrams, search bars, product panels, icons, badges, citation chips.
- 3-5 problem/friction visuals.
- 3-5 transformation/mechanism visuals.
- 2-4 payoff/CTA visuals.
- 2-4 transition or texture assets for motion variety.

If the script has 8-10 scenes, generate at least:
- one full scene plate per scene
- one reusable component for every major repeated motif
- one CTA/end frame
- several optional close-up details or transition plates

## Common Mistakes

Avoid these failures:

- Generating only one image per scene when the edit needs reusable pieces.
- Baking subtitles or long script lines into the images.
- Producing decorative images that do not map to a narration beat.
- Using the same composition repeatedly across 20 assets.
- Treating visual references as static slides instead of ingredients for animated systems.
- Stopping after writing prompts when the user asked to generate end to end.
- Ignoring brand docs that exist beside the script.
- Creating 10 assets by default when the script can support 20+.
- Making thumbnails look like generic ads instead of real YouTube packaging.
- Making channel mockups feel empty, fake, or inconsistent from video to video.
- Letting image models invent fake analytics, citations, subscriber counts, or unreadable UI text.

## Quality Gate

Before final response, verify:

- The script source is identified.
- The asset plan includes at least 10 assets, with a target of 20+ considered.
- Each asset has a stable descriptive filename.
- Each prompt specifies allowed in-image text and text left for Remotion.
- For Remotion jobs, `asset-manifest.json` exists beside the generated files and classifies each asset's role, visual world, trigger words, motion intent, text policy, and programmatic rebuild notes.
- Thumbnail/channel prompts include realism notes, platform packaging logic, and negative prompts against fake metrics or AI-looking UI.
- `imagegen` was used for live generation unless no callable imagegen tool is available, the local CLI is blocked by missing `OPENAI_API_KEY`, or the user explicitly requested prompts only.
- Generated files exist at the reported paths.
- Visuals are motion-ready source plates or components, not finished static slides.
- Full poster-style visuals are marked as `poster_reference` unless they are intentionally used with camera movement, masking, overlays, and a timed exit.
- CreatorCanon brand rules were applied when relevant.
- Any generation failures, missing credentials, or assets needing regeneration are reported plainly.
