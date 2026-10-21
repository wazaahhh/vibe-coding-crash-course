<!-- ====== HOW 1 — Divider ====== -->
<!-- _class: ink divider -->

<span class="clock">6 min</span>

<span class="kicker">17:30 · Part 2 · Objective 2 · Understand</span>

# How vibe coding works

When you write code yourself, understanding comes for free. When you direct an agent, you have to *choose* to engage it. Four disciplines make the new loop safe.

---

<!-- ====== HOW 2 — Pillars 1 and 2 ======
From module 02 (pillars 1 and 2), as read in the pre-work.
-->

<span class="kicker">Module 02 · the four pillars · 1–2</span>

## Diverge first, then think critically

<div class="cols" style="margin-top: 6px;">
<div class="card">
<h3>1 · Divergence</h3>
<p>Science trains <b>convergence</b>: narrow to the one right method. Generation is now nearly free, so <b>diverge first</b>: <i>"Give me three approaches, with trade-offs."</i> Curate rather than produce; converge later, with more on the table.</p>
</div>
<div class="card">
<h3>2 · Critical thinking</h3>
<p>The model is confident, fluent and occasionally fabricating, in flawless prose. Treat every output as a pull request from a brilliant, overconfident intern. Ask <b>"How would I know if this is wrong?"</b> <i>before</i> trusting the pretty plot.</p>
</div>
</div>

<br>

> Trust the vibe to **write** it; never trust the vibe that it's **right**.

---

<!-- ====== HOW 3 — Pillars 3 and 4 ======
From module 02 (pillars 3 and 4). The METR poll just made pillar 3 concrete.
-->

<span class="kicker">Module 02 · the four pillars · 3–4</span>

## Think fast and slow; try and fail

<div class="cols" style="margin-top: 6px;">
<div class="card">
<h3>3 · Thinking fast / slow</h3>
<p>The AI is your <b>System 1</b>: fast, fluent, sometimes wrong. <b>You</b> supply System 2: slow, deliberate, checking. <i>"System 2 is in charge of doubting, but System 2 is often lazy"</i> (Kahneman).</p>
</div>
<div class="card">
<h3>4 · Try and fail</h3>
<p>Generation is cheap → more attempts, smaller stakes. Prototype to throw away. Failure costs <b>minutes, not a day</b>, so failure becomes the unit of search, as long as you can always go back (Part 3: git).</p>
</div>
</div>

<br>

> The more the result matters, the more slowly you must read it.

---

<!-- ====== HOW 4 — One project folder, one rule file ======
From module 03 ("Mode B, done right") and module 07 (CLAUDE.md conventions).
AGENTS.md is the cross-tool name (Codex, Copilot, Cline); Claude Code reads
CLAUDE.md, which can simply import AGENTS.md.
-->

<span class="kicker">Modules 03 &amp; 07 · set the agent up</span>

<div class="cols" style="grid-template-columns: 1.1fr 1fr; gap: 30px; align-items: start;">
<div>

## One project folder, one rule file

- Put **code · figures · notes · the paper** in one project folder: the agent sees the whole picture.
- Raw or private **data stays out of what gets shared** (Part 3).
- A rule file at the top, **`AGENTS.md`** (or `CLAUDE.md` for Claude Code), tells the agent your house rules, every time.

> Chat answers a question. A project folder lets the agent **work on your actual project**.

</div>
<div>

```text
my-project/
├── AGENTS.md    ← house rules for the agent
├── NOTES.md     ← what we verified / trusted
├── code/        ← analysis, notebooks
├── results/     ← figures, tables
└── data/        ← stays local, never shared
```

```markdown
# Rules
- Python, pandas. Figures go to results/.
- Never modify files in data/.
- Plan first and wait for my OK.
```

</div>
</div>

---

<!-- ====== HOW 5 — How to ask ======
From module 03 ("How to ask").
-->

<span class="kicker">Module 03 · the intent half of the job</span>

## How to ask: direct it like a capable new student

<div class="cols" style="grid-template-columns: 1.3fr 1fr; gap: 30px;">
<div>

- **Give context, not just the task**: the data, the goal, the constraints, what you've tried.
- **Ask for a plan before code**: *"outline your approach; I'll approve, then you write it."*
- **Constrain it**: language, libraries, *"match the style in this file"*, *"no new dependencies"*.
- **Make it show its work**: *"explain your reasoning; flag anything you assumed."*
- **Small steps**: one change, run, read, correct. Never accept a 300-line dump blind.

</div>
<div>

<div class="card">
<h3>Vague in → generic out</h3>
<p>❌ <i>"Analyse my sleep data."</i></p>
<br>
<p>✅ <i>"sleep.csv has bedtime and wake time in Geneva local time. Plan how you'd compute sleep duration per night and plot the nightly mean. Don't write code until I approve."</i></p>
</div>

</div>
</div>

---

<!-- ====== HOW 6 — Three dials ======
From module 06 (three dials + edit modes table). Tool-agnostic: Claude Code,
Codex, Copilot and Cline all have these, named differently.
-->

<span class="kicker">Module 06 · the controls</span>

## Three dials, whichever agent you use

| Dial | Settings | Use when |
|---|---|---|
| **1 · Edit mode**: how much rope | **Ask** (touches nothing) · **Plan first** (writes a plan, waits) · **Edit** (you accept each change) · **Auto** (edits and runs on its own) | Exploring → ask · anything big → plan · results that matter → edit · throwaway attempts → auto, **only because git makes it reversible** |
| **2 · Model**: the right brain | Frontier / "thinking" models · fast, small models | Statistics, study design, subtle bugs → frontier · boilerplate → fast · stuck → escalate |
| **3 · Steering**: hand on the wheel | Interrupt · correct with specifics · paste the error · clear a stale thread | The moment it drifts: a drifting agent rarely fixes itself. Stop it, re-aim, continue |

<br>

<span class="small">At the hack: your own agent (Claude Code, Codex, GitHub Copilot, Cline), or Cline on open models served on the HPE / NVIDIA environment.</span>

---

<!-- ====== HOW 7 — Putting it together ======
From module 06 ("Putting the three together"). This is the rhythm the
practical asks for.
-->

<span class="kicker">Module 06 · a worked rhythm</span>

## Right mode, right model, hand on the wheel

1. **Plan mode + a strong model** → *"plan how you'd test this; don't write code yet."*
2. Approve the plan → **save a starting point** (Part 3: the agent does it for you).
3. **Edit mode, small steps** → accept good changes, ask *"what changed?"* after each.
4. Stuck or slow? **Switch model** or **interrupt and re-aim**.
5. Mechanical follow-ups (tests, formatting, tidying) → **auto mode**, on a separate branch.

> That's directing.
