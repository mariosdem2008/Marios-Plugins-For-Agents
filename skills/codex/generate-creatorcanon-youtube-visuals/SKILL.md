---
name: generate-creatorcanon-youtube-visuals
description: Use when creating realistic YouTube-native visual asset plans, image prompts, generated visuals, thumbnail concepts, believable channel/page mockups, source plates, diagrams, UI mockups, Remotion scene systems, component inventories, or complete visual packs for CreatorCanon long-form YouTube videos, animated explainers, authority videos, video essays, tutorials, and source-backed Knowledge Hub content.
---

# Generate CreatorCanon YouTube Visuals

## Core Principle

Turn a long-form YouTube script, outline, voiceover, or video idea into a motion-ready visual system.

Do not create generic stock visuals or static slide decks. Build visual assets that help the viewer understand, believe, and remember the strategic argument.

The visuals should feel like they belong to a real premium YouTube channel run by a serious creator-led expert brand. Thumbnails should look publishable on YouTube today. Channel and platform mockups should feel coherent, real, and professionally designed, not like placeholder AI UI.

Each visual must have a job in the edit:

- establish the problem
- explain a mechanism
- prove a claim
- reveal a false belief
- make a framework easier to understand
- show archive-to-asset transformation
- support a chapter transition
- create thumbnail/title packaging
- provide reusable Remotion components
- create a calm, qualified CTA moment

## Required Sub-Skill

Use `imagegen` for live image generation. Load it before generating images.

When a callable `imagegen` / `image_gen` tool is available, use that route directly after the prompts are ready. Do not require `OPENAI_API_KEY` for the hosted tool route.

If no callable imagegen route is available, provide a prompt pack and explain what could not be generated. Use a local CLI only when the active `imagegen` skill requires it or the user requests reproducible local generation.

## YouTube Difference

Short-form visual packs need many fast scene plates.

YouTube videos need reusable visual systems that can evolve across sections.

For 6-12 minute CreatorCanon videos, prioritize:

- 16:9 horizontal visual composition
- section-level diagrams and frameworks
- reusable cards, nodes, citation chips, search bars, video tiles, and panels
- thumbnail concepts separate from in-video assets
- chapter cards and progress markers
- source-backed diagrams, not decorative imagery
- high-readability visuals for desktop, TV, and mobile playback
- fewer generic image plates and more motion-ready components
- real YouTube packaging: thumbnails, channel identity, end screens, playlist rows, and chapter visuals that feel part of one credible channel ecosystem

## Realism And Professionalism Standard

Make every generated asset pass a "would this look real on a serious YouTube channel?" test.

Use:

- believable 16:9 composition, not poster art stretched into a video frame
- realistic screen surfaces, paper texture, lighting, shadows, and spatial depth
- strong focal hierarchy with one dominant idea per thumbnail or scene plate
- professional editorial/product-design polish
- consistent CreatorCanon channel identity across thumbnails, channel mockups, video grids, and end frames
- restrained visual drama that supports authority, not hype

Avoid:

- generic AI-gloss, random UI glyphs, fake tiny text, impossible dashboards, distorted browsers, warped typography, and incoherent interface panels
- fake analytics, fake subscriber counts, fake verified badges, fake creator endorsements, fake citations, or fake source titles
- thumbnails that look like generic SaaS ads, pitch decks, Instagram carousels, or AI concept art
- channel pages where every thumbnail looks unrelated
- shock faces, money stacks, red arrows, viral graph theatrics, and noisy creator-economy clickbait

When the user does not provide real channel details, create a fictional but coherent CreatorCanon channel ecosystem. Use placeholder channel/page details that look plausible without pretending to be factual.

## Output Targets

Choose the output depth based on the user's request.

Minimum for a useful YouTube visual plan:

- 1 thumbnail concept set
- 8-12 section visual systems
- 15-25 reusable visual components
- 8-15 generated source plates or image prompts
- 3-6 transition/texture assets
- 1 CTA/end-frame system

For full generation requests, do not generate dozens of redundant frames. Generate the assets that are hard or valuable to create as images, then specify which elements should be rebuilt programmatically in Remotion.

Default live generation target:

- 12-20 generated assets for a 6-9 minute video
- 20-30 generated assets for a 9-12 minute deep breakdown
- fewer assets when the video is mostly programmatic UI/diagram work

## Workflow

1. Resolve the source.
   - Use the script path the user gives first, then the active/obvious YouTube script or outline, then pasted text.
   - Accept scripts, outlines, voiceovers, timing manifests, transcripts, titles, or rough topics.
   - Label the source in the asset plan.

2. Inspect context.
   - Read the source fully.
   - Check nearby `assets/`, `visual references/`, `Brand Guidelines.md`, and project-specific visual docs when present.
   - For CreatorCanon projects, read `Brand Guidelines.md` and preserve the current cream editorial, source-backed, knowledge-system visual identity.
   - Read `references/creatorcanon-youtube-visual-system.md` before planning thumbnails, channel/page mockups, long-form section visuals, or Remotion-ready YouTube asset packs.
   - Inventory existing references by meaning, not filename.
   - Inspect prior thumbnails, channel assets, logo/avatar files, banner art, title formats, and visual examples when they exist.
   - If no channel references exist, define a consistent fictional CreatorCanon channel packaging system before generating assets.

3. Break the video into sections.
   - Use timestamps, headings, script paragraphs, or narration beats.
   - Identify cold open, ICP mirror, promise, surface problem, deeper diagnosis, false solution, reframe, new model, practical breakdown, future state, and CTA when present.
   - Create visuals for belief shifts and explanation moments, not arbitrary equal intervals.

4. Define the visual thesis.
   - State the main metaphor or system for the video.
   - Example: scattered archive tiles become a structured Knowledge Hub.
   - Keep the visual thesis consistent across the whole video so the video feels designed, not assembled.
   - Define the channel packaging thesis as well: the recurring thumbnail look, focal objects, text treatment, channel page style, and how this video fits beside other CreatorCanon uploads.

5. Create the asset plan before generation.
   - Include thumbnail packaging, section systems, source plates, reusable components, diagrams, transitions, and CTA visuals.
   - Mark each asset as `generate`, `rebuild in Remotion`, `use existing asset`, or `optional`.
   - Plan generated visuals as YouTube motion ingredients: thumbnail backgrounds, channel context plates, section plates, component sources, UI rebuild references, diagram rebuild references, texture plates, and end-screen plates.
   - Prefer generated images for scene plates, atmospheric textures, hero thumbnail backgrounds, abstract insight beats, and high-level product mockups.
   - Prefer Remotion rebuilds for text-heavy UI, diagrams, source citations, captions, lists, search results, and anything requiring exact wording.
   - Include realistic channel context assets when useful: channel header mockup, video grid row, playlist shelf, end-screen cards, and thumbnail family preview.

6. Write generation prompts.
   - Write one prompt per generated image asset.
   - Use structured prompt fields and classify each as `thumbnail-background`, `ui-mockup`, `infographic-diagram`, `source-plate`, `texture-background`, `product-mockup`, `transition-plate`, or `concept-visual`.
   - Include aspect ratio, composition, allowed text, text left for Remotion, palette, safe area, motion intent, and negative prompt.
   - Avoid baked-in subtitles, long labels, fake UI copy, tiny illegible text, or invented source citations.
   - Include realism notes: focal object, camera/lens or UI fidelity, lighting, surface material, YouTube mobile readability, thumbnail shelf fit, and channel consistency.
   - For channel/page mockups, request a believable fictional platform layout with coherent thumbnails and clean placeholder text, not exact real platform branding or invented metrics.

7. Generate images when requested.
   - Use `imagegen` after the asset plan and prompts are ready.
   - Save outputs under the project folder, usually `assets/generated-youtube-visuals/` or `assets/<video-label>-youtube-visuals/`.
   - Use descriptive filenames such as `thumbnail-archive-to-ip-background.png`, `section-04-scattered-archive-grid.png`, or `component-citation-chip-set.png`.
   - Write `youtube-asset-manifest.json` beside generated images with each asset's role, visual world, section, trigger phrases, packaging use, text policy, motion intent, and programmatic rebuild notes.
   - Do not move or delete original references.

8. Validate and iterate.
   - Inspect generated images for brand fit, 16:9 readability, safe margins, visual usefulness, and whether text is clean.
   - Regenerate images that are off-brand, too generic, overstuffed, illegible, or hard to animate.
   - Prefer targeted prompt correction over redoing the whole pack.

9. Return a production handoff.
   - List generated files or planned assets.
   - Include the section visual map.
   - Include Remotion implementation notes.
   - Separate generated image assets from elements that should be rebuilt as React/CSS/SVG.
   - Include the `youtube-asset-manifest.json` path when assets were generated for editing or Remotion.
   - Mention missing API keys, unavailable image generation, skipped assets, or manual review needs.

## Asset Plan Schema

Use this table before generation:

| # | Filename / component | Section / timestamp | Asset type | Build route | Purpose in edit | What to show | Animate in Remotion |
| --- | --- | --- | --- | --- | --- | --- | --- |

Asset types:

- thumbnail background
- thumbnail composition
- thumbnail family preview
- realistic YouTube thumbnail
- channel/page mockup
- playlist shelf mockup
- end-screen card system
- full section plate
- reusable component
- UI mockup
- framework diagram
- citation/source element
- archive/video tile
- transition plate
- texture/background
- CTA/end-frame system
- alternate crop/detail

Build routes:

- generate
- rebuild in Remotion
- use existing asset
- generate then annotate in Remotion
- optional

For generated YouTube asset packs, also track:
- YouTube role: `thumbnail_background`, `thumbnail_composition`, `thumbnail_family_preview`, `channel_mockup`, `playlist_mockup`, `section_plate`, `component_source`, `ui_rebuild_reference`, `diagram_rebuild_reference`, `texture_plate`, `transition_plate`, `end_screen_plate`, or `cta_plate`
- Visual world: `cream_editorial`, `dark_archive`, `product_ui`, `physical_product`, `search_friction`, `channel_packaging`, or `cta`
- Trigger phrases: section headings, narration phrases, or chapter moments that cause the asset to appear
- Rebuild in Remotion: exact text, official logo, counters, citations, diagrams, badges, source rows, and UI details

## YouTube Asset Manifest

For generated YouTube visual packs, write `youtube-asset-manifest.json` beside the generated images:

```json
[
  {
    "id": "thumbnail-archive-to-ip-background",
    "file": "assets/generated-youtube-visuals/thumbnail-archive-to-ip-background.png",
    "youtube_role": "thumbnail_background",
    "visual_world": "cream_editorial",
    "section": "thumbnail packaging",
    "trigger_phrases": ["archive", "intellectual property"],
    "packaging_use": "thumbnail base with clean 2-5 word headline zone",
    "text_policy": "no baked headline; design or Remotion adds exact title text",
    "motion_intent": "can be parallaxed for intro or reused as thumbnail still",
    "rebuild_in_remotion": ["headline", "official logo", "exact video title"]
  }
]
```

Do not generate, redraw, approximate, or typeset the official CreatorCanon logo inside image assets. Reserve logo placement for design or Remotion using the official asset from universal assets.

## Prompt Template

Write prompts in this form:

```text
Filename: <stable-file-name.png>
Use case: <taxonomy slug>
Asset type: <thumbnail background / section plate / component / etc.>
Aspect ratio: 16:9 horizontal, 1920x1080 unless another format is requested
Video section: <section label or timestamp>
Main composition: <what the viewer sees>
Key objects: <objects, UI, diagrams, cards, source elements, people if needed>
Style: <brand/style system>
Palette: <brand colors or visual palette>
Text allowed inside image: <short UI labels only, or none>
Text to leave for Remotion: <headlines, captions, citations, detailed labels>
Motion intent: <how the asset will be animated later>
Safe area: <negative space and title-safe notes>
Constraints: <readability, source-plate requirements, no clutter>
Realism notes: <YouTube packaging fidelity, camera/lens or UI fidelity, lighting, material, channel consistency>
Avoid: <negative prompt, including AI artifacts, fake platform stats, fake citations, random glyphs, warped UI>
```

## CreatorCanon Visual Defaults

When the video is for CreatorCanon:

- Follow `references/creatorcanon-youtube-visual-system.md` for realistic YouTube packaging, channel-context assets, long-form section systems, and manifest rules.
- Use cream paper as the default surface: `#F5F1EA`, `#EFEAE0`, white cards, `#1C1C1E` ink, and `#6B6B70` muted text.
- Use `#D97706` only for citations, step markers, small structural labels, timestamps, and source accents.
- Use sage green only for verified/outcome moments in light scenes.
- Use near-black scenes only for problem, insight, or CTA beats, with insight purple as the single accent.
- Make visuals feel like a premium knowledge operating system: archive cards, timestamps, citations, search, framework maps, source libraries, dashboards, and Knowledge Hub UI.
- Show creators as experts with bodies of work, not as generic influencers.
- Make the channel feel real: recurring thumbnail system, consistent title rhythm, credible creator-expert tone, polished banner/avatar treatment, playlist shelves, and end-screen assets that look like they belong together.
- Make thumbnails feel like strategic YouTube packaging: bold focal object, 2-5 words, strong contrast, one visible tension, mobile readability, and CreatorCanon's archive-to-asset motif.
- Avoid neon SaaS gradients, generic AI robots, stock creators pointing at laptops, loud YouTube aesthetics, fake social-media virality screens, fake YouTube metrics, fake verified badges, and long baked-in copy.

## Long-Form Visual Coverage

For every full YouTube video, cover these categories when possible:

- 1-3 thumbnail concepts with background, text area, and focal object.
- 1 thumbnail family preview showing how this upload fits the channel.
- 1 realistic channel/page or playlist mockup when the script discusses authority, archive structure, or future-state positioning.
- 1 cold-open visual hook.
- 2-4 problem/friction systems.
- 2-4 diagnosis/explanation systems.
- 2-4 false-solution or comparison visuals.
- 2-5 reframe/mechanism visuals.
- 1-3 framework or model diagrams.
- 2-4 future-state/outcome visuals.
- 1 CTA/end-frame system.
- 6-15 reusable components: cards, nodes, citation chips, video tiles, search rows, source badges, arrows, map nodes, chapter markers.
- 3-6 transition or texture plates for motion variety.

## Thumbnail Rules

Treat thumbnail concepts separately from in-video assets.

Good CreatorCanon thumbnail direction:

- one clear strategic tension
- 2-5 words of thumbnail text
- strong focal object, not a collage of tiny details
- archive/productization metaphor visible at a glance
- CreatorCanon brand palette without looking like a SaaS ad
- readable on mobile
- realistic enough to sit beside serious educational/business YouTube videos
- consistent with a repeatable CreatorCanon channel style

Thumbnail text examples:

- OLD VIDEOS, NEW ASSET
- YOUR HIDDEN IP
- PLAYLISTS AREN'T ENOUGH
- CONTENT IS TRAPPED
- THE ARCHIVE PRODUCT

Do not create thumbnails that rely on generic shock faces, red arrows, money stacks, fake analytics, or loud creator-economy hype.

Thumbnail composition examples:

- A real laptop screen on a warm desk showing a blurred grid of old video thumbnails on the left and a clean knowledge hub interface on the right, with a large empty headline zone.
- A premium browser-style channel page where scattered video tiles are being reorganized into a structured source library, with realistic shadows and no fake metrics.
- A close-up of physical archive cards, timestamp chips, and a clean product map, photographed like an editorial business magazine cover.
- A dark insight beat with one illuminated archive tile turning into a cited lesson card, leaving high-contrast space for 2-4 words.

Prompt example:

```text
Filename: thumbnail-playlists-not-enough.png
Use case: realistic-youtube-thumbnail
Asset type: thumbnail composition
Aspect ratio: 16:9 horizontal, 1920x1080
Video section: YouTube thumbnail
Main composition: A believable premium YouTube thumbnail for a serious creator business channel. Left side shows a messy playlist column and scattered video tiles. Right side shows a clean source-backed Knowledge Hub interface with citation chips and organized lesson cards. One strong focal transformation from scattered archive to structured asset.
Key objects: laptop screen, archive video tiles, source citation markers, clean knowledge map, subtle CreatorCanon mark area
Style: realistic editorial/product photography blended with polished UI mockup, not cartoon, not generic SaaS ad
Palette: CreatorCanon cream paper, ink black, muted grey, restrained amber accents
Text allowed inside image: no baked-in headline; only tiny abstract UI lines, no readable fake metrics
Text to leave for Remotion/design: 2-5 word thumbnail headline
Motion intent: can be parallaxed and split into before/after layers
Safe area: large clean headline space in upper left, focal object readable at mobile size
Constraints: professional, believable, coherent channel identity, no clutter
Realism notes: realistic screen reflections, natural desk shadows, aligned UI spacing, no warped browser chrome
Avoid: shock face, red arrows, money stacks, fake views, fake subscribers, fake verified badge, distorted UI, random glyphs, long text, AI robot
```

## Channel Realism Rules

When creating channel, playlist, or platform-context visuals:

- Build a coherent fictional CreatorCanon channel system if real channel details are not provided.
- Use a consistent avatar/logo treatment, banner style, thumbnail family, title rhythm, and playlist naming convention.
- Show enough interface context to feel like a real channel, but keep brand/platform marks secondary.
- Use placeholder or abstracted metrics unless the user provides exact values.
- Prefer credible titles like "Why Your Archive Is Unorganized IP" or "Playlists Are Not Learning Systems" over generic filler.
- Keep UI layout believable: aligned rows, consistent thumbnail ratios, real spacing, restrained metadata, and no impossible widgets.
- Treat the channel as proof of authority, not as a fake social proof machine.

Channel mockup prompt example:

```text
Filename: channel-page-creatorcanon-authority-grid.png
Use case: realistic-channel-mockup
Asset type: channel/page mockup
Aspect ratio: 16:9 horizontal, 1920x1080
Video section: Future-state channel authority visual
Main composition: A believable fictional CreatorCanon YouTube channel page shown in a clean browser frame. Premium banner at top, consistent avatar area, organized video grid with 6-8 thumbnails that share a visual system around archives, citations, and Knowledge Hubs. The page feels like a real serious educational channel, not a template.
Key objects: channel banner, thumbnail grid, playlist shelf, archive-to-asset thumbnail family, subtle CreatorCanon visual motifs
Style: realistic browser/product UI mockup with editorial polish
Palette: CreatorCanon cream paper, ink black, soft grey metadata, amber citation accents
Text allowed inside image: short fictional video titles only if legible; no fake metrics
Text to leave for Remotion/design: exact channel copy, subscriber count, labels, captions
Motion intent: can zoom from channel overview into one thumbnail or playlist shelf
Safe area: center grid readable, margins clean for camera movement
Constraints: no real platform claims, no fake verification, no clutter, consistent thumbnail system
Realism notes: accurate thumbnail proportions, believable spacing, subtle browser chrome, clean typography
Avoid: real YouTube logo as focal point, fake verified badge, fake subscriber/view counts, warped UI, tiny unreadable text, random icons
```

## Remotion Handoff Rules

For each asset plan, include implementation notes:

- which assets are scene plates
- which elements should be rebuilt as React/CSS/SVG
- which elements need word/phrase timing triggers
- which visuals support chapter transitions
- which assets need parallax/crop/camera motion
- which text must be added in Remotion, not baked into the image
- where `youtube-asset-manifest.json` lives and which files are thumbnails, section plates, components, UI references, diagrams, or end-screen plates

Prefer programmatic rebuilds for exact text and source-backed details. Generated images should supply mood, composition, texture, high-level mockups, and hard-to-illustrate concepts.

## Output Modes

Choose the mode based on the user's request.

### Mode 1 - Visual Asset Plan

Use when the user asks for a plan, breakdown, shot list, or visual direction.

Return:

1. Visual thesis
2. Section visual map
3. Asset plan table
4. Remotion handoff notes
5. Thumbnail concepts
6. Generation priorities

### Mode 2 - Prompt Pack

Use when the user asks for prompts only.

Return:

1. Visual thesis
2. Asset plan table
3. Image generation prompts
4. Negative prompt rules
5. Remotion rebuild list

### Mode 3 - Generate Visual Assets

Use when the user asks to generate images or create the asset pack end to end.

Return:

1. Source used
2. Asset plan summary
3. Generated file paths
4. Regeneration notes if any
5. Remotion handoff notes
6. Missing dependencies or skipped assets

### Mode 4 - Thumbnail Concepts

Use when the user asks only for thumbnail ideas, thumbnails, packaging, or title/thumbnail pairs.

Return:

1. Thumbnail strategy
2. 5-10 thumbnail concepts
3. Text options
4. Visual composition prompts
5. Best 3 title/thumbnail pairings

### Mode 5 - Remotion Visual System

Use when the user wants visuals for a Remotion YouTube build.

Return:

1. Visual thesis
2. Section/component architecture
3. Asset plan table
4. Timing/trigger notes
5. Generated asset prompts
6. Programmatic rebuild list
7. Quality checks

## Common Mistakes

Avoid:

- treating a 6-9 minute YouTube video like a 60-second reel
- generating one static image per section and calling it done
- baking long script lines into images
- creating visuals that do not map to a section, beat, or argument
- making every visual a dashboard or every visual an archive grid
- using tiny text that will fail on mobile playback
- inventing citations, timestamps, creator stats, source titles, or product screenshots
- using generic AI or creator-economy stock imagery
- ignoring a brand guide that exists beside the script
- stopping at prompts when the user asked to generate assets end to end
- creating thumbnails that look like pitch-deck covers instead of real YouTube thumbnails
- making channel mockups with random thumbnail styles, fake metrics, or inconsistent branding
- accepting AI-looking UI with warped type, random glyphs, impossible browser layouts, or illegible details

## Quality Gate

Before final response, verify:

- The source script, outline, or topic is identified.
- The plan is horizontal 16:9 unless the user requested otherwise.
- The visual thesis carries through the video.
- The asset plan includes thumbnail, section systems, reusable components, transitions, and CTA.
- For generated asset packs, `youtube-asset-manifest.json` exists beside the images and classifies each asset's YouTube role, visual world, section, trigger phrases, text policy, motion intent, and rebuild notes.
- Generated image prompts specify allowed in-image text and text left for Remotion.
- Thumbnail prompts include focal object, headline area, mobile readability, channel consistency, and negative prompts against fake metrics/clickbait.
- Channel/page mockup prompts avoid fake stats and define a coherent fictional CreatorCanon channel system.
- `imagegen` was used for live generation unless unavailable or the user requested prompts only.
- Generated files exist at the reported paths when generation was requested.
- CreatorCanon brand rules were applied when relevant.
- Remotion handoff notes distinguish generated plates from programmatic rebuilds.
- The official CreatorCanon logo was not generated inside image assets.
- Any generation failures, missing credentials, or assets needing manual review are reported plainly.
