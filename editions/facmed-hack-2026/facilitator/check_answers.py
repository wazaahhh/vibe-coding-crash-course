"""Facilitators only: the numbers behind Spot the trap and the review hunt, all on phone-study/.

Run:  python check_answers.py
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupShuffleSplit, train_test_split

PRACTICAL = Path(__file__).parent.parent / "practical"
sys.path.insert(0, str(PRACTICAL / "review-hunt"))
import analysis  # noqa: E402

DATA = PRACTICAL / "phone-study" / "data"


def spot_dst() -> None:
    """Spot the trap 1: subtract Geneva wall-clock times directly."""
    d = pd.read_csv(DATA / "daily.csv")
    d["naive"] = (pd.to_datetime(d.wake_time) - pd.to_datetime(d.bedtime)).dt.total_seconds() / 3600
    d["utc"] = analysis.load_daily().sort_index()["sleep_h"]
    sat = d[d.weekday == "Sun"].groupby("date")[["naive", "utc"]].mean()  # nights Saturday -> Sunday
    print("Spot the trap 1 · clock change, night 24 -> 25 Oct")
    print(f"   clock times: {sat.loc['2026-10-25', 'naive']:.1f} h   UTC: {sat.loc['2026-10-25', 'utc']:.1f} h"
          f"   other Saturday nights: {sat.drop('2026-10-25').utc.mean():.1f} h"
          f"   all nights: {d.utc.mean():.1f} h\n")


def spot_missing() -> None:
    """Spot the trap 2: who answers the mood prompt."""
    d = pd.read_csv(DATA / "daily.csv")
    phq = pd.read_csv(DATA / "phq9.csv")
    print("Spot the trap 2 · unanswered mood prompts")
    print(f"   mean of answered moods: {d.mood.mean():.1f} / 7;  prompts unanswered: {d.mood.isna().mean():.0%}")
    ans = d.groupby("week").mood.apply(lambda s: s.notna().mean())
    print(f"   answered: week 1 {ans[1]:.0%}, week 11 {ans[11]:.0%}, exam weeks {ans[7]:.0%} / {ans[12]:.0%}")
    rate = d.groupby("participant_id").mood.apply(lambda s: s.notna().mean())
    base = phq[phq.week == 0].set_index("participant_id").phq9
    low = rate < rate.quantile(0.25)
    print(f"   PHQ-9 at enrolment: quarter answering least {base[low].mean():.1f}, others {base[~low].mean():.1f}")
    # The day before a prompt goes unanswered vs answered, same student (passive data never stops)
    d = d.sort_values(["participant_id", "date"])
    d["prev_mood"] = d.groupby("participant_id").mood.shift(1)
    d["skipped"] = d.mood.isna()
    m = d.dropna(subset=["prev_mood"]).groupby("skipped").prev_mood.mean()
    print(f"   mood the evening before a skipped prompt: {m[True]:.1f}, before an answered one: {m[False]:.1f}")
    last = d.dropna(subset=["mood"]).groupby("participant_id").date.max()
    silent = last[last < "2026-11-20"].index  # stopped answering 2+ weeks before the end
    early = d[d.week <= 3].groupby("participant_id").mood.mean()
    print(f"   {len(silent)} students stop answering before the last two weeks; their mood in weeks 1-3:"
          f" {early[early.index.isin(silent)].mean():.1f}, others {early[~early.index.isin(silent)].mean():.1f}")
    print(f"   PHQ-9 mean, weeks 0 / 6 / 12: {' / '.join(f'{v:.1f}' for v in phq.groupby('week').phq9.mean())}\n")


def review_hunt() -> None:
    df = analysis.build_dataset()
    print("Review hunt · as shipped")
    print(f"   r(sleep, mood) = {df.sleep_h.corr(df.mood_next):+.2f}   r(steps, mood) = {df.steps.corr(df.mood_next):+.2f}\n")

    # Error 1: mood shifted one day too far; the row's night ends that morning.
    d = analysis.load_daily().dropna(subset=["sleep_h", "steps", "mood"]).copy()
    print("Error 1 · night paired with the wrong evening")
    print(f"   r(sleep, mood): {df.sleep_h.corr(df.mood_next):+.2f} shifted -> {d.sleep_h.corr(d.mood):+.2f} same row\n")

    # Error 2: phone left lying (carried_minutes = 0) kept as steps = 0.
    carried = d[d.carried_minutes > 0].copy()
    print("Error 2 · phone left lying kept as steps = 0")
    print(f"   {(d.carried_minutes == 0).mean():.0%} of days have carried_minutes = 0 (steps 0)")
    print(f"   r(steps, mood): {d.steps.corr(d.mood):+.2f} with zeros -> {carried.steps.corr(carried.mood):+.2f} carried days only\n")

    # Error 3: row-level split leaks participants into the test set.
    carried["person_mean_sleep"] = carried.groupby("participant_id").sleep_h.transform("mean")
    carried["person_mean_steps"] = carried.groupby("participant_id").steps.transform("mean")
    carried["low_mood"] = (carried.mood <= 3).astype(int)
    feats = ["sleep_h", "steps", "person_mean_sleep", "person_mean_steps"]
    rf = lambda: RandomForestClassifier(n_estimators=300, random_state=0, n_jobs=-1)
    Xtr, Xte, ytr, yte = train_test_split(carried[feats], carried.low_mood, test_size=0.3, random_state=0,
                                          stratify=carried.low_mood)
    auc_rows = roc_auc_score(yte, rf().fit(Xtr, ytr).predict_proba(Xte)[:, 1])
    aucs = []
    for tr, te in GroupShuffleSplit(n_splits=20, test_size=0.3, random_state=0).split(
            carried, carried.low_mood, carried.participant_id):
        m = rf().fit(carried.iloc[tr][feats], carried.iloc[tr].low_mood)
        aucs.append(roc_auc_score(carried.iloc[te].low_mood, m.predict_proba(carried.iloc[te][feats])[:, 1]))
    print("Error 3 · random row split: the same participants sit in train and test")
    print(f"   AUC, row split: {auc_rows:.2f}  ->  AUC, held-out participants: {np.mean(aucs):.2f}"
          f" (range {min(aucs):.2f}-{max(aucs):.2f}, 20 splits)")


if __name__ == "__main__":
    spot_dst()
    spot_missing()
    review_hunt()
