# EEG Eye State: a real, open EEG recording

**Source.** Roesler, O. (2013). *EEG Eye State* [Dataset]. UCI Machine Learning Repository.
https://doi.org/10.24432/C57G7J · licence **CC BY 4.0** (share and adapt with credit).
Converted here from the original ARFF file to CSV; values unchanged.

**What it is** (from the repository page): one continuous EEG measurement with the Emotiv EEG
Neuroheadset, **117 seconds** long. The eye state was detected with a camera during the
recording and added to the file afterwards from the video frames. All values are in
chronological order, first measurement at the top.

## `data/eeg_eye_state.csv`
| Column | Meaning |
|---|---|
| `sample` | row number = position in time (0 = first measurement) |
| `AF3` … `AF4` | 14 EEG channels (10–20 positions: AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4) |
| `eye_closed` | `1` = eyes closed, `0` = eyes open |

14,980 rows. The repository page does not state units, reference or filtering; 14,980 samples
over 117 s suggests about 128 samples per second.

**The question for round 2:** can these 14 channels tell whether the eyes are open or closed,
and how well, *honestly*?
