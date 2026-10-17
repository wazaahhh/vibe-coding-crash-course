"""Facilitators only: rerun the analysis with each planted error fixed, to show what changes.

Run:  python check_answers.py
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupShuffleSplit, train_test_split

import analysis

DATA = Path(__file__).parent / "data"


def naive_sleep() -> pd.DataFrame:
    """The live-build trap: subtract Geneva wall-clock times directly."""
    s = pd.read_csv(DATA / "sleep.csv")
    s["sleep_h"] = (pd.to_datetime(s["wake_local"]) - pd.to_datetime(s["bedtime_local"])).dt.total_seconds() / 3600
    return s


def main() -> None:
    # Trap 0 (live build): daylight saving.
    s = naive_sleep()
    by_night = s.groupby("night")["sleep_h"].mean()
    print("Trap 0 · daylight saving (live build)")
    print(f"   naive mean sleep, night 24->25 Oct: {by_night['2026-10-24']:.2f} h"
          f"  vs other nights: {by_night.drop('2026-10-24').mean():.2f} h")
    tz = analysis.load_sleep()
    print(f"   tz-aware mean sleep, same night:    {tz[tz.date == '2026-10-25'].sleep_h.mean():.2f} h\n")

    df = analysis.build_dataset()
    print("As shipped by the agent")
    print(f"   r(sleep, mood) = {df.sleep_h.corr(df.mood):+.2f}   r(steps, mood) = {df.steps.corr(df.mood):+.2f}\n")

    # Error 1: reverse-keyed mood_3.
    ema = pd.read_csv(DATA / "ema.csv")
    ema["mood_fixed"] = (ema.mood_1 + ema.mood_2 + (8 - ema.mood_3) + ema.mood_4) / 4
    df = df.merge(ema[["participant_id", "date", "mood_fixed"]], on=["participant_id", "date"])
    print("Error 1 · mood_3 not reverse-scored")
    print(f"   r(sleep, mood): {df.sleep_h.corr(df.mood):+.2f} -> {df.sleep_h.corr(df.mood_fixed):+.2f}"
          f"   (mood SD {df.mood.std():.2f} -> {df.mood_fixed.std():.2f})\n")

    # Error 2: non-wear days counted as 0 steps.
    steps = pd.read_csv(DATA / "steps.csv")
    nonwear = (steps.wear_minutes == 0).mean()
    worn = df.merge(steps[["participant_id", "date", "wear_minutes"]], on=["participant_id", "date"])
    worn = worn[worn.wear_minutes > 0]
    print("Error 2 · non-wear days kept as steps = 0")
    print(f"   {nonwear:.0%} of days are non-wear (steps 0, wear_minutes 0)")
    print(f"   r(steps, mood): {df.steps.corr(df.mood_fixed):+.2f} with zeros -> "
          f"{worn.steps.corr(worn.mood_fixed):+.2f} worn days only\n")

    # Error 3: row-level split leaks participants into the test set.
    worn = worn.copy()
    worn["low_mood"] = (worn.mood_fixed <= worn.mood_fixed.quantile(0.25)).astype(int)
    feats = ["sleep_h", "steps", "person_mean_sleep", "person_mean_steps"]
    rf = lambda: RandomForestClassifier(n_estimators=300, random_state=0)
    Xtr, Xte, ytr, yte = train_test_split(worn[feats], worn.low_mood, test_size=0.3, random_state=0,
                                          stratify=worn.low_mood)
    auc_rows = roc_auc_score(yte, rf().fit(Xtr, ytr).predict_proba(Xte)[:, 1])
    aucs = []
    for tr, te in GroupShuffleSplit(n_splits=20, test_size=0.3, random_state=0).split(
            worn, worn.low_mood, worn.participant_id):
        m = rf().fit(worn.iloc[tr][feats], worn.iloc[tr].low_mood)
        aucs.append(roc_auc_score(worn.iloc[te].low_mood, m.predict_proba(worn.iloc[te][feats])[:, 1]))
    print("Error 3 · random row split: the same participants sit in train and test")
    print(f"   AUC, row split: {auc_rows:.2f}  ->  AUC, held-out participants: {np.mean(aucs):.2f}"
          f" (range {min(aucs):.2f}-{max(aucs):.2f}, 20 splits)")


if __name__ == "__main__":
    main()
