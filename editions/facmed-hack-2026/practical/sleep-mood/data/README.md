# Codebook — synthetic digital-phenotyping study

**Synthetic data.** 40 adult participants, smartphone + wearable + daily EMA (ecological
momentary assessment: short questionnaires answered on the phone), 12 October – 2 November 2026,
Geneva. No real person is in these files.

## `participants.csv`
| Column | Meaning |
|---|---|
| `participant_id` | P01–P40 |
| `age` | years |
| `phq9_baseline` | PHQ-9 depression score at enrolment (0–27, higher = more depressive symptoms) |

## `sleep.csv` — one row per night, from the phone's sleep detection
| Column | Meaning |
|---|---|
| `night` | the evening the night starts |
| `bedtime_local` | time asleep, **Geneva wall-clock time as shown on the phone, no UTC offset stored** |
| `wake_local` | time awake, same convention |

## `steps.csv` — one row per day, from the wearable
| Column | Meaning |
|---|---|
| `steps` | step count for the day |
| `wear_minutes` | minutes the device was worn. **`0` means the device was not worn that day; the app then writes `steps = 0`, which is not a measurement** |

## `ema.csv` — one row per answered evening prompt (≈10 % of prompts unanswered)
Four items, each on a 1–7 scale:

| Column | Item | Keying |
|---|---|---|
| `mood_1` | "Today I felt cheerful" | positive |
| `mood_2` | "Today I felt calm" | positive |
| `mood_3` | "Today I felt down" | **reverse-keyed: score as 8 − value before averaging** |
| `mood_4` | "Today I felt full of energy" | positive |

The mood score for a day is the mean of the four items after reverse-keying `mood_3`
(higher = better mood). Mood on day *d* is linked to the night that ends on the morning of *d*.
