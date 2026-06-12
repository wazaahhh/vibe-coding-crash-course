---
marp: true
theme: default
paginate: true
header: 'Vibe Coding for Scientists'
footer: 'CC BY-NC 4.0 · Thomas Maillart'
---

<!-- Render with Marp: `marp session-2-the-mindset.md`. Session 2 of 6 (20 min) — see COURSE.md. -->

<style>
section::after {
  content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}
</style>

<!-- _class: lead -->

# Session 2 · The mindset

### Why this isn't just *faster typing*

When **you** write code, understanding comes for free. When you **direct** an AI, it doesn't — you have to *choose* to engage it. The four pillars make the new loop safe.

---

# Pillar 1 — Divergence / creativity

- Science trains **convergence**: narrow to the one right method.
- Vibe coding rewards **divergence first**: generation is nearly free, so generate many.
- **Do:** *"Give me three approaches, with trade-offs."* Curate, don't produce.
- Divergence is the **search**; convergence is the **selection**. You still converge — later, with more on the table.

---

# Pillar 2 — Critical thinking *(the non-negotiable)*

- The model is **confident, fluent, and occasionally fabricating** — in flawless prose.
- **Reviewer stance:** every output is a PR from a brilliant, overconfident intern.
- Ask **"How would I know if this is wrong?"** *before* trusting the pretty plot.
- Tactics: explain its reasoning · argue against itself · check vs. a back-of-envelope · run a case you know.

> Trust the vibe to **write** it; never trust the vibe that it's **right**.

---

# Pillar 3 — Thinking fast / slow

> "System 1 is gullible and biased to believe, System 2 is in charge of doubting and unbelieving — but System 2 is sometimes busy, and often **lazy**." — *Kahneman, Thinking, Fast and Slow*

- The AI is your **System 1**: fast, fluent, sometimes wrong.
- **You** supply **System 2**: slow, deliberate, checking.
- Failure mode: speed seduces you into skipping System 2 — which is lazy by default.

> The more the result matters, the more slowly you must read it.

---

# Pillar 4 — Try and fail

- Generation is cheap → **more attempts, smaller stakes.**
- Prototype to throw away. Fork, branch, experiment, delete.
- Failure costs **minutes, not a day** → failure becomes the **unit of search.**
- Keep prototypes disposable and version-controlled. Git is your safety net.

---

# What the science says

The pillars counter **measured** cognitive effects:

- **Automation bias** — we over-trust automated output and stop checking. *(Parasuraman & Manzey, 2010)*
- **Cognitive offloading** — the more you trust GenAI, the less you think critically. *(Lee et al., CHI 2025)*
- **Illusion of explanatory depth** — fluent output makes you *feel* you understand what you couldn't rebuild. *(Rozenblit & Keil, 2002)*
- **Cognitive debt / generation effect** — you retain what you *produce*, not what you read. *(Kosmyna 2025 — preprint; Slamecka & Graf, 1978)*

> Offload the typing. **Never offload the understanding** your name depends on.

---

# Where it shines · where it bites

Verifying *everything* is exhausting. Spend your System 2 where it fails.

| ✅ Trust-but-skim | ⚠️ Slow down — it fails quietly here |
|---|---|
| Plotting, formatting, refactoring | **Domain correctness** — units, signs, edge cases |
| Boilerplate, glue, file I/O | **Statistics** — the wrong-but-plausible test |
| Explaining unfamiliar code | **Novel math / your specific method** |
| Translating between languages | **Anything needing ground truth** — data, citations |

> It's strongest on **syntax**, weakest on **truth.**

---

# A 30-second horror story

The failure is never a crash — it's a **green run with a wrong number.**

- A **sign flip** in a loss term: trains fine, looks plausible, effect **reversed.**
- **`df.dropna()`** quietly deletes 40% of rows → "significance" from survivors only.
- **Test data leaks** into training → 0.98 accuracy that evaporates on real data.

Every one of these **ran perfectly.** That's the whole point.

> The bug that ends a paper compiles, runs, and looks beautiful.

---

# Which pillar is hardest for *you*?

🙋 Divergence  ·  🙋 Critical thinking  ·  🙋 Slowing down  ·  🙋 Failing fast

<!-- Speaker: quick hands-up poll. Usually #2 and #3. Then move straight to Session 3. -->

---

<!-- _class: lead -->

# Next · Session 3

### How you actually do it — modes, prompting, and a live demo
