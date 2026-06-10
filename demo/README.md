# Demo — Plant Growth Analysis

A 20-minute hands-on demo for the *Vibe Coding for Scientists* crash course.
Participants **fork this repo**, then use any AI coding tool to analyze a deliberately-messy dataset — practicing the four pillars live.

## The scenario
You're testing whether **fertilizer** affects plant **height**, accounting for **light exposure**. The data is in [`data/plant_growth.csv`](data/plant_growth.csv).

## The dataset is messy on purpose
It contains traps that teach the mindset:
- **Missing values** in `height_cm` and `light_hours`.
- **A unit inconsistency** — 4 rows recorded in **millimetres** (10× too large). The AI usually flags these as "outliers" instead of a unit bug. *You* catch it because you know plants. **This is the centerpiece of the demo.**
- **One implausible outlier** (a data-entry typo).
- **Inconsistent treatment labels** (`fertilizer` vs `Fertilizer`).

Regenerate it any time (deterministic seed):
```bash
python generate_data.py
```

## How to run the demo
1. **Fork** this repo (your own sandbox to break) — or "Use this template" / clone.
2. Open your AI tool of choice (Claude Code, Cursor, Copilot, or paste-into-chat — tool-agnostic).
3. Work through [`notebook_starter.ipynb`](notebook_starter.ipynb) **by prompting, not typing**. The six steps are:
   1. Orient by asking, not reading — *"brief me on this dataset's problems."*
   2. Catch the unit bug the AI misses → fix it with domain knowledge.
   3. Clean missing values + the outlier (ask for the strategy first).
   4. Diverge — three ways to test the effect, with assumptions.
   5. Visualize — does the picture match the statistic?
   6. Slow down at the claim — *"what would make this conclusion wrong?"*

> After **every** AI answer, ask: **"How would I know if this is wrong?"**

## Notebook or not?
- **Notebook** → great for exploration (inline plots, poke at state); beware hidden/out-of-order state.
- **Script + agent** → great for reproducibility; the AI can run, read errors, and self-fix.
- **Best of both:** explore here, then prompt *"harden this into a script I can rerun from scratch."*

## Requirements
Python 3 with `pandas`, `matplotlib`, `statsmodels` (or `scipy`). Or just let your AI tool install what it needs.
```bash
pip install pandas matplotlib statsmodels
```

## The "answer key" (facilitators — don't reveal early)
- True effect built into the data: fertilizer adds **~6 cm**; light adds **~0.7 cm/hour**.
- A correct analysis should recover a positive, significant fertilizer effect **after** the mm→cm fix and outlier handling — and should regress on / control for `light_hours`.
- If a participant skips the unit fix, the spurious mm rows inflate variance and can distort the estimate — a perfect illustration of "plausible, beautiful, wrong."
