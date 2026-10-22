# Practical: direct an AI agent on real analyses

Crash Course #2 · FacMed Hack #1 · *Vibe Coding for Scientists*. Work in **pairs**, in a Zoom
breakout room, with two roles:

- **Driver**: shares their screen and talks to the agent, saying out loud what they ask and why.
- **Skeptic**: never touches the keyboard. After every answer: *how would we know if this is wrong?*

**Switch roles halfway** (the host will broadcast it).

## Setup (2 minutes)

| You have… | Do this |
|---|---|
| VS Code with an agent (Claude Code, Codex, GitHub Copilot, Cline) | Download this folder (or ask your agent to clone it), open it in VS Code, open the agent |
| Only a chat AI (ChatGPT, Claude, Gemini…) | Upload the CSV files and the README of each round to the chat; all the data here is synthetic or open, so this is allowed. Skip the git steps |
| Nothing working | Be the skeptic first; drive in round 2 from your partner's machine via Zoom remote control, or in chat mode |

The agent reads `AGENTS.md` (Claude Code reads it through `CLAUDE.md`): it runs **git** for you
and explains each step. You only ask in plain English.

## Round 1 · Driver A · ~15 min · `sleep-mood/`

Synthetic smartphone + wearable data: 40 participants, 21 nights. Codebook: `sleep-mood/data/README.md`.
**Question: how long do people sleep each night?**

1. *"Brief me on `sleep-mood/` and its codebook. Don't change anything."*
2. *"Start a new branch for this task."* (The agent explains what a branch is in one sentence.)
3. *"Plan how you'd compute sleep duration per night and plot the average per night. Wait for my OK."*
4. Approve, let it run, **look at the plot together**. Skeptic: is anything strange?
5. If something is: find out why, and fix it with a precise instruction.
6. *"Save my work with a clear message, and add a line to NOTES.md."*

## Round 2 · Driver B · ~15 min · `eeg-eye-state/`

A **real, open** EEG recording: 14 channels, 117 seconds, eyes open or closed. See `eeg-eye-state/README.md`.
**Question: can these channels tell whether the eyes are closed, and how well, honestly?**

1. *"Load `eeg-eye-state/data/eeg_eye_state.csv`, describe it, and plot the 14 channels over time."*
   Skeptic: does the plot look like EEG?
2. *"Train a simple classifier to predict `eye_closed` and report its accuracy."*
3. Skeptic: *"Would this still work on the last part of the recording if we trained on the first part?"*
   Ask the agent to test exactly that, and compare.
4. *"Save my work, send it to GitHub and open a pull request saying what we verified and what we
   trusted."* (No GitHub account yet? Just save.)

**Back in the main room:** post in the chat (1) the strange thing you found in round 1, and
(2) your two accuracy numbers from round 2.

## Review hunt · `review-hunt/`

`analysis.py` was written by an agent from the prompt at the top of the file. Run it, read it,
read the codebook. **List everything you would not put your name on.**
