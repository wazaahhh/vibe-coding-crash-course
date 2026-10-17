<!-- ====== LIVE BUILD 1 — Divider ====== -->
<!-- _class: ink divider -->

<span class="clock">25 min</span>

<span class="kicker">17:15 · Objective 2 · Understand</span>

# Live build: from a question to a pull request

A real analysis on digital-phenotyping data, directed live, with an agent in the editor.

**Your job while you watch:** type in the chat whenever you see a pillar being skipped.

---

<!-- ====== LIVE BUILD 2 — The pre-work in one slide ======
From module 02 (the mindset). 2 minutes, no more: they read it.
The thesis from module 01 sits on top: you move from author of code to director of code.
-->

<span class="kicker">The pre-work in one slide · module 02</span>

## You direct; the agent writes. Four disciplines keep it honest.

<div class="cols4" style="margin-top: 6px;">
<div class="card"><h3>Diverge</h3><p>Generation is nearly free: ask for three approaches with trade-offs, then choose.</p></div>
<div class="card"><h3>Think critically</h3><p>Every output is a pull request from a brilliant, overconfident intern. <i>How would I know if this is wrong?</i></p></div>
<div class="card"><h3>Fast and slow</h3><p>The agent is System 1: fast, fluent, sometimes wrong. You supply System 2. The more it matters, the slower you read.</p></div>
<div class="card"><h3>Try and fail</h3><p>Attempts cost minutes. Branch, try, throw away. Git makes failure reversible.</p></div>
</div>

<br>

> Trust the vibe to **write** it; never trust the vibe that it's **right**.

---

<!-- ====== LIVE BUILD 3 — Tonight's question ======
The dataset is synthetic but shaped like a challenge dataset: say so.
The move to name: this is what teams do on 6 November. Start from a need or a
breakthrough-app opportunity on the challenge page, turn it into one testable question.
-->

<span class="kicker">The demo</span>

<div class="cols" style="grid-template-columns: 1.15fr 1fr; align-items: start;">
<div>

## Does last night's sleep predict today's mood?

40 participants · 21 nights, 12 Oct → 1 Nov 2026 · phone sleep detection, wearable steps, a four-item mood questionnaire every evening.

Synthetic, and messy on purpose, like the plant dataset in the pre-work: the traps teach the mindset.

<span class="small">Repository: <code>editions/facmed-hack-2026/demo-phenotyping/</code> in the course repo. Fork it and follow along, or just watch.</span>

</div>
<div>

```text
data/
├── README.md          ← the codebook: read it
├── participants.csv   age, PHQ-9 at baseline
├── sleep.csv          bedtime, wake time
├── steps.csv          steps, minutes worn
└── ema.csv            mood_1 … mood_4 (1–7)
```

<span class="small">On 6 Nov the same move starts from your challenge page: a need, a breakthrough-app opportunity, one testable question.</span>

</div>
</div>

---

<!-- ====== LIVE BUILD 4 — The arc ======
From module 04's demo arc, re-cut for this dataset. Facilitator script in
demo-phenotyping/README.md. Name the pillar out loud at each move.
-->

<span class="kicker">The arc · six moves</span>

## Watch for where it goes fast, and where we slow down

| # | Move | What we type | Pillar |
|---|---|---|---|
| 1 | Orient by asking | *"Brief me on `data/` and the codebook. What problems do you see?"* | Fast |
| 2 | Plan before code | *"Plan how you'd relate sleep to next-day mood. Don't write code yet."* | Diverge |
| 3 | Let it run | sleep per night → mean per night → a plot | Fast |
| 4 | Slow down at the picture | *one night looks strange: why?* | **Slow** |
| 5 | Fix with intent | *"Localise to Europe/Zurich, convert to UTC, then subtract. Show me before and after."* | Critical |
| 6 | Review and commit | `git diff` → commit → a line in `NOTES.md` → pull request | Try and fail |

---

<!-- ====== LIVE BUILD 5 — Three dials ======
From module 06 (edit modes, models and steering). One slide; point at the
editor while saying it.
Tools named for the hack: Claude Code or Codex with your own subscription;
GitHub Copilot (free for students through GitHub Education); Cline with the open
models served on the HPE / NVIDIA environment at the hack.
-->

<span class="kicker">Module 06 · the controls</span>

## Three dials, whichever agent you use

<div class="cols3" style="margin-top: 6px;">
<div class="card">
<h3>1 · Edit mode: how much rope</h3>
<p><b>Plan first</b> for anything big · <b>edit</b> with every diff approved for results that matter · <b>agent / auto</b> only on a throwaway branch, because git makes it reversible.</p>
</div>
<div class="card">
<h3>2 · Model: the right brain</h3>
<p>A frontier or "thinking" model for statistics, study design and subtle bugs; a fast one for boilerplate. Escalate when it is stuck.</p>
</div>
<div class="card">
<h3>3 · Steering: hand on the wheel</h3>
<p>Interrupt the moment it drifts · correct with specifics · paste the traceback · small steps · clear a thread that goes in circles.</p>
</div>
</div>

<br>

<span class="small">Same dials in Claude Code, Codex, GitHub Copilot and Cline. At the hack: your own agent, or Cline on the open models served on the HPE / NVIDIA environment.</span>

---

<!-- ====== LIVE BUILD 6 — The git loop ======
From module 05. The vibe loop is the git loop. The agent can run all of this
through `gh`; the human reads the diff and merges.
-->

<span class="kicker">Module 05 · the safety net</span>

<div class="cols" style="grid-template-columns: 1fr 1fr; align-items: start;">
<div>

## The vibe loop is the git loop

- `git diff` is how you review the agent's work: the diff is the intern's pull request.
- **Commit before a big prompt**: a guaranteed way back.
- **Branches** make the risky attempt cheap. `main` stays known-good.
- The agent can run git and `gh` for you. **You read the diff; you merge.**

</div>
<div>

```bash
# the agent changed something
git status        # what did it touch?
git diff          # read exactly what changed
# good: snapshot it
git commit -am "sleep in UTC: DST night fixed, checked by plot"
# bad: back to the last commit
git restore .

# try the risky thing on a branch
git switch -c thomas/mixed-model
```

</div>
</div>

---

<!-- ====== LIVE BUILD 7 — What just happened ======
Show after the demo. Numbers from demo-phenotyping/check_answers.py.
Callback to quiz Q6: the run felt fast and finished cleanly; the number was
wrong for one night and nothing complained.
-->

<span class="kicker">What just happened</span>

## A clean run with a wrong number

<div class="cols" style="grid-template-columns: 1fr 1.2fr; gap: 30px; align-items: center;">
<div>

<div class="card"><div style="font-size:2.6em; font-weight:800; color:var(--accent); line-height:1">5.9 h</div><p>mean sleep on the night of 24 → 25 October, subtracting clock times</p></div>
<br>
<div class="card"><div style="font-size:2.6em; font-weight:800; color:var(--science); line-height:1">6.9 h</div><p>the same night in UTC, and every other night</p></div>

</div>
<div>

- No error, no warning: the clocks went back an hour at 03:00 on Sunday.
- The agent was **mostly right**, the dangerous kind of wrong.
- Found by a **plot** and the **calendar**: domain knowledge.
- Recorded in `NOTES.md`: *verified: DST night, by plot · trusted: pandas time-zone handling*.

> Quiz Q6: it felt fast. The question is whether it was right.

</div>
</div>
