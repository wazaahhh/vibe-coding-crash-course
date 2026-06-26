<!-- _class: lead -->

# 2 · The mindset

### Why this isn't just *faster typing*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

---

# Where we've been — and what's next

**Covered so far**
- **01 · Why it matters** — author → director.

**This module · 02 — The mindset**
- The **four pillars** — diverge, think critically, fast/slow, try &amp; fail
- The **cognitive science** that makes the new loop safe
- Where it **shines vs. bites** — and keeping your own voice

---

# Why it's not a trivial adaptation

When **you** write code, understanding comes **for free** — as a byproduct.

When you **direct** an AI, understanding is **no longer automatic.** You have to *choose* to engage it.

→ Your **role** changes. Your **cognitive loop** changes. The four pillars are the disciplines that make the new loop safe.

---

# Pillar 1 — Divergence / creativity

- Science trains **convergence**: narrow to the one right method.
- Vibe coding rewards **divergence first**: generation is nearly free, so generate many.
- **Do:** *"Give me three approaches, with trade-offs."* Curate, don't produce.
- Divergence is the **search**; convergence is the **selection**. You still converge — later, with more on the table.

---

# Pillar 2 — Critical thinking

### The non-negotiable

- The model is **confident, fluent, and occasionally fabricating** — in flawless prose.
- **Reviewer stance:** every output is a PR from a brilliant, overconfident intern.
- Ask **"How would I know if this is wrong?"** *before* trusting the pretty plot.

> Trust the vibe to **write** it; never trust the vibe that it's **right**.

---

# Pillar 3 — Thinking fast / slow

> "System 1 is gullible and biased to believe; System 2 is in charge of doubting — but System 2 is often **lazy**."
> — *Daniel Kahneman*

- The AI is your **System 1**: fast, fluent, sometimes wrong.
- **You** supply **System 2**: slow, deliberate, checking.

> The more the result matters, the more slowly you must read it.

---

# Pillar 4 — Try and fail

- Generation is cheap → **more attempts, smaller stakes.**
- Prototype to throw away. Fork, branch, experiment, delete.
- Failure costs **minutes, not a day** → failure becomes the **unit of search.**
- Keep prototypes disposable and version-controlled. Git is your safety net.

---

# What the science says — the brain on autopilot

- **Automation bias &amp; complacency** — we over-trust automated output and stop checking it. *(Parasuraman &amp; Manzey, 2010)*
- **Cognitive offloading → less critical thinking** — the more workers trust GenAI, the less critical thinking they report. *(Lee et al., CHI 2025)*
- **Illusion of explanatory depth** — fluent output makes you *feel* you understand a system you couldn't rebuild. *(Rozenblit &amp; Keil, 2002)*

> The danger isn't a wrong answer. It's a **confident** one that **switches your checking off.**

---

# What the science says — protecting your edge

- **"Cognitive debt"** — heavy LLM use during writing showed reduced neural connectivity, weaker memory of one's own output, and more homogenized prose. *(Kosmyna et al., MIT Media Lab, 2025 — preprint)*
- **Generation effect** — you understand and retain far better what *you* produce than what you merely read. Directing ≠ generating. *(Slamecka &amp; Graf, 1978)*

> Offload the typing. **Never offload the understanding** that your name depends on.

---

# Where it shines · where it bites

| ✅ Trust-but-skim | ⚠️ Slow down — it fails quietly here |
|---|---|
| Plotting, formatting, refactoring | **Domain correctness** — units, sign conventions, edge cases |
| Boilerplate, glue, file I/O | **Statistics** — the wrong-but-plausible test |
| Explaining unfamiliar code | **Novel math / your specific method** |
| Translating between languages | **Anything needing ground truth** — data semantics, citations |

> Strongest on **syntax**, weakest on **truth.**

---

# A 30-second horror story

The failure is never a crash — it's a **green run with a wrong number.**

- A **sign flip** in a loss term → plausible curve, reversed effect.
- **`df.dropna()`** silently deletes 40% of rows.
- **Test data leaks** into training → 0.98 that evaporates.
- A **hallucinated citation** no reviewer caught — until one did.

> The bug that ends a paper compiles, runs, and looks beautiful.

---

# Which pillar is hardest for *you*?

🙋 Divergence  ·  🙋 Critical thinking  ·  🙋 Slowing down  ·  🙋 Failing fast

<!-- Speaker: quick hands-up poll. Usually #2 and #3 — exactly the ones the demo will tempt them to skip. -->

---

# Keep your own voice

AI is trained on the **average of everything** → its default is **generic.**

- **Delegate boilerplate; keep what carries meaning** — which question, which comparison, how it's told.
- **Direct toward *your* style:** *"match the conventions in this file."*
- The first output is a draft in someone else's handwriting — the last mile is where *you* go back in.

> Let it handle the boilerplate; keep the parts that are **you.**

---

# End of Module 2 — recap, discussion &amp; support

**Module 02 recap — The mindset**
- Four pillars — **diverge, critical thinking, fast/slow, try &amp; fail**.
- The AI is System 1; **you're System 2**.
- Strong on syntax, **weak on truth** — aim your checking.

**Open question — let's discuss:** *Which pillar are you most likely to skip under deadline pressure — and how would you catch yourself?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`
