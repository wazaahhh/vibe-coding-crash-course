# Vibe Coding for Scientists — One-Page Cheat Sheet

> **Director, not author.** The AI writes the code; you own the question, the judgment, and the result.

## The loop
1. **Describe** the goal in plain language (intent, inputs, what "done" looks like).
2. **Generate** — let the model write it. Go fast here.
3. **Read & verify** — slow down in proportion to how much the result matters.
4. **Iterate** — correct with domain knowledge; throw away and retry freely.

## The four disciplines
| Pillar | In one line | Try this prompt |
|---|---|---|
| **Divergence** | Generate many options before choosing | *"Give me 3 approaches to do X, with trade-offs."* |
| **Critical thinking** | Treat every output as a PR from an overconfident intern | *"How would I know if this is wrong? Argue against your own answer."* |
| **Fast / slow** | AI = System 1 (fast); you = System 2 (checking) | *"What assumptions did you make? What would make this conclusion wrong?"* |
| **Try & fail** | Cheap attempts, small stakes, disposable prototypes | *"Make a quick throwaway version so I can see if this is even worth doing."* |

## Good prompting moves for analysis
- **Brief me, don't make me squint:** *"Load this file, summarize the columns, and flag data-quality problems."*
- **Ask for reasoning:** *"Explain your choice of statistical test."*
- **Verify on a known case:** *"Run this on a tiny example where I know the answer is N."*
- **Harden it:** *"Turn this exploratory notebook into a script I can rerun from scratch."*

## Keep your own voice
AI's default output is **generic** (it's the average of everything). Don't let your work drift to the mean.
- **Delegate boilerplate; keep the meaning** — which question, which comparison, how the result is told.
- **Direct toward your style:** *"match the conventions in this file."* Don't adopt the AI's.
- **Edit toward your voice** — the first output is a draft in someone else's handwriting; the last mile is yours.
- **Keep your hands in** so you can still feel when output is bland or off.

## Working together in a lab
When generation is cheap, the scarce resources become **review, standards, and rhythm.**
- **Peer review matters more** — no AI-generated analysis reaches a paper without a second human reading it.
- **Shorter sprints + show-and-tells** — demo what you built *and how you verified it.*
- **Pair on prompts** — one drives, one plays skeptic.
- **Share conventions** — a lab `CONVENTIONS.md` / `CLAUDE.md` + pinned environments.
- **Mentor on judgment, not syntax** — and track provenance (whose prompt, which model, what data version).

## Notebook or script?
- **Notebook** → exploration (inline plots, poke at state). Beware hidden/out-of-order state — the reproducibility trap.
- **Script + agent** → reproducibility; the AI can run, read errors, and self-fix.
- **Best of both:** explore in a notebook, then have the AI harden it into a rerunnable script.

## Five safety rules (your name is on the paper)
1. **Don't leak data** — no patient/unpublished/embargoed data into uncleared cloud tools.
2. **Reproducibility** — commit the code, pin versions, keep the prompts (the prompt is part of your method).
3. **Correctness is yours** — it fabricates methods, stats, and citations fluently. Verify everything that reaches a claim.
4. **Disclose** — note AI assistance; AI is not an author; check journal/funder policy.
5. **Stay fluent** — keep enough skill to review what it writes.

---
**Remember:** *Trust the vibe to write it; never trust the vibe that it's right.*
