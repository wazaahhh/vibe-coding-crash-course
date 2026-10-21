# Answer key — facilitators only

Keep this folder (`facilitator/`) out of anything participants receive. Numbers from
`python check_answers.py` and `python check_eeg.py` (synthetic data seed 2026).

## Practical, round 1 · `sleep-mood/` · daylight saving (25 October 2026)

Times in `sleep.csv` are Geneva wall-clock times with no offset. Clocks went back at 03:00 on
Sun 25 Oct, so subtracting wall-clock times gives one hour too little for everyone asleep across
the change. No error is raised.

- Naive mean sleep, night 24→25 Oct: **5.9 h**, against **6.9 h** on other nights.
- Time-zone-aware (localise to `Europe/Zurich`, convert to UTC, then subtract): **6.9 h**.
- How it gets caught: plot mean sleep per night. One night drops by an hour for every participant
  at once; only the calendar explains that.
- If the agent gets it right first time, say so in the debrief, and show the naive number.

## Practical, round 2 · `eeg-eye-state/` · two real traps

Roesler (2013), UCI Machine Learning Repository, CC BY 4.0: one continuous 117 s recording,
14 channels, 14,980 samples, eyes closed in 45 % of samples, 24 open/closed periods.

1. **Artifacts.** 4 samples have values more than 20 median absolute deviations from the median,
   up to **715,897** where the median is about **4,268**. Raw plots look flat; standard deviations
   of AF3, FC5, P7, O1, P8, F8 and AF4 are inflated by orders of magnitude.
2. **Random split on one continuous recording.** Neighbouring samples (about 128 per second) are
   near-copies, so a random split puts each test sample's twin in the training set.
   - kNN (k = 5, standardised), artifacts removed: **0.96** with a random 5-fold split,
     **0.46** with 5 consecutive time blocks.
   - Always guessing "open": **0.55**.
   - The honest answer: from this one recording, a simple classifier does not generalise to a
     later part of the same session.

## Review hunt · `review-hunt/analysis.py` · five problems

It runs cleanly, is well commented, and handles daylight saving correctly, which is what makes
the rest believable.

| # | Problem | Where | What it does | How to catch it |
|---|---|---|---|---|
| 1 | `mood_3` is reverse-keyed and is averaged as is | `load_mood()` | Mood SD 1.00 → 0.56; r(sleep, mood) +0.45 → +0.39 | Read the codebook; correlate the four items: `mood_3` runs negative against the others |
| 2 | Non-wear days (`wear_minutes = 0`) are kept as `steps = 0` | `load_steps()` | Non-wear happens on low-mood days, so the zeros manufacture a steps–mood link: r +0.15 (worn days) → +0.28 | Histogram of steps: a spike at exactly 0; the codebook says what it means |
| 3 | Random row split: the same participants sit in train and test, and the person-level features identify them | `train_test_split` | AUC 0.89 (row split) → 0.69 on held-out participants (range 0.55–0.86 over 20 splits) | Ask "would this work on a new patient?"; split by participant (`GroupShuffleSplit` / `GroupKFold`) |
| 4 | The summary contradicts its own numbers: "activity is the stronger correlate" while r(steps) = +0.25 < r(sleep) = +0.39 | `main()` summary | The headline comes from the prompt's framing and the agent's priors, not from the output | Read the numbers before the prose |
| 5 | Overclaim: "high accuracy", "early-warning signal for depressive episodes" | `main()` summary | A low-mood *day* on a 4-item EMA is not a depressive *episode*; AUC 0.77 (and 0.69 honestly) is not high accuracy | Ask what the outcome actually measures |

After fixing 1–3, the honest result is: sleep predicts next-day mood (r ≈ +0.45); steps add little
(r ≈ +0.15); a low-mood-day classifier generalises to new people only modestly (AUC ≈ 0.69).
The shipped headline is reversed on every point. Problem 3 is the EEG trap of round 2, again.
