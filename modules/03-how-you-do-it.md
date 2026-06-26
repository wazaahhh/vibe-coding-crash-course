<!-- _class: lead -->

# 3 · How you actually do it

### Two modes — same loop underneath

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

---

# Where we've been — and what's next

**Covered so far**
- **01 · Why it matters** — author → director.
- **02 · The mindset** — four pillars; you are System 2.

**This module · 03 — How you actually do it**
- Two modes — **chat** vs. **agent in your repo**
- **One repo** for code, data, figures and the paper
- **How to ask** — prompting for intent

---

# Mode A: chat · Mode B: agent in your repo

| **Chat** (browser / app) | **Agent** (editor + repo) |
|---|---|
| Paste code, data, error → get an answer | AI **reads your files, runs code, edits in place** |
| **Zero setup**, works in 10 seconds | One-time setup: clone, open editor, connect |
| ⚠️ **You** are the copy-paste bus — context dies each message | **Context-aware** — sees the whole project, remembers |
| Great for a quick question or snippet | Great for a real, multi-file analysis |

Most scientists start in **chat**. The leap in power is letting the AI **into the repo.**

---

# Mode B, done right: one repo for everything

Put **code · data · figures · the paper · your prompts** in **one repository.**

- **The AI sees the whole picture** → answers grounded in *your* data and *your* draft.
- **One source of truth** → the analysis behind Figure 3 lives next to Figure 3.
- A root **`CLAUDE.md`** → the agent (and the lab) follow the same rules.

> Chat answers a question. A repo lets the AI **work on your actual project.**

---

# How to ask — the *intent* half of the job

Direct it like a capable new student.

- **Give context, not just the task** — the data, the goal, the constraints, what you've tried.
- **Ask for a plan *before* code** — *"outline your approach; I'll approve, then you write it."*
- **Constrain it** — language, libraries, "match the style in this file," "no new dependencies."
- **Make it show its work** — *"explain your reasoning; flag anything you assumed."*
- **Iterate in small steps** — one change, run, read, correct. Never accept a 300-line dump blind.

> Vague in → generic out. **Specific intent is the lever.**

---

# End of Module 3 — recap, discussion &amp; support

**Module 03 recap — How you actually do it**
- Two modes — **chat** vs. **agent in your repo**.
- **One repo** for code, data, figures and the paper.
- **Specific intent** is the lever.

**Open question — let's discuss:** *How can a junior student — who can't yet write the code — direct an AI efficiently and correctly?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`
