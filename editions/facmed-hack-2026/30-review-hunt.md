<!-- ====== REVIEW HUNT 1 — Divider ======
Facilitator: reopen the same breakout rooms for 15 minutes. Paste in the chat
the link to demo-phenotyping/analysis.py and data/README.md first.
Answer key: demo-phenotyping/ANSWER_KEY.md (five problems). Don't hint.
-->
<!-- _class: ink divider -->

<span class="clock">20 min</span>

<span class="kicker">18:15 · Objective 2 · The slow part</span>

# Review hunt

An agent wrote this analysis. It runs, it reads well, and it reaches a confident conclusion.

**Would you put your name on it?**

---

<!-- ====== REVIEW HUNT 2 — The task, with the output ======
Output is verbatim from `python analysis.py` (seed 2026).
-->

<span class="kicker">15 min in your pairs · then post your list in the chat</span>

<div class="cols" style="grid-template-columns: 1fr 1.2fr; gap: 30px; align-items: start;">
<div>

## List everything you would not sign

1. Open `demo-phenotyping/analysis.py` and the codebook `data/README.md`.
2. Run it (or read the output on the right).
3. Hunt: the code, the data, the method, the summary.
4. For each problem: **what tipped you off?**

<span class="small">Allowed: plots, the codebook, a second AI, your own judgment. The prompt the agent got is at the top of the file.</span>

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

<!-- ====== REVIEW HUNT 3 — Where it bites ======
From module 02. Optional while rooms are open; useful to leave shared for
people who return early.
-->

<span class="kicker">Module 02 · aim your checking</span>

## Strongest on syntax, weakest on truth

| Trust, but skim | Slow down: it fails quietly here |
|---|---|
| Plotting, formatting, refactoring | **Domain correctness**: units, time zones, reverse-keyed items |
| Boilerplate, glue, file reading | **Statistics**: the wrong-but-plausible test, leakage |
| Explaining unfamiliar code | **What the outcome really measures** |
| Translating between languages | **Anything needing ground truth**: codebooks, citations |

> The bug that ends a paper compiles, runs, and looks beautiful.

---

<!-- ====== REVIEW HUNT 4 — Reveal ======
Show only after reading 3–4 lists from the chat. Numbers from check_answers.py.
Ask: which of these would a second AI have caught? (Usually 1 and 3 when given
the codebook; rarely 4 and 5.)
Callback to quiz Q2: judging whether a result is true is the skill this block
practises.
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

<span class="small">Fixed: sleep predicts next-day mood (r ≈ +0.45), steps add little (r ≈ +0.15), the classifier generalises modestly (AUC ≈ 0.69).</span>

---

<!-- ====== REVIEW HUNT 5 — Peer review matters more ======
From module 08. Bridge to objective 3: at the hack, every pull request gets a
second pair of eyes, and NOTES.md records what was verified.
-->
<!-- _class: ink -->

<span class="kicker">Module 08 · working together</span>

## When code is cheap, review is the work

Peer review matters **more** when generation is cheap: the failure mode is unreviewed AI code flowing straight into results.

<div class="cols3" style="margin-top: 14px;">
<div class="card"><h3>Show how you checked</h3><p>Demo what you built and how you verified it.</p></div>
<div class="card"><h3>A second pair of eyes</h3><p>No AI-written analysis reaches a claim without a human reading the reasoning.</p></div>
<div class="card"><h3>Keep the record</h3><p>Whose prompt, which model, what was verified and what was trusted.</p></div>
</div>
