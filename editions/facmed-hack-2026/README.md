# FacMed Hack edition — Crash Course #2

*Vibe Coding for Scientists* re-cut as **Crash Course #2 of FacMed Hack #1 — Digital
Phenotyping of Mental Health** (UNIGE Faculty of Medicine; module B2 of the course proposal to the
Lemanic Neuroscience Doctoral School). Thursday 22 October 2026, 17:00–19:00, **on Zoom**.
Audience: PhD students, postdocs and PIs, mostly neuroscience, a third with some Python.

The edition reuses the course's content and pedagogy, in the FacMed Hack design system, around
three objectives:

1. **Imagine**: see your place in agentic science: contribution, career, purpose.
2. **Understand**: how vibe coding works: fast and slow, try and fail, GitHub, working collectively.
3. **Prepare**: how it runs at the hack, with or without your own tools; the HPE / NVIDIA
   environment is open to every team.

## Running order (≈ 45 slides)

| Time | File | Block | Objective | Draws on course module |
|---|---|---|---|---|
| 17:00 | `00-opening.md` | Title · opening question (Zoom chat) · six Zoom polls · objectives · programme | 1 | — (new) |
| 17:15 | `10-live-build.md` | Live build on `demo-phenotyping/`: the daylight-saving trap | 2 | 01, 02, 04, 05, 06 |
| 17:40 | `20-hands-on.md` | Pairs in breakout rooms, driver + skeptic, four quests to a pull request in a challenge repo | 2 | 03, 08 |
| 18:15 | `30-review-hunt.md` | Pairs hunt five problems in an AI-written analysis | 2 | 02, 08 |
| 18:35 | `40-hack.md` | Two paths (own tools / HPE environment), team repository rules, data rules, before 6 Nov | 3 | 05, 09 |
| 18:50 | `50-your-place.md` | Room's poll results vs. voices from the field · back to the opening question · close | 1 | 11 |

Pre-work (sent with the announcement): DePasquale, *Models at the speed of thought*,
*The Transmitter*, 16 Jun 2026 (~17 min) + course modules 01–04 + vote on challenges.
Install (module 07) is optional: participants without tools are covered at the hack.

## Files

| Path | What |
|---|---|
| `_header.md` | Marp front matter and the FacMed Hack design system (tokens from the hack website) |
| `[0-9][0-9]-*.md` | The modules, in order. **Edit these** |
| `build.sh` | `./build.sh --pdf` → `slides.md` (generated), `slides.html`, `slides.pdf` |
| `zoom_polls.md` | The six polls, ready to enter in Zoom |
| `demo-phenotyping/` | Synthetic sleep · steps · mood dataset (40 participants, across the 25 Oct clock change), the agent-written `analysis.py` for the review hunt, facilitator script, `ANSWER_KEY.md` |
| `assets/` | Partner logos |

Speaker notes (talking points, facilitator moves, sources) are HTML comments under each slide
banner: they show in the presenter view and PPTX notes, never on the projected slide.

## Before the session

- Create the six Zoom polls (`zoom_polls.md`); enable breakout rooms.
- Pick the hands-on fallback: challenge repositories open to participants, or the demo only.
- **[CONFIRM]** where participants send their GitHub username; the challenge-voting link; whether
  team repositories are private or public (implementation plan says private, handbook says
  public: slides say "in the hack's GitHub organisation").
- Dry-run the live build once with the agent you will use (`demo-phenotyping/README.md`).

## Sources

DePasquale (2026), *The Transmitter*, doi:10.53053/FVAU9567 · METR (2025), "Measuring the impact of
early-2025 AI on experienced open-source developer productivity" · Tao (2026), "Math 2.0",
terrytao.wordpress.com · course modules 01–11 and their sources (`../../modules/11-close.md`).
