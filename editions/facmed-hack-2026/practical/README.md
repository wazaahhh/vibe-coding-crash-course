# Course folder

Crash Course #2 · FacMed Hack #1 · *Vibe Coding for Scientists*. One dataset all evening: a
fictional phone study, synthetic, so you may upload it to a chat AI.

| When | Part | What you do |
|---|---|---|
| 17:10 | Same data, your question | Read the codebook; answer in the live quiz: *what would you find worth exploring?* |
| 18:00 | Spot the trap | Vote in the live quiz on two analyses of this data; redo them yourself afterwards |
| 18:20 | Review hunt | Read an analysis an agent wrote on this data; post in the chat everything you would not sign |

## The phone study · `phone-study/`

150 students over 12 weeks: bedtime and wake-up, steps, GPS radius, screen time, calls and
messages, an evening mood rating, and PHQ-9 at weeks 0, 6 and 12. Codebook:
`phone-study/data/README.md`.

## Review hunt · `review-hunt/analysis.py`

An agent wrote `analysis.py` from the prompt at the top of the file. Read it with the codebook
and **list everything you would not put your name on**, and what tipped you off. Allowed: plots,
the codebook, a second AI, your judgment.

To run it: `python review-hunt/analysis.py` (needs `pandas` and `scikit-learn`).

## Redo it with an agent (after the session, or at the hack)

Open this folder in VS Code with an agent (Claude Code, Codex, GitHub Copilot, Cline), or ask your
agent to clone it. The agent reads `AGENTS.md` (Claude Code reads it through `CLAUDE.md`): it runs
**git** for you, explains each step, and waits for your OK. `NOTES.md` is where it records what was
verified and what was trusted.

- *"Compute hours slept per night and plot the average per night."* Is any night strange? Why?
- *"Plot the average evening mood per week. Who answers, and who doesn't?"*

Five prompts worth stealing:

1. *"Explain what this code does before you change anything."*
2. *"Outline your plan, then wait for my OK."*
3. *"Write a test that would fail if this result were wrong."*
4. *"What could make this conclusion wrong? Argue against yourself."*
5. *"Summarise in plain language what you changed and what you assumed."*

For git, just say it: *"start a branch"* · *"save my work"* · *"what changed?"* · *"undo that"* ·
*"send it to GitHub"*.
