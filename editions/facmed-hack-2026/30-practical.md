<!-- ====== SPOT 1 — Divider ======
Replaces the practical in pairs (Thomas, 22 Oct): small quizzes on the live
quiz app, each followed by a short discussion. Both traps come from the
practical's data (sleep-mood/, eeg-eye-state/; numbers from
facilitator/check_answers.py and check_eeg.py). The course folder stays
available for anyone who wants to redo them hands on.
-->
<!-- _class: ink divider -->

<span class="clock">20 min</span>

<span class="kicker">18:00 · Part 4 of 7 · Objective 2 · Understand</span>

# Spot the trap

Two analyses an agent ran cleanly: no error, a plausible number. Vote on what went wrong, then talk: where would the same trap hide in your data?

---

<!-- ====== SPOT 2 — QUIZ · The sleep trap ======
Live quiz question "dst" (single choice, correct = C). 45 seconds, then show
the result. Don't comment before the reveal.
-->

<span class="qnum">Spot the trap · 1 of 2 · sleep</span>

## An agent computes hours slept per night for 40 people from bedtime and wake-up times (Geneva clock). Everyone seems to sleep about **1 hour less** on the night of 24 → 25 October. Most likely?

<div class="opts" style="width: 58%;">
<div class="opt"><b>A</b>Exam stress that week</div>
<div class="opt"><b>B</b>The sleep app crashed that night</div>
<div class="opt"><b>C</b>The clocks went back at 03:00: subtracting clock times loses an hour</div>
<div class="opt"><b>D</b>Random noise</div>
</div>

<div class="quizbox"><img src="assets/quiz_qr.svg" alt="QR code to the live quiz"><div><b>Vote live · {{QUIZ_PIN_LABEL}}</b><span>{{QUIZ_URL}}</span></div></div>

---

<!-- ====== SPOT 3 — Reveal and discuss: time ======
2–3 minutes of discussion: ask two or three people to unmute. Typical answers:
device clocks drifting, sampling rates, recordings that cross midnight,
participants travelling, time zones in multi-site data.
-->

<span class="kicker">Spot the trap · 1 of 2 · the answer</span>

## C: no error, no warning, one hour lost

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 6px;">
<div>

- Mean sleep **5.9 h** that night with clock times, against **6.9 h** in UTC, as on every other night.
- Caught by **a plot per night** and **the calendar**: domain knowledge, not code.
- Ask the agent: *"convert to UTC before subtracting, then plot one value per night."*

</div>
<div>

<div class="card" style="border-left: 5px solid var(--accent);">
<h3>Discuss · 2 minutes</h3>
<p>Where does <b>time</b> hide in your data? Device clocks, sampling rates, recordings across midnight, time zones in multi-site studies… Unmute, or write it in the chat.</p>
</div>

</div>
</div>

---

<!-- ====== SPOT 4 — QUIZ · The EEG trap ======
Live quiz question "leakage" (single choice, correct = C). 45 seconds.
Data: Roesler (2013), EEG Eye State, UCI, CC BY 4.0: one continuous
117-second recording, 14 channels.
-->

<span class="qnum">Spot the trap · 2 of 2 · EEG</span>

## An agent trains a classifier on one continuous 2-minute EEG recording to tell eyes open from closed. Random train/test split: **96% accuracy**. Tested on the **last part** of the recording instead, accuracy is about…

<div class="opts" style="width: 58%;">
<div class="opt"><b>A</b>95%: the model is solid</div>
<div class="opt"><b>B</b>80%: a bit worse, as expected</div>
<div class="opt"><b>C</b>46%: below the 55% of always guessing "open"</div>
<div class="opt"><b>D</b>100%: more data, better model</div>
</div>

<div class="quizbox"><img src="assets/quiz_qr.svg" alt="QR code to the live quiz"><div><b>Vote live · {{QUIZ_PIN_LABEL}}</b><span>{{QUIZ_URL}}</span></div></div>

---

<!-- ====== SPOT 5 — Reveal and discuss: leakage ======
2–3 minutes of discussion. Typical answers: the same patient in train and
test, the same session or day, repeated measures, augmented copies, features
computed on the whole dataset before the split. Bridge to the hack: several
challenges use continuous signals (wearables, EEG, video).
-->

<span class="kicker">Spot the trap · 2 of 2 · the answer</span>

## C: neighbouring samples are near-copies

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 6px;">
<div>

- A random split puts each test sample next to its **twin in training**: the model recognises, it does not predict.
- On a later part of the recording: **46%**, worse than always guessing "open" (**55%**).
- Ask the agent: *"would it still work on data recorded later, or on another person? Test exactly that."*

</div>
<div>

<div class="card" style="border-left: 5px solid var(--accent);">
<h3>Discuss · 2 minutes</h3>
<p>Where could <b>leakage</b> hide in your field? The same patient in train and test, the same session, repeated measures, features computed before the split… Unmute, or write it in the chat.</p>
</div>

</div>
</div>

> Both agents were **mostly right**: the dangerous kind of wrong. What catches them is a skeptic asking one more question.

---

<!-- ====== SPOT 6 — Prompts worth stealing ======
From module 03 and the course handout. Keep this slide shared in the main room
while the breakouts run, and paste the five prompts in the chat.
-->

<span class="kicker">From the course handout · keep these open</span>

## Five prompts worth stealing

1. *"Explain what this code does before you change anything."*
2. *"Outline your plan, then wait for my OK."*
3. *"Write a test that would fail if this result were wrong."*
4. *"What could make this conclusion wrong? Argue against yourself."*
5. *"Summarise in plain language what you changed and what you assumed."*

<br>

> And for git, just say it: *"start a branch"* · *"save my work"* · *"what changed?"* · *"undo that"* · *"send it to GitHub"*.

---

<!-- ====== SPOT 7 — POLL 4 · Training ======
Opinion, and the one where PhD students and PIs tend to split. They have just
seen two agents go quietly wrong: ask it now. Show the result, then ask in the chat: "PhD
students: does this match what you'd want? PIs: is this what you do?"
DePasquale: the struggle of turning an idea into code is "a form of
disciplined thinking". Schuck's lab policy: trainees do by hand the work that
builds core skills, hand off what they don't need to learn, and draft text
themselves before any AI editing.
-->

<span class="qnum">Poll 4 of 6 · Training</span>

## A first-year PhD student can now get working analysis code from an agent in minutes. In their first year, they should…

<div class="opts" style="width: 58%;">
<div class="opt"><b>A</b>Use agents freely: directing them is the skill that matters now</div>
<div class="opt"><b>B</b>Write their core analyses by hand first, agents later</div>
<div class="opt"><b>C</b>Use agents, but explain every line at lab meeting</div>
<div class="opt"><b>D</b>Keep agents away from thesis-critical analyses</div>
</div>

<div class="quizbox"><img src="assets/quiz_qr.svg" alt="QR code to the live quiz"><div><b>Vote live · {{QUIZ_PIN_LABEL}}</b><span>{{QUIZ_URL}}</span></div></div>
