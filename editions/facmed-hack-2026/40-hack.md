<!-- ====== HACK 1 — Divider ====== -->
<!-- _class: ink divider -->

<span class="clock">15 min</span>

<span class="kicker">18:35 · Objective 3 · Prepare</span>

# How it runs at the hack

Friday 6 – Saturday 7 November · Campus Biotech · 32 hours.

---

<!-- ====== HACK 2 — Two paths ======
The message to land: arriving without tools is fine. Both paths reach the same
team repository, and both can run work on the HPE / NVIDIA environment.
Source: vibe_coding_environment/implementation_plan.md (corp repo).
-->

<span class="kicker">With or without your own tools</span>

## Two ways in, one team repository

<div class="cols" style="margin-top: 6px;">
<div class="card">
<h3>You already have the tools</h3>
<p>VS Code on your laptop with your own agent: Claude Code or Codex on your own plan, GitHub Copilot, or Cline. Clone your team's repository and work as tonight.</p>
</div>
<div class="card">
<h3>You don't, or you'd rather not install</h3>
<p>A ready-made VS Code in the browser on the HPE / NVIDIA environment: nothing to install, an agent already set up on open models served there, your team's repository already cloned.</p>
</div>
</div>

<br>

> **Either way, every team can build and test on the HPE / NVIDIA environment**: GPUs for heavy jobs, and the challenge datasets, which stay there.

---

<!-- ====== HACK 3 — Your team's repository ======
From the agents' rules (AGENTS.md, implementation plan §3.5). For credit
candidates, the contribution history is the assessment (LNDS syllabus,
Module C, A2).
-->

<span class="kicker">The workflow you rehearsed tonight</span>

## Your team's repository

| Rule | Why |
|---|---|
| One repository per team, in the hack's GitHub organisation | One place for code, notes and the demo |
| A branch per person and task: `firstname/topic` | `main` stays working while you try things |
| **Commit small and often**, under your own name | For credit candidates, the contribution history is the assessment |
| Merge through a pull request, with `NOTES.md` updated: *verified* and *trusted* | The record of what was checked, by whom |
| Tag `demo` on `main` before the final presentations | The jury looks at exactly what you showed |

<br>

<span class="small">Each repository comes with an <code>AGENTS.md</code>: the same rules, written for your agent, so it branches, commits and opens pull requests the way the team does.</span>

---

<!-- ====== HACK 4 — Data rules ======
Recap of B1 (Swiss data rules) in agent terms. Source: implementation plan §5.
-->

<span class="kicker">Data rules · the short version of Crash Course #1</span>

## The agent sees the structure of the data, never the records

<div class="cols3" style="margin-top: 6px;">
<div class="card"><h3>Real data stays put</h3><p>Challenge datasets live on the HPE / NVIDIA environment, read-only. Analyses run there.</p></div>
<div class="card"><h3>Laptops get samples</h3><p>Each repository has a small synthetic sample in <code>examples/</code>, so code runs anywhere.</p></div>
<div class="card"><h3>Nothing sensitive in git</h3><p>A pre-commit check blocks data files and secrets. Never paste records into a chat tool.</p></div>
</div>

---

<!-- ====== HACK 5 — Before 6 November ======
[CONFIRM before the session] where participants register their GitHub username,
and the challenge-voting link.
-->

<span class="kicker">Before 6 November</span>

## Five things to do

| | What | When |
|---|---|---|
| 1 | **Vote** on the challenges you want to work on | Now: voting is open |
| 2 | A **GitHub account** with two-factor authentication, and your username sent to us | This week |
| 3 | *Optional:* VS Code + one agent on your laptop; try the demo repository | Before 6 Nov |
| 4 | **Crash Course #3**: grant writing for pop-up projects, with the RGO | Thu 29 Oct, 17:00 |
| 5 | Come with one idea for **your** challenge: a need, an opportunity, a question | 6 Nov, 11:00 |
