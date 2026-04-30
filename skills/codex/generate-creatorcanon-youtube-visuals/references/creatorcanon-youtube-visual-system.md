# CreatorCanon YouTube Visual System

Read this when planning or generating CreatorCanon visuals for long-form YouTube videos, authority videos, video essays, tutorials, animated explainers, or Remotion YouTube builds.

The goal is to make a credible CreatorCanon YouTube channel ecosystem: publishable thumbnails, believable channel/page mockups, section-level visual systems, reusable components, and motion-ready source plates that can support 6-12 minute videos.

## Contents

- Core Output Rule
- Required Dimensions
- YouTube Asset Roles
- Visual Worlds
- Thumbnail Packaging System
- Channel And Platform Context
- Long-Form Section Systems
- Text Policy
- Logo And Claim Safety
- Prompt Recipes
- Negative Prompt Baseline
- Pack Composition Guidance
- Final Handoff Checklist

## Core Output Rule

Generate YouTube assets as a reusable channel system, not as isolated pretty images.

Each pack should include:

1. **Packaging assets**: thumbnail backgrounds/compositions, thumbnail family previews, channel or playlist context, and end-screen plates.
2. **Section assets**: horizontal scene plates, explanation diagrams, chapter cards, source plates, and transition textures.
3. **Component sources**: video cards, citation chips, search rows, Knowledge Hub panels, archive stacks, nodes, badges, icons, and CTA cards.
4. **Programmatic rebuild references**: UI-heavy or text-heavy visuals that should be rebuilt in Remotion for exact text and timing.

For generated packs, write `youtube-asset-manifest.json` and classify every file by its YouTube role, visual world, section, packaging use, text policy, motion intent, and rebuild notes.

## Required Dimensions

Default to exact `1920x1080`, 16:9 horizontal.

Use 16:9 for:
- thumbnails
- channel mockups
- section plates
- framework diagrams
- end-screen systems
- Remotion YouTube scenes

Only use vertical or square crops when the user explicitly asks for Shorts, community posts, or platform variants.

## YouTube Asset Roles

Use these roles in `youtube-asset-manifest.json`:

- `thumbnail_background`: visual base with clean headline zone
- `thumbnail_composition`: near-final thumbnail still, usually with only short placeholder text or none
- `thumbnail_family_preview`: row/grid showing how this upload fits the channel style
- `channel_mockup`: believable fictional channel page or video grid
- `playlist_mockup`: playlist shelf or course-like sequence
- `section_plate`: full 16:9 scene base for a video section
- `component_source`: isolated cards, tiles, phones, panels, badges, icons, or product objects
- `ui_rebuild_reference`: UI composition to recreate in React/CSS/SVG
- `diagram_rebuild_reference`: framework or model to rebuild programmatically
- `texture_plate`: paper, dark grid, source-line, blur, light, or archive texture
- `transition_plate`: asset intended for wipes, match cuts, gathers, or camera moves
- `end_screen_plate`: final YouTube end-screen base with space for recommended videos and subscribe area
- `cta_plate`: CTA visual such as archive audit, DM CANON, or next-step panel

## Visual Worlds

Use one visual world per asset. Consistency matters more in long-form YouTube than in a reel.

### Cream Editorial Authority

Use for thumbnails, title moments, section headers, frameworks, productization arguments, and solved-state explanations.

Look:
- warm cream paper, not pure white
- ink-black serif headline space
- clean sans UI components
- white cards with hairline borders
- restrained amber markers for sources, steps, and citations
- sage for outcome/verified moments only

Best for:
- "your archive is IP"
- "playlists are not enough"
- "content becomes a knowledge product"
- framework and model visuals
- thumbnail backgrounds with clean title zones

### Dark Archive Tension

Use for problem, hidden value, discovery friction, buried ideas, and dramatic insight beats.

Look:
- near-black background
- floating video cards and source trails
- realistic screen glow and depth
- subtle grid or data lines
- one accent only, usually insight purple for dark insight moments

Best for:
- content trapped in old videos
- audience search friction
- archive scale
- "one insight hidden 42 minutes in"
- intro hooks and dramatic chapter openers

### Product UI Solved State

Use for Knowledge Hub, source-backed lesson pages, citation systems, search, and organized curriculum/product views.

Look:
- clean product UI with believable spacing
- sidebar, search, cards, tabs, source rows, citation chips
- information density that reads on a 16:9 YouTube frame
- no fake analytics or random widgets

Best for:
- Knowledge Hub reveal
- source-backed citations
- lesson organization
- archive-to-product transformation
- "audience can find the answer"

### Channel Packaging

Use for thumbnail family previews, fictional channel pages, playlists, video grids, and end-screen systems.

Look:
- a coherent CreatorCanon upload ecosystem
- recurring thumbnail shapes, focal objects, title rhythms, and color rules
- believable browser/channel layout without fake metrics or fake verification
- platform context secondary to the CreatorCanon visual system

Best for:
- authority proof
- "body of work" positioning
- channel flyovers
- future-state channel/product ecosystem

### Physical Product Metaphor

Use sparingly for premium productization.

Look:
- editorial product photography
- archive cards, binders, matte boxes, product covers, card decks, source folders
- realistic surfaces and shadows
- not fantasy, not treasure chest by default

Best for:
- archive becoming a product
- IP made tangible
- premium knowledge product
- "the product already exists"

## Thumbnail Packaging System

Treat thumbnails as a separate deliverable from in-video visuals.

Every thumbnail concept should define:
- strategic tension
- focal object
- 2-5 word headline zone
- mobile readability
- channel family fit
- what text is left for design

Strong CreatorCanon thumbnail tensions:
- archive vs product
- playlists vs learning systems
- old videos vs intellectual property
- search results vs answer
- scattered expertise vs structured hub
- content output vs business asset

Good headline spaces:
- upper left cream area
- right-side dark negative space
- clean central title band
- large object on one side with text on the other

Avoid:
- tiny UI details as the main hook
- generic SaaS ad layout
- fake shock faces
- red arrows
- money stacks
- "viral growth" visual language

## Channel And Platform Context

If real channel details are not supplied, create a fictional CreatorCanon channel ecosystem without pretending metrics are factual.

Rules:
- Use placeholder or abstracted metadata, not fake subscriber counts or fake view claims.
- Keep thumbnail ratios and channel rows believable.
- Make thumbnails visually related, not random.
- Use serious creator-expert title rhythms.
- Keep platform branding secondary.
- Do not add fake verified badges.

Good fictional title rhythms:
- "Why Your Archive Is Unorganized IP"
- "Playlists Are Not Learning Systems"
- "The Product Hidden In Old Videos"
- "How Source-Backed Knowledge Hubs Work"
- "Turn A Video Archive Into A Learning System"

## Long-Form Section Systems

For 6-12 minute YouTube videos, plan repeatable section systems:

- Cold open: high-contrast archive tension or bold productization claim
- Diagnosis: search friction, scattered source maps, audience question panels
- False solution: playlist/course/chatbot comparison visuals
- Reframe: archive as IP, body of work, source-backed system
- Mechanism: extraction, mapping, citation, structuring, packaging
- Proof: Knowledge Hub UI, lesson pages, source citations, framework cards
- Payoff: audience/business/product outcomes
- CTA/end screen: archive audit, next video cards, subscribe area, official logo left to design/Remotion

Prefer reusable motifs:
- chapter cards
- progress rail
- citation chip
- source card
- video tile
- search row
- before/after split
- framework node map
- Knowledge Hub panel
- end-screen recommendation cards

## Text Policy

Use in-image text sparingly.

Safe short labels:
- Archive
- Lessons
- Frameworks
- Playbooks
- Citations
- Source
- Search
- Knowledge Hub
- Tutorial
- Interview
- Podcast
- 12:45
- 18:32
- 24:10

Leave these for design or Remotion:
- thumbnail headline
- exact video title
- official CreatorCanon logo and wordmark
- exact script lines
- chapter titles
- detailed source citations
- counters that should animate
- subscriber counts, views, revenue, testimonials, or performance claims
- end-screen copy

If a thumbnail composition includes baked text, keep it to 2-5 words and flag it for legibility review.

## Logo And Claim Safety

- Do not generate, redraw, trace, approximate, or typeset the official CreatorCanon logo.
- Reserve logo placement for the official universal asset in design or Remotion.
- Do not create fake verified badges, fake subscriber counts, fake views, fake revenue claims, fake citations, or fake testimonials.
- Avoid real platform trademarks as focal points unless the user supplies exact assets.
- Keep brand/page mockups fictional and coherent.

## Prompt Recipes

Adapt these recipes to the source video's argument.

### Thumbnail Background - Archive To IP

```text
Filename: thumbnail-archive-to-ip-background.png
Use case: realistic-youtube-thumbnail
Asset type: thumbnail background
Aspect ratio: 16:9 horizontal, 1920x1080
Video section: thumbnail packaging
Main composition: premium CreatorCanon thumbnail base with a warm cream headline zone on the left and a realistic stack of old video cards transforming into a clean knowledge product object on the right
Key objects: layered video cards, timestamp chips, source markers, premium product card or Knowledge Hub panel, subtle dotted connectors
Style: realistic editorial product photography blended with polished UI mockup, serious educational creator channel
Palette: Paper #F5F1EA, Card White #FFFFFF, Canon Ink #1C1C1E, muted grey, restrained amber source accents
Text allowed inside image: none except tiny abstract UI marks
Text to leave for design/Remotion: 2-5 word thumbnail headline, official logo, exact title
Motion intent: can be parallaxed for intro and exported as thumbnail still
Safe area: large clean headline zone, focal object readable at mobile size
Avoid: fake logo, fake metrics, red arrows, money stacks, shock face, warped UI, random glyphs, generic SaaS gradient
```

### Channel Family Preview

```text
Filename: channel-family-preview-archive-assets.png
Use case: realistic-channel-mockup
Asset type: thumbnail family preview
Aspect ratio: 16:9 horizontal, 1920x1080
Video section: channel packaging
Main composition: a believable row of 6 CreatorCanon thumbnail concepts in a clean channel grid, all sharing a premium archive-to-asset visual language but each with a different focal object
Key objects: thumbnail row, channel page surface, recurring archive cards, Knowledge Hub UI, product objects, source markers
Style: realistic browser/channel layout with editorial polish, coherent serious creator business channel
Palette: cream editorial base, ink headlines, dark archive thumbnails for problem videos, restrained amber markers
Text allowed inside image: short generic thumbnail words only if legible; no fake metrics
Text to leave for design/Remotion: exact titles, subscriber count, official logo
Motion intent: can zoom into the selected upload or become a channel authority scene
Avoid: fake verified badge, fake view counts, platform logo as focal point, inconsistent thumbnail styles, tiny unreadable text
```

### Section Plate - Search Friction

```text
Filename: section-03-search-friction-results.png
Use case: ui-mockup
Asset type: section plate
Aspect ratio: 16:9 horizontal, 1920x1080
Video section: audience cannot find the answer
Main composition: warm cream editorial frame with a large search results panel on the right and audience question bubbles on the left, showing that too many old videos still do not reveal the answer
Key objects: search bar, result rows, video thumbnails, timestamps, question bubbles, warning strip area
Style: believable product UI plus editorial explanatory composition, not a real platform screenshot
Palette: Paper, Card White, Canon Ink, Soft Ink, restrained amber warning/source marker
Text allowed inside image: short UI labels and timestamp chips only
Text to leave for Remotion: exact questions, search query, warning copy, subtitles
Motion intent: Remotion types query, reveals rows, connects question bubbles, highlights the problem line
Safe area: room for lower-third subtitles and chapter label
Avoid: fake YouTube branding, fake view counts, clutter, unreadable results, red alert styling
```

### Product UI - Knowledge Hub Lesson

```text
Filename: section-06-knowledge-hub-lesson-ui.png
Use case: ui-mockup
Asset type: ui rebuild reference
Aspect ratio: 16:9 horizontal, 1920x1080
Video section: solved state / Knowledge Hub reveal
Main composition: polished CreatorCanon Knowledge Hub lesson page with sidebar, source video card, key takeaways, citation rows, related lessons, and clean product hierarchy
Key objects: sidebar, lesson hero, embedded video thumbnail placeholder, citation chips, source rows, progress/action card
Style: premium knowledge operating system, realistic SaaS-grade UI on warm editorial surface
Palette: Paper, Card White, Canon Ink, Soft Ink, sage verified markers, tiny amber source markers
Text allowed inside image: Lessons, Frameworks, Citations, Source, short timestamps
Text to leave for Remotion: exact lesson title, body copy, official logo, citations, source titles
Motion intent: Remotion rebuilds exact UI panels, reveals citations and cards from narration timing
Avoid: generic analytics dashboard, neon blue UI, fake data, unreadable microtext, random icons
```

### Framework Diagram Rebuild Reference

```text
Filename: diagram-archive-to-product-system.png
Use case: infographic-diagram
Asset type: diagram rebuild reference
Aspect ratio: 16:9 horizontal, 1920x1080
Video section: mechanism / archive transformation model
Main composition: clean cream editorial framework diagram showing video archive inputs flowing through extraction, structure, citations, and packaging into a Knowledge Hub
Key objects: archive cards, process columns, dotted connectors, citation chips, final hub card
Style: editorial strategy diagram, clear enough for YouTube playback, designed to be rebuilt in Remotion
Palette: cream paper, white cards, ink text, connector grey, amber step markers, sage verified final state
Text allowed inside image: very short process labels only
Text to leave for Remotion: all exact labels, titles, and explanations
Motion intent: Remotion draws connectors, reveals steps one by one, animates cards into final hub
Avoid: crowded flowchart, tiny labels, rainbow colors, generic business icons
```

### Dark Archive Insight Plate

```text
Filename: section-02-hidden-insight-dark.png
Use case: source-plate
Asset type: section plate
Aspect ratio: 16:9 horizontal, 1920x1080
Video section: hidden value in old videos
Main composition: near-black cinematic archive environment with one illuminated video card and a highlighted timestamp area, background cards receding into depth
Key objects: large video tile, play button, timeline scrubber, timestamp chip, subtle source lines, blurred archive cards
Style: cinematic CreatorCanon dark archive world, documentary tech trailer, controlled glow
Palette: Night #0B0B0D, Night Surface #1A1A1D, Paper on Night #F4F1EA, Insight Purple only for the highlighted timestamp
Text allowed inside image: timestamp only
Text to leave for Remotion: headline, exact insight copy, subtitles, logo
Motion intent: Remotion pushes into timestamp, highlights phrase, transitions to citation card
Avoid: neon grid overload, random UI glyphs, fake platform logo, clutter, pure black
```

### End Screen Plate

```text
Filename: end-screen-archive-audit-next-videos.png
Use case: concept-visual
Asset type: end-screen plate
Aspect ratio: 16:9 horizontal, 1920x1080
Video section: CTA / end screen
Main composition: warm cream CreatorCanon end-screen base with official logo space, two clean recommended-video card areas, one subscribe/avatar area, and a calm archive audit CTA panel
Key objects: empty video recommendation cards, source-line texture, CTA panel, subtle archive cards, clean logo slot
Style: premium YouTube end screen, editorial and product-like, not salesy
Palette: Paper, Card White, Canon Ink, Soft Ink, restrained amber source marker, sage CTA check if appropriate
Text allowed inside image: none or short placeholder labels only
Text to leave for Remotion: official logo, exact CTA, recommended video titles, subscribe text
Motion intent: Remotion places official logo and clickable end-screen safe areas, animates CTA in sync
Avoid: generated logo, fake subscriber claims, cluttered outro, loud button styling
```

## Negative Prompt Baseline

Append or adapt this to CreatorCanon YouTube prompts:

```text
Avoid generic AI gloss, neon SaaS gradients, impossible UI, distorted browser chrome, warped typography, fake logos, recreated CreatorCanon logo, fake verified badges, fake analytics, fake subscriber counts, fake view counts, fake revenue claims, fake citations, random glyphs, unreadable tiny text, cluttered dashboards, shock-face thumbnail style, red arrows, money stacks, stock creator pointing at laptop, cartoon stickers, pure white background, pure black background.
```

## Pack Composition Guidance

For a 6-12 minute CreatorCanon YouTube video, target:

- 2-4 thumbnail concepts or backgrounds
- 1 thumbnail family preview
- 1 channel/page or playlist mockup when authority or channel context matters
- 6-10 section plates or UI/diagram references
- 10-20 reusable component sources
- 3-6 texture or transition plates
- 1 CTA or end-screen plate

Useful paired outputs:
- thumbnail background plus thumbnail family preview
- channel page overview plus selected thumbnail crop
- search friction section plate plus blank search-row component
- Knowledge Hub UI reference plus citation chip/card components
- framework diagram reference plus isolated process cards
- end-screen plate plus CTA card component

## Final Handoff Checklist

Before reporting the pack as ready:

- `youtube-asset-manifest.json` exists and covers every generated file.
- Every asset has a YouTube role and visual world.
- Thumbnail assets define headline safe area and mobile readability.
- Channel mockups avoid fake metrics and fake verification.
- Text that needs accuracy is left for design or Remotion.
- Official CreatorCanon logo is not generated inside images.
- UI-heavy and diagram-heavy assets identify what should be rebuilt programmatically.
- End-screen assets leave space for official logo, recommendation cards, and CTA copy.
- Assets are exact 1920x1080 unless the user requested another format.
