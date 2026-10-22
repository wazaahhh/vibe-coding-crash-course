"""Generate the fictional "phone study" dataset for the "Same data, your question" exercise.

150 students, 12 weeks (Mon 14 Sep -> Sun 6 Dec 2026), one phone app:
  data/participants.csv   participant_id, age, gender, faculty
  data/daily.csv          participant_id, date, week, weekday, exam_week, steps, gps_radius_km,
                          screen_minutes, sleep_hours, calls, messages, mood
  data/phq9.csv           participant_id, week, phq9          (weeks 0, 6, 12)

Everything is synthetic: no real person is in these files. The structure is built to reward
different questions (exam weeks, weekends, who stops answering, the clock change on 25 Oct,
dropouts, between- vs. within-person links), not to hide one trap.
Writes to ../practical/phone-study/data/. Deterministic: same seed, same files.
Run:  python generate_phone_study.py
"""
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 1938  # The Evolution of Physics
N = 150
START = date(2026, 9, 14)  # Monday of week 1
N_DAYS = 84
EXAM_WEEKS = {7, 12}  # mid-terms, then the end-of-term exams
DST_DAY = date(2026, 10, 25)

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
activity = rng.normal(0, 1, N) + 0.35 * mood_trait     # active people feel a bit better
sociability = rng.normal(0, 1, N)
screen_trait = rng.normal(0, 1, N) - 0.3 * mood_trait
sleep_trait = rng.normal(0, 0.5, N)
answer_rate = np.clip(rng.beta(8, 2, N), 0.3, 0.99)   # how reliably they answer the mood prompt
# Some drop out: stop sending data after a given day
dropout_day = np.where(rng.random(N) < 0.12, rng.integers(28, 70, N), N_DAYS)
# Faculty effect on exam stress (Medicine and Law feel it most)
exam_stress = participants["faculty"].map(
    {"Medicine": 1.3, "Law": 1.2, "Science": 1.0, "Economics": 0.9, "Psychology": 0.8, "Humanities": 0.6}
).to_numpy()

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
        sleep = 7.2 + sleep_trait[i] + 0.6 * weekend - 0.7 * stress + rng.normal(0, 0.9)
        if day == DST_DAY:
            sleep += 1.0  # clocks went back: the phone records an extra hour in bed
        steps = np.exp(8.7 + 0.35 * activity[i] + 0.15 * weekend - 0.25 * stress + rng.normal(0, 0.35))
        gps = np.exp(1.0 + 0.3 * sociability[i] + 0.6 * weekend - 0.35 * stress
                     + 0.15 * mood_trait[i] + rng.normal(0, 0.5))
        screen = np.exp(5.2 + 0.25 * screen_trait[i] + 0.2 * stress + 0.1 * weekend + rng.normal(0, 0.3))
        calls = rng.poisson(np.exp(0.3 + 0.4 * sociability[i] - 0.3 * stress))
        messages = rng.poisson(np.exp(3.0 + 0.5 * sociability[i] + 0.2 * weekend))
        mood_latent = (4.6 + 0.8 * mood_trait[i] + mood_state[i] + 0.25 * (sleep - 7)
                       + 0.15 * np.log(steps / 6000) - 0.6 * stress - 0.5 * term_fatigue)
        mood = int(np.clip(np.round(mood_latent + rng.normal(0, 0.6)), 1, 7))
        # Who answers the evening prompt: less often late in term, and less often on bad days
        p_answer = answer_rate[i] - 0.15 * term_fatigue - 0.06 * max(0, 4 - mood)
        mood_val = mood if rng.random() < p_answer else np.nan
        phone_off = rng.random() < 0.03  # no passive data at all that day
        rows.append({
            "participant_id": pid,
            "date": day.isoformat(),
            "week": week,
            "weekday": day.strftime("%a"),
            "exam_week": int(exam),
            "steps": np.nan if phone_off else int(round(steps)),
            "gps_radius_km": np.nan if phone_off else round(float(gps), 2),
            "screen_minutes": np.nan if phone_off else int(round(min(screen, 900))),
            "sleep_hours": np.nan if phone_off else round(float(np.clip(sleep, 2.5, 13)), 1),
            "calls": np.nan if phone_off else int(calls),
            "messages": np.nan if phone_off else int(messages),
            "mood": mood_val,
        })

daily = pd.DataFrame(rows)
for c in ["steps", "screen_minutes", "calls", "messages", "mood"]:
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
