<!-- ====== SPOT 1 — Divider ======
Replaces the practical in pairs (Thomas, 22 Oct): small quizzes on the live
quiz app, each followed by a short discussion. Both traps come from the
phone study of the exercise in Part 1 (phone-study/; numbers from
facilitator/check_answers.py). The course folder stays available for anyone
who wants to redo them hands on.
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
[CONFIRM] In the live-quiz app, the "dst" question text should say "150
students" (it said "40 people" when the data was sleep-mood/).
-->

<span class="qnum">Spot the trap · 1 of 2 · sleep</span>

## An agent computes hours slept per night for 150 students from bedtime and wake-up times (Geneva clock). Everyone seems to sleep about **1 hour less** on the night of 24 → 25 October. Most likely?

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

- Mean sleep **6.9 h** that night with clock times, against **7.9 h** in UTC, in line with the other Saturday nights (**7.7 h**).
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

<!-- ====== SPOT 4 — QUIZ · The missing-answers trap ======
Live quiz question "missing" (single choice, correct = C). 45 seconds.
[CONFIRM] Replace the old "leakage" question in the live-quiz app (/admin)
with this one before 17:00. Data: phone-study/ (facilitator/check_answers.py).
D is the cautious answer: take it seriously, then show that the data are not
silent about who goes missing (next slide).
-->

<span class="qnum">Spot the trap · 2 of 2 · missing answers</span>

## An agent averages every evening mood answer in the phone study: **4.6 out of 7**, "students coped well with the term". But **37%** of the prompts went unanswered. The true average is most likely…

<div class="opts" style="width: 58%;">
<div class="opt"><b>A</b>About the same: missing answers are random</div>
<div class="opt"><b>B</b>Higher: happy, busy students skip the prompt</div>
<div class="opt"><b>C</b>Lower: students skip it on bad days, and go silent when struggling</div>
<div class="opt"><b>D</b>Impossible to say anything</div>
</div>

<div class="quizbox"><img src="assets/quiz_qr.svg" alt="QR code to the live quiz"><div><b>Vote live · {{QUIZ_PIN_LABEL}}</b><span>{{QUIZ_URL}}</span></div></div>

---

<!-- ====== SPOT 5 — Reveal and discuss: missing data ======
2–3 minutes of discussion. Typical answers: patients who miss visits when
sicker, trial dropouts, wearables taken off on bad days, scans excluded for
head movement, surveys answered by the motivated. Bridge to the hack: in
digital phenotyping, who stops sending data is itself a signal.
-->

<span class="kicker">Spot the trap · 2 of 2 · the answer</span>

## C: the missing answers are not missing at random

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 6px;">
<div>

- The evening before a skipped prompt, mood was **4.3**; before an answered one, **4.8**.
- The quarter who answer least start the term with PHQ-9 **10.7**, the others **6.9**.
- 32 students go silent before the last two weeks: early mood **4.2**, against **5.0**.
- Ask the agent: *"who is missing, and are they different? Compare what we know about them."*

</div>
<div>

<div class="card" style="border-left: 5px solid var(--accent);">
<h3>Discuss · 2 minutes</h3>
<p>Where does <b>missing data</b> hide in your field? Patients who miss visits when sicker, trial dropouts, wearables taken off on bad days, scans excluded for movement… Unmute, or write it in the chat.</p>
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
