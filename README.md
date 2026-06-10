# Vibe Coding for Scientists — A 60-Minute Crash Course

A tool-agnostic, demo-heavy crash course that teaches working scientists how to **direct** an AI to write analysis code — and how to catch it when it's confidently wrong.

> **Thesis:** Vibe coding moves you from *author* of code to *director* of code. Your job becomes intent, judgment, and verification — not syntax.

## Who it's for
Scientists (grad students → PIs) who code a little (usually Python/R in notebooks) and treat code as a means to an answer, not a craft.

## The hour at a glance
| Time | Block |
|------|-------|
| 0:00–0:03 | Hook + what "vibe coding" means |
| 0:03–0:10 | **Why it matters** (for scientists specifically) |
| 0:10–0:30 | **The mindset** — 4 pillars (divergence · critical thinking · fast/slow · try-and-fail) + keeping your own voice |
| 0:30–0:49 | **Demo / hands-on** — fork the repo, vibe-code a real analysis |
| 0:49–0:56 | **Working together in a lab** — peer-review, sprints, shared conventions |
| 0:56–0:60 | **Safety / ethics** |

## What's in here
- **[facilitator-guide.md](facilitator-guide.md)** — the run-of-show: timings, talking points, the demo script, a 30-min cut. *Start here to teach.*
- **[slides.md](slides.md)** — presentable deck (Marp markdown). Render with `marp slides.md` or the VS Code Marp extension.
- **[handout.md](handout.md)** — one-page participant cheat-sheet (print or share).
- **[demo/](demo/)** — the forkable hands-on: a deliberately-messy dataset, a generator, and a starter notebook.

## To run the session
1. Read [facilitator-guide.md](facilitator-guide.md).
2. Push the `demo/` contents somewhere participants can **fork** (its own repo, or this one), and put the URL on the title slide.
3. Regenerate the dataset: `python demo/generate_data.py`.
4. Have your AI tool open and test the cold-open prompt once beforehand.

## The four pillars (the heart of it)
1. **Divergence / creativity** — generate many options before converging; generation is now nearly free.
2. **Critical thinking** — every output is a PR from a brilliant, overconfident intern. *"How would I know if this is wrong?"*
3. **Thinking fast / slow** — the AI is System 1 (fast); you supply System 2 (deliberate checking). Slow down where it matters.
4. **Try and fail** — cheap attempts, small stakes, disposable prototypes. Failure is the unit of search.

> Trust the vibe to **write** it; never trust the vibe that it's **right**.
