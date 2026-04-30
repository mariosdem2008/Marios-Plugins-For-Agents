---
name: creatorcanon-hub-builder
description: Use when a user asks to build, plan, implement, ship, continue, or verify a CreatorCanon Knowledge Hub from a creator video audit, generated hub mockup, creator-audit.md, *VIDEO_AUDIT.md, hub-build-prompt-filled.md, or CreatorCanon project folder.
---

# CreatorCanon Hub Builder

Build a premium CreatorCanon Knowledge Hub from a creator video audit and generated visual mockup. The output is a source-backed learning product with structured lessons, frameworks, playbooks, search, and timestamp citations; it is not a transcript dump or generic marketing site.

## Required Inputs

Resolve a creator project folder that contains:

- A creator audit file named `creator-audit.md`, `*VIDEO_AUDIT.md`, or similar.
- A `mockups/` folder with at least one generated mockup image (`.png`, `.jpg`, `.jpeg`, `.webp`).

If a mockup is missing, continue only when the user explicitly accepts that limitation or the helper is run with `--allow-missing-mockup`.

## Companion Capabilities

Use these skills/plugins/tools when available. If one is missing, note it briefly and use the closest alternative:

- `frontend-design` is mandatory for visual direction.
- `animation-components` / Framer Motion for tasteful editorial motion.
- GSAP skills for scroll-triggered reveals on long-form pages.
- `core-3d-animation` only when the creator brand or mockup clearly supports a hero moment.
- Context7 MCP or primary official docs for current Next.js, MDX, Tailwind, Fuse.js, Framer Motion, and GSAP APIs before implementing.
- Playwright MCP or Playwright skill for responsive and interaction verification.
- `web-quality-audit`, `performance`, `core-web-vitals`, and `accessibility` for verification.
- `documents:documents` or available PDF/DOCX tooling only when downloadable creator-branded assets are part of the deliverable.

Do not invent library APIs. Use `tool_search` to load deferred Context7/Playwright tooling when needed.

## Workflow

1. Resolve the creator project folder. Use the folder named by the user; otherwise use the current working directory if it contains an audit; otherwise search immediate child folders.
2. Run the helper:

```powershell
python C:\Users\mario\.codex\skills\creatorcanon-hub-builder\scripts\prepare_hub_build_context.py --project "<creator-folder>"
```

3. Read the reported `audit_file`, `mockup_file`, `filled_prompt_file`, and `context_file`.
4. Inspect the mockup image with the local image viewing tool before making design decisions.
5. Treat the mockup as the authoritative visual reference for layout, density, hierarchy, palette, card styles, mobile behavior, and citation presentation.
6. Execute `hub-build-prompt-filled.md` exactly. It contains the full phase workflow and the creator audit inserted under `[CREATOR_AUDIT]`.
7. Stop after Phase 2 and wait for user approval unless the user already said `go`, `ship it`, or equivalent. If resuming after approval, continue at Phase 3.
8. Keep generated hub code and handoff artifacts inside the creator project folder unless the user explicitly asks for a different location.

## Phase Contract

The filled prompt must drive the work:

- Phase 0: Load companion skills/plugins/tools and inspect project context.
- Phase 1: Parse the audit into `_hub_plan.md`, preserving creator identity, verbatim vocabulary, canon nodes, per-video intelligence, visual moments, and evidence segment IDs.
- Phase 2: Add the sitemap and IA to `_hub_plan.md`, then pause for approval.
- Phase 3: Commit to one creator-specific design brief.
- Phase 4: Document the Next.js/MDX/Tailwind/search/citation technical plan and file tree.
- Phase 5: Build in layers: content import, layout, canon node templates, indexes/theme pages, citations, home, search, motion.
- Phase 6: Verify responsive screenshots, Lighthouse/Core Web Vitals, citation integrity, content completeness, reduced motion, and keyboard navigation.
- Phase 7: Deliver code, `README.md`, `CREATOR_NOTES.md`, verification table, and next-day recommendation.

## Hard Rules

- Source-grounding is sacred. Never fabricate quotes, citations, statistics, framework steps, examples, tools, or YouTube URLs.
- Preserve terms listed as `vocabulary preserved verbatim` exactly.
- Every audit-derived claim with an evidence segment ID needs a timestamp citation.
- If the audit lacks a public YouTube ID, use an evidence drawer or disabled outbound link and document the limitation.
- Use the creator's dominant tone and creator voice notes, not generic SaaS copy.
- Default Tailwind palette is forbidden; define a creator-specific color system.
- Mobile-first. Keep text inside containers at 375px, 768px, and 1440px.
- Honor `prefers-reduced-motion` for all motion.
- Do not declare completion until verification artifacts exist or you clearly report what could not be run.

## Output Files

The helper writes:

- `hub-build-prompt-filled.md`
- `hub-build-context.json`

The build should produce:

- `_hub_plan.md`
- Hub source code
- `README.md`
- `CREATOR_NOTES.md`
- Verification screenshots/reports
