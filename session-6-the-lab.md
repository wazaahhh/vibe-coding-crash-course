---
marp: true
theme: default
paginate: true
header: 'Vibe Coding for Scientists'
footer: 'CC BY-NC 4.0 · Thomas Maillart'
---

<!-- Render with Marp: `marp session-6-the-lab.md`. Session 6 of 6 — see COURSE.md. -->

<style>
section::after {
  content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}
</style>

<!-- _class: lead -->

# Session 6 · The lab & the responsibility

### When generation is cheap, the real work is review, standards & rhythm

---

# How a lab works in the age of vibe coding

1. **Peer review matters *more*** — no AI-generated analysis reaches a paper without a second human reading it. Review the *reasoning and checks*, not just that it runs.
2. **Shorter sprints, visible demos** — end each cycle with a show-and-tell: what you vibe-coded **and how you verified it.**
3. **Pair on the prompts** — one drives, one plays skeptic in real time.
4. **Share conventions** — a lab `CONVENTIONS.md` / `CLAUDE.md` + pinned environments, so output is consistent and reproducible.
5. **Mentor on judgment, not syntax** — onboarding gets easier; teaching taste and verification gets more important.

> When generation is cheap, the lab's real work is **review, standards, and rhythm.**

---

# Keep your own voice

AI is trained on the **average of everything** → its default is **generic.** Lean on it uncritically and your work drifts to the mean.

- **Delegate the boilerplate; keep what carries meaning** — which question, which comparison, how it's told.
- **Direct toward *your* style** — *"match the conventions in this file."* Don't adopt the AI's.
- **Edit toward your voice** — the first output is a draft in someone else's handwriting; the last mile is where *you* go back in.

> Let it handle the boilerplate; keep the parts that are **you.**

---

<!-- _class: lead -->

# Safety & ethics

### Your name is on the paper

---

# Five rules

1. **Data confidentiality** — don't paste patient/unpublished/embargoed data into uncleared cloud tools.
2. **Reproducibility & provenance** — commit the code, pin versions, **keep the prompts**. "The AI wrote it" ≠ a methods section.
3. **Correctness is yours** — it fabricates methods, stats, citations. Verify anything that reaches a result.
4. **Disclosure & authorship** — disclose assistance; AI is not an author; check journal/funder policy.
5. **Skill atrophy** — keep enough fluency to *review*. Don't outsource judgment.

---

# Start Monday

Don't redesign your workflow. Pick **one** low-stakes thing.

1. **Today:** open a chat tool, paste a script you already trust, ask *"what would you improve, and why?"* Read the answer critically.
2. **This week:** fork the course repo · let an agent into **one** real analysis · make it harden a notebook into a rerunnable script.
3. **Every time:** keep the prompt, verify the number, re-derive the one step that matters.

> One real task beats ten demos. Low stakes, this week.

---

<!-- _class: lead -->

# Director, not author.

The AI brings **speed and breadth.**
You bring the **question, the judgment, the responsibility.**

### That division of labor *is* the skill.

Go practice it on something low-stakes this week.

---

# Further reading

For when you fork the repo and want to go deeper.

- **Nature (2026)** — *How to vibe code in science: early adopters share their tips.* The best survey of researchers actually doing this.
- **Nature (2026)** — *We vibe-coded a custom AI poetry lab. Here's how you can, too.* A concrete lab case study.
- **Scott Cunningham** — *Scott's Mixtape* / "Claude Code for Economists" — an economist documenting real agentic research workflows.
- **arXiv 2506.23253** — *Vibe coding: programming through conversation with AI.*
- **arXiv 2502.17348** — *How Scientists Use Large Language Models to Program.*

→ Full annotated list with links in **`RESOURCES.md`** in the repo.

---

# Sources

- Kahneman, D. (2011). *Thinking, Fast and Slow.* Farrar, Straus & Giroux.
- Parasuraman, R. & Manzey, D. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3).
- Rozenblit, L. & Keil, F. (2002). The misunderstood limits of folk science: an illusion of explanatory depth. *Cognitive Science*, 26(5).
- Slamecka, N. J. & Graf, P. (1978). The generation effect. *J. Experimental Psychology: Human Learning & Memory*, 4(6).
- Lee, H.-P. et al. (2025). The Impact of Generative AI on Critical Thinking. *CHI 2025*, Microsoft Research / CMU.
- Kosmyna, N. et al. (2025). Your Brain on ChatGPT: Accumulation of Cognitive Debt… *arXiv preprint* (MIT Media Lab).

<!-- Speaker: the Kosmyna study is a preprint with active methodological debate — cite it as suggestive, not settled. -->
