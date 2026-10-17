# Answer key — facilitators only

Numbers from `python check_answers.py` (seed 2026). Do not share before the debrief.

## Live build trap: daylight saving (25 October 2026)

Times in `sleep.csv` are Geneva wall-clock times with no offset. Clocks went back at 03:00 on
Sun 25 Oct, so subtracting wall-clock times gives one hour too little for everyone asleep across
the change. No error is raised.

- Naive mean sleep, night 24→25 Oct: **5.9 h**, against **6.9 h** on other nights.
- Time-zone-aware (localise to `Europe/Zurich`, convert to UTC, then subtract): **6.9 h**.
- How it gets caught: plot mean sleep per night. One night drops by an hour for every participant
  at once; only the calendar explains that.

## Review hunt: `analysis.py` has five problems

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
The shipped headline is reversed on every point.

## Debrief questions

- Which problem did your pair find first, and what found it: reading the code, a plot, the
  codebook, or a second method?
- Which ones would a second AI reviewer have caught? (Try it: paste `analysis.py` and the
  codebook and ask "what's wrong?")
- Problem 4 has no bug in the code. What check would have caught it?
