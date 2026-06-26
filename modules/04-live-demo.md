<!-- _class: lead -->

# 4 · Live demo

### Fork the repo → vibe-code a real analysis

`github.com/wazaahhh/vibe-coding-crash-course` → **Fork it**

★ Support this course → star it, fork it, open a PR

---

# Where we've been — and what's next

**Covered so far**
- **01 · Why it matters** — author → director.
- **02 · The mindset** — four pillars; you are System 2.
- **03 · How you actually do it** — chat vs. agent; intent is the lever.

**This module · 04 — Live demo**
- A **deliberately messy** dataset
- The **demo arc**, live — six moves
- The **unit-bug set-piece** — catch what the AI misses

---

# The scenario — a dataset that's messy on purpose

`demo/data/plant_growth.csv` — **does fertilizer affect plant height, controlling for light?**

- **Missing values** in `height_cm` and `light_hours`.
- ⚠️ A **unit inconsistency** — 4 rows in millimetres, 10× too large. The AI calls them "outliers." *You* know they're a unit bug. **This is the centerpiece.**
- One implausible **outlier** (data-entry typo) + **inconsistent labels** (`fertilizer` vs `Fertilizer`).

> The traps teach the mindset — you catch them because you know plants, not pandas.

---

# Demo arc

1. **Orient by asking, not reading** — "brief me on this dataset's problems."
2. **Watch it miss the unit bug** — the moment of the demo.
3. **Fix with domain knowledge** — mm vs cm; show me what you changed.
4. **Diverge** — three ways to test the effect, with assumptions.
5. **Notebook *or* script?** — explore in a notebook, harden into a script.
6. **Slow down at the claim** — "What would make this conclusion wrong?"

---

# The set-piece — it misses the one that matters

It gives a **confident, mostly-right** answer:

- ✅ 6 missing values in `height_cm` · ✅ 3 missing in `light_hours`
- ⚠️ "4 extreme outliers (> 200) — recommend dropping" → **wrong: those are mm, not cm.**

Dropping them would throw away real plants and bias the estimate. The fix is **domain knowledge:** *"some heights are in mm — detect and convert; show me the rows."*

> Mostly-right is the **dangerous** kind of wrong.

---

# Notebook or not?

| Notebook | Script + agent |
|---|---|
| Great for **exploration** | Great for **reproducibility** |
| See each step, plots inline | Reruns clean from scratch |
| ⚠️ hidden state, out-of-order cells | AI runs, reads errors, self-fixes |

**Recommendation:** explore in a notebook → *"harden this into a script I can rerun from scratch."* Get both.

---

# End of Module 4 — recap, discussion &amp; support

**Module 04 recap — Live demo**
- Forked the repo and worked a **deliberately messy** dataset.
- Caught the **unit bug the AI missed**.
- Notebook to explore → **script to reproduce**.

**Open question — let's discuss:** *What's a "unit bug" hiding in your own data that only your domain knowledge would catch?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`
