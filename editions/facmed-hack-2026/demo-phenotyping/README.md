# Demo — sleep, activity and mood (digital phenotyping)

The hands-on dataset for the FacMed Hack edition of *Vibe Coding for Scientists*: the same
pedagogy as [`demo/`](../../../demo/) (a dataset that is messy on purpose), on the kind of data
the hackathon works with. **Synthetic**: no real person is in it.

**Question:** does last night's sleep, and today's activity, predict today's mood?

| File | What |
|---|---|
| `data/` + [`data/README.md`](data/README.md) | 40 participants, 21 nights across the 25 Oct 2026 clock change: sleep, steps, EMA mood. **Read the codebook.** |
| `generate_data.py` | Regenerates `data/` (deterministic seed) |
| `analysis.py` | An analysis "written by an agent": runs cleanly, reads well. Used in the **review hunt** |
| `check_answers.py` · `ANSWER_KEY.md` | Facilitators only |

Requirements: Python 3 with `pandas`, `numpy`, `scikit-learn` (or let your agent install them).

## Live build (facilitator script, ~20 min)

Screen-shared on Zoom, in VS Code with an agent in the side panel. Say out loud which pillar each
move is.

1. **Orient by asking** (*fast*): "Brief me on the files in `data/` and the codebook. What
   problems do you see?" Read the answer; note what it does *not* mention.
2. **Plan before code** (*plan mode*): "Plan how you would compute sleep duration per night and
   relate it to next-day mood. Don't write code yet." Approve or correct the plan.
3. **Let it run** (*fast*): sleep duration per night, mean per night, a plot. It will likely
   subtract the two time columns.
4. **Slow down at the picture** (*slow*): the night of 24→25 Oct drops by an hour for everyone.
   Ask the room in the chat: *why?* Domain knowledge catches it: the clocks changed.
5. **Fix with intent**: "Times are Geneva wall-clock with no offset. Localise to
   Europe/Zurich, convert to UTC, then subtract. Show me the before/after for that night."
6. **Review and commit** (*git loop*): `git diff`, read it, commit with a message that says what
   was checked; add one line to `NOTES.md`: *verified: DST night by plot; trusted: pandas tz
   handling*. Open a pull request.

If the agent gets daylight saving right first time, say so: then show the naive version with
`python check_answers.py` (first block) and ask why it would have gone unnoticed.

## Review hunt (15 min in breakout rooms + 5 min debrief)

Pairs open `analysis.py` and `data/README.md`, run the script, and list everything they would
not sign. They post their list in the chat when the room closes. The answer key has five.
