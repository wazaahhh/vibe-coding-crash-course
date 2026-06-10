"""Generate the deliberately-messy demo dataset for the vibe-coding course.

The mess is intentional and pedagogical:
  - Missing values in `height` and `light_hours`.
  - A UNIT INCONSISTENCY: a handful of `height` values are recorded in
    millimetres instead of centimetres (10x too large). This is the bug the
    AI will *miss* during the demo, and that a domain expert catches.
  - One implausible outlier (a typo).
  - Slightly inconsistent treatment labels ("fertilizer" vs "Fertilizer").

Deterministic (fixed seed) so the demo is reproducible.
Run:  python generate_data.py
"""

import csv
import random
from pathlib import Path

random.seed(42)

N = 120
OUT = Path(__file__).parent / "data" / "plant_growth.csv"

# True effect: fertilizer adds ~6 cm on average; light adds ~0.7 cm/hour.
rows = []
for i in range(1, N + 1):
    treated = i % 2 == 0
    # mild label inconsistency for the treated group
    treatment = ("Fertilizer" if i % 10 == 0 else "fertilizer") if treated else "control"

    light = round(random.uniform(4, 14), 1)
    base = 12.0
    height = base + (6.0 if treated else 0.0) + 0.7 * light + random.gauss(0, 2.0)
    height = round(height, 1)

    light_out = "" if random.random() < 0.06 else light          # ~6% missing light
    height_out = "" if random.random() < 0.05 else height        # ~5% missing height

    rows.append({
        "plant_id": f"P{i:03d}",
        "treatment": treatment,
        "light_hours": light_out,
        "height_cm": height_out,
    })

# Inject the unit bug: 4 rows recorded in millimetres (x10), among rows that
# still have a height value.
mm_candidates = [r for r in rows if r["height_cm"] != ""]
for r in random.sample(mm_candidates, 4):
    r["height_cm"] = round(float(r["height_cm"]) * 10, 1)

# Inject one implausible outlier (data-entry typo: extra digit).
typo = random.choice([r for r in rows if r["height_cm"] != "" and float(r["height_cm"]) < 50])
typo["height_cm"] = round(float(typo["height_cm"]) + 200, 1)

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["plant_id", "treatment", "light_hours", "height_cm"])
    w.writeheader()
    w.writerows(rows)

print(f"Wrote {len(rows)} rows to {OUT}")
print("Intentional issues: missing values, 4 rows in mm (x10), 1 outlier, mixed-case labels.")
