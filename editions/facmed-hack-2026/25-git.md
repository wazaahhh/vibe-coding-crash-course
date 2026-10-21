<!-- ====== GIT 1 — Divider ======
Assume nobody knows git. Every word gets a plain meaning before it is used.
The promise to make early: you will rarely type a git command; you will say
what you want and the agent runs git for you.
-->
<!-- _class: ink divider -->

<span class="clock">11 min</span>

<span class="kicker">17:36 · Part 3 · Objective 2 · Understand</span>

# Git without the jargon

Why an agent needs a safety net, what git does in plain words, and how to hand 95% of it to the agent.

---

<!-- ====== GIT 2 — The problem ======
From module 05 ("The problem vibe coding creates").
-->

<span class="kicker">Module 05 · the problem vibe coding creates</span>

## An agent can edit ten files in thirty seconds, confidently, and sometimes wrong

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 6px;">
<div>

- Without a safety net, a bad edit **silently overwrites** what worked yesterday.
- "Undo" in your editor won't save you across many files, runs and days.
- You need a **known-good state** you can always return to, and a **record** of what changed, when and why.

</div>
<div>

<div class="card">
<h3>You already know the problem</h3>
<p><code>analysis_v2_final_FINAL_really.py</code> · <code>thesis_comments_JM_v3.docx</code></p>
<br>
<p>Git replaces that with one folder that remembers every saved version.</p>
</div>

</div>
</div>

> Cheap experiments (pillar 4) are only safe if failure is **reversible**. That's git.

---

<!-- ====== GIT 3 — Save points ======
The core picture. A commit is a save point, like a video game. A branch is a
parallel line of save points. Draw attention to "main" staying safe.
-->

<span class="kicker">The whole idea in one picture</span>

## Git is a time machine for a project folder

<svg viewBox="0 0 1100 250" width="100%" role="img" aria-label="A main line of five save points, with a branch of two save points that splits off after the second and merges back before the fifth">
  <line x1="80" y1="80" x2="1000" y2="80" stroke="#11233F" stroke-width="4"/>
  <path d="M 340 80 C 400 80, 400 180, 470 180 L 660 180 C 730 180, 730 80, 790 80" fill="none" stroke="#96004B" stroke-width="4"/>
  <g fill="#11233F">
    <circle cx="120" cy="80" r="16"/><circle cx="330" cy="80" r="16"/><circle cx="560" cy="80" r="16"/><circle cx="800" cy="80" r="16"/><circle cx="980" cy="80" r="16"/>
  </g>
  <g fill="#96004B"><circle cx="490" cy="180" r="16"/><circle cx="650" cy="180" r="16"/></g>
  <g font-family="Inter, sans-serif" font-size="19" fill="#11233F" text-anchor="middle">
    <text x="120" y="45">load data</text><text x="330" y="45">clean data</text><text x="560" y="45">first figure</text><text x="800" y="45">merge: new model</text><text x="980" y="45">final figures</text>
  </g>
  <g font-family="Inter, sans-serif" font-size="19" fill="#96004B" text-anchor="middle">
    <text x="490" y="222">try a mixed model</text><text x="650" y="222">it works: keep it</text>
  </g>
  <text x="1040" y="86" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#11233F">main</text>
  <text x="300" y="160" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#96004B">a branch</text>
</svg>

<div class="cols3" style="margin-top: 4px;">
<div class="card"><h3>● Commit = a save point</h3><p>A snapshot of the whole folder, with a one-line note: <i>"clean data: removed non-wear days"</i>.</p></div>
<div class="card"><h3>Branch = a parallel line</h3><p>Try something risky without touching the version that works.</p></div>
<div class="card"><h3>Merge = bring it back</h3><p>If the attempt works, fold it into <b>main</b>; if not, drop the branch.</p></div>
</div>

---

<!-- ====== GIT 4 — The dictionary ======
The jargon, once, in plain English. Leave it up while people read it.
-->
<!-- _class: dense -->

<span class="kicker">The dictionary · ten words you will hear</span>

## Git and GitHub words, in plain English

| Word | Plain meaning | Everyday analogy |
|---|---|---|
| **Repository** ("repo") | A project folder that remembers its whole history | A lab notebook that never loses a page |
| **Commit** | A save point, with a note saying what changed | A dated, signed notebook entry |
| **Diff** | What changed since the last save point (removed in red, added in green) | Track changes in Word |
| **Branch** · **main** | A parallel line of work · the line that works | A draft copy · the published version |
| **Merge** | Fold a branch's changes back into main | Accepting tracked changes |
| **GitHub** | A website that hosts a copy of your repo: backup, sharing, review | Google Drive, for projects with history |
| **Push** · **pull** · **clone** | Send your save points to GitHub · get others' · download a whole repo | Upload · sync · download |
| **Pull request** ("PR") | A page asking "please review these changes and merge them into main" | Sending a draft to your supervisor |
| **`.gitignore`** | A list of files git must never save or share (data, passwords) | A "do not photocopy" stamp |

---

<!-- ====== GIT 5 — Laptop, GitHub, team ======
From module 05 ("Local git vs. GitHub").
-->

<span class="kicker">Module 05 · two different jobs</span>

## Git lives on your laptop; GitHub is the shared copy

<div class="cols3" style="grid-template-columns: 1fr 0.35fr 1fr 0.35fr 1fr; align-items: center; gap: 10px; margin-top: 10px;">
<div class="card"><h3>Your laptop</h3><p>The project folder with its save points. Works offline, private, no account needed. <b>Protects you from yourself.</b></p></div>
<div style="text-align:center; font-weight:700; color:var(--accent); font-size:0.8em">push →<br>← pull</div>
<div class="card"><h3>GitHub</h3><p>The online copy: survives a dead laptop; one place for the team; pull requests for review. <b>Protects you from the world.</b></p></div>
<div style="text-align:center; font-weight:700; color:var(--accent); font-size:0.8em">← pull<br>push →</div>
<div class="card"><h3>Your teammates</h3><p>Each has their own copy and their own branches; GitHub keeps everyone in sync.</p></div>
</div>

<br>

| **Private** repository | **Public** repository |
|---|---|
| Only you and invited collaborators | Anyone can read and copy it |
| **Start here** while the work is live | At publication, for reproducibility, after checking the history |

<span class="small">⚠️ Public is permanent: a password or a dataset pushed in public may be copied before you delete it. Data stays out of git either way.</span>

---

<!-- ====== GIT 6 — The one loop ======
From module 05 ("The one loop that makes it safe"), with the plain-English
request beside each command. The commands are what the agent runs.
-->

<span class="kicker">Module 05 · the loop that makes it safe</span>

## The vibe-coding loop *is* the git loop

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px;">
<div>

1. **The agent changes something** (you asked it to).
2. **You ask: "what changed?"** It summarises in plain words; the detailed diff is there if the result matters. *This is your System 2 checkpoint.*
3. **Good? "Save it."** A save point with a clear note.
4. **Bad? "Undo that."** Back to the last save point, nothing lost but the bad change.

> **Save before every big request**: a guaranteed way back.

</div>
<div>

| You say | The agent runs |
|---|---|
| *"What did you change?"* | `git status` · `git diff` |
| *"Save it: cleaned the units"* | `git add` · `git commit -m "…"` |
| *"Undo that"* | `git restore .` |
| *"Show me the history"* | `git log --oneline` |

<span class="small">You don't need to remember the right-hand column. You do need to know it exists, and to read what the agent tells you it did.</span>

</div>
</div>

---

<!-- ====== GIT 7 — Branches ======
From module 05 ("Branches — try the risky thing safely").
-->

<span class="kicker">Module 05 · branches</span>

## Try the risky thing on a branch

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px;">
<div>

- Want the agent to attempt a big refactor, or a second way of analysing the data? Ask for it **on a branch**.
- **main** stays known-good while the agent experiments.
- Bad attempt? **Drop the branch**: zero trace, zero regret. Good? **Merge it.**
- At the hack, each person works on their own branch: `firstname/topic`.

> Branches turn *"I hope this doesn't break everything"* into *"let's just try it."*

</div>
<div>

| You say | The agent runs |
|---|---|
| *"Try a mixed model on a separate branch"* | `git switch -c thomas/mixed-model` |
| *"Go back to the main version"* | `git switch main` |
| *"It works, keep it"* | `git merge thomas/mixed-model` |
| *"Forget it"* | `git branch -D thomas/mixed-model` |

</div>
</div>

---

<!-- ====== GIT 8 — Hand off 95% ======
From module 05 ("Connect the AI agent to GitHub"): one-time `gh auth login`,
then the agent drives git and GitHub. This slide is the handoff contract.
-->
<!-- _class: dense -->

<span class="kicker">Module 05 · let the agent drive</span>

## Hand off 95% of git: say what you want, in plain words

| You say | What the agent does for you |
|---|---|
| *"Start a branch for this task."* | Creates `firstname/topic` and explains it in one sentence |
| *"Save my work with a clear message."* | Commits, with a note saying what changed and how it was checked |
| *"What changed since this morning?"* | Summarises the save points and changes in plain language |
| *"Undo what you just did."* | Goes back to the last save point, after telling you what will be lost |
| *"Get my teammates' latest work."* | Pulls from GitHub; if two people changed the same lines, explains the conflict and asks which version to keep |
| *"Send it to GitHub and open a pull request."* | Pushes the branch, opens the PR, writes what was verified and what was trusted |

<span class="small">One-time setup: a GitHub account with two-factor authentication, then <code>gh auth login</code> once on your machine. From then on the agent can run <code>git</code> and <code>gh</code> (GitHub's command-line tool) on your behalf.</span>

---

<!-- ====== GIT 9 — The 5% that stays yours ======
From module 05 (agent drafts, you merge) and module 09 (data confidentiality).
-->

<span class="kicker">The 5% that stays yours</span>

## The agent runs git. You keep five decisions.

<div class="cols" style="grid-template-columns: repeat(5, 1fr); gap: 14px; margin-top: 8px;">
<div class="card"><h3>When to save</h3><p>Ask for a save point at each step that works, and before every big request.</p></div>
<div class="card"><h3>Read the summary</h3><p>Every change gets a plain-language summary; read the detailed diff for anything that reaches a result.</p></div>
<div class="card"><h3>Approve the merge</h3><p>Nothing reaches <b>main</b> without your OK. Never let auto mode push to main unreviewed.</p></div>
<div class="card"><h3>Keep data out</h3><p>No data files, passwords or keys in git. The agent refuses; <code>.gitignore</code> backs it up.</p></div>
<div class="card"><h3>Own the history</h3><p>Commits carry <b>your</b> name. For credit at the hack, the history is the evidence.</p></div>
</div>

<br>

> The agent drafts; **you merge**.

---

<!-- ====== GIT 10 — The rule file that does the handoff ======
Excerpt of practical/AGENTS.md, the file participants get tonight. Their agent
reads it at the start of every session.
-->

<span class="kicker">One file makes it work · <code>AGENTS.md</code> in tonight's practical</span>

<div class="cols" style="grid-template-columns: 1fr 1.25fr; gap: 30px; align-items: start;">
<div>

## Write the rules once; the agent follows them every time

- The agent reads `AGENTS.md` at the start of every session (Claude Code via `CLAUDE.md`).
- It tells the agent to **run git for you, explain each step in plain words, and wait for your OK** before anything irreversible.
- Every team repository at the hack ships with one.

</div>
<div>

```markdown
# Rules for the AI agent working in this folder
You are helping researchers who may not know git.
You run git and GitHub for them; they decide.
Explain every git step in one plain-English sentence.

- Starting a task: create a branch <firstname>/<topic>.
- Saving work: after each step that works, commit with a
  plain-English message. Tell the human "Saved: …".
- "Undo that": go back to the last saved state, after saying
  what will be lost.
- "Send it to GitHub": push and open a pull request saying
  what was verified and what was trusted.
- Never force-push, rewrite history, or merge into main
  without the human's explicit OK.
- Never commit data files, passwords or keys.
```

</div>
</div>

---

<!-- ====== GIT 11 — POLL 3 · The literature ======
Opinion. Ties to git: once every analysis lives in a repository with its
history, anyone (or any agent) can re-run it. Show the result right away.
Push: A and C are the same technology with opposite incentives. Who would pay
for the checking? Dan Goodman (DePasquale responses): incentives already
reward producing models over understanding them.
-->

<span class="qnum">Poll 3 of 6 · The literature</span>

## Soon an agent can re-run any published analysis from its repository in minutes. What happens to your field's literature?

<div class="opts" style="width: 64%;">
<div class="opt"><b>A</b>Replication becomes routine and the literature gets cleaner</div>
<div class="opt"><b>B</b>A wave of corrections and retractions, then a cleaner literature</div>
<div class="opt"><b>C</b>Little changes: nobody is rewarded for checking</div>
<div class="opt"><b>D</b>AI-generated papers multiply faster than anyone can check them</div>
</div>

<div class="quizbox"><img src="assets/quiz_qr.svg" alt="QR code to the live quiz"><div><b>Vote live</b><span>{{QUIZ_URL}}</span></div></div>
