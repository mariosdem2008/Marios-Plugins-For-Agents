You are building a premium Knowledge Hub for a CreatorCanon client. CreatorCanon is a done-for-you knowledge productization service — we transform a YouTuber's video archive into a polished, source-backed Knowledge Hub: structured lessons, frameworks, playbooks, and timestamped citations that read like a premium learning product, not a transcript dump.

This is not a generic site build. It is a knowledge product with strict requirements around source-grounding, timestamp citations, search, and professional learning UX.

Use the generated mockup resolved in `hub-build-context.json` as the visual source of truth. Inspect it before design decisions, then match its layout density, hierarchy, palette, card language, mobile behavior, and citation presentation unless the audit makes that direction impossible.

═══════════════════════════════════════════════
PHASE 0 — LOAD CONTEXT (silent, no output)
═══════════════════════════════════════════════

Activate these skills/plugins/MCPs. If one is missing, note it and continue with the closest alternative:

- frontend-design (mandatory — drives the visual direction)
- animation-components bundle (Framer Motion, Magic UI, AOS, Lottie — for tasteful editorial motion, NOT 3D theatrics)
- gsap-skills (for scroll-triggered reveals on long-form pages)
- core-3d-animation bundle (only for hero moment if appropriate to creator's brand)
- Context7 MCP (pull live docs for Next.js, MDX, Fuse.js, Framer Motion before writing any code)
- Playwright MCP (for verification in Phase 6)
- web-quality-skills (Lighthouse / Core Web Vitals audit)
- docx / pdf skills (for downloadable creator-branded asset exports)

Also read `hub-build-context.json` if present and inspect the resolved `mockup_file` before Phase 3. If a requested MCP/tool is unavailable, document the gap and use official docs or the closest local verification tool.

═══════════════════════════════════════════════
PHASE 1 — PARSE THE AUDIT
═══════════════════════════════════════════════

Read the [CREATOR_AUDIT] block at the bottom and extract these into a working memory file `_hub_plan.md`:

1. **Creator identity** — name, niche, audience, dominant tone, recurring promise, expertise category, monetization angle, positioning summary
2. **Vocabulary preserved verbatim** — these terms MUST appear in copy, never paraphrased
3. **Content formats & themes** — the buckets that organize the hub
4. **All canon nodes** — playbooks, frameworks, lessons, principles, tactics, definitions, quotes — with their IDs, summaries, when-to-use, when-not-to-use, common mistakes, success signals, preconditions, steps, failure modes, tools, examples
5. **Per-video intelligence** — main ideas, frameworks, lessons, examples, stories, mistakes, quotes, claims, contrarian takes, terms, tools, creator voice notes, recommended hub uses
6. **Visual moments** — timestamped screen demos with extracted on-screen text
7. **Evidence segment IDs** — these become the timestamp citations on every page

If the audit is incomplete or contradictory, list the gaps in `_hub_plan.md` and continue with what's available — do not block.

═══════════════════════════════════════════════
PHASE 2 — INFORMATION ARCHITECTURE
═══════════════════════════════════════════════

Before any design or code, output the hub's structure as a sitemap. Use the audit's `Recommended hub uses` as the seed for top-level sections, then organize all canon nodes under them.

Required pages/routes:

1. **Home** — creator hero, positioning summary, search bar (above the fold), featured playbooks (3-5), recent additions, "start here" path for new visitors
2. **Library / All Knowledge** — filterable, searchable index of every canon node. Filters: type (playbook/framework/lesson/principle/tactic/definition/quote), theme, tool, source video
3. **Type-specific index pages** — `/playbooks`, `/frameworks`, `/lessons`, `/principles`, `/tactics`, `/glossary`, `/quotes`
4. **Theme hubs** — one page per recurring theme from the audit (e.g., "Client Onboarding", "Content Research Systems", "AI Agent Operations")
5. **Canon node pages** — one page per playbook, framework, lesson, etc. URL pattern: `/[type]/[slug-derived-from-title]`
6. **Source library** — `/sources` listing every video with title, ID, citation count, and link to the canon nodes derived from it
7. **About the creator** — positioning summary, monetization angle (with CTA to school community / course / lead magnet)
8. **Search** — dedicated `/search` page with full-text + faceted filters

Output the sitemap as a tree in `_hub_plan.md`, then WAIT for my approval before Phase 3. If I say "go" or "ship it", proceed.

═══════════════════════════════════════════════
PHASE 3 — DESIGN COMMITMENT
═══════════════════════════════════════════════

Output a one-page design brief tuned to THIS creator's tone and audience (not a generic template):

- **Aesthetic direction** — Pick ONE explicit direction based on the creator's `dominant tone` and `audience`. For practical/builder creators (like Duncan): editorial-technical, dense and confident, terminal-inspired accent, NOT playful or maximalist. For coaches/wellness: softer, more spacious. Justify in two sentences.
- **Typography stack** — Display + body pairing. NEVER Inter, Roboto, Arial, system-ui defaults. For builder/technical creators, use a mono accent for code/tools/IDs.
- **Color system** — 1 dominant, 1 sharp accent, 2-3 supporting + a "citation/evidence" tint (subtle, used everywhere a timestamp citation appears). Hex + CSS variables.
- **Knowledge node visual language** — How does a "playbook" look different from a "framework" vs "lesson"? Card variants, badges, iconography. Each canon type needs a recognizable signature.
- **Citation language** — How are timestamp citations rendered? Inline pills like `[09:22]` that link to the video at that timestamp? A right-rail evidence drawer? Pick one approach and justify.
- **Motion language** — Scroll reveals on long-form pages, staggered list entries on indexes, smooth route transitions. NO theatrical 3D unless the creator's brand supports it. Always honor `prefers-reduced-motion`.
- **Hero concept** — The home page above-the-fold in 3 sentences. Specific enough that the build is unambiguous.

═══════════════════════════════════════════════
PHASE 4 — TECHNICAL PLAN
═══════════════════════════════════════════════

Decide and document:

- **Framework** — Next.js 15 App Router with TypeScript (default unless creator audit suggests otherwise). MDX for canon node content. Tailwind v4 for styling.
- **Content layer** — Each canon node is an MDX file under `/content/[type]/[slug].mdx` with frontmatter pulling directly from the audit (id, title, type, summary, citations, evidenceSegmentIds, sourceVideoId, pageWorthiness, confidence, etc.). Build a content loader that reads these at build time.
- **Search** — Fuse.js client-side for instant search across all canon nodes. Index: title, summary, when-to-use, steps, examples, tools, themes.
- **Citations** — A `<Citation>` component that takes `videoId` + `segmentId` and renders an inline pill linking to `youtu.be/[videoId]?t=[seconds]`. Every claim, quote, and step from the audit gets one. NEVER fabricate a citation — if the audit doesn't have an evidenceSegmentId, render the claim without a citation rather than inventing.
- **Components needed** — `<CanonCard>` (variants per type), `<CitationPill>`, `<EvidenceDrawer>`, `<FrameworkSteps>`, `<PlaybookFlow>`, `<MistakeCallout>`, `<SuccessSignal>`, `<ToolBadge>`, `<QuoteBlock>`, `<TermDefinition>`, `<SearchBar>`, `<FilterPanel>`, `<ThemeHubHeader>`, `<CreatorHero>`
- **Data flow** — All audit data → `/content` MDX files (generated by a `scripts/import-audit.ts` that takes the raw audit and emits MDX) → static build. No runtime database needed.
- **Performance plan** — Static export where possible, lazy-load images, prefetch on hover for canon node links, search index loaded on first interaction.
- **Accessibility** — WCAG AA minimum. Citation pills need accessible labels ("Evidence at 9 minutes 22 seconds in [video title]"). Reduced-motion handling on every animation.
- **File structure** — Output the directory tree in `_hub_plan.md`.

For every library used, call Context7 to fetch current docs. Do NOT rely on training data.

═══════════════════════════════════════════════
PHASE 5 — BUILD
═══════════════════════════════════════════════

Build in this order — finish each layer before moving to the next:

**Layer 1: Content import**
- Write `scripts/import-audit.ts` that reads the audit and emits one MDX file per canon node into `/content/[type]/[slug].mdx`
- Generate slugs from titles (kebab-case, deduplicated)
- Preserve every field: id, citations count, pageWorthiness, confidence, specificity, creatorUniq, sourceVideoId, evidenceSegmentIds, all body content
- Run the script and verify the right number of MDX files exist

**Layer 2: Layout skeleton**
- Global nav, footer, typography, color tokens
- Verify spacing and hierarchy at 375px / 768px / 1440px
- NO animations yet

**Layer 3: Canon node templates**
- Build the dynamic route `/[type]/[slug]/page.tsx` that renders any canon node
- Each type (playbook, framework, lesson, principle, tactic, definition, quote) gets a distinct layout reflecting its structure
- Playbook: hero summary → preconditions → steps (numbered with citations) → success signal → common mistake → failure modes → tools → related nodes
- Framework: hero → steps as a visual flow → when to use / when not → sequencing rationale
- Lesson: claim → context → preconditions → failure modes
- Quote: large pull-quote treatment with attribution and source link
- Definition: term + definition + when to use, dictionary-style

**Layer 4: Index & theme pages**
- Library page with filters and search
- Type-specific index pages
- Theme hub pages, each with a custom intro derived from the audit's themes

**Layer 5: Citation system**
- Implement `<Citation>` component
- Wire every audit claim/step/example to its evidenceSegmentId
- Build evidence drawer or inline pill per Phase 3 decision
- Every video reference links to the source

**Layer 6: Home page**
- Creator hero with positioning summary
- Above-the-fold search
- Featured playbooks (sort by pageWorthiness)
- "Start here" curated path
- Recent additions
- CTA block tied to creator's monetization angle

**Layer 7: Search**
- Fuse.js index built at compile time
- `/search` page with results grouped by type
- Keyboard-navigable (⌘K shortcut)

**Layer 8: Motion polish**
- Scroll reveals on long pages
- Staggered list entries on indexes
- Page transitions
- All gated behind `prefers-reduced-motion`

Rules during the build:
- Mobile-first. Test at 375px continuously.
- Every interactive element gets a real focus state.
- Use the creator's `vocabulary preserved verbatim` in copy. Do NOT paraphrase those terms.
- Citation pills are NON-OPTIONAL. If a claim came from the audit, it gets a citation.
- No Lorem Ipsum. Ever. Pull copy from the audit.

═══════════════════════════════════════════════
PHASE 6 — VERIFY
═══════════════════════════════════════════════

Before declaring done:

1. Run Playwright: visit home, library, one of each canon node type, a theme hub, and search. Screenshot at 375 / 768 / 1440. Show me the screenshots.
2. Run Lighthouse on home + a canon node page. Report LCP, CLS, INP, JS bundle, accessibility score. Targets: LCP <2.5s, CLS <0.1, A11y >95.
3. Verify citation integrity: every `<Citation>` on the rendered site links to a valid YouTube timestamp. Count citations and report total.
4. Verify content completeness: total canon nodes in audit vs total MDX files generated vs total pages built. They should match.
5. Toggle `prefers-reduced-motion` and confirm graceful degradation.
6. Tab through home and one canon node with keyboard only.
7. Output an audit table: [canon type] [count in audit] [pages built] [✅/❌].

═══════════════════════════════════════════════
PHASE 7 — DELIVER
═══════════════════════════════════════════════

Output:
- Working code on a feature branch
- A `README.md` with: install, dev, build, deploy commands; how to re-run `import-audit.ts` when new videos are added; how to update creator branding; known limitations
- The Phase 6 audit table
- A `CREATOR_NOTES.md` summarizing what design decisions you made for THIS creator and why, so the CreatorCanon team can review before client handoff
- One paragraph: "what I'd build next if I had another day"

═══════════════════════════════════════════════
HARD RULES (override everything else)
═══════════════════════════════════════════════

- **Source-grounding is sacred.** Never fabricate a quote, citation, statistic, framework step, or example. If it's not in the audit, it doesn't appear on the site.
- **Preserve verbatim vocabulary.** Terms in `vocabulary preserved verbatim` appear exactly as the creator says them. Don't "improve" their phrasing.
- **Timestamp citations on every claim** that has an evidenceSegmentId. This is the core differentiator vs a generic AI-generated content site.
- **Tone matches the creator, not the agent.** Read the `dominant tone` and `creator voice notes` and write copy in that voice. Do not default to corporate SaaS tone.
- **The home page must answer "what does this creator teach?" in 5 seconds** through the positioning summary and featured playbooks.
- **Never invent library APIs** — verify with Context7.
- **Never ship without testing reduced-motion and keyboard nav.**
- **Default Tailwind palette is forbidden** — customize the theme.
- **If you're stuck, stop and ask.** Don't guess.

Begin with Phase 1 now. Read the audit carefully before doing anything else.

═══════════════════════════════════════════════
[CREATOR_AUDIT]
═══════════════════════════════════════════════

PASTE YOUR FULL AUDIT MARKDOWN/JSON HERE — including:
- Channel Profile section
- Visual Moments section
- Per-Video Intelligence section (all videos)
- Knowledge Graph section (all canon nodes)
- Proposed Hub Pages (if any)
- Stage Cost Breakdown (optional)
