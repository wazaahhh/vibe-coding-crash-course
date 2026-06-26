---
marp: true
theme: default
paginate: true
header: 'Vibe Coding for Scientists'
footer: 'CC BY-NC 4.0 · Thomas Maillart'
---

<!-- Render with Marp: `marp slides.md`. slides.md is GENERATED from modules/ by ./build.sh — edit the module files, then rebuild. -->

<style>
section::after { content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total); }
section pre { font-size: 0.72em; }
</style>

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


---

# Why it matters — for *you*, specifically

Code is **friction** between a question and an answer.

1. **The bottleneck was never the science — it was the plumbing.** Hours of Stack-Overflow archaeology → minutes.
2. **Exploration becomes cheap.** Five model specs, three plots, two normalizations — in the time of one.
3. **It lowers the barrier for the whole lab.** The student who "can't code" can ship a working pipeline.

⚠️ It's also trivially easy to produce **plausible · beautiful · wrong**.

---

# End of Module 1 — recap, discussion &amp; support

**Module 01 recap — Why it matters**
- You shift from **author** of code to **director** of code.
- Code is friction — exploration gets cheap, the whole lab's barrier drops.
- The risk: **plausible · beautiful · wrong**.

**Open question — let's discuss:** *If code stops being the bottleneck, what becomes the new scarce skill in your lab?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`


---

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


---

<!-- _class: lead -->

# 3 · How you actually do it

### Two modes — same loop underneath

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

---

# Where we've been — and what's next

**Covered so far**
- **01 · Why it matters** — author → director.
- **02 · The mindset** — four pillars; you are System 2.

**This module · 03 — How you actually do it**
- Two modes — **chat** vs. **agent in your repo**
- **One repo** for code, data, figures and the paper
- **How to ask** — prompting for intent

---

# Mode A: chat · Mode B: agent in your repo

| **Chat** (browser / app) | **Agent** (editor + repo) |
|---|---|
| Paste code, data, error → get an answer | AI **reads your files, runs code, edits in place** |
| **Zero setup**, works in 10 seconds | One-time setup: clone, open editor, connect |
| ⚠️ **You** are the copy-paste bus — context dies each message | **Context-aware** — sees the whole project, remembers |
| Great for a quick question or snippet | Great for a real, multi-file analysis |

Most scientists start in **chat**. The leap in power is letting the AI **into the repo.**

---

# Mode B, done right: one repo for everything

Put **code · data · figures · the paper · your prompts** in **one repository.**

- **The AI sees the whole picture** → answers grounded in *your* data and *your* draft.
- **One source of truth** → the analysis behind Figure 3 lives next to Figure 3.
- A root **`CLAUDE.md`** → the agent (and the lab) follow the same rules.

> Chat answers a question. A repo lets the AI **work on your actual project.**

---

# How to ask — the *intent* half of the job

Direct it like a capable new student.

- **Give context, not just the task** — the data, the goal, the constraints, what you've tried.
- **Ask for a plan *before* code** — *"outline your approach; I'll approve, then you write it."*
- **Constrain it** — language, libraries, "match the style in this file," "no new dependencies."
- **Make it show its work** — *"explain your reasoning; flag anything you assumed."*
- **Iterate in small steps** — one change, run, read, correct. Never accept a 300-line dump blind.

> Vague in → generic out. **Specific intent is the lever.**

---

# End of Module 3 — recap, discussion &amp; support

**Module 03 recap — How you actually do it**
- Two modes — **chat** vs. **agent in your repo**.
- **One repo** for code, data, figures and the paper.
- **Specific intent** is the lever.

**Open question — let's discuss:** *How can a junior student — who can't yet write the code — direct an AI efficiently and correctly?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`


---

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


---

<!-- _class: lead -->

# 🛠 Install fest · Code — your analysis workspace

### Get the agent into a real repo — code &amp; data

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

<!-- Speaker: hands-on clinic, not a lecture. Pair up — no one debugs alone. Don't rush it to a slot; installs set the pace. The manuscript setup (Overleaf → VS Code/GitHub) is the final module. -->

---

# Where we've been — and what's next

**Covered so far**
- **01 · Why it matters** — author → director.
- **02 · The mindset** — four pillars; you are System 2.
- **03 · How you actually do it** — chat vs. agent; intent is the lever.
- **04 · Live demo** — we caught the bug the AI missed.

**This module · 🛠 Install fest · Code**
- **Editor + agent** — VS Code, Git, your AI tool
- **One repo** — code &amp; data (data untracked)
- **First loop** — and push to GitHub

---

# Move 1 — editor + agent

```bash
# VS Code → code.visualstudio.com
#   + extensions: Python · your AI tool (Claude Code / Cursor / Copilot)

# Git + GitHub
git config --global user.name  "Your Name"
git config --global user.email "you@university.edu"

# Claude Code (needs Node 18+) — or use Cursor / Copilot
npm install -g @anthropic-ai/claude-code
```

✅ Check: run `claude` in a folder → *"list my files, don't change anything."* The agent can see the repo — the whole point.

---

# Move 2 — one repo for your analysis

```bash
mkdir my-project && cd my-project && git init
mkdir code data results
printf "data/\n!data/README.md\n.env\n" > .gitignore
```

```text
my-project/
├── CLAUDE.md      # house rules for the agent
├── code/          # analysis, notebooks
├── results/       # tables, figures, outputs
└── data/          # UNTRACKED — raw data stays local
```

> Track the **recipe**, not the **ingredients.** Big/private data never goes in git. *(We add `paper/` in the final module.)*

---

# Put it together — `CLAUDE.md`, first loop, push

A root **`CLAUDE.md`** keeps the agent consistent:

```markdown
# Conventions
- Python 3.11, pandas. Figures → results/.
- Never modify files in data/ (read-only). Plan before coding.
```

Then run one real loop and ship it:

```bash
claude   # "load data/…, clean it, plot X vs Y → results/, save a rerunnable script"
gh repo create my-project --private --source=. --push
```

✅ Check: the script reruns from scratch; the repo is on GitHub — and **`data/` is not.**

---

# End of Install fest · Code — recap, discussion &amp; support

**Install fest · Code recap**
- **One workspace:** editor + agent + a code / data **monorepo**.
- Data stays **untracked**; `CLAUDE.md` keeps the agent in line.
- Your analysis now reruns **clean from scratch**, on GitHub.

**Open question — let's discuss:** *What in your current data setup — where it lives, how big, how private — will be hardest to bring into one repo?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`


---

<!-- _class: lead -->

# 5 · Working together in a lab

### When generation is cheap, the real work is review, standards &amp; rhythm

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

---

# Where we've been — and what's next

**Covered so far**
- **01 · Why it matters** — author → director.
- **02 · The mindset** — four pillars; you are System 2.
- **03 · How you actually do it** — chat vs. agent; intent is the lever.
- **04 · Live demo** — we caught the bug the AI missed.
- **🛠 · Install fest · Code** — one repo, the agent inside it.

**This module · 05 — Working together in a lab**
- How a **lab works** when generation is cheap
- Why **peer review matters more**, not less
- Shared standards, provenance, and rhythm

---

# How a lab works in the age of vibe coding

1. **Peer review matters *more*** — no AI-generated analysis reaches a paper without a second human reading the *reasoning and checks*.
2. **Shorter sprints, visible demos** — show what you vibe-coded **and how you verified it.**
3. **Pair on the prompts** — one drives, one plays skeptic in real time.
4. **Share conventions** — a lab `CLAUDE.md` + pinned, shared environments.
5. **Mentor on judgment, not syntax** — onboarding gets easier; teaching taste gets more important.
6. **Track provenance as a team** — whose prompt, which model, what data version.

---

# The shift, in one line

## Peer review matters **more**, not less.

When code is cheap to produce and easy to trust, the failure mode is **unreviewed AI code flowing straight into results.**

---

# End of Module 5 — recap, discussion &amp; support

**Module 05 recap — Working together in a lab**
- **Peer review matters more**, not less.
- Shorter sprints, visible demos, pair on the prompts.
- Shared standards &amp; **provenance**.

**Open question — let's discuss:** *What would peer review of AI-assisted analysis actually look like in your group?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`


---

<!-- _class: lead -->

# 6 · Safety &amp; ethics

### Your name is on the paper

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

---

# Where we've been — and what's next

**Covered so far**
- **01 · Why it matters** — author → director.
- **02 · The mindset** — four pillars; you are System 2.
- **03 · How you actually do it** — chat vs. agent; intent is the lever.
- **04 · Live demo** — we caught the bug the AI missed.
- **🛠 · Install fest · Code** — one repo, the agent inside it.
- **05 · Working in a lab** — review, standards, rhythm.

**This module · 06 — Safety &amp; ethics**
- **Five non-negotiable rules** · what to **start Monday**

---

# Five rules

1. **Data confidentiality** — don't paste patient/unpublished/embargoed data into uncleared cloud tools.
2. **Reproducibility &amp; provenance** — commit the code, pin versions, **keep the prompts**. "The AI wrote it" ≠ a methods section.
3. **Correctness is yours** — it fabricates methods, stats, citations. Verify anything that reaches a result.
4. **Disclosure &amp; authorship** — disclose assistance; AI is not an author; check journal/funder policy.
5. **Skill atrophy** — keep enough fluency to *review*. Don't outsource judgment.

---

# Start Monday

Pick **one** low-stakes thing.

1. **Today:** paste a script you already trust into a chat tool — *"what would you improve, and why?"* Read it critically.
2. **This week:** fork the repo · let an agent into **one** real analysis · harden a notebook into a rerunnable script.
3. **Every time:** keep the prompt, verify the number, re-derive the one step that matters.

> One real task beats ten demos. Low stakes, this week.

---

# End of Module 6 — recap, discussion &amp; support

**Module 06 recap — Safety &amp; ethics**
- **Five rules** — confidentiality, provenance, correctness, disclosure, skill.
- **Start Monday**, low stakes.
- Correctness is yours — **your name is on the paper**.

**Open question — let's discuss:** *Where's the line between acceptable assistance and undisclosed authorship in your field?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`


---

<!-- _class: lead -->

# 🖋 Install fest · Manuscript — Overleaf → VS Code + GitHub

### Write the paper where the agent can help — without losing your co-authors

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

<!-- Speaker: the final hands-on module. Payoff: the manuscript joins the repo, so the agent can draft, revise, and keep numbers consistent. Pre-flight: a LaTeX distribution (~4 GB) downloaded ahead. -->

---

# Where we've been — and what's next

**Covered so far**
- **01–06** — why, mindset, doing it, the demo, the lab, safety.
- **🛠 · Install fest · Code** — code &amp; data in one repo.

**This module · 🖋 Install fest · Manuscript**
- **LaTeX in VS Code** — build locally
- **Overleaf ↔ GitHub** — keep co-authors where they are
- **Zotero → a live `.bib`**

---

# Add `paper/` to the repo

```bash
cd my-project
mkdir -p paper/figures
```

```text
my-project/
├── code/   results/   data/   (untracked)
└── paper/
    ├── main.tex      # the manuscript
    ├── refs.bib      # auto-exported from Zotero
    └── figures/      # your code writes plots here
```

> Same repo as your analysis → the figure in the paper is the figure your code made.

---

# LaTeX in VS Code

- Install a **LaTeX distribution** — MacTeX / MiKTeX / TeX Live *(it's big, ~4 GB — download ahead)*.
- Add the **LaTeX Workshop** extension → `paper/main.tex` builds **on save**, PDF preview side-by-side.
- No more "compile" button in a browser; it runs `latexmk` for you.

✅ Check: edit a word in `main.tex`, save, watch the PDF update.

---

# Overleaf → without losing your co-authors

Bring the manuscript over, and **keep Overleaf in sync** for everyone else.

- **Import once:** Overleaf → **Menu → Git** → `git clone https://git.overleaf.com/<id> paper` *(free plan: Download → Source zip)*.
- **Two-way sync:** Overleaf → **Menu → GitHub → Link to GitHub**. Co-authors edit in Overleaf; you **pull** in VS Code, let the agent work, **push** back.
- ⚠️ Sync is **manual** on Overleaf's side and can conflict — push often, keep the `.tex` plain.

> Everyone keeps their tool. One synced manuscript the **AI can edit too.**

---

# References — Zotero → a live `.bib`

1. Install the **Better BibTeX** plugin in Zotero.
2. Right-click your collection → **Export → Better BibTeX** → save as `paper/refs.bib`, tick **"Keep updated."**
3. In `main.tex`: `\addbibresource{refs.bib}` (biblatex) or `\bibliography{refs}`.

> Zotero stays your library; the repo gets an **always-fresh** `.bib` the AI and LaTeX both read.

---

# Now the agent can maintain the paper

With code, data, and the manuscript in one repo, a result change can **propagate**:

> *"I re-ran model 2 — update Table 3, the abstract number, and the figure; show me a diff."*

- The agent edits prose, regenerates figures, fixes quoted numbers — you **review the diff**.
- Keep numbers **computed, not typed** (`\input{coef.tex}`) so they can't silently drift.

> A paper is software: a new result is a **refactor** — propagate · diff · review · rebuild.

---

# End of Install fest · Manuscript — recap, discussion &amp; support

**Install fest · Manuscript recap**
- The manuscript joins the repo: **LaTeX in VS Code**, **Overleaf synced**, **Zotero → live `.bib`**.
- The agent can **draft, revise, and keep numbers consistent** — you review every diff.

**Open question — let's discuss:** *What's the one thing stopping your co-authors from a shared repo — and what's the smallest step past it?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`


---

<!-- _class: lead -->

# Director, not author.

The AI brings **speed and breadth.** You bring the **question, the judgment, the responsibility.**

### That division of labor *is* the skill.

Go practice it on something low-stakes this week.

---

# Further reading

- **Nature (2026)** — *How to vibe code in science: early adopters share their tips.*
- **Nature (2026)** — *We vibe-coded a custom AI poetry lab. Here's how you can, too.*
- **Scott Cunningham** — *Scott's Mixtape* · "Claude Code for Economists."
- **arXiv 2506.23253** — *Vibe coding: programming through conversation with AI.*
- **arXiv 2502.17348** — *How Scientists Use Large Language Models to Program.*

→ Full annotated list with links in **`RESOURCES.md`** in the repo.

---

# Sources

- Kahneman, D. (2011). *Thinking, Fast and Slow.* Farrar, Straus &amp; Giroux.
- Parasuraman, R. &amp; Manzey, D. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3).
- Rozenblit, L. &amp; Keil, F. (2002). The illusion of explanatory depth. *Cognitive Science*, 26(5).
- Slamecka, N. &amp; Graf, P. (1978). The generation effect. *J. Exp. Psychology*, 4(6).
- Lee, H.-P. et al. (2025). The Impact of Generative AI on Critical Thinking. *CHI 2025.*
- Kosmyna, N. et al. (2025). Your Brain on ChatGPT: Cognitive Debt. *arXiv preprint.*

<!-- Speaker: the Kosmyna study is a preprint with active debate — cite it as suggestive, not settled. -->

---

<!-- _class: lead -->

# The first six modules — more are on the way.

**Support the development of this course:** star it, fork it, open a pull request.

`github.com/wazaahhh/vibe-coding-crash-course`
