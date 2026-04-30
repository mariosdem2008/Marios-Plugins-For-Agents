# Voiceover-Synced Trailer Workflow

## Timing First

1. Generate or import the final voiceover.
2. Extract word timings into seconds and frames.
3. Group words into phrase beats.
4. Build visuals around those phrase beats.

Recommended timing object:

```ts
type TimedWord = {
  text: string;
  start: number;
  end: number;
  from: number;
  to: number;
};

type PhraseTiming = {
  id: string;
  text: string;
  from: number;
  to: number;
  words: TimedWord[];
};
```

Use phrase starts and word triggers directly in Remotion `Sequence` placement and component delays.

## Reel Canvas And Safe Zones

Use `1080x1920`, `9:16`, `30fps` for CreatorCanon reels unless the user requests a different export.

Full-bleed backgrounds may touch the canvas edges, but critical content must stay inside these 1080x1920 safe rectangles:

```ts
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

Keep captions, logos, CTA text, headlines, faces, product labels, and key numbers inside these bounds. Keep the top 270px and bottom 670px free of critical information. Reserve extra right-side room for the Reels engagement rail.

## CreatorCanon Logo Asset

Always use the official CreatorCanon logo from `C:\Users\mario\Desktop\Creator Canon Social Content\universal assets`.

- Prefer `creatorcanon_logo_transparent.svg`.
- Fall back to `creatorcanon_logo_transparent.png` only when SVG cannot be used.
- Use `creatorcanon_logo_secondary.png` only when that variant is the better fit.
- Do not generate, redraw, trace, typeset, approximate, recolor, or recreate the logo.
- If the logo asset is missing, report the blocker instead of rendering a recreated mark.

Use the logo as a real image asset in CTA/end frames and explicit brand moments. Preserve its aspect ratio.

## Visual Mapping

Create a table before implementation:

| Voiceover phrase | Trigger words | Visual response |
| --- | --- | --- |
| "your audience" | audience | Audience card enters, arrow draws |
| "your business" | business | Business card enters, arrow extends |
| "DM CANON" | DM, CANON | DM card slides in, CANON highlights |

Every key UI component should have a trigger word or phrase. If it cannot be tied to narration, remove it or make it background detail.

## Subtitle Rules

- Place subtitles in `REEL_CAPTIONS`, visually bottom-anchored but above native Reels UI.
- Reveal words in sync with timing data.
- Keep a stable subtitle container so the layout does not jump.
- Keep the caption surface to one or two lines. If text wraps beyond two lines, split the subtitle beat.
- Never let the caption surface extend below `y = 1250` on a 1080x1920 reel.
- Highlight current/emphasis words, not all words at once.
- Do not show the upcoming sentence before the voiceover reaches it.

## Visual Reference Usage

Use supplied visuals in one of three ways:

1. **Programmatic rebuild**: recreate the visual as React/CSS/SVG elements so every card, label, arrow, and badge can animate independently.
2. **Intentional crop**: crop into a meaningful region such as a dashboard panel, citation chip, video stack, or CTA detail.
3. **Design reference**: use colors, hierarchy, typography, spacing, and component style without rendering the image itself.

Avoid using the entire visual as a static poster. If a full visual is shown, it still needs camera movement, masked reveal, overlays, and a deliberate exit.

## Transition Variety

Use the story to choose transition type:

- Chaos to search: scattered cards smear into search rows.
- Search to product: search bar expands or wipes into a product card.
- Product to hub: cards converge into a central hub.
- Hub to outcomes: hub emits arrows to outcome cards.
- Outcomes to CTA: cards gather into the CTA panel.

Avoid using the same fade and top-down component build on every scene.

## Audit Frames

Render stills at:

- Each scene start.
- Each important word trigger.
- 6-12 frames after each important trigger.
- Each transition midpoint.
- Final CTA hold.

Create a contact sheet and inspect for sync, readability, variety, dead time, and safe-zone compliance. Use a temporary safe-zone overlay when adjusting layout or when captions/CTA placement is uncertain.
