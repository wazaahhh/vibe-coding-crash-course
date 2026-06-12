# Vibe Coding for Scientists — A Hands-On Course

A tool-agnostic, demo-heavy course that teaches working scientists how to **direct** an AI to write analysis code — and how to catch it when it's confidently wrong. Organized as **6 × 20-minute sessions**; run them together or à la carte.

> **Thesis:** Vibe coding moves you from *author* of code to *director* of code. Your job becomes intent, judgment, and verification — not syntax.

## Who it's for
Scientists (grad students → PIs) who code a little (usually Python/R in notebooks) and treat code as a means to an answer, not a craft.

## The course at a glance
| # | Session (20 min) | Mode |
|---|------------------|------|
| 1 | **The hook** — why this changes your research | talk + live demo |
| 2 | **The mindset** — four pillars + the cognitive science | talk + poll |
| 3 | **How you actually do it** — modes, prompting, demo | talk + demo |
| 4 | **Install fest** — build your real setup | 🛠 hands-on clinic |
| 5 | **The recursive researcher** — one change, propagated | talk + demo |
| 6 | **The lab & the responsibility** — collaboration, safety | talk |

→ Full syllabus with per-session objectives and prep in **[COURSE.md](COURSE.md)**.

## What's in here
- **[COURSE.md](COURSE.md)** — the syllabus: the six sessions, objectives, and how the decks fit together. *Start here to plan.*
- **[facilitator-guide.md](facilitator-guide.md)** — per-session run-of-show: timings, talking points, the demo script, and compressed options. *Start here to teach.*
- **One Marp deck per 20-min session** (render with `marp session-N-….md` or the VS Code Marp extension):
  - **[session-1-the-hook.md](session-1-the-hook.md)** — why this changes your research.
  - **[session-2-the-mindset.md](session-2-the-mindset.md)** — four pillars + the cognitive science.
  - **[session-3-how-you-do-it.md](session-3-how-you-do-it.md)** — modes, prompting, live demo.
  - **[session-4-install-fest.md](session-4-install-fest.md)** — hands-on migration from ChatGPT/Claude web + Overleaf + Zotero to Claude Code in VS Code, with a code + LaTeX monorepo (data untracked).
  - **[session-5-recursive-researcher.md](session-5-recursive-researcher.md)** — change one result and propagate it through tables, figures, abstract, and Supplementary Materials — why a paper is software.
  - **[session-6-the-lab.md](session-6-the-lab.md)** — collaboration, standards, safety, and the close.
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

## Further reading
See **[RESOURCES.md](RESOURCES.md)** for an annotated reading list (vibe coding in science, academic framing, best practices, and the cognitive-science references behind the slides).

## License
Course materials (slides, guides, handouts) © 2026 Thomas Maillart, licensed under **[CC BY-NC 4.0](LICENSE)** — share and adapt with attribution, non-commercial use only. See [LICENSE](LICENSE) for details.
