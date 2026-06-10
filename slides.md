---
marp: true
theme: default
paginate: true
header: 'Vibe Coding for Scientists'
---

<!-- Render with Marp: `marp slides.md` (HTML/PDF/PPTX), or open in VS Code with the Marp extension. -->

# Vibe Coding for Scientists

### A 60-minute crash course

From *writing* code to *directing* it.

<!-- Speaker: cold-open. Take a task from the room, vibe-code it live in 20s, run it. Then this slide. -->

---

# What "vibe coding" means

- You describe **what you want** in plain language; the model writes the code.
- Term popularized by **Andrej Karpathy (2025)** — "give in to the vibes."
- The honest version for scientists:
  > The vibe is in **how you produce** code — **not** in whether it's correct.
- Tool-agnostic: Claude Code, Cursor, Copilot, paste-into-chat — same loop underneath.

---

# The thesis (we'll repeat this)

## You move from **author** of code to **director** of code.

Your job becomes **intent · judgment · verification** — not syntax.

---

<!-- _class: lead -->

# 1 · Why it matters

---

# Why it matters — for *you*, specifically

You're not a professional programmer. Code is **friction** between a question and an answer.

1. **The bottleneck was never the science — it was the plumbing.**
   Hours of Stack-Overflow archaeology → minutes.
2. **Exploration becomes cheap.**
   Five model specs, three plots, two normalizations — in the time of one.
3. **It lowers the barrier for the whole lab.**
   The student who "can't code" can ship a working pipeline.

⚠️ It's also trivially easy to produce **plausible · beautiful · wrong**.

---

<!-- _class: lead -->

# 2 · The mindset

### Why this isn't just *faster typing*

---

# Why it's not a trivial adaptation

When **you** write code, understanding comes **for free** — as a byproduct.

When you **direct** an AI, understanding is **no longer automatic.**
You have to *choose* to engage it.

→ Your **role** changes. Your **cognitive loop** changes.
The four pillars are the disciplines that make the new loop safe.

---

# Pillar 1 — Divergence / creativity

- Science trains **convergence**: narrow to the one right method.
- Vibe coding rewards **divergence first**: generation is nearly free, so generate many.
- **Do:** *"Give me three approaches, with trade-offs."* Curate, don't produce.
- Reframe: divergence is the **search**; convergence is the **selection**. You still converge — later, with more on the table.

---

# Pillar 2 — Critical thinking

### The non-negotiable

- The model is **confident, fluent, and occasionally fabricating** — in flawless prose.
- **Reviewer stance:** every output is a PR from a brilliant, overconfident intern.
- Ask **"How would I know if this is wrong?"** *before* trusting the pretty plot.
- Tactics: explain its reasoning · argue against itself · check vs. a back-of-envelope · run a case you know.

> Trust the vibe to **write** it; never trust the vibe that it's **right**.

---

# Pillar 3 — Thinking fast / slow

- The AI is your **System 1**: fast, fluent, sometimes wrong.
- **You** supply **System 2**: slow, deliberate, checking.
- Failure mode: speed seduces you into skipping System 2.
- Discipline: **fast on generation, slow on consequential checkpoints.**

> The more the result matters, the more slowly you must read it.

---

# Pillar 4 — Try and fail

- Generation is cheap → **more attempts, smaller stakes.**
- Prototype to throw away. Fork, branch, experiment, delete.
- Failure costs **minutes, not a day** → failure becomes the **unit of search.**
- Keep prototypes disposable and version-controlled. Git is your safety net.

---

# Which pillar is hardest for *you*?

🙋 Divergence  ·  🙋 Critical thinking  ·  🙋 Slowing down  ·  🙋 Failing fast

<!-- Speaker: quick hands-up poll. Usually #2 and #3. Emphasize those before the demo — it's where they'll be tempted to skip both. -->

---

# Keep your own voice

AI is trained on the **average of everything** → its default is **generic.**
Lean on it uncritically and your work drifts to the mean.

- **Style vs. boilerplate:** delegate the boilerplate; keep the parts that carry meaning (which question, which comparison, how it's told).
- **Direct toward *your* style:** *"match the conventions in this file."* Don't adopt the AI's.
- **Edit toward your voice:** the first output is a draft in someone else's handwriting. The last mile is where *you* go back in.
- **Keep your hands in** — retain the taste that lets you notice when output is bland.

> Let it handle the boilerplate; keep the parts that are **you.**

---

<!-- _class: lead -->

# 3 · Demo

### Fork the repo → vibe-code a real analysis

`github.com/<you>/vibe-coding-crash-course`  → **Fork it**

---

# Demo arc

1. **Orient by asking, not reading** — "brief me on this dataset's problems."
2. **Watch it miss the unit bug** ← the moment of the demo.
3. **Fix with domain knowledge** — mm vs cm; show me what you changed.
4. **Diverge** — three ways to test the effect, with assumptions.
5. **Notebook *or* script?** — explore in a notebook, harden into a script.
6. **Slow down at the claim** — "What would make this conclusion wrong?"

---

# Notebook or not?

| Notebook | Script + agent |
|---|---|
| Great for **exploration** | Great for **reproducibility** |
| See each step, plots inline | Reruns clean from scratch |
| ⚠️ hidden state, out-of-order cells | AI runs, reads errors, self-fixes |

**Recommendation:** explore in a notebook → *"harden this into a script I can rerun from scratch."* Get both.

---

<!-- _class: lead -->

# 4 · Working together in a lab

### When generation is cheap, the real work is review, standards & rhythm

---

# How a lab works in the age of vibe coding

1. **Peer review matters *more*** — no AI-generated analysis reaches a paper without a second human reading it. Review the *reasoning and checks*, not just that it runs.
2. **Shorter sprints, visible demos** — end each cycle with a show-and-tell: what you vibe-coded **and how you verified it.**
3. **Pair on the prompts** — one drives, one plays skeptic in real time.
4. **Share conventions** — a lab `CONVENTIONS.md` / `CLAUDE.md` + pinned environments, so output is consistent and reproducible.
5. **Mentor on judgment, not syntax** — onboarding gets easier; teaching taste and verification gets more important.

> When generation is cheap, the lab's real work is **review, standards, and rhythm.**

---

<!-- _class: lead -->

# 5 · Safety & ethics

### Your name is on the paper

---

# Five rules

1. **Data confidentiality** — don't paste patient/unpublished/embargoed data into uncleared cloud tools.
2. **Reproducibility & provenance** — commit the code, pin versions, **keep the prompts**. "The AI wrote it" ≠ a methods section.
3. **Correctness is yours** — it fabricates methods, stats, citations. Verify anything that reaches a result.
4. **Disclosure & authorship** — disclose assistance; AI is not an author; check journal/funder policy.
5. **Skill atrophy** — keep enough fluency to *review*. Don't outsource judgment.

---

<!-- _class: lead -->

# Director, not author.

The AI brings **speed and breadth.**
You bring the **question, the judgment, the responsibility.**

### That division of labor *is* the skill.

Go practice it on something low-stakes this week.
