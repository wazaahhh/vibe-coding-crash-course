"""Generate the fictional "phone study" dataset used for the whole crash course.

150 students, 12 weeks (Mon 14 Sep -> Sun 6 Dec 2026), one phone app:
  data/participants.csv   participant_id, age, gender, faculty
  data/daily.csv          participant_id, date, week, weekday, exam_week, bedtime, wake_time,
                          carried_minutes, steps, gps_radius_km, screen_minutes, calls, messages, mood
  data/phq9.csv           participant_id, week, phq9          (weeks 0, 6, 12)

Everything is synthetic: no real person is in these files. The structure rewards different
questions (exam weeks, weekends, who stops answering, the clock change on 25 Oct, dropouts,
between- vs. within-person links), and carries the traps used later in the session:
  - bedtime / wake_time are Geneva wall-clock times with no offset: subtracting them loses an
    hour on the night of 24 -> 25 Oct (Spot the trap 1);
  - students answer the mood prompt less on bad days and late in term, and low-mood students
    drop out more: the mean of answered moods hides the decline (Spot the trap 2);
  - on days the phone is left lying (carried_minutes = 0) the app writes steps = 0 and
    gps_radius_km = 0, and this happens more on low-mood days (review hunt, problem 2).
Writes to ../practical/phone-study/data/. Deterministic: same seed, same files.
Run:  python generate_phone_study.py
"""
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

SEED = 1938  # The Evolution of Physics
N = 150
START = date(2026, 9, 14)  # Monday of week 1
N_DAYS = 84
EXAM_WEEKS = {7, 12}  # mid-terms, then the end-of-term exams
GENEVA = ZoneInfo("Europe/Zurich")
UTC = ZoneInfo("UTC")

rng = np.random.default_rng(SEED)
out = Path(__file__).parent.parent / "practical" / "phone-study" / "data"
out.mkdir(parents=True, exist_ok=True)

ids = [f"S{i:03d}" for i in range(1, N + 1)]
faculties = ["Medicine", "Science", "Psychology", "Economics", "Humanities", "Law"]
participants = pd.DataFrame({
    "participant_id": ids,
    "age": np.clip(np.round(rng.gamma(9, 0.6, N) + 17), 18, 34).astype(int),
    "gender": rng.choice(["woman", "man", "non-binary"], N, p=[0.55, 0.42, 0.03]),
    "faculty": rng.choice(faculties, N, p=[0.25, 0.2, 0.18, 0.15, 0.12, 0.10]),
})

# Stable traits
mood_trait = rng.normal(0, 1, N)                      # higher = better mood
activity = rng.normal(0, 1, N) + 0.10 * mood_trait     # active people feel a little better
sociability = rng.normal(0, 1, N)
screen_trait = rng.normal(0, 1, N) - 0.3 * mood_trait
sleep_trait = rng.normal(0, 0.5, N)
chrono = rng.normal(0, 0.6, N)                         # late sleepers go to bed later (hours)
answer_rate = np.clip(rng.beta(8, 2, N), 0.3, 0.99)   # how reliably they answer the mood prompt
# Some drop out (stop sending data after a given day); low-mood students more often
p_drop = np.clip(0.06 + 0.12 * (mood_trait < -0.5) + 0.08 * (mood_trait < -1.2), 0, 1)
dropout_day = np.where(rng.random(N) < p_drop, rng.integers(28, 70, N), N_DAYS)
# Others stay in but go silent: the phone keeps sending data, the mood prompt goes unanswered
p_silent = np.clip(0.04 + 0.30 * (mood_trait < -0.3), 0, 1)
silent_day = np.where(rng.random(N) < p_silent, rng.integers(21, 63, N), N_DAYS)
# Faculty effect on exam stress (Medicine and Law feel it most)
exam_stress = participants["faculty"].map(
    {"Medicine": 1.3, "Law": 1.2, "Science": 1.0, "Economics": 0.9, "Psychology": 0.8, "Humanities": 0.6}
).to_numpy()


def wall_clock(t: datetime) -> str:
    """Geneva wall-clock time as the phone shows it, without the UTC offset."""
    return t.astimezone(GENEVA).strftime("%Y-%m-%d %H:%M")


rows = []
mood_state = np.zeros(N)  # slow, autocorrelated mood drift
for d in range(N_DAYS):
    day = START + timedelta(days=d)
    week = d // 7 + 1
    weekday = day.weekday()
    weekend = weekday >= 5
    exam = week in EXAM_WEEKS
    term_fatigue = d / N_DAYS  # the term wears people down a little
    mood_state = 0.85 * mood_state + rng.normal(0, 0.35, N)
    for i, pid in enumerate(ids):
        if d >= dropout_day[i]:
            continue
        stress = exam_stress[i] * exam
        sleep = float(np.clip(7.2 + sleep_trait[i] + 0.6 * weekend - 0.7 * stress + rng.normal(0, 0.9), 4, 12))
        # The night ending this morning: bedtime the evening before, between 21:30 and 01:45
        bed_h = float(np.clip(23.75 + chrono[i] + 0.6 * weekend + 0.3 * stress + rng.normal(0, 0.6), 21.5, 25.75))
        # (aware arithmetic in one zone is wall-clock arithmetic; the offset follows the wall time)
        bed_local = datetime(day.year, day.month, day.day, tzinfo=GENEVA) - timedelta(days=1) + timedelta(hours=bed_h)
        wake = bed_local.astimezone(UTC) + timedelta(hours=sleep)  # real elapsed time, in UTC
        steps = np.exp(8.7 + 0.35 * activity[i] + 0.15 * weekend - 0.25 * stress + rng.normal(0, 0.35))
        gps = np.exp(1.0 + 0.3 * sociability[i] + 0.6 * weekend - 0.35 * stress
                     + 0.15 * mood_trait[i] + rng.normal(0, 0.5))
        screen = np.exp(5.2 + 0.25 * screen_trait[i] + 0.2 * stress + 0.1 * weekend + rng.normal(0, 0.3))
        calls = rng.poisson(np.exp(0.3 + 0.4 * sociability[i] - 0.3 * stress))
        messages = rng.poisson(np.exp(3.0 + 0.5 * sociability[i] + 0.2 * weekend))
        mood_latent = (4.6 + 0.8 * mood_trait[i] + mood_state[i] + 0.45 * (sleep - 7)
                       + 0.03 * np.log(steps / 6000) - 0.6 * stress - 0.8 * term_fatigue)
        mood = int(np.clip(np.round(mood_latent + rng.normal(0, 0.6)), 1, 7))
        # Phone left lying all day (at home, charging): more likely on bad days
        left = rng.random() < 0.02 + 0.10 * max(0.0, 4.5 - mood_latent)
        carried = 0 if left else int(np.clip(rng.normal(620, 140), 150, 960))
        # Who answers the evening prompt: less often late in term, much less often on bad days
        p_answer = answer_rate[i] - 0.10 * term_fatigue - 0.15 * max(0, 4.5 - mood)
        mood_val = mood if rng.random() < p_answer and d < silent_day[i] else np.nan
        phone_off = rng.random() < 0.02  # no passive data at all that day
        rows.append({
            "participant_id": pid,
            "date": day.isoformat(),
            "week": week,
            "weekday": day.strftime("%a"),
            "exam_week": int(exam),
            "bedtime": None if phone_off else wall_clock(bed_local),
            "wake_time": None if phone_off else wall_clock(wake),
            "carried_minutes": np.nan if phone_off else carried,
            "steps": np.nan if phone_off else (0 if left else int(round(steps))),
            "gps_radius_km": np.nan if phone_off else (0.0 if left else round(float(gps), 2)),
            "screen_minutes": np.nan if phone_off else int(round(min(screen, 900))),
            "calls": np.nan if phone_off else int(calls),
            "messages": np.nan if phone_off else int(messages),
            "mood": mood_val,
        })

daily = pd.DataFrame(rows)
for c in ["carried_minutes", "steps", "screen_minutes", "calls", "messages", "mood"]:
    daily[c] = daily[c].astype("Int64")

# PHQ-9 at weeks 0, 6 and 12 (missing after dropout, and ~5% skipped)
phq = []
for i, pid in enumerate(ids):
    for wk, d in [(0, 0), (6, 41), (12, 83)]:
        if d >= dropout_day[i] or (wk > 0 and rng.random() < 0.05):
            continue
        sev = 8 - 3.2 * mood_trait[i] + 1.5 * exam_stress[i] * (wk == 12) + 1.2 * (wk / 12) + rng.normal(0, 2.2)
        phq.append({"participant_id": pid, "week": wk, "phq9": int(np.clip(round(sev), 0, 27))})

participants.to_csv(out / "participants.csv", index=False)
daily.to_csv(out / "daily.csv", index=False)
pd.DataFrame(phq).to_csv(out / "phq9.csv", index=False)
print(f"participants: {len(participants)}, daily rows: {len(daily)}, phq9 rows: {len(phq)} -> {out}")
