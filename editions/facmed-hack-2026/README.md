# FacMed Hack edition — Crash Course #2

*Vibe Coding for Scientists* re-cut as **Crash Course #2 of FacMed Hack #1 — Digital
Phenotyping of Mental Health** (UNIGE Faculty of Medicine; module B2 of the course proposal to the
Lemanic Neuroscience Doctoral School). Thursday 22 October 2026, 17:00–19:00, **on Zoom**.
Audience: PhD students, postdocs and PIs, mostly neuroscience, a third with some Python, most new
to git.

Three objectives:

1. **Imagine**: where AI agents come from, what they already do in research, and your place
   (contribution, career, purpose) in a bright, sustainable and safe future with them.
2. **Understand**: how vibe coding works: fast and slow, try and fail, git run by the agent for
   you, working collectively.
3. **Prepare**: the hack's status, and how it runs with or without your own tools; the HPE /
   NVIDIA environment is open to every team.

## Running order (69 slides)

| Time | File | Part | Polls | Draws on course module |
|---|---|---|---|---|
| 17:00 | `00-opening.md` | Title · Zador quote · opening question (Zoom chat) · objectives · programme | — | — |
| 17:05 | `10-context.md` | **1 · Where this comes from**: history (1943 → 2026), what an LLM is, chatbot → agent, why coding first, uses in science and neuroscience, opportunities, **pre-read 1 (DePasquale)**: four directions and the field's worries, pitfalls, what the science says | 1 · 2 | 00, 01, 02, 03, 09 |
| 17:25 | `20-how-it-works.md` | **2 · How vibe coding works**: four pillars, one folder + one rule file, how to ask, three dials, a worked rhythm | — | 02, 03, 06, 07 |
| 17:33 | `25-git.md` | **3 · Git without the jargon**: the problem, save points (diagram), a ten-word dictionary, laptop vs. GitHub, the loop, branches, **hand off 95% of git to the agent**, the 5% that stays yours, `AGENTS.md` | 3 | 05, 07, 09 |
| 17:45 | `30-practical.md` | **4 · Practical in pairs** (breakout rooms, driver + skeptic, switch at 18:06): round 1 synthetic sleep data (daylight-saving trap), round 2 a real open EEG recording (artifacts, temporal leakage); debrief | 4 | 03, 08 |
| 18:25 | `40-review-hunt.md` | **5 · Review hunt** (plenary): five problems in an agent-written analysis; peer review | 5 | 02, 08 |
| 18:33 | `50-hack.md` | **6 · The hack**: needs campaign (181 needs, 30 contributors), eight draft challenges, rank + confirm (diet, access, sleeping on site), two paths, team workflow, final steps, what's at stake | — | 05 |
| 18:43 | `60-your-place.md` | **7 · A future worth building**: **pre-read 2 (Schuck)**: lab AI policy and field norms, five rules; a bright, sustainable, safe future; poll recap; opening question revisited; close; Zador quote | 6 | 09, 11 |

Pre-work: DePasquale (2026) and Schuck (2026), both in *The Transmitter* (links below), and course
modules 01–04. Polls: `zoom_polls.md` (results shown right after each poll).

## Files

| Path | What | Who |
|---|---|---|
| `_header.md` · `[0-9][0-9]-*.md` | Design system and modules. **Edit these** | Facilitator |
| `build.sh` | `./build.sh --pdf` → `slides.md` (generated), `slides.html`, `slides.pdf` | Facilitator |
| `zoom_polls.md` | The six polls, where they go, settings | Facilitator |
| `practical/` | **What participants get**: `README.md` (steps), `AGENTS.md` + `CLAUDE.md` (git handed to the agent), `NOTES.md`, `sleep-mood/` (synthetic data + codebook), `eeg-eye-state/` (real open EEG, CC BY 4.0), `review-hunt/analysis.py` | Participants |
| `facilitator/` | `ANSWER_KEY.md`, `check_answers.py`, `check_eeg.py`, `generate_data.py`. **Never share** | Facilitator |
| `assets/` | Partner logos | — |

Speaker notes (talking points, facilitator moves, sources, [CONFIRM] flags) are HTML comments under
each slide banner: they show in the presenter view and PPTX notes, never on the projected slide.

## Before the session

- **Publish the participant folder**: `practical/` only (never `facilitator/`), e.g. as its own
  public repository or a zip; put the link in the Zoom chat at 17:45.
- Create the six Zoom polls (`zoom_polls.md`); enable breakout rooms; dry-run both practical rounds
  with the agent you will use.
- **[CONFIRM]** Friday start time (14 Oct steering committee: 12:30; public programme: 11:00);
  the ranking deadline; where GitHub usernames are collected; private or public team repositories;
  any update to the challenge list or needs count after 15 Oct.

## Sources

- DePasquale, B. (2026, June 16). Models at the speed of thought: How AI coding is reshaping
  theoretical neuroscience. *The Transmitter*. https://doi.org/10.53053/FVAU9567
- Schuck, N. (2026, August 24). How, when and why to use agentic AI in our neuroscience labs.
  *The Transmitter*. https://doi.org/10.53053/NSSZ1001
- Roesler, O. (2013). EEG Eye State [Dataset]. UCI Machine Learning Repository.
  https://doi.org/10.24432/C57G7J (CC BY 4.0)
- METR (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity.
- Luo, X. et al. (2024). Large language models surpass human experts in predicting neuroscience
  results. *Nature Human Behaviour*.
- Course modules 00–11 and their sources (`../../modules/11-close.md`).
