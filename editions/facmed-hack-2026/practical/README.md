# Course folder

Crash Course #2 · FacMed Hack #1 · *Vibe Coding for Scientists*. The data and files used tonight,
in the order they come up. All data here is synthetic or open, so you may upload it to a chat AI.

| When | Part | Folder | What you do |
|---|---|---|---|
| 17:10 | Same data, your question | `phone-study/` | Read the codebook; answer in the live quiz: *what would you find worth exploring?* |
| 18:00 | Spot the trap | `sleep-mood/`, `eeg-eye-state/` | Vote in the live quiz; the files are here to redo both analyses yourself afterwards |
| 18:20 | Review hunt | `review-hunt/`, `sleep-mood/` | Read an analysis an agent wrote; post in the chat everything you would not sign |

## The datasets

- **`phone-study/`**: fictional phone study, 150 students over 12 weeks: daily steps, GPS radius,
  screen time, sleep, calls and messages, an evening mood rating, and PHQ-9 at weeks 0, 6 and 12.
  Codebook: `phone-study/data/README.md`.
- **`sleep-mood/`**: synthetic smartphone + wearable data, 40 participants, 21 nights: bedtimes,
  steps, mood questionnaires. Codebook: `sleep-mood/data/README.md`.
- **`eeg-eye-state/`**: a real, open EEG recording (14 channels, 117 seconds, eyes open or closed;
  CC BY 4.0). See `eeg-eye-state/README.md`.

## Review hunt · `review-hunt/analysis.py`

An agent wrote `analysis.py` from the prompt at the top of the file. Read it with the codebook
`sleep-mood/data/README.md` and **list everything you would not put your name on**, and what
tipped you off. Allowed: plots, the codebook, a second AI, your judgment.

To run it: `python review-hunt/analysis.py` (needs `pandas`, `numpy` and `scikit-learn`).

## Redo it with an agent (after the session, or at the hack)

Open this folder in VS Code with an agent (Claude Code, Codex, GitHub Copilot, Cline), or ask your
agent to clone it. The agent reads `AGENTS.md` (Claude Code reads it through `CLAUDE.md`): it runs
**git** for you, explains each step, and waits for your OK. `NOTES.md` is where it records what was
verified and what was trusted.

- **Sleep:** *"Compute hours slept per night from `sleep-mood/` and plot the average per night."*
  Is any night strange? Why?
- **EEG:** *"Train a simple classifier to predict `eye_closed` and report its accuracy."* Then:
  *"Would it still work on the last part of the recording if we trained on the first part? Test
  exactly that."*

Five prompts worth stealing:

1. *"Explain what this code does before you change anything."*
2. *"Outline your plan, then wait for my OK."*
3. *"Write a test that would fail if this result were wrong."*
4. *"What could make this conclusion wrong? Argue against yourself."*
5. *"Summarise in plain language what you changed and what you assumed."*

For git, just say it: *"start a branch"* · *"save my work"* · *"what changed?"* · *"undo that"* ·
*"send it to GitHub"*.
