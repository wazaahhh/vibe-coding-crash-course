# Vibe Coding for Scientists — A Hands-On Course

A tool-agnostic, demo-heavy course that teaches working scientists how to **direct** an AI to write analysis code — and how to catch it when it's confidently wrong. A ~75-minute main deck of **eight modules**, plus two deeper **add-on modules** (more on the way).

> **Thesis:** Vibe coding moves you from *author* of code to *director* of code. Your job becomes intent, judgment, and verification — not syntax.

## Who it's for
Scientists (grad students → PIs) who code a little (usually Python/R in notebooks) and treat code as a means to an answer, not a craft.

## The main deck at a glance — [slides.md](slides.md)
| # | Module | ~min |
|---|--------|------|
| 1 | **Why it matters** — for scientists specifically | 5 |
| 2 | **The mindset** — four pillars + the cognitive science | 15 |
| 3 | **How you actually do it** — modes, prompting | 10 |
| 4 | **Live demo** — direct a real analysis | 15 |
| 5 | **Git & GitHub** — the safety net (local vs. GitHub, private vs. public) | 8 |
| 6 | **Edit modes, models & prompting** — the controls | 8 |
| 7 | **Working together in a lab** — review, standards, rhythm | 7 |
| 8 | **Safety & ethics** | 5 |

Two hands-on **install fests** are interleaved with the talk modules: **🛠 Code** (after the demo) and **🖋 Manuscript — Overleaf → VS Code + GitHub** (the final module).

→ Full syllabus and prep in **[COURSE.md](COURSE.md)**.

## What's in here
- **[COURSE.md](COURSE.md)** — the syllabus: modules, objectives, and how the decks fit together. *Start here to plan.*
- **[facilitator-guide.md](facilitator-guide.md)** — run-of-show: timings, talking points, the demo script, and compressed options. *Start here to teach.*
- **[modules/](modules/)** — the deck **source**, one Markdown file per module. *Edit these.*
- **[build.sh](build.sh)** — assembles the module files into **`slides.md`**. Run `./build.sh`, then `marp slides.md`.
- **[slides.md](slides.md)** — the full deck, **generated** from `modules/` (don't hand-edit; rebuild instead).
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

## Editions
Versions of the course re-cut for a specific event live in **[editions/](editions/)**, each with its own deck source and build script.

- **[FacMed Hack #1 — Crash Course #2](editions/facmed-hack-2026/)** (UNIGE Faculty of Medicine, 22 October 2026, on Zoom): the course re-cut for *Digital Phenotyping of Mental Health*, with one dataset (a synthetic phone study) for the whole session. Participants' materials, slides (PDF) included, are on the [`facmed-2026-participants`](https://github.com/wazaahhh/vibe-coding-crash-course/tree/facmed-2026-participants/editions/facmed-hack-2026) branch.

## Further reading
See **[RESOURCES.md](RESOURCES.md)** for an annotated reading list (vibe coding in science, academic framing, best practices, and the cognitive-science references behind the slides).

## License
Course materials (slides, guides, handouts) © 2026 Thomas Maillart, licensed under **[CC BY-NC 4.0](LICENSE)** — share and adapt with attribution, non-commercial use only. See [LICENSE](LICENSE) for details.
