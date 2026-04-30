# Voiceover-Synced YouTube Workflow

Use this reference when planning, implementing, or auditing a full long-form Remotion YouTube video.

## 1. Timing First

Build the edit from the final voiceover.

1. Generate or import the final narration.
2. Extract word timings into seconds and frames.
3. Group words into phrase beats.
4. Group phrase beats into video sections.
5. Derive `durationInFrames` from audio/timing.
6. Build visuals around phrase and section timing.

Recommended timing objects:

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

type SectionTiming = {
  id: string;
  title: string;
  from: number;
  to: number;
  phrases: PhraseTiming[];
  visualGoal: string;
};
```

Use phrase starts, phrase ends, and word triggers directly in Remotion `Sequence` placement and component delays.

## CreatorCanon Logo Asset

Always use the official CreatorCanon logo from `C:\Users\mario\Desktop\Creator Canon Social Content\universal assets`.

- Prefer `creatorcanon_logo_transparent.svg`.
- Fall back to `creatorcanon_logo_transparent.png` only when SVG cannot be used.
- Use `creatorcanon_logo_secondary.png` only when that variant is the better fit.
- Do not generate, redraw, trace, typeset, approximate, recolor, or recreate the logo.
- If the logo asset is missing, report the blocker instead of rendering a recreated mark.

Use the logo as a real image asset in intro signatures, final CTA/end frames, channel/package mockups, and explicit brand moments. Preserve its aspect ratio.

## 2. Section Map

Create a table before implementation:

| Section | Voiceover range | Core job | Visual system | Transition |
| --- | --- | --- | --- | --- |
| Cold open | 0:00-0:20 | Create self-recognition | Scattered archive tiles | Fast assemble into title |
| Surface problem | 1:15-2:30 | Show friction | Search failures and buried lessons | Search row wipes into diagnosis |
| Reframe | 4:45-6:15 | Shift belief | Archive-to-hub diagram | Cards converge into map |
| New model | 6:15-7:30 | Make it practical | Step framework | Step cards build one by one |
| CTA | 8:30-9:00 | Qualified next step | Calm audit panel | Hub resolves into CTA |

Each section should have one visual system that evolves. Avoid building a separate visual gag for every sentence.

## 3. Visual Mapping

Create a phrase-to-visual map before coding:

| Voiceover phrase | Trigger words | Visual response |
| --- | --- | --- |
| "50 educational videos" | 50, videos | Archive grid counts up to 50 tiles |
| "questions you already answered" | questions, answered | Audience question cards connect to old clips |
| "source-backed Knowledge Hub" | source-backed, Knowledge Hub | Citation chips attach to hub pages |
| "DM CANON" | DM, CANON | CTA panel appears, CANON highlights |

Every key UI component should have a trigger word or phrase. If an element cannot be tied to narration, make it subtle background texture or remove it.

## 4. Long-Form Caption Strategy

Use captions for clarity, not constant visual noise.

Acceptable patterns:

- bottom phrase subtitles throughout the video
- selective emphasis captions for key lines
- chapter-title captions at section starts
- callout labels tied to diagrams
- quoted source captions when the script includes source material

Rules:

- Keep captions in the lower safe area unless a diagram requires a local label.
- Do not show the next sentence before it is spoken.
- Use stable containers so subtitles do not resize the layout.
- Keep captions readable against both cream and dark scenes.
- Highlight only current/emphasis words, not the entire sentence.

## 5. Visual Systems To Prefer

Use programmatic, editable visual systems:

- archive grids with video tiles
- search bars and result rows
- citation chips and timestamp markers
- framework cards
- source-backed summary panels
- knowledge map nodes and paths
- playlist vs learning-system comparisons
- audience question inboxes
- old-video-to-product pipelines
- chapter progress markers
- final audit/CTA panel

Avoid static screenshots as the primary visual. If a screenshot is useful, crop into a meaningful detail and layer annotation, camera motion, or a rebuilt overlay.

## 6. Transition Language

Choose transitions that explain the idea:

- Scatter to structure: loose cards align into a grid.
- Search to citation: search result expands into a cited lesson card.
- Feed to system: vertical feed tiles rotate or slide into a horizontal map.
- Archive to product: video tiles extract lesson cards into a product panel.
- Problem to insight: cream scene cuts to dark cinematic insight beat.
- Insight to outcome: dark scene resolves back to cream with sage verification.
- Outcome to CTA: framework cards gather into the audit panel.

Avoid using the same fade or slide direction for every section.

## 7. Remotion Build Pattern

Prefer a structure like:

```ts
export const YouTubeVideo = ({ timing, audioSrc }: Props) => {
  return (
    <AbsoluteFill>
      <Audio src={audioSrc} />
      <BackgroundSystem timing={timing} />
      <ChapterSequences sections={timing.sections} />
      <CaptionLayer words={timing.words} />
    </AbsoluteFill>
  );
};
```

Use helpers for timing:

```ts
const frame = useCurrentFrame();
const { fps } = useVideoConfig();
const at = (seconds: number) => Math.round(seconds * fps);
const isIn = (from: number, to: number) => frame >= from && frame <= to;
```

Keep reusable primitives small:

- `ChapterTitle`
- `TimedCaption`
- `ArchiveTile`
- `CitationChip`
- `FrameworkStep`
- `KnowledgeHubMock`
- `SourcePanel`
- `CTAEndCard`

## 8. Audit Frames

Render stills at:

- 0:00 cold open frame
- each chapter start
- each important word trigger
- 6-12 frames after each important trigger
- each diagram completion frame
- subtitle-heavy frames
- transition midpoints
- final CTA hold

Create a contact sheet from the final MP4. Inspect:

- sync between voiceover and visual triggers
- subtitle placement
- small text readability
- chapter pacing
- visual variety
- safe margins
- brand consistency
- audio presence
- absence of long dead visual holds

## 9. Final Verification Commands

Use project-specific scripts when available. Otherwise, run equivalents:

```powershell
npm run typecheck
npm run build
npx remotion render [composition-id] [output.mp4]
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate,duration -of json [output.mp4]
```

If the repo uses `pnpm`, `yarn`, or custom render commands, use the existing package manager and scripts.

## 10. Final Response Checklist

Report:

- changed files
- narration source and fallback if any
- timing manifest path
- render command
- output MP4 path
- video specs from verification
- tests/checks run
- any missing env vars, assets, or limitations
