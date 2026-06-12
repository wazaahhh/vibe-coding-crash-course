---
marp: true
theme: default
paginate: true
header: 'Vibe Coding for Scientists'
footer: 'CC BY-NC 4.0 · Thomas Maillart'
---

<!-- Render with Marp: `marp session-1-the-hook.md`. Session 1 of 6 — see COURSE.md. -->

<style>
section::after {
  content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}
</style>

# Vibe Coding for Scientists

### A hands-on course · 6 × 20 minutes

From *writing* code to *directing* it.

<!-- Speaker: cold-open. Take a task from the room, vibe-code it live in 20s, run it. Then this slide. -->

---

<!-- _class: lead -->

# Session 1 · Why this changes your research

### The 20 minutes that make you want the rest

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

# Why it matters — for *you*, specifically

You're not a professional programmer. Code is **friction** between a question and an answer.

1. **The bottleneck was never the science — it was the plumbing.**
   Hours of Stack-Overflow archaeology → minutes.
2. **Exploration becomes cheap.**
   Five model specs, three plots, two normalizations — in the time of one.
3. **It lowers the barrier for the whole lab.**
   The student who "can't code" can ship a working pipeline.

⚠️ It's also trivially easy to produce **plausible · beautiful · wrong** — we handle that in Session 2.

---

# What you'll be able to do by the end

By the final session, from **one window**:

- **Ask, don't plumb** — *"load this data, fit the model, plot it"* → minutes, not a day.
- **One repo for everything** — code, paper, and data in a single place the AI can see.
- **Write the paper *with* the agent** — LaTeX in VS Code, references and all.
- **Change one result → it propagates** — tables, figures, abstract, and Supplementary Materials update together.

> A reviewer demands a new robustness check. Today: a dreaded week. By Session 5: an afternoon.

---

# The course — 6 × 20 minutes

| # | Session | Mode |
|---|---|---|
| 1 | **The hook** — why this changes your research | talk + live demo |
| 2 | **The mindset** — four pillars + the cognitive science | talk + poll |
| 3 | **How you actually do it** — modes, prompting, demo | talk + demo |
| 4 | **Install fest** — build your real setup | 🛠 hands-on clinic |
| 5 | **The recursive researcher** — one change, propagated | talk + demo |
| 6 | **The lab & the responsibility** — collaboration, safety | talk |

> Mix and match: run 1–3 as a seminar, 4 as a clinic, 5–6 as a follow-up.

---

<!-- _class: lead -->

# Next · Session 2

### The mindset — why this isn't just *faster typing*

The upside is real. So is the way it can fool you. That's next.
