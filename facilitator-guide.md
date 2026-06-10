# Vibe Coding for Scientists — Facilitator Guide

**Format:** 60 minutes, tool-agnostic, demo-heavy.
**Audience:** Working scientists (grad students → PIs) who already code a little — typically Python/R in notebooks — and treat code as a means to an end, not a craft.
**Goal of the hour:** Shift mindset, not just show a tool. Participants leave able to *direct* an AI to write working analysis code, *and* able to catch it when it's confidently wrong.

> **One-sentence thesis to repeat 3×:** *Vibe coding moves you from author of code to director of code — your job becomes intent, judgment, and verification, not syntax.*

---

## Run of show (60 min)

| Time | Block | Mode |
|------|-------|------|
| 0:00–0:03 | Hook + what "vibe coding" actually means | Talk |
| 0:03–0:10 | **Why it matters** (for scientists specifically) | Talk |
| 0:10–0:30 | **The mindset** — 4 pillars + keeping your own voice | Talk + 1 quick poll |
| 0:30–0:49 | **Demo / hands-on** — fork the repo, vibe-code an analysis | Live + follow-along |
| 0:49–0:56 | **Working together in a lab** — peer-review, sprints, shared conventions | Talk |
| 0:56–0:60 | **Safety / ethics** + close | Talk |

Keep a clock visible. The demo will try to eat the whole hour — protect the last 11 minutes for the "working responsibly" blocks (lab + safety); they're the parts scientists most need and most skip.

---

## 0:00–0:03 — Hook + definition

**Do:** Open with a live, cold prompt. Don't pre-bake it. Ask the room for a tiny task ("plot a sine wave with noise and fit it") and let the AI produce it in ~20 seconds. Run it. It works (or it doesn't — also a teachable moment).

**Say:**
- "Vibe coding" (term popularized by Andrej Karpathy, 2025): you describe what you want in natural language and let the model write the code. You "give in to the vibes" and stay at the level of intent.
- The honest version for scientists: you are still responsible for the result. The vibe is in *how you produce* code, not in *whether it's correct*.
- Today is about the **mindset shift**, with a hands-on demo. Tool doesn't matter — Claude Code, Cursor, Copilot, or paste-into-chat all work the same way underneath.

---

## 0:03–0:11 — Why it matters

**Frame:** Scientists are not professional programmers. Code is friction between a question and an answer. Vibe coding removes most of that friction — which is a bigger deal for you than for a software engineer.

**Three concrete arguments (pick the ones that fit your room):**

1. **The bottleneck was never the science — it was the plumbing.** Reading a CSV with weird encodings, remembering matplotlib's API, wrangling a dataframe. AI collapses hours of Stack-Overflow archaeology into minutes. You spend your scarce attention on the question, not the syntax.

2. **Exploration becomes cheap.** The cost of "what if I tried it this other way?" drops to near zero. You can test five model specifications, three plots, two normalizations — in the time it used to take to do one. This changes *what experiments you even consider*.

3. **It lowers the barrier for the whole lab.** The grad student who "can't code" can now produce a working pipeline. This is democratizing — and dangerous (see safety). It widens who can participate, which is exactly the collective-intelligence upside.

**Honest caveat to state out loud:** It also makes it trivially easy to produce *plausible, beautiful, wrong* results. That tension is the whole reason the mindset section exists.

---

## 0:11–0:30 — The mindset (the core of the hour)

**Open with the key claim:** "You already use computers every day. So why isn't this just *faster typing*? Why is it a genuinely new skill?"

**Answer:** Because it changes your *role* and your *cognitive loop*. When you write code yourself, you understand it as a byproduct of writing it. When you direct an AI, understanding is no longer automatic — you have to *choose* to engage it. That's the non-trivial adaptation. The four pillars are the disciplines that make the new loop safe and powerful.

### Pillar 1 — Divergence / creativity
- Scientific training rewards *convergence*: narrow to the one right method, the one hypothesis. Vibe coding rewards *divergence first*: generate many candidate approaches fast, because generation is now nearly free.
- **Practice:** ask the model for 3 different ways to do something before picking one. "Give me three approaches to detect the change-point in this series, with trade-offs." You become a curator of options, not a producer of one.
- This is uncomfortable for trained scientists — it feels unrigorous. Reframe: divergence is the *search*, convergence is the *selection*. You still converge — just later, with more options on the table.

### Pillar 2 — Critical thinking (the non-negotiable)
- The model is a confident, fluent, occasionally-fabricating collaborator. It will invent a statistical method, misuse a test, hallucinate a function or a citation — in flawless prose.
- **The reviewer stance:** treat every output as a pull request from a brilliant, overconfident intern. Default to skeptical. Ask "how would I know if this is wrong?" *before* you trust the pretty plot.
- **Practical tactics:** ask the model to explain its reasoning; ask it to argue against its own answer; check the result against a back-of-envelope expectation; run on a tiny case where you know the answer.
- Slogan: **"Trust the vibe to write it; never trust the vibe that it's right."**

### Pillar 3 — Thinking fast / slow (Kahneman, weaponized)
- The AI is your **System 1**: fast, fluent, associative, pattern-matched, sometimes wrong. *You* must supply **System 2**: slow, deliberate, checking.
- The failure mode of vibe coding is letting the AI's speed seduce you into skipping System 2. The plot appears in 10 seconds and looks great, so you move on.
- **The discipline:** go fast on generation, deliberately slow on *consequential* checkpoints. Where does slow matter? Anywhere a wrong answer would end up in a paper, a grant, or a decision. Speed for scaffolding; deliberation for claims.
- Practical rule: *the more the result matters, the more slowly you must read it.*

### Pillar 4 — Try and fail (cheap, fast, often)
- Generation is now so cheap that the optimal strategy is *more attempts, smaller stakes*. Prototype to throw away. Fork, branch, experiment, delete.
- This rewires risk: a failed attempt costs minutes, not a day. Failure stops being a setback and becomes the unit of search.
- **Practice:** keep prototypes disposable and version-controlled. Name the throwaway as throwaway. The git repo is your safety net — you can always revert.

**Quick poll (30 sec, optional):** "Which pillar is hardest for you?" Hands up per pillar. It usually surfaces #2 (critical thinking) and #3 (slowing down) — exactly the ones to emphasize before the demo, because the demo is where they'll be tempted to skip both.

### Keeping your own voice (don't regress to the mean)
- AI is trained on the average of everything, so its default output is **generic** — median variable names, median figures, median prose, median method choices. Lean on it uncritically and your work drifts toward that mean. For a scientist, your *taste* — the questions you pose, how you frame a figure, the structure of an argument — is part of what makes the work yours and good.
- **Distinguish style from boilerplate.** Boilerplate (reading a CSV, a standard plot scaffold) — delegate freely, no one's voice lives there. Style (which question, which comparison, how the result is told) — that's yours to keep; don't outsource it.
- **Direct the AI toward your style, don't adopt its.** Feed it examples of your code and figures: *"match the conventions in this file."* Keep a lab/personal house style (naming, plotting defaults, structure) and make the AI conform to it, not the reverse.
- **Edit toward your voice.** Treat the first output as a draft in someone else's handwriting. Rewrite the parts that carry meaning until they sound like you. The AI gets you to a draft 10× faster; the *last mile* is where your voice goes back in.
- **Keep your hands in.** Do some things manually to retain the taste that lets you *notice* when AI output is bland or off. You can't direct toward a standard you've lost the ability to feel.
- One-liner: **"Let it handle the boilerplate; keep the parts that are you."**

---

## 0:30–0:49 — Demo / hands-on

**Setup (have this ready before the session):**
- The demo repo URL on screen. Tell everyone to **fork it** (or "Use this template" / clone). Forking — not just cloning — is the point: it gives them their own sandbox to break.
- See `demo/README.md` for the full script. The dataset (`demo/data/plant_growth.csv`) is deliberately messy: missing values, a unit inconsistency (some heights in mm, most in cm), and a stray outlier.

**The arc (drive it live; narrate your thinking):**

1. **Orient by asking, not reading.** Don't open the CSV and squint. Prompt: *"Load `data/plant_growth.csv`, summarize the columns, and tell me about data-quality problems I should worry about."* — Model the "ask the AI to brief you" move.

2. **Watch it miss something.** The model will likely report the missing values but *miss the mm/cm unit mix* (or flag it as an outlier instead of a unit error). **This is the set-piece of the demo.** Stop. Point it out. "This is Pillar 2 live — it gave a confident, mostly-right answer that would have corrupted my analysis. I caught it because I know plants, not because I know pandas."

3. **Direct the fix with domain knowledge.** Prompt the correction: *"Some heights look like they're in millimetres. Detect and convert those rows; show me which rows you changed and why."* Verify the changed rows by eye.

4. **Diverge (Pillar 1).** *"Give me three ways to test whether fertilizer affects height, with the assumptions each one makes."* Discuss trade-offs out loud. Pick one *with the room*.

5. **Notebooks-or-not — address it directly.** Show the same task two ways and name the trade-off:
   - **Notebook:** great for *exploration* — see each step, plots inline, poke at intermediate state. Bad for *reproducibility* (hidden state, out-of-order cells) — exactly the trap that bites science.
   - **Script + agent:** great for *reproducibility and reruns*; the AI can run, read errors, and fix itself end-to-end. Less immediate.
   - **Recommendation to give them:** explore in a notebook, then have the AI "harden this into a script I can rerun from scratch." Get both.

6. **Slow down at the claim (Pillar 3).** When you reach the result ("fertilizer increases height by X, p=…"), stop and read it slowly. Ask the model: *"What would make this conclusion wrong? What assumptions did you make?"* Show that the verification prompt is part of the workflow, not an afterthought.

**If the demo runs long:** cut step 4 or 5, never step 2 or 6 — those carry the lesson.

**If something breaks live:** good. Narrate how you'd debug it by pasting the error back. Failure recovery *is* the skill (Pillar 4).

---

## 0:49–0:56 — Working together in a lab

**Frame:** "Vibe coding doesn't just change how *you* work — it changes how a *lab* works. When everyone can generate code fast, the scarce resources shift to **review, shared standards, and rhythm.**"

1. **Peer review matters *more*, not less.** When code is cheap to produce and easy to trust, the failure mode is unreviewed AI code flowing straight into results. Make it a norm: **no AI-generated analysis reaches a paper without a human besides the author reading it** — the same bar you'd hold a colleague's PR to. Review the *reasoning and the checks*, not just whether it runs.

2. **Shorter sprints, visible demos.** Cheap iteration makes short cycles natural. Adopt a lightweight rhythm: week-long (or shorter) sprints ending in a **show-and-tell** where people demo what they vibe-coded and how they verified it. The demo culture spreads good verification habits faster than any guideline.

3. **Pair on the prompts.** Vibe coding is great for pairing: one person drives the prompts, the other plays skeptic (Pillar 2) in real time. Two people catch the confident-but-wrong output far better than one in flow.

4. **Share conventions, not just code.** Maintain a lab "house style" and a shared prompt/context file (e.g. a `CONVENTIONS.md` or `CLAUDE.md`) so everyone's AI produces consistent, reviewable output. Shared, pinned environments so "it ran for me" means "it runs for you."

5. **Onboarding gets easier — mentorship gets more important.** New members ship working pipelines on day one, but the thing that *doesn't* come from the AI — judgment about what's worth doing and whether a result is trustworthy — now has to be taught deliberately. Mentor on taste and verification, not syntax.

6. **Track provenance as a team.** Whose prompt, which model, what data version. Reproducibility is a team contract: someone else must be able to rerun it next year.

**One-liner:** *"When generation is cheap, the lab's real work is review, standards, and rhythm."*

---

## 0:56–0:60 — Safety / ethics

**Frame:** "You're scientists. Your output has to be reproducible, honest, and not harmful. Vibe coding stresses all three. Five rules:"

1. **Data confidentiality.** Pasting data or code into a cloud model may send it off your machine. Never paste patient data, unpublished results, human-subjects data, or anything under embargo/NDA into a tool you haven't cleared. Know your institution's policy; prefer local or approved tools for sensitive data.

2. **Reproducibility & provenance.** AI-written code is still a research artifact. Commit it to git, pin package versions, and keep the prompts — the prompt is part of your method. "The AI wrote it" is not a methods section.

3. **Correctness is your name on the paper.** The model can fabricate methods, misapply statistics, and invent citations fluently. You are accountable for everything it produces. Verify anything that reaches a result, figure, or claim. (Pillar 2 + 3, restated as professional duty.)

4. **Disclosure & authorship.** Norms are still forming, but trending toward: disclose AI assistance, and AI is not an author. Check your journal/funder policy. Don't hide it; don't over-claim it.

5. **Skill atrophy & over-reliance.** If you can no longer evaluate the code, you can no longer trust it. Keep enough fluency to review. Use it to go faster on what you understand and to learn what you don't — not to outsource judgment.

**Close (30 sec):** Repeat the thesis. "Director, not author. The AI brings speed and breadth; you bring the question, the judgment, and the responsibility. That division of labor is the whole skill — go practice it on something low-stakes this week."

---

## Pre-session checklist
- [ ] Demo repo pushed and public; URL on a slide.
- [ ] Your AI tool of choice open and authenticated; test the cold-open prompt once beforehand.
- [ ] Dataset regenerated (`python demo/generate_data.py`) and committed.
- [ ] Backup: a screen-recording of the demo in case of network/tool failure.
- [ ] Decide your stance on participants following along live vs. watching — both work; following along eats more time but sticks better.

## If you only have 30 minutes
Cut "why it matters" to 3 min, do pillars 2 + 3 only, run demo steps 1–3 + 6, keep safety rules 1–3.
