# Vibe Coding for Scientists — Facilitator Guide

**Format:** a ~60-minute **main deck** ([slides.md](slides.md)) of six modules, plus two standalone **add-on modules** — a hands-on install fest and the recursive-researcher deep-dive. Tool-agnostic, demo-heavy.
**Audience:** Working scientists (grad students → PIs) who already code a little — typically Python/R in notebooks — and treat code as a means to an end, not a craft.
**Goal:** Shift mindset, not just show a tool. Participants leave able to *direct* an AI to write working analysis code, *and* able to catch it when it's confidently wrong.

> **One-sentence thesis to repeat:** *Vibe coding moves you from author of code to director of code — your job becomes intent, judgment, and verification, not syntax.*

The decks: **[slides.md](slides.md)** (main) · **[install-fest.md](install-fest.md)** · **[recursive-research.md](recursive-research.md)**. Syllabus in [COURSE.md](COURSE.md).

---

## Run of show

| Order | Block | Deck | ~min | Mode |
|-------|-------|------|------|------|
| 1 | Why it matters | slides.md | 5 | Talk + cold demo |
| 2 | The mindset + science | slides.md | 15 | Talk + poll |
| 3 | How you actually do it | slides.md | 10 | Talk |
| 4 | Live demo | slides.md | 15 | Live |
| 🛠 | **Install fest** | install-fest.md | 45–60 | Hands-on clinic |
| ＋ | The recursive researcher | recursive-research.md | 20 | Talk + live demo |
| 5 | Working together in a lab | slides.md | 7 | Talk |
| 6 | Safety & ethics | slides.md | 5 | Talk |

**Ways to run it:** the main hour (modules 1–6) as a seminar · the **install fest right after the demo** as its own clinic, then **the recursive researcher** while everyone has a fresh repo open · lab & safety to close.

**The cardinal rule:** keep a clock on the talk modules (the demo and poll want to overrun), and **don't** clock the install fest — installs and per-laptop snags set its pace.

---

## Module 1 — Why it matters (the hook)

**Objective:** make the value undeniable, and make them want Session 2. *Protect the energy here — don't front-load caveats.*

**0–3 — Cold-open demo.** Open with a live, un-baked prompt. Ask the room for a tiny task ("plot a sine wave with noise and fit it") and let the AI produce it in ~20 seconds. Run it. It works (or it doesn't — also teachable).

**3–12 — Definition + why it matters.**
- "Vibe coding" (Karpathy, 2025): you describe what you want in natural language and let the model write the code. The honest version for scientists: *the vibe is in how you produce code, not whether it's correct.*
- Three arguments (pick what fits the room): **(1)** the bottleneck was never the science — it was the plumbing; **(2)** exploration becomes cheap — five specs, three plots, two normalizations in the time of one; **(3)** it lowers the barrier for the whole lab.
- State the catch *once*, then move on: "It's also trivially easy to produce *plausible, beautiful, wrong*. Session 2 is how we handle that."

**12–20 — The vision + roadmap.** Walk the "what you'll be able to do by the end" slide — land the reviewer line (*"a new robustness check goes from a dreaded week to an afternoon — that's Session 5"*). Show the 6-session roadmap. Close on the hook to Session 2.

---

## Module 2 — The mindset

**Objective:** why directing an AI is not just *faster typing*. This is the conceptual core.

**Open with the key claim:** "Why isn't this just faster typing?" Answer: it changes your *role* and your *cognitive loop*. When you write code, understanding is a byproduct; when you direct, understanding is no longer automatic — you must *choose* to engage it. The four pillars are the disciplines that make the new loop safe.

**The four pillars (≈2 min each):**
1. **Divergence / creativity** — science trains convergence; vibe coding rewards generating many options first. *"Give me three approaches, with trade-offs."* You curate, not produce.
2. **Critical thinking (non-negotiable)** — every output is a PR from a brilliant, overconfident intern. Ask *"how would I know if this is wrong?"* before trusting the pretty plot. Slogan: *"Trust the vibe to write it; never trust the vibe that it's right."*
3. **Thinking fast / slow** — the AI is System 1 (fast, sometimes wrong); you supply System 2 (slow, checking). The Kahneman quote lands the point: System 2 is *lazy* by default. *The more the result matters, the more slowly you read it.*
4. **Try and fail** — generation is cheap → more attempts, smaller stakes. Failure costs minutes; it becomes the unit of search. Git is the safety net.

**The science (1 slide).** The pillars counter *measured* effects — automation bias, cognitive offloading, the illusion of explanatory depth, and cognitive debt / the generation effect. The takeaway line: *offload the typing, never offload the understanding your name depends on.* (Citations are on the slide and in [RESOURCES.md](RESOURCES.md); the MIT "cognitive debt" study is a preprint — cite as suggestive.)

**Calibration + a scare.** "Where it shines · where it bites" tells them *where to spend System 2* (truth, not syntax). The 30-second horror story makes it visceral: the failures all *ran perfectly*.

**Quick poll (30 sec):** "Which pillar is hardest for you?" Hands up per pillar. Usually surfaces #2 and #3 — the two they'll be tempted to skip in the demo.

> Note: "Keep your own voice" now lives in **Session 6** (it fits standards/responsibility). If you'd rather teach it here, it's a clean lift.

---

## Modules 3–4 — How you do it + the live demo

**Objective:** the practical loop — and a live demo where the AI is caught being confidently wrong.

**0–8 — The setup.**
- **Two modes:** chat in a browser (zero setup, you're the copy-paste bus) vs. an agent in your repo (reads files, runs code, edits in place). Most scientists start in chat; the leap is letting the AI *into the repo*.
- **The monorepo:** code · data · figures · paper in one place, so the AI sees the whole picture. *(We build this in Session 4.)*
- **How to ask (the *intent* half):** give context, ask for a plan before code, constrain it, make it show its work, iterate in small steps. *Vague in → generic out.*

**8–20 — Live demo.** Fork the repo (`demo/`, the deliberately-messy `plant_growth.csv` — missing values, an mm/cm unit mix, a stray outlier). See [demo/README.md](demo/README.md) for the full script. Drive it live; narrate your thinking:

1. **Orient by asking, not reading** — *"summarize the columns and the data-quality problems I should worry about."*
2. **Watch it miss the unit bug** — it flags the missing values but misses (or mislabels) the mm/cm mix. **This is the set-piece.** Stop and name it: *"Pillar 2, live — a confident, mostly-right answer that would have corrupted my analysis. I caught it because I know plants, not pandas."*
3. **Direct the fix with domain knowledge** — *"some heights look like millimetres; detect and convert those rows, show me which and why."* Verify by eye.
4. **Diverge** — *"three ways to test whether fertilizer affects height, with assumptions."* Pick one with the room.
5. **Slow down at the claim** — *"what would make this conclusion wrong? what did you assume?"* Verification is part of the workflow, not an afterthought. Mention notebook → script: explore in a notebook, then *"harden this into a script I can rerun from scratch."*

**If the demo runs long:** cut step 4, never step 2 or 5. **If something breaks live:** good — narrate debugging by pasting the error back. Failure recovery *is* the skill (Pillar 4).

---

## 🛠 Install fest — add-on clinic *(run it right after the demo)*

**Objective:** everyone leaves with a working setup — VS Code + Git + Claude Code, a code + LaTeX monorepo (data untracked), Overleaf → local LaTeX (with **GitHub sync** so co-authors stay in Overleaf), Zotero → a live `.bib`. Follow [install-fest.md](install-fest.md) step by step.

**This is a clinic, not a lecture. Don't compress it to a slot** — installs and per-laptop snags set the pace. Run it as:
- **Pre-flight (send ahead, days before):** create GitHub + Anthropic accounts; **pre-download a LaTeX distribution** (MacTeX/MiKTeX/TeX Live, ≈4 GB).
- **At the start:** kick off the LaTeX install immediately so it finishes by the time you reach Move 3.
- **Pair people up** — no one debugs alone. Float and unblock.
- **Optional break after Move 2** (the deck has a slide for it): by then everyone has an editor, an agent, and a repo on GitHub.

**Keep the troubleshooting slide up** during the hands-on stretch — most questions are the usual suspects (`claude: command not found`, LaTeX still installing, `refs.bib` not auto-updating, agent pointed at the wrong folder, data committed by accident).

---

## ＋ The recursive researcher — add-on module *(follow-up)*

**Objective:** show the payoff that sells the whole approach — and frame *a paper as software*.

**0–4 — The moment.** Tell it as a story (ideally your own): you re-run a regression with a fix; the coefficient moves 0.12 → 0.09; now the abstract number, a table, a figure, the interpretation, the robustness paragraph, and three SI tables are all stale. The agent re-ran the regression, updated everything, propagated into the SI, and handed back a *diff*. *"It didn't answer a question — it maintained the document like a codebase."*

**4–12 — Why this is software engineering.** A paper is a *dependency graph* (data → regression → numbers → tables/figures → claims → abstract → SI). A new result is a **refactor**: propagate · diff · review · rebuild. Walk the analogy table (call graph, regression tests, `make`, PR review). Make the user's point explicitly: **LLM use was optimized for code first** — machine-checkable correctness, mature tooling (git/CI/`make`), oceans of training data — and a paper is *informal software*, so we bring that tooling to it.

**12–18 — How to make it real.** The enabling condition is the monorepo (Session 4) plus making the graph explicit: **computed, not typed** numbers (`\input{coef.tex}`), generated tables/figures, a reproducible one-command build, consistency checks. The propagation prompt is a *refactor request* (show the example on the slide). 

**If you can, demo it live** on a prepared repo with a tiny paper: change one input, ask the agent to propagate, and show the diff. No repo handy? Walk the prompt and the diff conceptually — it still lands.

**18–20 — The discipline + payoff.** A refactor can over- or under-propagate; **you review every diff** (Pillar 2, restated). Payoff: a late data fix or a reviewer's new spec drops from a dreaded week to an afternoon. Close: *treat your paper like a codebase.*

---

## Modules 5–6 — The lab & safety

**Objective:** make it work for a team, safely, and close the course.

**0–7 — How a lab works when generation is cheap.** The scarce resources shift to **review, standards, and rhythm.**
1. **Peer review matters *more*** — no AI-generated analysis reaches a paper without a second human reading the *reasoning and checks*, not just that it runs.
2. **Shorter sprints, visible demos** — show-and-tell what you vibe-coded *and how you verified it.*
3. **Pair on the prompts** — one drives, one plays skeptic in real time.
4. **Share conventions** — a lab `CONVENTIONS.md` / `CLAUDE.md` + pinned environments.
5. **Mentor on judgment, not syntax** — onboarding gets easier; teaching taste and verification gets more important.

**7–11 — Keep your own voice.** AI defaults to the *average of everything* → generic. Delegate boilerplate; keep what carries meaning (which question, which comparison, how it's told). Direct toward *your* style (*"match the conventions in this file"*); edit the meaningful parts until they sound like you. *"Let it handle the boilerplate; keep the parts that are you."*

**11–18 — Safety & ethics (five rules).**
1. **Data confidentiality** — never paste patient/unpublished/embargoed data into uncleared cloud tools; know your institution's policy.
2. **Reproducibility & provenance** — commit the code, pin versions, keep the prompts. "The AI wrote it" ≠ a methods section.
3. **Correctness is yours** — it fabricates methods, stats, citations fluently. Verify anything that reaches a result.
4. **Disclosure & authorship** — disclose assistance; AI is not an author; check journal/funder policy.
5. **Skill atrophy** — keep enough fluency to *review*. Don't outsource judgment.

**18–20 — Close.** Repeat the thesis: *"Director, not author. The AI brings speed and breadth; you bring the question, the judgment, the responsibility. Go practice it on something low-stakes this week."* Point them to "Start Monday" and [RESOURCES.md](RESOURCES.md).

---

## Pre-session checklist
- [ ] Decks render (`marp session-N-….md`) or open in the VS Code Marp extension.
- [ ] **Sessions 1 & 3:** your AI tool open and authenticated; test the cold-open and demo prompts once beforehand.
- [ ] **Session 3:** demo repo pushed and public, URL on the slide; dataset regenerated (`python demo/generate_data.py`) and committed; a screen-recording as network/tool backup.
- [ ] **Session 4:** pre-flight sent (accounts + LaTeX download); you've run the full install path on a clean machine once.
- [ ] **Session 5:** ideally a small prepared paper-repo to propagate a change live; otherwise the prompt + diff walkthrough.

## Compressed options
- **One 60-min seminar (no install):** Sessions 1 + 2 + 3, demo steps 1–3 + 5 only. Defer 4–6 to a follow-up.
- **One 20-min lightning talk:** Session 1 only, plus the Session 5 "moment" as the closing hook.
- **Skip the clinic:** run the main deck (modules 1–6) as talks; point people to [install-fest.md](install-fest.md) to set themselves up on their own time.
