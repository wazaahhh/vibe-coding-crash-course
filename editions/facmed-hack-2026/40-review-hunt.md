<!-- ====== REVIEW HUNT 0 — Divider ====== -->
<!-- _class: ink divider -->

<span class="clock">8 min</span>

<span class="kicker">18:20 · Part 5 of 7 · Objective 2 · Understand</span>

# Review hunt

An agent wrote an analysis that runs cleanly. Would you sign it? Find what is wrong, together.

---

<!-- ====== REVIEW HUNT 1 — Task, with the output ======
Plenary: everyone has review-hunt/analysis.py and sleep-mood/data/README.md
from the course folder (link in the chat), or reads the output on the slide. 5 minutes to read and
post in the chat everything they would not sign; then reveal. Answer key:
facilitator/ANSWER_KEY.md (five problems). Don't hint.
Output is verbatim from `python analysis.py` (seed 2026).
-->

<span class="kicker">Review hunt · everyone together</span>

<div class="cols" style="grid-template-columns: 1fr 1.2fr; gap: 30px; align-items: start;">
<div>

## An agent wrote this. Would you sign it?

1. Open `review-hunt/analysis.py` and the codebook `sleep-mood/data/README.md`.
2. Read the output on the right (or run it).
3. Hunt: the code, the data, the method, the summary.
4. In the chat: every problem, and **what tipped you off**.

<span class="small">The prompt the agent got is at the top of the file. Allowed: plots, the codebook, a second AI, your judgment.</span>

</div>
<div>

```text
Analysed 743 participant-days from 40 participants.

1. Associations with next-day mood (Pearson r)
   sleep duration : r = +0.39
   daily steps    : r = +0.25

2. Low-mood day classifier (random forest,
   30% held-out test set)
   AUC = 0.77

Summary
   Physical activity is the stronger correlate
   of mood (r = +0.25 vs +0.39 for sleep).
   Wearable data flag low-mood days with high
   accuracy (AUC = 0.77), supporting passive
   sensing as an early-warning signal for
   depressive episodes.
```

</div>
</div>

---

<!-- ====== REVIEW HUNT 2 — Reveal ======
Show after reading 3–4 chat lists. Numbers from facilitator/check_answers.py.
Ask: which of these would a second AI have caught? (Usually 1 and 3 when given
the codebook; rarely 4 and 5.) Schuck (pre-read 2): "AI output sounds
confident even when wrong, so know how you can falsify what a model produces":
write scripts that check the output rather than asking the model to check
itself.
-->

<span class="kicker">The answer key</span>

## Five problems, and the headline flips

| # | Problem | Effect | What catches it |
|---|---|---|---|
| 1 | `mood_3` reverse-keyed, averaged as is | mood spread halves; r(sleep) +0.45 → +0.39 | the codebook |
| 2 | Non-wear days kept as 0 steps | fake steps–mood link: r +0.15 → +0.28 | a histogram: spike at 0 |
| 3 | Same participants in train and test | AUC 0.89 → **0.69** on new people | "would it work on a new patient?" |
| 4 | Summary contradicts its numbers | "activity is stronger": 0.25 < 0.39 | numbers before prose |
| 5 | Overclaim | a low-mood *day* is no depressive *episode* | what does the outcome measure? |

<span class="small">Fixed: sleep predicts next-day mood (r ≈ +0.45), steps add little (r ≈ +0.15), the classifier generalises modestly (AUC ≈ 0.69). Problem 3 is round 2's EEG trap, again.</span>

---

<!-- ====== REVIEW HUNT 3 — Peer review matters more ======
From module 08 ("How a lab works in the age of vibe coding" and "The shift, in
one line").
-->
<!-- _class: ink -->

<span class="kicker">Working together in a lab</span>

## When code is cheap, review is the work

<div class="cols3" style="margin-top: 10px;">
<div class="card"><h3>Peer review matters more</h3><p>No AI-generated analysis reaches a paper without a second human reading the reasoning and the checks.</p></div>
<div class="card"><h3>Show how you checked</h3><p>Short sprints, visible demos: what you built <i>and how you verified it</i>. Pair on the prompts.</p></div>
<div class="card"><h3>Share the rules, track provenance</h3><p>A lab <code>AGENTS.md</code>, shared environments; whose prompt, which model, which data version.</p></div>
</div>

<br>

> The failure mode is **unreviewed AI code flowing straight into results**.

---

<!-- ====== REVIEW HUNT 4 — POLL 5 · The scarce skill ======
Opinion. They have just practised D. Show the result right away.
Push: if C or D wins, ask the PIs how they hire for it today, and how a PhD
student practises it. Voices: Stachenfeld ("a flashlight as opposed to a laser
pointer") for C; Gjorgjieva (recognising invented concepts) for D.
-->

<span class="qnum">Poll 5 of 6 · The scarce skill</span>

## In 2031, the scarcest skill in a neuroscience lab will be…

<div class="opts" style="width: 58%;">
<div class="opt"><b>A</b>Programming</div>
<div class="opt"><b>B</b>Statistics and methods</div>
<div class="opt"><b>C</b>Choosing the question worth asking</div>
<div class="opt"><b>D</b>Judging whether a result is true</div>
</div>
<div class="opts" style="grid-template-columns: 1fr; margin-top: 14px; width: 58%;">
<div class="opt"><b>E</b>Collecting good data from real people</div>
</div>

<div class="quizbox"><img src="assets/quiz_qr.svg" alt="QR code to the live quiz"><div><b>Vote live · {{QUIZ_PIN_LABEL}}</b><span>{{QUIZ_URL}}</span></div></div>
