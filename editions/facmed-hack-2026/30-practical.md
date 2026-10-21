<!-- ====== PRACTICAL 1 — Divider ======
Facilitator: before opening the rooms, paste in the chat the link to the
practical repository (the edition's practical/ folder, published without the
facilitator/ folder) and the two-line setup. Breakout rooms of two (Zoom:
assign automatically, 30 min, let participants return early off). Mix
seniorities where you can. Broadcast at 18:05 "Switch roles: round 2", and at
18:17 "Save your work and post your numbers in the main chat".
-->
<!-- _class: ink divider -->

<span class="clock">37 min</span>

<span class="kicker">17:47 · Part 4 · Objective 2 · Understand, by doing it</span>

# Practical in pairs

Zoom breakout rooms of two. Round 1 on synthetic sleep data, round 2 on a real, open EEG recording. One driver, one skeptic, and the agent runs git for you.

---

<!-- ====== PRACTICAL 2 — Roles and setup ======
From module 08 (working in a lab): pair on the prompts, one drives, one plays
skeptic. Insist on the skeptic role; it is the one people skip.
Nobody without tools is left out: all data here is synthetic or open, so
chat mode with file upload is allowed tonight (and only tonight).
-->

<span class="kicker">Module 08 · pair on the prompts</span>

## Two roles, switch at 18:05

<div class="cols" style="margin-top: 4px;">
<div class="card">
<h3>Driver</h3>
<p>Shares their screen and talks to the agent. Says out loud what they are about to ask, and why.</p>
</div>
<div class="card">
<h3>Skeptic</h3>
<p>Never touches the keyboard. After every answer: <i>how would we know if this is wrong?</i> Decides when to slow down.</p>
</div>
</div>

<br>

| You have… | Setup (2 min) |
|---|---|
| VS Code with an agent (Claude Code, Codex, GitHub Copilot, Cline) | Download the practical folder from the link in the chat (or ask your agent to clone it), open it in VS Code, open the agent. It reads `AGENTS.md` and runs git for you |
| Only a chat AI (ChatGPT, Claude, Gemini…) | Upload the CSV files and READMEs to the chat: tonight's data is synthetic or open, so this is allowed. Skip the git steps |
| Nothing working yet | Be the skeptic first; in round 2, drive from your partner's machine (Zoom remote control) or in chat mode |

---

<!-- ====== PRACTICAL 3 — Round 1 ======
The former live demo, now done by the pairs. The trap: sleep times are Geneva
wall-clock times; clocks went back at 03:00 on Sun 25 Oct, so subtracting
them gives one hour too little that night (5.9 h vs 6.9 h). Answer key:
facilitator/ANSWER_KEY.md.
-->

<span class="kicker">Round 1 · Driver A · 17:50 → 18:05 · <code>sleep-mood/</code></span>

## How long do people sleep each night?

<div class="cols" style="grid-template-columns: 1.35fr 1fr; gap: 30px;">
<div>

1. *"Brief me on `sleep-mood/` and its codebook. Don't change anything."*
2. *"Start a new branch for this task."* (It explains what a branch is in one sentence.)
3. *"Plan how you'd compute sleep duration per night and plot the average per night. Wait for my OK."*
4. Approve, let it run, **look at the plot together**. Skeptic: is anything strange?
5. If something is: find out **why**, and fix it with a precise instruction.
6. *"Save my work with a clear message, and add a line to NOTES.md."*

</div>
<div>

<div class="card">
<h3>The data</h3>
<p>Synthetic smartphone and wearable data: 40 participants, 21 nights from 12 October, a four-item mood questionnaire each evening. Codebook: <code>sleep-mood/data/README.md</code>.</p>
</div>
<br>
<div class="card">
<h3>Pillars to watch</h3>
<p>Fast (orient, run) · Diverge (plan) · <b>Slow</b> (the plot) · Critical (the fix) · Try and fail (save, or undo)</p>
</div>

</div>
</div>

---

<!-- ====== PRACTICAL 4 — Round 2 ======
Real data, real traps (facilitator/check_eeg.py):
1. Four samples with values up to 715,897 (median ~4,300): the raw plot looks
   flat until they are removed.
2. One continuous recording, 24 open/closed periods: a random train/test split
   puts near-identical neighbouring samples on both sides. kNN accuracy 0.96
   with a random split vs 0.46 with time blocks; always guessing "open" = 0.55.
-->

<span class="kicker">Switch! · Round 2 · Driver B · 18:05 → 18:19 · <code>eeg-eye-state/</code></span>

## Can EEG tell whether the eyes are closed, and how well, honestly?

<div class="cols" style="grid-template-columns: 1.35fr 1fr; gap: 30px;">
<div>

1. *"Load `eeg-eye-state/data/eeg_eye_state.csv`, describe it, and plot the 14 channels over time."* Skeptic: does that look like EEG?
2. *"Train a simple classifier to predict `eye_closed` and report its accuracy."*
3. Skeptic: *"Would it still work on the last part of the recording if we trained on the first part?"* Ask the agent to test exactly that, and compare.
4. *"Save my work, send it to GitHub and open a pull request saying what we verified and what we trusted."* (No GitHub account yet? Just save.)

</div>
<div>

<div class="card">
<h3>The data · real and open</h3>
<p>One continuous 117-second recording, Emotiv headset, 14 channels, eyes open or closed from video. Roesler (2013), UCI Machine Learning Repository, CC BY 4.0.</p>
</div>
<br>
<div class="card">
<h3>Bring back to the main room</h3>
<p>In the chat: (1) the strange thing from round 1 · (2) your two accuracy numbers from round 2.</p>
</div>

</div>
</div>

---

<!-- ====== PRACTICAL 5 — Prompts worth stealing ======
From module 03 and the course handout. Keep this slide shared in the main room
while the breakouts run, and paste the five prompts in the chat.
-->

<span class="kicker">Module 03 &amp; the course handout · keep these open</span>

## Five prompts worth stealing

1. *"Explain what this code does before you change anything."*
2. *"Outline your plan, then wait for my OK."*
3. *"Write a test that would fail if this result were wrong."*
4. *"What could make this conclusion wrong? Argue against yourself."*
5. *"Summarise in plain language what you changed and what you assumed."*

<br>

> And for git, just say it: *"start a branch"* · *"save my work"* · *"what changed?"* · *"undo that"* · *"send it to GitHub"*.

---

<!-- ====== PRACTICAL 6 — Debrief ======
Back at ~18:20. Read 3–4 chat posts first, then reveal. Numbers from
facilitator/check_answers.py and facilitator/check_eeg.py.
-->

<span class="kicker">Debrief · what the pairs found</span>

## Two clean runs, two wrong numbers

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px;">
<div class="card">
<h3>Round 1 · the night of 24 → 25 October</h3>
<p>Mean sleep <b>5.9 h</b> subtracting clock times, against <b>6.9 h</b> in UTC and on every other night. Clocks went back at 03:00 on Sunday: no error, no warning. Caught by a <b>plot</b> and the <b>calendar</b>: domain knowledge.</p>
</div>
<div class="card">
<h3>Round 2 · eyes closed from EEG</h3>
<p>Four artifact samples (up to 715,897 against ~4,300) flatten every plot. Then: <b>96%</b> accuracy with a random split, <b>46%</b> when tested on a later part of the recording, below the <b>55%</b> of always guessing "open". Neighbouring samples are near-copies.</p>
</div>
</div>

<br>

> Both agents were **mostly right**: the dangerous kind of wrong. What caught them was a skeptic asking one more question.

---

<!-- ====== PRACTICAL 7 — POLL 4 · Training ======
Opinion, and the one where PhD students and PIs tend to split. They have just
directed an agent: ask it now. Show the result, then ask in the chat: "PhD
students: does this match what you'd want? PIs: is this what you do?"
DePasquale: the struggle of turning an idea into code is "a form of
disciplined thinking". Schuck's lab policy: trainees do by hand the work that
builds core skills, hand off what they don't need to learn, and draft text
themselves before any AI editing.
-->

<span class="qnum">Poll 4 of 6 · Training</span>

## A first-year PhD student can now get working analysis code from an agent in minutes. In their first year, they should…

<div class="opts" style="width: 64%;">
<div class="opt"><b>A</b>Use agents freely: directing them is the skill that matters now</div>
<div class="opt"><b>B</b>Write their core analyses by hand first, agents later</div>
<div class="opt"><b>C</b>Use agents, but explain every line at lab meeting</div>
<div class="opt"><b>D</b>Keep agents away from thesis-critical analyses</div>
</div>

<div class="quizbox"><img src="assets/quiz_qr.svg" alt="QR code to the live quiz"><div><b>Vote live</b><span>{{QUIZ_URL}}</span></div></div>
