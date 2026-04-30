---
name: motion
description: Use when building, reviewing, or revising animations with Motion from motiondivision/motion, including React motion/react, JavaScript animate(), Vue motion-v, Framer Motion migrations, gestures, layout animations, AnimatePresence, scroll-linked effects, springs, timelines, and production animation performance.
---

# Motion

## Source

Official library: https://github.com/motiondivision/motion

Official docs: https://motion.dev/docs

The upstream repo is a JavaScript animation library, not a Codex skill. This local skill captures the practical setup and usage rules for working with Motion.

## Default Stance

Use Motion as the modern default for new animation work.

- Install React or JavaScript package: `npm install motion`
- Install Vue package: `npm install motion-v`
- React import for new work: `import { motion } from "motion/react"`
- JavaScript import for DOM animations: `import { animate } from "motion"`
- Vue import: `import { motion } from "motion-v"`
- Treat Framer Motion as the older import path. If a project already uses `framer-motion`, follow the existing pattern for small edits unless the user asks for a migration.

Do not mix `framer-motion` and `motion/react` in the same feature without a migration reason.

## Before Coding

1. Inspect the project dependencies and existing imports.
2. Identify the framework: React, plain JavaScript, Vue, or another environment.
3. Check whether animations already use Motion, Framer Motion, GSAP, CSS transitions, or another library.
4. Choose one animation system per element or property.
5. Design the animation around state, not timers, whenever possible.
6. Preserve accessibility and reduced-motion behavior.

## React Patterns

Use `motion/react` for React components.

```tsx
import { motion } from "motion/react"

export function Card() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.35, ease: "easeOut" }}
    />
  )
}
```

For mount/unmount transitions, use `AnimatePresence`.

```tsx
import { AnimatePresence, motion } from "motion/react"

<AnimatePresence mode="wait">
  {open ? (
    <motion.div
      key="panel"
      initial={{ opacity: 0, scale: 0.98 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.98 }}
    />
  ) : null}
</AnimatePresence>
```

For state families, use variants.

```tsx
const item = {
  hidden: { opacity: 0, y: 12 },
  visible: { opacity: 1, y: 0 },
}

<motion.li variants={item} initial="hidden" animate="visible" />
```

For layout changes, prefer Motion's layout system over manual height and position math.

```tsx
<motion.div layout transition={{ type: "spring", stiffness: 420, damping: 34 }} />
```

Use `layoutId` only for shared element transitions between related visual states. Keep `layoutId` values stable and unique in the animation scope.

## JavaScript Patterns

Use `animate()` from `motion` for plain DOM animations.

```ts
import { animate, stagger } from "motion"

animate(
  ".item",
  { opacity: [0, 1], y: [12, 0] },
  { delay: stagger(0.05), duration: 0.35, ease: "easeOut" }
)
```

Prefer direct element refs or tight selectors. Avoid broad selectors that animate unrelated UI.

## Gestures

Use Motion gestures for interaction states instead of manual pointer handlers when the built-in behavior is enough.

```tsx
<motion.button
  whileHover={{ scale: 1.03 }}
  whileTap={{ scale: 0.97 }}
  transition={{ type: "spring", stiffness: 500, damping: 30 }}
/>
```

Keep gestures subtle. They should confirm interaction, not move layout unexpectedly.

## Scroll And Motion Values

For scroll-linked effects in React, use Motion hooks such as `useScroll`, `useTransform`, and `useSpring`.

```tsx
import { motion, useScroll, useSpring, useTransform } from "motion/react"

const { scrollYProgress } = useScroll()
const scaleX = useSpring(scrollYProgress, { stiffness: 100, damping: 30 })
const opacity = useTransform(scrollYProgress, [0, 0.15], [0, 1])

return <motion.div style={{ scaleX, opacity }} />
```

Keep scroll effects readable on mobile and disable or reduce effects when they interfere with content.

## Next.js And Server Components

Motion components run on the client.

- Put `"use client"` at the top of files that render Motion components in the Next.js App Router.
- Keep animated client components small when possible.
- Pass data into animation components from server components instead of moving whole pages client-side.

## Performance Rules

Prefer properties that stay on the compositor:

- `transform`
- `opacity`
- CSS variables that drive transforms or opacity

Be careful with:

- `width`
- `height`
- `top`
- `left`
- `box-shadow`
- filters
- large SVG path animations

When layout properties must change, prefer Motion's `layout` animations and test for jank.

Avoid animating many large DOM nodes at once. Stagger large lists, virtualize long lists, or reduce the animation surface.

## Accessibility

Respect reduced motion.

Use `MotionConfig` for broad defaults:

```tsx
import { MotionConfig } from "motion/react"

<MotionConfig reducedMotion="user">
  <App />
</MotionConfig>
```

Use `useReducedMotion()` when an animation needs a custom reduced version.

```tsx
import { motion, useReducedMotion } from "motion/react"

const reduceMotion = useReducedMotion()

<motion.div animate={reduceMotion ? { opacity: 1 } : { opacity: 1, y: 0 }} />
```

Reduced motion should remove travel, parallax, looping motion, and large scale changes. Fades are usually acceptable.

## Migration Notes

When migrating from `framer-motion`:

1. Replace imports with `motion/react` only when the package is installed and the migration scope is clear.
2. Update all imports in the same feature together.
3. Preserve existing variants, transitions, gestures, and layout props unless there is a specific bug.
4. Run the app and inspect animated states visually.
5. Do not migrate unrelated files just because one component changed.

## Avoid

- Opening with animation before content is understandable.
- Animating layout in ways that cause text overlap or reflow surprises.
- Infinite loops without user value.
- Large motion on hover for dense tools or dashboards.
- Mixing CSS transitions and Motion on the same property.
- Using Motion for a simple one-off hover color change that CSS handles cleanly.
- Adding a new animation dependency when the project already has a suitable animation system.

## Quality Checklist

Before finishing Motion work, verify:

1. Imports match the installed package and framework.
2. The animation has a clear UX purpose.
3. Motion does not obscure or delay important content.
4. Reduced motion is handled for substantial movement.
5. Layout does not shift unexpectedly.
6. Mobile and desktop both look intentional.
7. The animation remains smooth under normal interaction.
8. Existing animation patterns in the codebase were respected.
