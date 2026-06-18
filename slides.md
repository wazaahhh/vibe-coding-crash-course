---
marp: true
theme: default
paginate: true
header: 'Vibe Coding for Scientists'
footer: 'CC BY-NC 4.0 · Thomas Maillart'
---

<!-- Render with Marp: `marp slides.md` (HTML/PDF/PPTX), or open in VS Code with the Marp extension. -->

<style>
/* Page numbering as "x / total" (Marp exposes the total via data attribute) */
section::after {
  content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}
</style>

# Vibe Coding for Scientists

### A 60-minute crash course

From *writing* code to *directing* it.

★ **Support this course** → `github.com/wazaahhh/vibe-coding-crash-course`

<!-- Speaker: cold-open. Take a task from the room, vibe-code it live in 20s, run it. Then this slide. -->

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

---

# The first six modules

These are the **first six modules** — more are on the way.

| # | Module | ~min |
|---|---|---|
| 1 | Why it matters | 5 |
| 2 | The mindset + the science | 15 |
| 3 | How you actually do it (modes · prompting) | 10 |
| 4 | **Live demo** — a real analysis | 15 |
| 🛠 | **Install fest** — set up your repo *(hands-on)* | clinic |
| 5 | Working together in a lab | 7 |
| 6 | Safety &amp; ethics | 5 |

<!-- Speaker: don't dwell — this is a map, not content. The demo is the centre of gravity; protect its 15 min. The install fest is a hands-on clinic (its own deck) run right after the demo. -->

---

# Learning objectives

By the end, you'll be able to:

1. **Understand why &amp; how to vibe code in science** — the author→director shift, the four pillars, and the cognitive science that makes the new loop safe.
2. **Use vibe coding for data science** — direct a real analysis end to end: clean messy data, diverge on methods, and catch the plausible-but-wrong result.
3. **Use vibe coding for manuscript writing** — draft, tighten, and revise alongside the AI while keeping your own voice and the claims your name depends on.

> One throughline: keep the understanding your name depends on.

---

<!-- _class: lead -->

# 1 · Why it matters

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

---

# Why it matters — for *you*, specifically

You're not a professional programmer. Code is **friction** between a question and an answer.

1. **The bottleneck was never the science — it was the plumbing.**
   Hours of Stack-Overflow archaeology → minutes.
2. **Exploration becomes cheap.**
   Five model specs, three plots, two normalizations — in the time of one.
3. **It lowers the barrier for the whole lab.**
   The student who "can't code" can ship a working pipeline.

⚠️ It's also trivially easy to produce **plausible · beautiful · wrong**.

---

<!-- _class: lead -->

# Support this course ★

**Support the development of this course** on GitHub —
star it, fork it, open a pull request.

`github.com/wazaahhh/vibe-coding-crash-course`

---

<!-- _class: lead -->

# 2 · The mindset

### Why this isn't just *faster typing*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

---

# Why it's not a trivial adaptation

When **you** write code, understanding comes **for free** — as a byproduct.

When you **direct** an AI, understanding is **no longer automatic.**
You have to *choose* to engage it.

→ Your **role** changes. Your **cognitive loop** changes.
The four pillars are the disciplines that make the new loop safe.

---

# Pillar 1 — Divergence / creativity

- Science trains **convergence**: narrow to the one right method.
- Vibe coding rewards **divergence first**: generation is nearly free, so generate many.
- **Do:** *"Give me three approaches, with trade-offs."* Curate, don't produce.
- Reframe: divergence is the **search**; convergence is the **selection**. You still converge — later, with more on the table.

---

# Pillar 2 — Critical thinking

### The non-negotiable

- The model is **confident, fluent, and occasionally fabricating** — in flawless prose.
- **Reviewer stance:** every output is a PR from a brilliant, overconfident intern.
- Ask **"How would I know if this is wrong?"** *before* trusting the pretty plot.
- Tactics: explain its reasoning · argue against itself · check vs. a back-of-envelope · run a case you know.

> Trust the vibe to **write** it; never trust the vibe that it's **right**.

---

# Pillar 3 — Thinking fast / slow

> "System 1 is gullible and biased to believe, System 2 is in charge of doubting and unbelieving — but System 2 is sometimes busy, and often **lazy**."
> — *Daniel Kahneman, Thinking, Fast and Slow*

- The AI is your **System 1**: fast, fluent, sometimes wrong.
- **You** supply **System 2**: slow, deliberate, checking.
- Failure mode: speed seduces you into skipping System 2 — and System 2 is lazy by default.
- Discipline: **fast on generation, slow on consequential checkpoints.**

> The more the result matters, the more slowly you must read it.

---

# Pillar 4 — Try and fail

- Generation is cheap → **more attempts, smaller stakes.**
- Prototype to throw away. Fork, branch, experiment, delete.
- Failure costs **minutes, not a day** → failure becomes the **unit of search.**
- Keep prototypes disposable and version-controlled. Git is your safety net.

---

# What the science says — the brain on autopilot

The pillars aren't moralizing — they counter **measured** cognitive effects:

- **Automation bias &amp; complacency** — we over-trust automated output and stop checking it; errors of *omission* (missed) and *commission* (followed a wrong suggestion). *(Parasuraman &amp; Manzey, 2010)*
- **Cognitive offloading → less critical thinking** — the more workers trust GenAI, the less critical thinking they report. *(Lee et al., Microsoft/CMU, CHI 2025)*
- **Illusion of explanatory depth** — fluent output makes you *feel* you understand a system you couldn't actually rebuild. *(Rozenblit &amp; Keil, 2002)*

> The danger isn't a wrong answer. It's a **confident** one that **switches your checking off.**

---

# What the science says — protecting your edge

- **"Cognitive debt"** — heavy LLM use during writing showed reduced neural connectivity, weaker memory of one's own output, and more homogenized prose. *(Kosmyna et al., MIT Media Lab, 2025 — preprint)*
- **Generation effect** — you understand and retain far better what *you* produce than what you merely read. Directing ≠ generating. *(Slamecka &amp; Graf, 1978)*

**The discipline:** re-derive the key step yourself · explain the code back without the model · keep enough fluency to *review*, not just accept.

> Offload the typing. **Never offload the understanding** that your name depends on.

---

# Where it shines · where it bites

Verifying *everything* is exhausting. Spend your System 2 where it fails.

| ✅ Trust-but-skim | ⚠️ Slow down — it fails quietly here |
|---|---|
| Plotting, formatting, refactoring | **Domain correctness** — units, sign conventions, edge cases |
| Boilerplate, glue, file I/O | **Statistics** — the wrong-but-plausible test |
| Explaining unfamiliar code | **Novel math / your specific method** |
| Translating between languages | **Anything needing ground truth** — data semantics, citations |

> It's strongest on **syntax**, weakest on **truth.** Aim your checking accordingly.

---

# A 30-second horror story

The failure is never a crash — it's a **green run with a wrong number.**

- A **sign flip** in a loss term: the model trains, the curve looks plausible, the effect is **reversed.**
- **`df.dropna()`** quietly deletes 40% of rows → a "significant" result from survivors only.
- **Test data leaks** into training → 0.98 accuracy that evaporates on real data.
- A **hallucinated citation** in the intro that no reviewer caught — until one did.

Every one of these **ran perfectly.** That's the whole point.

> The bug that ends a paper compiles, runs, and looks beautiful.

---

# Which pillar is hardest for *you*?

🙋 Divergence  ·  🙋 Critical thinking  ·  🙋 Slowing down  ·  🙋 Failing fast

<!-- Speaker: quick hands-up poll. Usually #2 and #3. Emphasize those before the demo — it's where they'll be tempted to skip both. -->

---

# Keep your own voice

AI is trained on the **average of everything** → its default is **generic.**
Lean on it uncritically and your work drifts to the mean.

- **Style vs. boilerplate:** delegate the boilerplate; keep the parts that carry meaning (which question, which comparison, how it's told).
- **Direct toward *your* style:** *"match the conventions in this file."* Don't adopt the AI's.
- **Edit toward your voice:** the first output is a draft in someone else's handwriting. The last mile is where *you* go back in.
- **Keep your hands in** — retain the taste that lets you notice when output is bland.

> Let it handle the boilerplate; keep the parts that are **you.**

---

<!-- _class: lead -->

# Support this course ★

**Support the development of this course** on GitHub —
star it, fork it, open a pull request.

`github.com/wazaahhh/vibe-coding-crash-course`

---

<!-- _class: lead -->

# 3 · How you actually do it

### Two modes — same loop underneath

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

---

# Mode A: chat · Mode B: agent in your repo

| **Chat** (browser / app) | **Agent** (VS Code + GitHub) |
|---|---|
| ChatGPT, Claude.ai — paste code, data, error → get an answer | Claude Code, Cursor, Copilot — AI **reads your files, runs code, edits in place** |
| **Zero setup**, works in 10 seconds | One-time setup: clone repo, open editor, connect |
| ⚠️ **You** are the copy-paste bus — context dies each message | **Context-aware** — sees the whole project, remembers |
| Great for a quick question or snippet | Great for a real, multi-file analysis |

Most scientists start in **chat** (and that's fine). The leap in power is letting the AI **into the repo.**

---

# Mode B, done right: one repo for everything

Put **code · data · figures · the paper · your prompts/notes** in **one repository** (a *monorepo*).

- **The AI sees the whole picture** → answers grounded in *your* data and *your* draft, not a generic guess.
- **One source of truth** → the analysis that made Figure 3 lives next to Figure 3 and the paragraph that cites it.
- **Reproducible &amp; shareable** → a collaborator (or reviewer, or future-you) clones *one thing* and has it all.
- Add a **`CLAUDE.md` / `CONVENTIONS.md`** at the root → the agent (and the lab) follow the same rules.

> Chat answers a question. A repo lets the AI **work on your actual project.**

---

# Why GitHub, specifically

Beyond "the AI sees everything," a repo gives you:

- **Version history** — every change is reversible; nothing is ever truly lost.
- **Branches** — try a risky reanalysis in isolation; keep it only if it works.
- **Diffs & pull requests** — *see* exactly what changed, and review it (yours or a collaborator's).
- **Issues** — a lightweight to-do / bug list living next to the work.
- **Remote backup + sharing** — your laptop dies, the work doesn't; share one URL.
- **Provenance & release** — tag the exact version behind a paper; mint a **DOI via Zenodo**.

> Git turns `final_v3_REALLY_final.py` into a **history you can trust.**

---

# How to ask — the *intent* half of the job

A vague prompt gets a generic answer. Direct it like a capable new student.

- **Give context, not just the task** — the data, the goal, the constraints, what you've tried.
- **Ask for a plan *before* code** — *"Outline your approach first; I'll approve, then you write it."*
- **Constrain it** — language, libraries, "match the style in this file," "no new dependencies."
- **Make it show its work** — *"explain your reasoning,"* *"flag anything you assumed."*
- **Iterate in small steps** — one change, run, read, correct. Don't accept a 300-line dump blind.

> Vague in → generic out. **Specific intent is the lever** that makes everything downstream better.

---

<!-- _class: lead -->

# Support this course ★

**Support the development of this course** on GitHub —
star it, fork it, open a pull request.

`github.com/wazaahhh/vibe-coding-crash-course`

---

<!-- _class: lead -->

# 4 · Demo

### Fork the repo → vibe-code a real analysis

`github.com/wazaahhh/vibe-coding-crash-course`  → **Fork it**

★ Support this course → star it, fork it, open a PR

---

# The scenario — a dataset that's messy on purpose

`demo/data/plant_growth.csv` — **does fertilizer affect plant height, controlling for light?**

- **Missing values** in `height_cm` and `light_hours`.
- ⚠️ A **unit inconsistency** — 4 rows in millimetres, 10× too large. The AI calls them "outliers." *You* know they're a unit bug.
- One implausible **outlier** (data-entry typo) + **inconsistent labels** (`fertilizer` vs `Fertilizer`).

> The traps teach the mindset — you catch them because you know plants, not pandas.

---

# Demo arc

1. **Orient by asking, not reading** — "brief me on this dataset's problems."
2. **Watch it miss the unit bug** ← the moment of the demo.
3. **Fix with domain knowledge** — mm vs cm; show me what you changed.
4. **Diverge** — three ways to test the effect, with assumptions.
5. **Notebook *or* script?** — explore in a notebook, harden into a script.
6. **Slow down at the claim** — "What would make this conclusion wrong?"

---

# Notebook or not?

| Notebook | Script + agent |
|---|---|
| Great for **exploration** | Great for **reproducibility** |
| See each step, plots inline | Reruns clean from scratch |
| ⚠️ hidden state, out-of-order cells | AI runs, reads errors, self-fixes |

**Recommendation:** explore in a notebook → *"harden this into a script I can rerun from scratch."* Get both.

---

<!-- _class: lead -->

# 🛠 Install Fest — build it on *your* laptop

### Now that you've seen it, set up the real thing

→ open **`install-fest.md`** *(hands-on clinic, ~45–60 min)*

Four browser tabs → **one VS Code workspace**: Claude Code in the editor, a code + LaTeX monorepo, **Overleaf and Zotero bridged in**, data kept untracked.

---

<!-- _class: lead -->

# 5 · Working together in a lab

### When generation is cheap, the real work is review, standards &amp; rhythm

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

---

# How a lab works in the age of vibe coding

1. **Peer review matters *more*** — no AI-generated analysis reaches a paper without a second human reading it. Review the *reasoning and checks*, not just that it runs.
2. **Shorter sprints, visible demos** — end each cycle with a show-and-tell: what you vibe-coded **and how you verified it.**
3. **Pair on the prompts** — one drives, one plays skeptic in real time.
4. **Share conventions** — a lab `CONVENTIONS.md` / `CLAUDE.md` + pinned environments, so output is consistent and reproducible.
5. **Mentor on judgment, not syntax** — onboarding gets easier; teaching taste and verification gets more important.

> When generation is cheap, the lab's real work is **review, standards, and rhythm.**

---

# Working in a shared repo — the constraints

A repo is a contract. Collaboration adds friction worth planning for:

- **Git has a learning curve** — not every co-author will `branch` and `merge`. Agree on a simple flow: branch → pull request → review.
- **Merge conflicts** — two people editing the same lines. Small, frequent commits hurt less than big rare ones.
- **Binaries don't diff** — Word docs, `.xlsx`, figures bloat history and can't be merged. Keep the paper in **plain text (LaTeX/Markdown)** so changes are reviewable.
- **Data still doesn't belong in git** — share it out-of-band (drive, S3, DVC); keep the repo to **code + text**.
- **Access & secrets** — private repos for unpublished work; never commit keys (`.env` in `.gitignore`).

> The repo rewards **plain text and small commits** — and punishes binaries and big data.

---

# "But my co-authors live in Overleaf"

The most common blocker. You don't have to drag anyone out — **bridge Overleaf to the repo.**

- Overleaf → **Menu → GitHub → Link to GitHub**: syncs the project to a GitHub repo, **both ways**.
- Co-authors keep editing in **Overleaf**; you **pull** into VS Code, let the agent work, **push** back.
- No premium? Overleaf's **Git bridge** (`git.overleaf.com/<id>`) does the same with plain `git`.

> Everyone keeps their tool. The manuscript becomes **one synced source** the AI can also edit. *(Full setup in the install fest.)*

---

<!-- _class: lead -->

# Support this course ★

**Support the development of this course** on GitHub —
star it, fork it, open a pull request.

`github.com/wazaahhh/vibe-coding-crash-course`

---

<!-- _class: lead -->

# 6 · Safety &amp; ethics

### Your name is on the paper

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

---

# Five rules

1. **Data confidentiality** — don't paste patient/unpublished/embargoed data into uncleared cloud tools.
2. **Reproducibility &amp; provenance** — commit the code, pin versions, **keep the prompts**. "The AI wrote it" ≠ a methods section.
3. **Correctness is yours** — it fabricates methods, stats, citations. Verify anything that reaches a result.
4. **Disclosure &amp; authorship** — disclose assistance; AI is not an author; check journal/funder policy.
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

- Kahneman, D. (2011). *Thinking, Fast and Slow.* Farrar, Straus &amp; Giroux.
- Parasuraman, R. &amp; Manzey, D. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3).
- Rozenblit, L. &amp; Keil, F. (2002). The misunderstood limits of folk science: an illusion of explanatory depth. *Cognitive Science*, 26(5).
- Slamecka, N. J. &amp; Graf, P. (1978). The generation effect. *J. Experimental Psychology: Human Learning &amp; Memory*, 4(6).
- Lee, H.-P. et al. (2025). The Impact of Generative AI on Critical Thinking. *CHI 2025*, Microsoft Research / CMU.
- Kosmyna, N. et al. (2025). Your Brain on ChatGPT: Accumulation of Cognitive Debt… *arXiv preprint* (MIT Media Lab).

<!-- Speaker: the Kosmyna study is a preprint with active methodological debate — cite it as suggestive, not settled. -->

---

<!-- _class: lead -->

# Support this course ★

These are the **first six modules** — more are on the way.
**Support the development of this course** on GitHub: star it, fork it, open a pull request.

`github.com/wazaahhh/vibe-coding-crash-course`
