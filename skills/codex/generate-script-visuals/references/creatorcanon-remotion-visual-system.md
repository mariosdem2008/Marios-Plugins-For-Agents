# CreatorCanon Remotion Visual System

Read this when generating CreatorCanon visual assets for Remotion trailers, reels, shorts, or voiceover-synced videos.

The goal is not to create a pack of finished posters. The goal is to create realistic, high-trust visual ingredients that `voiceover-synced-remotion-trailer` can animate from spoken-word triggers.

## Contents

- Core Output Rule
- Required Dimensions
- Visual Worlds
- Reference Image Reading Rules
- Remotion Asset Roles
- Text Policy
- Logo And Platform Safety
- Prompt Recipes
- Negative Prompt Baseline
- Pack Composition Guidance
- Final Handoff Checklist

## Core Output Rule

Generate assets in three classes:

1. **Motion plates**: cinematic backgrounds or full scene bases with room for Remotion text and overlays.
2. **Component sources**: cards, panels, phones, video tiles, citation chips, search bars, product UI modules, icons, and texture plates that can be cropped or rebuilt.
3. **Poster references**: polished full compositions used as style references or optional social stills, never the default animation surface.

For a Remotion job, every asset must say what is baked into the image and what should be rebuilt in React/CSS/SVG.

## Required Dimensions

Default to exact `1080x1920`, 9:16 vertical.

If supplied references are close but not exact, such as 941x1672 vertical, preserve the composition style but generate exact Remotion dimensions. Keep important content inside a center safe area with generous top, side, and subtitle-safe bottom margins.

## Visual Worlds

Use one visual world per asset. Do not blend them casually.

### Dark Cinematic Archive

Use for scale, scattered archive, hidden value, search friction, insight, and CTA beats.

Look:
- near-black background, not pure black
- floating glass video cards with realistic thumbnails
- subtle grid, source lines, depth haze, small particles only when they imply data paths
- large count-up spaces and category badges
- realistic screen glow, thin borders, controlled reflections

Good motifs:
- 300 tutorials, 100 interviews, 50 podcasts
- video cards orbiting or converging
- timestamps and play buttons
- source paths flowing into one point
- dark phone DM CTA

Avoid:
- neon SaaS gradients
- sci-fi hologram overload
- random platform logos
- fake metrics or fake verification
- cluttered dashboards with unreadable tiny text

### Cream Editorial Knowledge

Use for claims, education, productization, source-backed trust, and solved-state product scenes.

Look:
- warm cream paper surface
- ink-black serif headline area
- clean sans-serif UI cards
- white panels with hairline borders and soft shadows
- amber for small citation or step markers
- sage only for verified/outcome moments

Good motifs:
- stacked video cards on cream paper
- Knowledge Hub card in the center
- dotted connector lines
- citation chips and source rows
- white product panels with restrained interface detail

Avoid:
- pure white background
- generic beige monotone with no hierarchy
- long baked-in copy
- decorative cards with no story function

### Product UI Solved State

Use for Knowledge Hub, organized lessons, frameworks, playbooks, source citations, and search.

Look:
- product-grade UI, not a random dashboard
- sidebar, search field, category cards, lesson pages, citation rows, source thumbnails
- consistent spacing and small labels
- realistic information density without illegible microtext

Only bake short labels that image generation can handle, such as:
- Lessons
- Frameworks
- Playbooks
- Examples
- Citations
- Search
- Source
- 12:45

Leave long titles, exact CTA copy, subtitles, and official logo placement for Remotion.

### Photoreal CTA

Use for the final DM CANON or archive audit scene.

Look:
- realistic hand holding a modern phone
- dark Instagram-style business chat or generic dark DM interface
- typed keyword field or empty message bar for Remotion overlay
- left-side value badges such as `50+ videos`, `Expert review`, `Free archive audit`
- dark/cream split background or dark archive field behind the phone

Rules:
- Leave `DM "CANON"` and the exact CTA line for Remotion when possible.
- Do not generate the official CreatorCanon logo. Reserve a logo slot or leave clean space.
- If in-image text is required, keep it short and validate legibility.

### Physical Product Metaphor

Use for archive becoming an asset or product.

Look:
- structured binder, premium box, knowledge product cover, card deck, archive drawer, or source library
- realistic paper, leather, matte black surfaces, metal handles, edge highlights
- source cards rising from archive folders into one product object
- warm light or white glow only when it represents extraction or structure

Avoid:
- treasure chest cliches unless the script explicitly uses hidden-value language
- literal piles of documents with no knowledge-system meaning
- generated brand logo on product covers

## Reference Image Reading Rules

When the project includes CreatorCanon visual references, inventory them by meaning:

- archive scale: floating dark video cards, category labels, large numbers
- scattered content: white/cream or dark boards with thumbnails, notes, transcripts, dotted paths
- search friction: audience questions connected to too many video results
- extraction: scattered archive flows into organized cards or a hub
- Knowledge Hub UI: clean light product interface with source-backed citations
- payoff: archive branches into audience, business, and next product
- CTA: phone DM, free archive audit, CANON keyword
- component sheet: icons, chips, arrows, progress bars, citation badges, check states

Do not copy a reference as a static final slide unless the user asked for a poster. Extract the composition logic, component shapes, hierarchy, depth, and motion potential.

## Remotion Asset Roles

Classify each output in `asset-manifest.json`:

- `scene_plate`: full-frame environment for camera movement and overlays
- `component_source`: isolated cards, phones, product objects, or UI modules
- `crop_source`: larger image intended to be cropped into meaningful regions
- `ui_rebuild_reference`: product UI or diagram that should be recreated programmatically
- `poster_reference`: polished still used for style or social output
- `texture_plate`: paper, dark grid, archive haze, light beam, or source-line texture
- `cta_plate`: end-frame base for official logo and CTA overlay

Prefer one scene plate plus 2-5 component sources for major beats instead of one fully baked poster.

## Text Policy

Use in-image text sparingly.

Safe short labels:
- Tutorials
- Interviews
- Podcasts
- Livestreams
- Old Uploads
- Lessons
- Frameworks
- Playbooks
- Examples
- Citations
- Source-backed
- 12:45
- 18:32
- 24:10

Leave these for Remotion:
- main headlines
- full CTA lines
- subtitles
- exact script lines
- exact creator names or channel claims
- official CreatorCanon logo and wordmark
- counters that should animate
- long lesson titles

If a poster reference needs baked text, keep it short and include a text validation note in the handoff.

## Logo And Platform Safety

- Never generate, redraw, trace, approximate, or typeset the official CreatorCanon logo.
- For final CreatorCanon videos, the Remotion skill must place the official logo from universal assets.
- Avoid real platform trademarks as focal points unless the user supplies explicit assets.
- Use fictional platform-style UI when showing archive cards, search results, or DM screens.
- Do not invent real subscriber counts, revenue claims, endorsements, verified badges, or citations.

## Prompt Recipes

Use these as prompt patterns, adapting the script beat and exact motif.

### Dark Archive Scale Scene Plate

```text
Filename: scene-01-archive-scale-dark.png
Use case: stylized-concept
Asset type: scene plate
Aspect ratio: 9:16 vertical, 1080x1920
Main composition: premium near-black cinematic archive space with floating realistic video cards at varied depths, category badge areas for tutorials, interviews, podcasts, livestreams, and old uploads, large negative space for animated count-up numbers
Key objects: glass video cards with play buttons and timestamps, subtle source-line paths, small category label chips, deep background cards blurred by depth of field
Style: CreatorCanon dark cinematic archive world, editorial product trailer, realistic UI glass, controlled studio lighting
Palette: Night #0B0B0D, Night Surface #1A1A1D, Paper on Night #F4F1EA, small Insight Purple only if the beat is an insight
Text allowed inside image: short category labels only; no long headline
Text to leave for Remotion: main claim, large numbers, official logo, subtitles
Motion intent: Remotion adds count-up numbers, card parallax, line drawing, and word-triggered category reveals
Avoid: fake platform logos, unreadable microtext, neon gradients, random glyphs, warped UI, plastic faces, cluttered dashboards
```

### Cream Scattered Ideas Board

```text
Filename: scene-02-scattered-ideas-cream.png
Use case: infographic-diagram
Asset type: crop source
Aspect ratio: 9:16 vertical, 1080x1920
Main composition: warm cream editorial canvas with realistic video cards, transcript scraps, sticky notes, quote cards, timestamp chips, and dotted connector paths showing ideas scattered across formats
Key objects: video thumbnails, note scraps, transcript card, framework checklist, timestamp badges, muted connector lines
Style: premium research-board layout, calm editorial CreatorCanon visual identity
Palette: Paper #F5F1EA, Card White #FFFFFF, Canon Ink #1C1C1E, Connector Grey #C9C5BD, small amber and sage markers only
Text allowed inside image: short labels like Tutorial, Interview, Podcast, Transcript, 12:45
Text to leave for Remotion: headline and narration-specific copy
Motion intent: Remotion crops individual notes/cards, draws dotted paths, and reveals timestamps on spoken words
Avoid: messy scrapbook chaos, illegible handwriting, random filler notes, pure white page, cartoon stickers
```

### Search Friction Scene

```text
Filename: scene-03-search-friction.png
Use case: ui-mockup
Asset type: ui rebuild reference
Aspect ratio: 9:16 vertical, 1080x1920
Main composition: realistic search-results interface on warm paper showing too many video results, with audience question bubbles connected to the search panel
Key objects: search bar, stacked result rows, thumbnails, duration chips, question bubbles, subtle warning area
Style: clean product UI plus editorial poster composition, high trust and readable hierarchy
Palette: cream paper, white cards, Canon Ink, muted grey, restrained amber warning accent
Text allowed inside image: short generic UI labels and timestamps only
Text to leave for Remotion: exact question copy, headline, final warning line
Motion intent: Remotion types the search query, reveals results, connects question bubbles, highlights "too many results"
Avoid: fake YouTube branding as focal point, real creator names, fake view counts, cluttered tiny rows, red alert styling
```

### Knowledge Hub Product UI

```text
Filename: scene-05-knowledge-hub-ui.png
Use case: ui-mockup
Asset type: ui rebuild reference
Aspect ratio: 9:16 vertical, 1080x1920
Main composition: polished light Knowledge Hub interface with sidebar, search field, category cards, knowledge pages, source rows, citation cards, and one lesson detail area
Key objects: white product panels, card grid, source thumbnail placeholders, citation chips, checkmarks, tabs
Style: premium knowledge operating system, clean SaaS-grade UI but warm editorial CreatorCanon surface
Palette: Paper #F5F1EA, Card White #FFFFFF, Canon Ink #1C1C1E, Soft Ink #6B6B70, sage checkmarks, tiny amber source markers
Text allowed inside image: Lessons, Frameworks, Playbooks, Citations, Search, Source, short timestamps
Text to leave for Remotion: exact page titles, official logo, subtitles, CTA
Motion intent: Remotion rebuilds or overlays UI modules, reveals categories and citation rows from word timings
Avoid: generic dashboard widgets, neon blue SaaS UI, fake analytics, unreadable microtext, random icons
```

### Archive To Product Metaphor

```text
Filename: scene-06-archive-to-structured-asset.png
Use case: product-mockup
Asset type: scene plate
Aspect ratio: 9:16 vertical, 1080x1920
Main composition: realistic archive drawer or premium black box with labeled folders and video cards, source lines rising into a clean structured knowledge product object above it
Key objects: archive folders, video cards, timestamp chips, premium binder or product box, vertical light lines representing extraction
Style: cinematic physical product metaphor, precise and premium, not fantasy
Palette: near-black surfaces, warm paper highlights, white edge light, restrained amber source accents
Text allowed inside image: short labels like YouTube Archive, Interviews, Podcasts, Structured Asset
Text to leave for Remotion: main headline, official logo, longer product copy
Motion intent: Remotion animates source-line extraction, product lift, glow, and final label overlay
Avoid: treasure chest cliche, magical clutter, unreadable folder labels, fake logo on the product cover
```

### Audience Business Product Payoff

```text
Filename: scene-07-archive-to-outcomes.png
Use case: infographic-diagram
Asset type: scene plate
Aspect ratio: 9:16 vertical, 1080x1920
Main composition: dark cinematic top archive panel branching through glowing source paths into three outcome panels: Audience, Business, Next Product
Key objects: archive video card cluster, three tall outcome cards, subtle metrics placeholders, product object, community/library panel, authority/trust panel
Style: premium dark product trailer diagram with realistic UI depth
Palette: Night, Night Surface, Paper on Night, white linework, one restrained accent based on beat
Text allowed inside image: Audience, Business, Next Product only
Text to leave for Remotion: exact outcomes, metrics, logo, subtitles
Motion intent: Remotion triggers each branch from spoken words and adds final values programmatically
Avoid: fake revenue claims, fake subscriber numbers, overstuffed dashboards, neon lines
```

### Photoreal DM CANON CTA

```text
Filename: scene-08-dm-canon-cta-phone.png
Use case: product-mockup
Asset type: cta plate
Aspect ratio: 9:16 vertical, 1080x1920
Main composition: realistic hand holding a modern phone with dark DM interface, message input area left clean for keyword overlay, value badges on the left, dark archive cards fading behind, cream or white light edge on one side
Key objects: phone, hand, dark chat screen, blank profile/logo slot, value badges, archive card background, clean send button area
Style: photoreal premium CTA, editorial studio lighting, believable phone reflections and finger anatomy
Palette: Night #0B0B0D, Paper on Night #F4F1EA, Card White, Canon Ink, small sage or amber only for value cues
Text allowed inside image: short badge labels only if readable
Text to leave for Remotion: DM "CANON", free archive audit line, official logo, exact profile name
Motion intent: Remotion types CANON, highlights the CTA, places official logo, and animates badges in sync
Avoid: distorted hands, warped keyboard, fake Instagram claims, generated CreatorCanon logo, illegible chat text, glossy ad look
```

## Negative Prompt Baseline

Append or adapt this to CreatorCanon prompts:

```text
Avoid generic AI gloss, neon SaaS gradients, impossible UI, distorted hands, warped phone, plastic faces, fake logos, recreated CreatorCanon logo, real platform trademarks as focal point, fake verified badges, fake analytics, random glyphs, unreadable tiny text, cluttered dashboards, overfilled panels, stock creator pointing at laptop, shock-face thumbnail style, money stacks, red arrows, cartoon stickers, pure black background, pure white background.
```

## Pack Composition Guidance

For a 35-90 second CreatorCanon trailer, target:

- 5-8 scene plates
- 8-14 component or crop-source assets
- 3-5 product UI or UI rebuild references
- 2-4 texture or transition plates
- 1-2 CTA plates
- optional poster references only after motion assets are covered

Useful paired outputs:
- archive-scale scene plate plus isolated video-card stack
- search-friction UI reference plus blank search panel component
- Knowledge Hub full UI plus isolated citation chip/cards
- CTA phone plate plus blank CTA card component
- dark source-line texture plus cream dotted-connector texture

## Final Handoff Checklist

Before reporting the pack as ready for Remotion:

- `asset-manifest.json` exists and covers every generated file.
- Every asset has a Remotion role and visual world.
- Trigger words are tied to the voiceover or script beat.
- Text that should animate is not baked into the image.
- Official CreatorCanon logo is not generated inside any image.
- Poster-style files are marked as `poster_reference`.
- UI-heavy files identify which parts should be rebuilt programmatically.
- CTA plate leaves room for the official logo and exact DM CANON copy.
- Assets are exact 1080x1920 unless another target was requested.
