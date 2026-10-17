<!-- _class: lead -->

# 6 · Edit modes, models &amp; steering the prompt

### Same agent, very different behaviour — learn the controls

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

<!-- Speaker: this is the "driver's ed" module — the knobs that decide how much rope you give the AI. Tool-agnostic: Claude Code / Cursor / Copilot all have these three dials, named differently. Keep it concrete. -->

---

# Where we've been — and what's next

**Covered so far**
- **01 · Why it matters** — author → director.
- **02 · The mindset** — four pillars; you are System 2.
- **03 · How you actually do it** — chat vs. agent; intent is the lever.
- **04 · Live demo** — we caught the bug the AI missed.
- **05 · Git &amp; GitHub** — the safety net; the agent can drive `gh`.

**This module · 06 — Edit modes, models &amp; the prompt**
- **Edit modes** — how much rope you give it
- **Models** — pick the right brain for the job
- **Steering** — interact with the prompt in flight

---

# Three dials you control

Every agentic tool (Claude Code · Cursor · Copilot) gives you the **same three knobs**, named differently:

1. **Edit mode** — *may it change files, and do you approve each edit?*
2. **Model** — *how strong (and how expensive/slow) is the brain?*
3. **The prompt loop** — *how you steer, correct, and stop it mid-task.*

> The mindset (Module 2) is the *why*. These are the **controls that put it into practice.**

---

# Dial 1 — edit modes: how much rope

| Mode | What it does | Use when |
|---|---|---|
| **Ask / chat** | Answers, suggests — **touches nothing** | Exploring, learning, "what would you do?" |
| **Edit / inline** | Proposes edits, **you accept each diff** | Real work — the **default** for results that matter |
| **Agent / auto** | Edits, runs, self-corrects across files | Scaffolding, mechanical refactors, tests |
| **Plan first** | Writes a plan, waits for your **OK** | Anything big or unfamiliar |

⚠️ **Auto-accept ("yolo") is the danger zone** — fast, but it's **Pillar 2 switched off.** Fine on a throwaway branch; never on `main`, never on the analysis behind a claim.

> Match the rope to the stakes. Low stakes → agent. Your name on it → **review every diff.**

---

# Edit modes + git = a seatbelt

The looser the edit mode, the more you lean on **Module 5:**

- **Commit before** you hand over auto/agent mode → a guaranteed way back.
- Let it run, then **`git diff`** the whole thing → your review checkpoint.
- Hate it? `git restore .` Love it? Commit.

> **Auto-accept is only safe because git makes it reversible.** The two modules are one system.

---

# Dial 2 — pick the right model

Models trade **capability** against **speed &amp; cost**. You choose per task.

| Reach for a **frontier / "thinking"** model | Reach for a **fast / small** model |
|---|---|
| Tricky stats, subtle bugs, study design | Boilerplate, renaming, formatting |
| Multi-step reasoning, "why is this wrong?" | Quick edits, obvious fixes |
| The result **matters** | You want **speed &amp; volume** |

- **Reasoning / extended-thinking** modes think longer before answering — better on hard problems, slower and pricier.
- **Bigger context window** = it can hold more of your repo at once (whole notebook + data dictionary + paper).

> Don't pay a frontier model to rename a variable — and don't ask a tiny one to design your analysis. **Escalate when it's stuck.**

---

# Dial 3 — steer the prompt in flight

You are **in the loop**, not firing one prompt and hoping.

- **Plan before code** — *"outline your approach; I'll approve, then you write it."*
- **Interrupt &amp; redirect** — stop it the moment it drifts; don't wait for 300 lines.
- **Correct with specifics** — *"no — use the cleaned df from Step 3, and don't drop rows."*
- **Feed back errors** — paste the traceback; let it read and self-fix.
- **Manage context** — point to the right files; **clear/reset** a stale thread that's gone in circles.
- **Small steps** — one change → run → read → correct. Never accept a blind dump.

> A drifting agent rarely fixes itself. **Stop it, re-aim, continue** — steering beats restarting.

---

# Putting the three together

A worked rhythm for a real task:

1. **Plan mode + frontier model** → *"plan how you'd test this; don't write code yet."*
2. Approve the plan → **commit** the clean starting point (Module 5).
3. **Edit mode**, small steps → accept good diffs, **`git diff`** each one.
4. Stuck or slow? **Switch model** or **interrupt and re-aim.**
5. Mechanical follow-ups (tests, formatting) → **agent mode** on a branch.

> Right **mode**, right **model**, hand on the **wheel.** That's directing.

---

# End of Module 6 — recap, discussion &amp; support

**Module 06 recap — Edit modes, models &amp; the prompt**
- **Edit mode** = how much rope; **auto-accept** only safe because **git** makes it reversible.
- **Model** = capability vs. speed/cost — escalate for hard, cheap out for boilerplate.
- **Steer in flight** — plan first, interrupt, correct with specifics, small steps.

**Open question — let's discuss:** *On your last AI-assisted task, which dial was wrong — too much rope, the wrong model, or a prompt you should have interrupted sooner?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`
