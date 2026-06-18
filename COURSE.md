# Vibe Coding for Scientists — Course Outline

A ~60-minute **main deck** of six modules, plus two deeper **add-on modules**
(more on the way). It moves working scientists from *writing* code to *directing*
it — and shows how to catch the confident-but-wrong result.

Run it however fits your group:
- **The main hour** — [slides.md](slides.md), modules 1–6 (~60 min, demo-centric).
- **Install clinic** — [install-fest.md](install-fest.md), a hands-on setup that
  **takes the time it needs** (~45–60 min). Run it right after the demo.
- **Deep dive** — [recursive-research.md](recursive-research.md), the "a paper is
  software" module (~20 min). Slot it after the install fest and before the lab
  module, while everyone has a fresh repo open.

## Who it's for
Scientists (grad students → PIs) who code a little (usually Python/R in notebooks)
and treat code as a means to an answer, not a craft.

## The main deck — [slides.md](slides.md)

| # | Module | Goal | ~min |
|---|--------|------|------|
| 1 | Why it matters | Make the value undeniable | 5 |
| 2 | The mindset + the science | The disciplines that keep the new loop safe | 15 |
| 3 | How you actually do it | Modes (chat vs. agent) + how to prompt | 10 |
| 4 | Live demo | Direct a real analysis; catch the plausible-but-wrong | 15 |
| 5 | Working together in a lab | Review, shared standards, rhythm | 7 |
| 6 | Safety & ethics | Confidentiality, provenance, disclosure, atrophy | 5 |

**Learning objectives.** By the end, participants can: understand *why & how* to
vibe code in science (author→director, the four pillars, the cognitive science);
use vibe coding for a real **data-science** analysis end to end; and use it for
**manuscript writing** while keeping their own voice and the claims their name depends on.

## Add-on modules

### 🛠 Install fest — [install-fest.md](install-fest.md) *(hands-on, ~45–60 min)*
Everyone leaves with a working setup: VS Code + Git + Claude Code · a code + LaTeX
monorepo (data untracked) · Overleaf → local LaTeX · Zotero → a live `.bib` ·
`CLAUDE.md` · first in-repo loop · push to GitHub. Optional break after Move 2.
**Don't compress it** — installs (LaTeX ≈ 4 GB) and per-laptop debugging set the pace.
**Pre-flight (send ahead):** GitHub + Anthropic accounts; pre-download a LaTeX distribution.

### The recursive researcher — [recursive-research.md](recursive-research.md) *(~20 min)*
Change one result → the agent re-runs the regression and propagates through tables,
figures, the abstract, and the Supplementary Materials. Why this *is* software
engineering (a paper is a dependency graph; a new result is a refactor) · why LLM
tooling was optimized for code first · how to make your paper "buildable" (computed
numbers, reproducible build, consistency checks) · review every diff.

## Materials map
- **[COURSE.md](COURSE.md)** — this outline.
- **[slides.md](slides.md)** — the main course deck (modules 1–6).
- **[install-fest.md](install-fest.md)** — the hands-on setup clinic.
- **[recursive-research.md](recursive-research.md)** — the propagation deep-dive.
- **[facilitator-guide.md](facilitator-guide.md)** — run-of-show, talking points, demo script.
- **[handout.md](handout.md)** — one-page participant cheat-sheet.
- **[RESOURCES.md](RESOURCES.md)** — annotated reading list.
- **[demo/](demo/)** — the forkable hands-on dataset and starter notebook.

## Facilitator notes
- **Module 1 must excite.** Lead with a live demo and the end-state vision; keep the
  caveats for module 2. If they're not leaning forward, slow down on the demo.
- **The install clinic will run long.** Treat it as a clinic, not a lecture. No one debugs alone.
- **The recursive module lands hardest with a real repo.** If you can, propagate a change live.
