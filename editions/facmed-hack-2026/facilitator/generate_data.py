"""Generate the synthetic digital-phenotyping dataset for the FacMed Hack edition.

40 participants, 21 nights (12 Oct -> 1 Nov 2026, across the 25 Oct clock change):
  data/participants.csv   participant_id, age, phq9_baseline
  data/sleep.csv          participant_id, night, bedtime_local, wake_local   (Geneva wall-clock time, no offset)
  data/steps.csv          participant_id, date, steps, wear_minutes
  data/ema.csv            participant_id, date, mood_1..mood_4             (1-7; see data/README.md)

Everything is synthetic. The traps are deliberate (answer key in ANSWER_KEY.md, facilitators only).
Writes to ../practical/sleep-mood/data/. Deterministic: same seed, same files.  Run:  python generate_data.py
"""
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

SEED = 2026
N = 40
FIRST_NIGHT = datetime(2026, 10, 12)
N_NIGHTS = 21
TZ = ZoneInfo("Europe/Zurich")
UTC = ZoneInfo("UTC")

rng = np.random.default_rng(SEED)
out = Path(__file__).parent.parent / "practical" / "sleep-mood" / "data"
out.mkdir(exist_ok=True)

ids = [f"P{i:02d}" for i in range(1, N + 1)]
trait_mood = rng.normal(0, 1, N)        # stable between-person differences in mood
trait_activity = rng.normal(0, 1, N)
sleep_offset_h = rng.normal(0, 0.6, N)  # habitual sleep duration offset
bed_offset_min = rng.normal(0, 40, N)   # habitual bedtime offset

participants = pd.DataFrame({
    "participant_id": ids,
    "age": rng.integers(19, 66, N),
    "phq9_baseline": np.clip(np.round(8 - 3.5 * trait_mood + rng.normal(0, 2, N)), 0, 27).astype(int),
})

sleep_rows, steps_rows, ema_rows = [], [], []
for i, pid in enumerate(ids):
    for d in range(N_NIGHTS):
        night = FIRST_NIGHT + timedelta(days=d)
        # Bedtime between ~22:00 and 01:30 local, never in the repeated 02:00-03:00 hour.
        bed_min = 23 * 60 + bed_offset_min[i] + rng.normal(0, 35)
        bed_min = float(np.clip(bed_min, 22 * 60, 25.5 * 60))
        bed_local = (night + timedelta(minutes=bed_min)).replace(tzinfo=TZ)
        true_sleep_h = float(np.clip(7.0 + sleep_offset_h[i] + rng.normal(0, 0.8), 4.0, 10.5))
        # Wake = bedtime + true elapsed time, computed in UTC, then shown as Geneva wall-clock time.
        wake_local = (bed_local.astimezone(UTC) + timedelta(hours=true_sleep_h)).astimezone(TZ)
        sleep_rows.append({
            "participant_id": pid,
            "night": night.date().isoformat(),
            "bedtime_local": bed_local.strftime("%Y-%m-%d %H:%M"),
            "wake_local": wake_local.strftime("%Y-%m-%d %H:%M"),
        })

        day = (night + timedelta(days=1)).date()
        # Next-day mood: trait + sleep effect + noise.
        mood = 4.0 + 0.9 * trait_mood[i] + 0.4 * (true_sleep_h - 7.0) + rng.normal(0, 0.4)
        steps = max(0.0, rng.normal(8000 + 2000 * trait_activity[i] + 150 * (mood - 4.0), 1500))
        # Non-wear: more likely on low-mood days. The app writes steps = 0 with wear_minutes = 0.
        p_nonwear = 0.03 + 0.25 * (mood < 3.3)
        if rng.random() < p_nonwear:
            steps_rows.append({"participant_id": pid, "date": day.isoformat(), "steps": 0, "wear_minutes": 0})
        else:
            steps_rows.append({"participant_id": pid, "date": day.isoformat(), "steps": int(round(steps)),
                               "wear_minutes": int(rng.integers(600, 960))})
        if rng.random() < 0.9:  # ~10% of EMA prompts unanswered
            items = np.clip(np.round(mood + rng.normal(0, 0.6, 4)), 1, 7).astype(int)
            ema_rows.append({
                "participant_id": pid, "date": day.isoformat(),
                "mood_1": items[0],
                "mood_2": items[1],
                "mood_3": 8 - items[2],  # "I felt down": reverse-keyed, as in the codebook
                "mood_4": items[3],
            })

participants.to_csv(out / "participants.csv", index=False)
pd.DataFrame(sleep_rows).to_csv(out / "sleep.csv", index=False)
pd.DataFrame(steps_rows).to_csv(out / "steps.csv", index=False)
pd.DataFrame(ema_rows).to_csv(out / "ema.csv", index=False)
print(f"Wrote {len(sleep_rows)} nights, {len(steps_rows)} step days, {len(ema_rows)} EMA entries to {out}/")
