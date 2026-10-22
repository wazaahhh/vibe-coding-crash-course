# Codebook — the "phone study" (fictional)

**Synthetic data, used all evening: "Same data, your question", Spot the trap and the review
hunt.** 150 university
students, 12 weeks (Monday 14 September → Sunday 6 December 2026), one phone app, consent on
file. No real person is in these files.

## `participants.csv`
| Column | Meaning |
|---|---|
| `participant_id` | S001–S150 |
| `age` | years |
| `gender` | woman · man · non-binary |
| `faculty` | Medicine · Science · Psychology · Economics · Humanities · Law |

## `daily.csv` — one row per participant and day, while they are in the study
Passive data, recorded by the phone:

| Column | Meaning |
|---|---|
| `date`, `week`, `weekday` | calendar day; study week 1–12; Mon–Sun |
| `exam_week` | `1` in the mid-term week (week 7) and the exam week (week 12) |
| `bedtime`, `wake_time` | the phone's estimate of falling asleep and waking up, for **the night ending on the morning of `date`** (so `bedtime` is usually the evening before). **Geneva wall-clock time as shown on the phone, no UTC offset stored** |
| `carried_minutes` | minutes the phone was being carried (motion sensor). **`0` means the phone lay all day (at home, charging); the app then writes `steps = 0` and `gps_radius_km = 0`, which are not measurements** |
| `steps` | step count for the day |
| `gps_radius_km` | how far they roamed: radius of gyration of the day's GPS points, km |
| `screen_minutes` | minutes with the screen on |
| `calls`, `messages` | number of calls and messages (counts only, never content) |

Self-report, every evening:

| Column | Meaning |
|---|---|
| `mood` | one-tap answer, the evening of `date`, to "How was your mood today?", 1 (very bad) – 7 (very good); empty when the prompt was not answered |

Empty passive values mean the phone sent no data that day. Participants who leave the study
simply have no rows after their last day.

## `phq9.csv` — depression questionnaire
| Column | Meaning |
|---|---|
| `week` | 0 (enrolment), 6, 12 |
| `phq9` | PHQ-9 total, 0–27 (higher = more depressive symptoms) |
