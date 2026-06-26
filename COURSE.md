# Vibe Coding for Scientists — Course Outline

A ~75-minute course: six talk modules plus two hands-on **install fests**
(🛠 Code, 🖋 Manuscript). It moves working scientists from *writing* code to
*directing* it — and shows how to catch the confident-but-wrong result.

The deck is **assembled from per-module files**: edit [modules/](modules/), run
`./build.sh`, then `marp slides.md`. One file = one module.

Run it however fits your group:
- **The main hour** — modules 1–6 as a seminar (~60 min, demo-centric).
- **Install fest · Code** — right after the live demo; a hands-on clinic that
  **takes the time it needs** (~30–45 min). Don't rush it to a slot.
- **Install fest · Manuscript** — the final module (~30–45 min): Overleaf → VS
  Code + GitHub, so the paper joins the repo and the agent can help maintain it.

## Who it's for
Scientists (grad students → PIs) who code a little (usually Python/R in notebooks)
and treat code as a means to an answer, not a craft.

## Running order

| Order | Module | Source | ~min |
|-------|--------|--------|------|
| — | Intro · thesis · learning objectives | [00-intro.md](modules/00-intro.md) | 3 |
| 1 | Why it matters | [01-why-it-matters.md](modules/01-why-it-matters.md) | 5 |
| 2 | The mindset + the science | [02-the-mindset.md](modules/02-the-mindset.md) | 15 |
| 3 | How you actually do it (modes · prompting) | [03-how-you-do-it.md](modules/03-how-you-do-it.md) | 10 |
| 4 | **Live demo** — a real analysis | [04-live-demo.md](modules/04-live-demo.md) | 15 |
| 🛠 | **Install fest · Code** — repo + agent | [05-install-fest-code.md](modules/05-install-fest-code.md) | 30–45 |
| 5 | Working together in a lab | [06-working-in-a-lab.md](modules/06-working-in-a-lab.md) | 7 |
| 6 | Safety & ethics | [07-safety-ethics.md](modules/07-safety-ethics.md) | 5 |
| 🖋 | **Install fest · Manuscript** — Overleaf → VS Code/GitHub | [08-install-fest-manuscript.md](modules/08-install-fest-manuscript.md) | 30–45 |
| — | Director, not author · further reading · sources | [09-close.md](modules/09-close.md) | 3 |

**Learning objectives.** By the end, participants can: understand *why & how* to
vibe code in science (author→director, the four pillars, the cognitive science);
use vibe coding for a real **data-science** analysis end to end; and use it for
**manuscript writing** while keeping their own voice and the claims their name depends on.

## The two install fests

### 🛠 Install fest · Code *(after the demo, ~30–45 min)*
Everyone leaves with a working analysis setup: VS Code + Git + Claude Code · a
**code + data monorepo** (data untracked) · `CLAUDE.md` · first in-repo loop · push to GitHub.
**Pre-flight (send ahead):** GitHub + AI-tool accounts.

### 🖋 Install fest · Manuscript *(the final module, ~30–45 min)*
The paper joins the repo: **LaTeX in VS Code** · **Overleaf ↔ GitHub sync** (co-authors
stay in Overleaf) · **Zotero → a live `.bib`** · the agent can draft, revise, and keep
numbers consistent (a paper is software — propagate · diff · review · rebuild).
**Pre-flight:** pre-download a LaTeX distribution (~4 GB). Don't compress it — installs set the pace.

## Discussion questions
Each module ends with an open question (collected in [notes/](notes/)) — use them as
think-pair-share or whole-room prompts. They are the natural seeds for the next modules.

## Materials map
- **[modules/](modules/)** — the deck source, one file per module. *Edit these.*
- **[build.sh](build.sh)** — assembles `modules/` → `slides.md`. Run it, then `marp slides.md`.
- **[slides.md](slides.md)** — the full deck, **generated** (don't hand-edit).
- **[facilitator-guide.md](facilitator-guide.md)** — run-of-show, talking points, demo script.
- **[handout.md](handout.md)** — one-page participant cheat-sheet.
- **[RESOURCES.md](RESOURCES.md)** — annotated reading list.
- **[notes/](notes/)** — the per-module discussion questions (free-form scratch space).
- **[demo/](demo/)** — the forkable hands-on dataset and starter notebook.

## Facilitator notes
- **Module 1 must excite.** Lead with a live demo and the end-state vision; keep the
  caveats for module 2. If they're not leaning forward, slow down on the demo.
- **The install fests will run long.** Treat them as clinics, not lectures. No one debugs alone.
- **The manuscript fest lands hardest with a real repo + a paper.** If you can, propagate a change live.
- To change a slide, edit its module file and rerun `./build.sh` — never hand-edit `slides.md`.
