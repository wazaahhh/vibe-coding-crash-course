# Vibe Coding for Scientists — Facilitator Guide

**Format:** six talk modules + two hands-on **install fests** (🛠 Code, 🖋 Manuscript). Tool-agnostic, demo-heavy.
**Audience:** Working scientists (grad students → PIs) who already code a little — typically Python/R in notebooks — and treat code as a means to an end, not a craft.
**Goal:** Shift mindset, not just show a tool. Participants leave able to *direct* an AI to write working analysis code, *and* able to catch it when it's confidently wrong.

> **One-sentence thesis to repeat:** *Vibe coding moves you from author of code to director of code — your job becomes intent, judgment, and verification, not syntax.*

The deck is **built from per-module files**: edit [modules/](modules/), run `./build.sh`, render `marp slides.md`. Syllabus in [COURSE.md](COURSE.md); per-module discussion questions in [notes/](notes/).

---

## Run of show

| Order | Block | Module file | ~min | Mode |
|-------|-------|-------------|------|------|
| — | Intro · thesis · objectives | `00-intro` | 3 | Talk + cold demo |
| 1 | Why it matters | `01-why-it-matters` | 5 | Talk |
| 2 | The mindset + science | `02-the-mindset` | 15 | Talk + poll |
| 3 | How you actually do it | `03-how-you-do-it` | 10 | Talk |
| 4 | Live demo | `04-live-demo` | 15 | Live |
| 🛠 | **Install fest · Code** | `05-install-fest-code` | 30–45 | Hands-on clinic |
| 5 | Working together in a lab | `06-working-in-a-lab` | 7 | Talk |
| 6 | Safety & ethics | `07-safety-ethics` | 5 | Talk |
| 🖋 | **Install fest · Manuscript** | `08-install-fest-manuscript` | 30–45 | Hands-on clinic |
| — | Director, not author · close | `09-close` | 3 | Talk |

**Ways to run it:** the main hour (modules 1–6) as a seminar · **Install fest · Code right after the demo** · **Install fest · Manuscript as the finale** (the paper joins the repo) · or split the two clinics into their own sittings.

**The cardinal rule:** keep a clock on the talk modules (the demo and poll want to overrun), and **don't** clock the install fests — installs and per-laptop snags set the pace.

---

## Opening + Module 1 — Why it matters (the hook)

**Objective:** make the value undeniable, and make them want module 2. *Protect the energy here — don't front-load caveats.*

**Cold-open demo.** Open with a live, un-baked prompt. Ask the room for a tiny task ("plot a sine wave with noise and fit it") and let the AI produce it in ~20 seconds. Run it. It works (or it doesn't — also teachable).

**Definition + the "in practice" slides.** "Vibe coding" (Karpathy, 2025): you describe what you want in natural language and let the model write the code — *the vibe is in how you produce code, not whether it's correct.* Walk the **In practice** examples (genomics / EEG / climate) and the **real exchange** (nuclei-counting) — the point is *you specified the outcome and caught the plausible error.* Land the **thesis** (author → director).

**Module 1 proper.** Three arguments (pick what fits): the bottleneck was the plumbing; exploration becomes cheap; it lowers the barrier for the whole lab. State the catch *once* — "trivially easy to produce *plausible, beautiful, wrong* — module 2 is how we handle that." Close on the **End of Module 1** question: *if code stops being the bottleneck, what becomes the new scarce skill in your lab?*

---

## Module 2 — The mindset

**Objective:** why directing an AI is not just *faster typing*. This is the conceptual core.

**Open with the key claim:** it changes your *role* and your *cognitive loop*. When you write code, understanding is a byproduct; when you direct, you must *choose* to engage it. The four pillars are the disciplines that make the new loop safe.

**The four pillars (≈2 min each):**
1. **Divergence / creativity** — science trains convergence; vibe coding rewards generating many options first. *"Give me three approaches, with trade-offs."* You curate, not produce.
2. **Critical thinking (non-negotiable)** — every output is a PR from a brilliant, overconfident intern. *"How would I know if this is wrong?"* Slogan: *"Trust the vibe to write it; never trust the vibe that it's right."*
3. **Thinking fast / slow** — the AI is System 1 (fast, sometimes wrong); you supply System 2 (slow, checking). Kahneman: System 2 is *lazy* by default. *The more the result matters, the more slowly you read it.*
4. **Try and fail** — generation is cheap → more attempts, smaller stakes. Failure becomes the unit of search. Git is the safety net.

**The science (2 slides).** The pillars counter *measured* effects — automation bias, cognitive offloading, illusion of explanatory depth, cognitive debt / the generation effect. Takeaway: *offload the typing, never offload the understanding your name depends on.* (Citations on-slide and in [RESOURCES.md](RESOURCES.md); the MIT "cognitive debt" study is a preprint — cite as suggestive.)

**Calibration + a scare.** "Where it shines · where it bites" tells them *where to spend System 2* (truth, not syntax). The 30-second horror story makes it visceral. **Keep your own voice** closes the module: don't regress to the mean.

**Quick poll (30 sec):** "Which pillar is hardest for you?" Hands up per pillar. Usually #2 and #3 — the two the demo will tempt them to skip. End on the discussion question.

---

## Modules 3–4 — How you do it + the live demo

**Objective:** the practical loop — and a live demo where the AI is caught being confidently wrong.

**Module 3 setup.**
- **Two modes:** chat (zero setup, you're the copy-paste bus) vs. an agent in your repo (reads files, runs code, edits in place). Most start in chat; the leap is letting the AI *into the repo*.
- **The monorepo:** code · data · figures · paper in one place. *(We build it in the install fests.)*
- **How to ask (the *intent* half):** give context, ask for a plan before code, constrain it, make it show its work, iterate in small steps. *Vague in → generic out.*

**Module 4 — live demo.** Fork the repo (`demo/`, the deliberately-messy `plant_growth.csv` — missing values, an mm/cm unit mix, a stray outlier). See [demo/README.md](demo/README.md) for the full script. Drive it live; narrate your thinking:

1. **Orient by asking, not reading** — *"summarize the columns and the data-quality problems I should worry about."*
2. **Watch it miss the unit bug** — it flags the missing values but mislabels the mm/cm rows as "outliers." **This is the set-piece.** Name it: *"Pillar 2, live — a confident, mostly-right answer that would have corrupted my analysis. I caught it because I know plants, not pandas."*
3. **Direct the fix with domain knowledge** — *"some heights look like millimetres; detect and convert those rows, show me which and why."* Verify by eye.
4. **Diverge** — *"three ways to test whether fertilizer affects height, with assumptions."* Pick one with the room.
5. **Slow down at the claim** — *"what would make this conclusion wrong? what did you assume?"* Mention notebook → script: explore, then *"harden this into a script I can rerun from scratch."*

**If the demo runs long:** cut step 4, never step 2 or 5. **If something breaks live:** good — narrate debugging by pasting the error back. Failure recovery *is* the skill (Pillar 4).

---

## 🛠 Install fest · Code — clinic *(right after the demo)*

**Objective:** everyone leaves with a working analysis setup — VS Code + Git + Claude Code, a **code + data monorepo** (data untracked), `CLAUDE.md`, a first in-repo loop, and a push to GitHub. Follow `modules/05-install-fest-code.md`.

**This is a clinic, not a lecture. Don't compress it to a slot.**
- **Pre-flight (send ahead):** GitHub + AI-tool accounts.
- **Pair people up** — no one debugs alone. Float and unblock.
- **Usual suspects:** `claude: command not found` (Node / PATH), agent pointed at the wrong folder, data committed before `.gitignore`.

The paper deliberately waits — `paper/` is added in the **Manuscript** install fest at the end.

---

## Module 5 — Working together in a lab

**Objective:** make it work for a team. The scarce resources shift to **review, standards, and rhythm.**
1. **Peer review matters *more*** — no AI-generated analysis reaches a paper without a second human reading the *reasoning and checks*.
2. **Shorter sprints, visible demos** — show what you vibe-coded *and how you verified it.*
3. **Pair on the prompts** — one drives, one plays skeptic.
4. **Share conventions** — a lab `CLAUDE.md` + pinned, shared environments.
5. **Mentor on judgment, not syntax.**
6. **Track provenance** — whose prompt, which model, what data version.

The one-liner: **peer review matters more, not less** — the failure mode is unreviewed AI code flowing straight into results. End on the discussion question.

---

## Module 6 — Safety & ethics

**Objective:** the professional duties; your name is on the paper. Five rules:
1. **Data confidentiality** — never paste patient/unpublished/embargoed data into uncleared cloud tools.
2. **Reproducibility & provenance** — commit the code, pin versions, keep the prompts. "The AI wrote it" ≠ a methods section.
3. **Correctness is yours** — it fabricates methods, stats, citations. Verify anything that reaches a result.
4. **Disclosure & authorship** — disclose assistance; AI is not an author; check journal/funder policy.
5. **Skill atrophy** — keep enough fluency to *review*. Don't outsource judgment.

**Start Monday:** pick one low-stakes thing this week. End on the discussion question (*assistance vs. undisclosed authorship*).

---

## 🖋 Install fest · Manuscript — clinic *(the finale)*

**Objective:** the paper joins the repo, so the agent can help write and maintain it. Follow `modules/08-install-fest-manuscript.md`: add `paper/`, **LaTeX in VS Code** (LaTeX Workshop), **Overleaf ↔ GitHub sync** so co-authors stay put, **Zotero → a live `.bib`**.

**Pre-flight:** pre-download a LaTeX distribution (MacTeX/MiKTeX/TeX Live, ≈4 GB) — kick the install off first thing.

**The payoff — a paper is software.** With code, data, and the manuscript in one repo, a result change can **propagate**. Tell it as a story (ideally your own): you re-run a regression; the coefficient moves 0.12 → 0.09; now the abstract number, a table, a figure, the discussion, and SI tables are stale. The agent re-runs it, updates everything, propagates into the SI, and hands back a **diff**. Frame it: a paper is a *dependency graph*; a new result is a **refactor** — propagate · diff · review · rebuild. Keep numbers **computed, not typed** (`\input{coef.tex}`) so they can't drift. The discipline: a refactor can over- or under-propagate — **you review every diff** (Pillar 2, restated).

**If you can, demo it live** on a small prepared paper-repo: change one input, ask the agent to propagate, show the diff. No repo handy? Walk the prompt and diff conceptually.

**Close** (`09-close`): repeat the thesis — *"Director, not author. The AI brings speed and breadth; you bring the question, the judgment, the responsibility. Go practice it on something low-stakes this week."* Point to [RESOURCES.md](RESOURCES.md).

---

## Pre-session checklist
- [ ] Built the deck: `./build.sh`, then render `marp slides.md` (or open in the VS Code Marp extension).
- [ ] **Cold open + demo:** your AI tool open and authenticated; test the cold-open and demo prompts once beforehand.
- [ ] **Module 4 demo:** demo repo pushed and public, URL on the slide; dataset regenerated (`python demo/generate_data.py`) and committed; a screen-recording as network/tool backup.
- [ ] **Install fest · Code:** pre-flight sent (GitHub + AI-tool accounts); you've run the full path on a clean machine once.
- [ ] **Install fest · Manuscript:** LaTeX distribution pre-downloaded; ideally a small paper-repo ready to propagate a change live.

## Compressed options
- **One 60-min seminar (no installs):** modules 1–6, demo steps 1–3 + 5 only; point people to the two install fests to set themselves up on their own time.
- **One 20-min lightning talk:** opening + module 1, plus the **manuscript "paper is software" moment** as the closing hook.
- **Clinics as their own sittings:** run Install fest · Code and Install fest · Manuscript as standalone hands-on sessions once people have seen the talks.
