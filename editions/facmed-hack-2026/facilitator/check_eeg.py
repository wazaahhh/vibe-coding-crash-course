"""Facilitators only: the two real traps in the EEG Eye State data (practical, round 2).

Run:  python check_eeg.py
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

CSV = Path(__file__).parent.parent / "practical" / "eeg-eye-state" / "data" / "eeg_eye_state.csv"


def main() -> None:
    df = pd.read_csv(CSV)
    channels = [c for c in df.columns if c not in ("sample", "eye_closed")]
    X, y = df[channels].to_numpy(), df["eye_closed"].to_numpy()
    print(f"{len(df)} samples, {len(channels)} channels, eyes closed in {y.mean():.0%} of samples")

    # Trap 1: artifacts.
    med = np.median(X, axis=0)
    mad = np.median(np.abs(X - med), axis=0)
    art = (np.abs(X - med) > 20 * mad).any(axis=1)
    print(f"\nTrap 1 · artifacts: {art.sum()} samples with values > 20 MADs from the median "
          f"(max {X.max():,.0f} vs median ~{np.median(X):,.0f})")

    # Trap 2: random split on a continuous recording.
    runs = (df.eye_closed != df.eye_closed.shift()).cumsum().nunique()
    knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    Xc, yc = X[~art], y[~art]
    rnd = cross_val_score(knn, Xc, yc, cv=KFold(5, shuffle=True, random_state=0)).mean()
    blk = cross_val_score(knn, Xc, yc, cv=KFold(5, shuffle=False)).mean()
    print(f"\nTrap 2 · random split on one continuous recording ({runs} open/closed periods)")
    print(f"   kNN accuracy, random 5-fold split : {rnd:.2f}")
    print(f"   kNN accuracy, 5 time blocks       : {blk:.2f}")
    print(f"   always guessing 'open'            : {1 - yc.mean():.2f}")


if __name__ == "__main__":
    main()
