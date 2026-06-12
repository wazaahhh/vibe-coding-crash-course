# Vibe Coding for Scientists — Course Outline

A hands-on course in **6 × 20-minute sessions** (~2 hours of talks, plus the clinic).
It moves working scientists from *writing* code to *directing* it — and from four
scattered tools to one AI-native workspace where code, paper, and data live together.

Run it however fits your group:
- **Seminar** — Sessions 1–3 back to back (~60 min).
- **Clinic** — Session 4 **takes the time it needs** (~45–60 min with per-laptop
  debugging); don't rush it to fit a slot.
- **Follow-up** — Sessions 5–6 once everyone is set up (~40 min).

> Each **talk** module is tuned for **20 minutes** (~8–10 slides). Session 4 is the one
> exception — a hands-on clinic that keeps its full length, with an optional break after Move 2.

## Who it's for
Scientists (grad students → PIs) who code a little (usually Python/R in notebooks)
and treat code as a means to an answer, not a craft.

## The arc

| # | Session | Goal | Mode | Deck |
|---|---------|------|------|------|
| 1 | **The hook** | Make them *want* the rest | talk + live demo | [session-1-the-hook.md](session-1-the-hook.md) |
| 2 | **The mindset** | The disciplines that keep the new loop safe | talk + poll | [session-2-the-mindset.md](session-2-the-mindset.md) |
| 3 | **How you actually do it** | Modes, prompting, and a real demo | talk + demo | [session-3-how-you-do-it.md](session-3-how-you-do-it.md) |
| 4 | **Install fest** | Build the real setup, hands-on | 🛠 clinic | [session-4-install-fest.md](session-4-install-fest.md) |
| 5 | **The recursive researcher** | One change, propagated — a paper is software | talk + demo | [session-5-recursive-researcher.md](session-5-recursive-researcher.md) |
| 6 | **The lab & the responsibility** | Collaboration, standards, safety | talk | [session-6-the-lab.md](session-6-the-lab.md) |

> Each session is its own self-contained deck, ending with a pointer to the next.
> Render any one with `marp session-N-….md`, or teach them in sequence.

## Sessions in detail

### Session 1 — The hook *(exciting & enticing — protect this)*
**Objective:** in 20 minutes, make the value undeniable.
What vibe coding means · author → director · why it matters *for scientists* ·
**what you'll be able to do by the end** (the vision) · the course roadmap.
**Open with a live demo:** take a task from the room, vibe-code it in 20 seconds, run it.
*Leave them wanting Session 2 — don't front-load the caveats.*

### Session 2 — The mindset
**Objective:** why directing an AI is not just faster typing.
The four pillars (divergence · critical thinking · fast/slow · try-and-fail) ·
the cognitive science (one slide: automation bias, cognitive offloading, illusion of
explanatory depth, cognitive debt + generation effect) · where it shines vs. bites ·
a 30-second horror story · "which pillar is hardest?" poll.
*("Keep your own voice" moved to Session 6 to fit 20 min.)*

### Session 3 — How you actually do it
**Objective:** the practical loop.
Mode A (chat) vs. Mode B (agent in your repo) · the monorepo · how to ask
(the *intent* half of the job) · a live demo on a real, messy dataset (notebook → script).

### Session 4 — Install fest 🛠 *(hands-on — keeps its full length)*
**Objective:** everyone leaves with a working setup.
Moves 1–2: VS Code + Git + Claude Code · a code monorepo (data untracked).
Moves 3–4: Overleaf → local LaTeX · Zotero → a live `.bib` · `CLAUDE.md` · first
in-repo loop · push to GitHub. Optional break after Move 2.
**Note:** unlike the talk modules, this one **takes the time it needs** — budget ~45–60 min
with big downloads (LaTeX ≈ 4 GB) and per-laptop debugging. Don't compress it. Pair people up.
**Pre-flight (send ahead):** GitHub + Anthropic accounts; pre-download a LaTeX distribution.
Start the LaTeX install at the very beginning.

### Session 5 — The recursive researcher
**Objective:** show the payoff that sells the whole approach.
Change one result → the agent re-runs the regression and propagates through tables,
figures, the abstract, and the Supplementary Materials. Why this *is* software
engineering (a paper is a dependency graph; a new result is a refactor) · why LLM
tooling was optimized for code first · how to make your paper "buildable" (computed
numbers, reproducible build, consistency checks) · review every diff.

### Session 6 — The lab & the responsibility
**Objective:** make it work for a team, safely.
How a lab works when generation is cheap (peer review, sprints, shared conventions,
mentoring on judgment) · keep your own voice · safety & ethics (data confidentiality,
provenance, disclosure, skill atrophy) · start Monday · *director, not author.*

## Materials map
- **[COURSE.md](COURSE.md)** — this outline.
- **[session-1-the-hook.md](session-1-the-hook.md)** — Session 1, the enticing opener.
- **[session-2-the-mindset.md](session-2-the-mindset.md)** — Session 2, pillars + cognitive science.
- **[session-3-how-you-do-it.md](session-3-how-you-do-it.md)** — Session 3, modes, prompting, demo.
- **[session-4-install-fest.md](session-4-install-fest.md)** — Session 4, the hands-on clinic.
- **[session-5-recursive-researcher.md](session-5-recursive-researcher.md)** — Session 5, the propagation module.
- **[session-6-the-lab.md](session-6-the-lab.md)** — Session 6, collaboration + safety + close.
- **[facilitator-guide.md](facilitator-guide.md)** — run-of-show, talking points, demo script.
- **[handout.md](handout.md)** — one-page participant cheat-sheet.
- **[RESOURCES.md](RESOURCES.md)** — annotated reading list.
- **[demo/](demo/)** — the forkable hands-on dataset and starter notebook.

## Facilitator notes
- **Session 1 must excite.** Lead with a live demo and the end-state vision; keep the
  caveats for Session 2. If they're not leaning forward by the roadmap slide, slow down on the demo.
- **Session 4 will run long.** Treat it as a clinic, not a lecture. No one debugs alone.
- **Session 5 lands hardest with a real repo.** If you can, propagate a change live.
