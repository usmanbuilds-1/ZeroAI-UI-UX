# ZeroAI — agent operating contract

Use this repository as a universal, application-agnostic mobile product design reference. The target application's own instructions, user requirements, functionality, security and accessibility remain authoritative. Do not modify this reference repository while redesigning another application.

## Load the skill

1. Locate/clone this private repository in an authorized workspace; do not assume a bare URL grants access. Pin the commit used and keep the reference separate from the target app.
2. Locate `skill/ui-ux-mobile-design/SKILL.md` and `knowledge.db`. If the runtime is absent or cannot be read, report that the import/access is incomplete; do not claim full ZeroAI use. Read SKILL.md, DESIGN_CONSTITUTION.md, DESIGN_METHODOLOGY.md, FORBIDDEN_PATTERNS.md and workflows/redesign_safety.md. Load relevant playbooks, platform guidance and workflows/rendered_review.md on demand.
3. Run the installation smoke test and local query CLI where available. Retrieve evidence for the actual design problems, not the application category alone. Read full records and check relevance, applicability and quality. Unverified, commercial, historical and dark-pattern records are not implementation authority. If no relevant record exists, say so. Do not fabricate citations or treat transcript claims as independent experiments.

## Execute a redesign, not a proposal

- Inspect the target app's repository, existing screens, design tokens, navigation, features, data flows and tests. Capture the current rendered UI when possible.
- Define product purpose, audience, primary tasks, constraints and an intentional, distinctive visual direction. Use the existing brand or develop a coherent direction from the brief; never default to a single aesthetic, industry or arbitrary template.
- Inventory existing capabilities and states before changes. Preserve functionality, navigation, persisted data, security, permissions, business logic and accessibility. Get explicit approval before removing or materially changing a capability.
- Plan screen hierarchy and interaction flow around user tasks. Choose layouts and components because they serve a purpose, not because they are fashionable. Avoid decorative bento grids, glassmorphism, gratuitous gradients and blur, nested card soup, pill spam, generic icon tiles, fake data, filler copy and repetitive containers. Functional grids, selection controls, status indicators and other legitimate components remain valid.
- Implement in the target app's actual stack, reusing existing tokens and components where appropriate. Complete the relevant states: loading, empty, error, offline, permission, success and edge cases.
- Render on actual supported screen sizes; inspect screenshots, critique hierarchy, spacing, typography, visual identity, interaction states and accessibility. Correct findings and render again. Run builds, functional regressions and accessibility checks. Never claim a visual pass if no render was inspected.
- Treat lexical detectors as advisory; their output cannot certify design quality. Do not enable blocking CI or write waiver approvals on the user's behalf. Missing source paths, forged waiver strings and placeholder render reports are not valid evidence. Report any checks you could not run.
- Deliver working code, a concise change summary, evidence used, screenshots/tests where available, and remaining issues. Prefer staged changes with verification between stages over an unreviewable full-app rewrite.

## Research boundaries

This is a reference skill, not a substitute for product research or professional judgment. Do not claim that every source is verified or that the skill outperforms alternatives. Apply engagement and monetization knowledge only when relevant, transparently, without deceptive pricing, cancellation obstruction, fabricated urgency or coercive retention. Never expose private source code, credentials or user data to a research service.
