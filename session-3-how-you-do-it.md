---
marp: true
theme: default
paginate: true
header: 'Vibe Coding for Scientists'
footer: 'CC BY-NC 4.0 · Thomas Maillart'
---

<!-- Render with Marp: `marp session-3-how-you-do-it.md`. Session 3 of 6 — see COURSE.md. -->

<style>
section::after {
  content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}
</style>

<!-- _class: lead -->

# Session 3 · How you actually do it

### Two modes · one repo · the right way to ask

---

# Mode A: chat · Mode B: agent in your repo

| **Chat** (browser / app) | **Agent** (VS Code + GitHub) |
|---|---|
| ChatGPT, Claude.ai — paste code, data, error → get an answer | Claude Code, Cursor, Copilot — AI **reads your files, runs code, edits in place** |
| **Zero setup**, works in 10 seconds | One-time setup: clone repo, open editor, connect |
| ⚠️ **You** are the copy-paste bus — context dies each message | **Context-aware** — sees the whole project, remembers |
| Great for a quick question or snippet | Great for a real, multi-file analysis |

Most scientists start in **chat** (and that's fine). The leap in power is letting the AI **into the repo.**

---

# Mode B, done right: one repo for everything

Put **code · data · figures · the paper · your prompts/notes** in **one repository** (a *monorepo*).

- **The AI sees the whole picture** → answers grounded in *your* data and *your* draft, not a generic guess.
- **One source of truth** → the analysis that made Figure 3 lives next to Figure 3 and the paragraph that cites it.
- **Reproducible & shareable** → a collaborator (or reviewer, or future-you) clones *one thing* and has it all.
- Add a **`CLAUDE.md` / `CONVENTIONS.md`** at the root → the agent (and the lab) follow the same rules.

> Chat answers a question. A repo lets the AI **work on your actual project.** *(We build this in Session 4.)*

---

# How to ask — the *intent* half of the job

A vague prompt gets a generic answer. Direct it like a capable new student.

- **Give context, not just the task** — the data, the goal, the constraints, what you've tried.
- **Ask for a plan *before* code** — *"Outline your approach first; I'll approve, then you write it."*
- **Constrain it** — language, libraries, "match the style in this file," "no new dependencies."
- **Make it show its work** — *"explain your reasoning,"* *"flag anything you assumed."*
- **Iterate in small steps** — one change, run, read, correct. Don't accept a 300-line dump blind.

> Vague in → generic out. **Specific intent is the lever** that makes everything downstream better.

---

<!-- _class: lead -->

# Live demo

### Fork the repo → vibe-code a real analysis

`github.com/wazaahhh/vibe-coding-crash-course`  → **Fork it**

---

# Demo arc

1. **Orient by asking, not reading** — "brief me on this dataset's problems."
2. **Watch it miss the unit bug** ← the moment of the demo.
3. **Fix with domain knowledge** — mm vs cm; show me what you changed.
4. **Diverge** — three ways to test the effect, with assumptions.
5. **Notebook *or* script?** — explore in a notebook, harden into a script.
6. **Slow down at the claim** — "What would make this conclusion wrong?"

**Notebook → script:** explore in a notebook, then *"harden this into a script I can rerun from scratch."* Get both.

---

<!-- _class: lead -->

# Next · Session 4 🛠

### Install fest — build your real setup, hands-on

Bring a laptop and a charger. We move off the browser tabs for good.
