---
marp: true
theme: default
paginate: true
header: 'Vibe Coding for Scientists'
footer: 'CC BY-NC 4.0 · Thomas Maillart'
---

<!-- Render with Marp: `marp session-5-recursive-researcher.md`. Session 5 of 6 (20 min) — see COURSE.md. -->

<style>
section::after {
  content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}
section pre { font-size: 0.8em; }
</style>

# Session 5 · The Recursive Researcher

### One change, propagated — *a paper is software*

The single demo that turns skeptics into believers.

<!-- Speaker: if you can, do this live on a real repo. Change one number, watch it ripple. -->

---

# The moment that sells it

You re-run a regression with a fix — a clustered SE, a dropped outlier. The coefficient moves **0.12 → 0.09.** Now *everything downstream is stale*:

the abstract number · **Table 3** · the forest plot · the §4 interpretation · the robustness paragraph · **three SI tables.**

I described the new spec to the agent. It **re-ran** the regression, **updated** the table and figure, **rewrote** the interpretation and abstract, **propagated into the SI** — and handed me a **diff** of everything it touched.

> It didn't answer a question. It **maintained the document** like a codebase.

---

# Why this is *exactly* software engineering

A paper is a **dependency graph**, whether or not you draw it:

```
data → cleaning → regression → numbers → tables/figures
                                    ↓
                            claims in the text → abstract → SI
```

Change a node, and **everything downstream is now stale.** That's not a writing problem — it's a **rebuild** problem, and software engineers solved it decades ago.

---

# The analogy, line by line

| Software engineering | Your paper |
|---|---|
| Change a function's output | A new result / re-run regression |
| Call graph — who depends on this? | Which tables, claims, SI use this number |
| **Refactor** — propagate everywhere | Update every place the number appears |
| **Regression tests** — did anything break? | Do the numbers still agree across the paper? |
| **Build** (`make`) — recompile from source | Re-run pipeline: data → figures → PDF |
| **Diff / PR review** | Review the agent's changes before you accept |

> A new result is a **refactor.** Propagate · diff · review · rebuild.

---

# Why software came first

LLM use was **optimized for code first** — for good reasons:

- **Machine-checkable correctness** — compilers and tests give instant, ruthless feedback.
- **Mature tooling** — git, CI, `make`: the change-propagation machinery already existed.
- **Oceans of training data** — public code at a scale no other text has.

> A paper is **informal software**: the same dependency graph, weaker tooling. So we **bring the tooling to the paper.**

---

# Make your paper "buildable"

The agent can only propagate what it can **see** — so make the graph explicit:

- **One repo** — code, manuscript, and SI together (Session 4's monorepo).
- **Computed, not typed** — code writes `coef.tex`; the paper does `\input{coef.tex}`. *One source of truth* (the SE rule: DRY).
- **Generated tables/figures** — scripts emit `table3.tex`, `forest.pdf` into `paper/`.
- **A reproducible build** — one command: data → results → figures → PDF.

> If a number can only change by re-running code, it **can't silently lie.**

---

# The workflow with the agent

A good propagation prompt is a **refactor request**:

> *"I'm adding clustered SEs to Model 2. Re-run it, update Table 3, the coefficient quoted in §4.2, the abstract figure, and SI Tables S5–S6. Recompile. Show me a **diff** and list every number changed, old → new."*

- **Plan first**, then propagate. Small, reviewable steps.
- **Read the diff like a code review** — the System-2 checkpoint.
- **Recompile** and skim the PDF end to end.

---

# The discipline (don't skip this)

A refactor can go wrong two ways — both **your** job to catch:

- **Over-propagation** — it changes a number that should *not* move. The diff catches it.
- **Under-propagation** — it misses a dependency it couldn't see (a hand-typed number, the cover letter, a slide).

> The agent maintains the graph it can **see.** Make dependencies explicit, and **review every diff.** You are the reviewer of record.

---

<!-- _class: lead -->

# Treat your paper like a codebase.

A new result is a **refactor**: propagate · diff · review · rebuild.

A late data fix or a reviewer's new spec drops from a **dreaded week** to an **afternoon** — when the paper is buildable and you review every diff.

---

<!-- _class: lead -->

# Next · Session 6

### The lab & the responsibility — collaboration, standards, safety
