# Vibe Coding for Scientists

### A crash course · the first six modules

From *writing* code to *directing* it.

★ **Support this course** → `github.com/wazaahhh/vibe-coding-crash-course`

<!-- Speaker: cold-open. Take a task from the room, vibe-code it live in 20s, run it. Then this slide. -->

---

# The first six modules

These are the **first six modules** — more are on the way.

| # | Module | ~min |
|---|---|---|
| 1 | Why it matters | 5 |
| 2 | The mindset + the science | 15 |
| 3 | How you actually do it (modes · prompting) | 10 |
| 4 | **Live demo** — a real analysis | 15 |
| 5 | Working together in a lab | 7 |
| 6 | Safety &amp; ethics | 5 |

<!-- Speaker: a map, not content. The demo is the centre of gravity; protect its 15 min. Two hands-on install fests (code · manuscript) sit between and after the talk modules. -->

---

# Learning objectives

Three things you'll be able to do:

1. **Understand why &amp; how to vibe code in science** — the author→director shift, the four pillars, and the cognitive science that makes the new loop safe.
2. **Use vibe coding for data science** — direct a real analysis end to end: clean messy data, diverge on methods, and catch the plausible-but-wrong result.
3. **Use vibe coding for manuscript writing** — draft, tighten, and revise alongside the AI while keeping your own voice and the claims your name depends on.

> One throughline: keep the understanding your name depends on.

---

# What "vibe coding" means

- You describe **what you want** in plain language; the model writes the code.
- Term popularized by **Andrej Karpathy (2025)** — "give in to the vibes."
- The honest version for scientists:
  > The vibe is in **how you produce** code — **not** in whether it's correct.
- Tool-agnostic: Claude Code, Cursor, Copilot, paste-into-chat — same loop underneath.

---

# In practice — one sentence in, a working analysis out

- **Genomics** — *"Here's my RNA-seq counts table — give me a volcano plot, label the top 10 genes by adjusted p-value."* → reads the CSV, runs the DE math, returns a labelled figure **+** the code.
- **Neuro / EEG** — *"Load this `.edf`, band-pass 8–12 Hz, plot alpha power per channel as a topomap."* → wires up MNE, filters, renders the scalp map.
- **Field / climate** — *"30 years of daily rainfall — fit a trend, test if it's significant, plot with a 12-month rolling mean."* → parses dates, fits + tests, plots.

> The question stays yours. The **plumbing** stops being the bottleneck.

---

# A real exchange — and catching what it gets wrong

**Task:** *"count fluorescent nuclei in every image in `data/dapi/`, output a CSV of counts per file."*

- It plans (threshold → watershed → count), writes `count_nuclei.py`, runs on 200 images → ✅ mean 47.3 nuclei/image.
- **You** notice dense clusters look undercounted → *"show me 3 overlays."* Touching nuclei had merged.
- You never wrote the segmentation code — you specified the outcome and **caught the plausible error.**

> Looking, doubting, correcting — that last step is the whole job.

---

# The thesis (we'll repeat this)

## You move from **author** of code to **director** of code.

Your job becomes **intent · judgment · verification** — not syntax.
