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
