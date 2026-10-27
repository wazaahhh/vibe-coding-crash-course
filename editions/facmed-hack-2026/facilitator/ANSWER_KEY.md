# Answer key — facilitators only

Keep this folder (`facilitator/`) out of anything participants receive. Everything runs on one
dataset, `practical/phone-study/` (fictional, `generate_phone_study.py`, seed 1938). Numbers from
`python check_answers.py`.

## Spot the trap 1 · daylight saving (25 October 2026)

`bedtime` and `wake_time` are Geneva wall-clock times with no offset. Clocks went back at 03:00 on
Sun 25 Oct, so subtracting wall-clock times gives one hour too little for everyone asleep across
the change. No error is raised.

- Naive mean sleep, night 24→25 Oct: **6.9 h**; time-zone-aware (localise to `Europe/Zurich`,
  convert to UTC, then subtract): **7.9 h**, in line with the other Saturday nights (**7.7 h**).
  All nights: 7.3 h (weekend nights are longer, so compare Saturday with Saturday).
- How it gets caught: plot mean sleep per night. The Saturday peak turns into a dip on one
  weekend, for every participant at once; only the calendar explains that.

## Spot the trap 2 · unanswered mood prompts

The mean of all answered moods is **4.6 / 7**, and **37%** of prompts are unanswered. The missing
answers are not random (built into the generator: answering drops on bad days and late in term,
low-mood students go silent or drop out more often):

- Mood the evening before a skipped prompt: **4.3**; before an answered one: **4.8**.
- The quarter answering least start with PHQ-9 **10.7**, the others **6.9**.
- 32 students stop answering before the last two weeks: mood in weeks 1–3 **4.2**, others **5.0**.
- Answered prompts: 77% in week 1, 57% in week 11, 55% and 48% in the exam weeks.
- So the true average is lower than 4.6 (C). D ("impossible to say") is the cautious answer: the
  data cannot give the missing values, but they say clearly who is missing.

## Review hunt · `review-hunt/analysis.py` · five problems

It runs cleanly, is well commented, and handles daylight saving correctly, which is what makes
the rest believable.

| # | Problem | Where | What it does | How to catch it |
|---|---|---|---|---|
| 1 | Mood shifted one day: each night is paired with the mood of the **next** evening, though the row's night already ends on the morning of `date` | `build_dataset()`, `shift(-1)` | r(sleep, mood) +0.35 → +0.10 | Read the codebook: what night does a row describe, which evening is its mood? |
| 2 | Phone left lying (`carried_minutes = 0`) kept as `steps = 0` | `build_dataset()` | Phones lie at home on low-mood days, so the zeros manufacture a steps–mood link: r +0.09 (carried days) → +0.15 | Histogram of steps: a spike at exactly 0; the codebook says what it means |
| 3 | Random row split: the same students sit in train and test, and the person-level features identify them | `train_test_split` | AUC 0.81 (row split) → 0.63 on held-out students (range 0.58–0.68 over 20 splits) | Ask "would this work on a new patient?"; split by participant (`GroupShuffleSplit` / `GroupKFold`) |
| 4 | A number no line computed: "students who walk 10,000 steps a day have half as many low-mood days" | `main()` summary | Hard-coded from the agent's priors. The data: about a third fewer (11% vs 17% of carried days), confounded by weekends and exams | Trace every number in the prose to a line of output |
| 5 | Overclaim: "high accuracy", "early-warning signal for depressive episodes" | `main()` summary | A low-mood *day* on a one-tap prompt is not a depressive *episode*; PHQ-9 is in the data and unused; AUC 0.73 (0.63 honestly) is not high accuracy | Ask what the outcome actually measures |

Shipped output: 7,314 participant-days, r(sleep) = +0.10, r(steps) = +0.14, AUC = 0.73. After
fixing 1–3 the honest result is: sleep goes with mood (r ≈ +0.35); steps add little (r ≈ +0.09);
a low-mood-day classifier generalises to new students only modestly (AUC ≈ 0.63). The shipped
headline ("activity is the stronger correlate") is reversed.
