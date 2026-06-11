---
marp: true
theme: default
paginate: true
header: 'Vibe Coding Install Fest'
footer: 'CC BY-NC 4.0 · Thomas Maillart'
---

<!-- Render with Marp: `marp install-fest.md` (HTML/PDF/PPTX), or open in VS Code with the Marp extension. -->
<!-- This is a HANDS-ON deck: people follow along on their laptops. Go slow, leave commands on screen. -->

<style>
/* Page numbering as "x / total" (Marp exposes the total via data attribute) */
section::after {
  content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}
/* Keep code blocks readable on a projector */
section pre { font-size: 0.78em; }
</style>

# Vibe Coding Install Fest

### One repo. One editor. The AI inside it.

From **scattered tools** → a single VS Code workspace where the AI sees your **code, your paper, and your data.**

<!-- Speaker: this is a clinic, not a lecture. Everyone leaves with a working setup. Pair people up: no one debugs alone. -->

---

# Where we're headed

**Today:** ChatGPT tab · Claude app · Overleaf · Zotero — four silos, lots of copy-paste.

**By the end:** one project folder, opened in VS Code, with an AI agent that can read and edit all of it.

| Leaving behind (as your *only* tool) | Moving toward |
|---|---|
| Chat in a browser tab | **Claude Code** in VS Code — reads your files |
| Overleaf as the only home for the paper | **LaTeX in VS Code** — same `.tex`, version-controlled |
| Zotero as a separate island | Zotero → a **live `.bib`** inside the repo |
| Code / paper / data in different places | **One monorepo** (data stays untracked) |

> We're not deleting anything today. We're **building the new home** and moving in gently.

---

# The golden rule: don't burn the boats

This is a **gentle** migration. Keep your old tools running in parallel.

- Overleaf still works → we'll **sync**, not abandon, until you're comfortable.
- Zotero stays your library → we just **bridge** it into the repo.
- The chat app is still fine for quick questions → the repo is for *real work.*

> Migrate one project. Keep the rest as-is. Cut over only when the new way feels easier.

---

# Before you start — pre-flight

Big downloads are slow on shared WiFi. If you haven't already:

- **Create accounts:** [github.com](https://github.com) · an Anthropic/Claude account (Pro/Max or API).
- **Pre-download the heavy one:** a LaTeX distribution (≈4 GB) — *start this now, it runs in the background.*
  - macOS: **MacTeX** · Windows: **MiKTeX** · Linux: **TeX Live**
- Have your **laptop charger** and your **GitHub password / 2FA** handy.

<!-- Speaker: kick off the LaTeX install at the very start so it finishes by the time you reach the LaTeX slide. -->

---

# The four moves (the whole plan)

We'll do these in order. Each is independent — if one stalls, move on.

1. **Editor + agent** — VS Code + Git + Claude Code, authenticated.
2. **The repo** — one folder: `code · paper · data`, on GitHub, data untracked.
3. **Paper** — Overleaf → LaTeX compiling locally in VS Code.
4. **References** — Zotero → an auto-updating `refs.bib` in the repo.

Then: **`CLAUDE.md`** + your **first in-repo vibe loop.**

---

<!-- _class: lead -->

# Move 1 · Editor + agent

### VS Code · Git · Claude Code

---

# Step 1 — Install VS Code

Download from **[code.visualstudio.com](https://code.visualstudio.com)** and open it.

- macOS: drag to Applications. Then `Cmd+Shift+P` → *"Shell Command: Install 'code' in PATH"*.
- Install two extensions now (Extensions panel, `Cmd+Shift+X`):
  - **Python** (Microsoft)
  - **LaTeX Workshop** (James Yu) — we'll use it in Move 3.

✅ Check: a terminal (`Ctrl+` `` ` ``) opens inside VS Code.

---

# Step 2 — Git + GitHub

Git is your safety net and how the repo lives online.

```bash
# macOS: installs with Xcode tools, or `brew install git`
git --version

git config --global user.name  "Your Name"
git config --global user.email "you@university.edu"
```

Sign in to GitHub from VS Code: `Cmd+Shift+P` → **"Sign in to GitHub"**
(or install the **GitHub CLI** and run `gh auth login`).

✅ Check: `git --version` prints a number.

---

# Step 3 — Install Claude Code

Claude Code runs as a **VS Code extension** *and* a CLI. It needs **Node.js**.

```bash
# Node 18+ (macOS: `brew install node`, or nodejs.org installer)
node --version

# Install Claude Code
npm install -g @anthropic-ai/claude-code
```

Then add the **Claude Code** extension from the VS Code Marketplace.

> *Equivalents:* Cursor (standalone editor), Cline / Continue (VS Code extensions), GitHub Copilot agent mode. Same idea — pick one; the rest of today still applies.

---

# Step 4 — Authenticate & first run

In the VS Code terminal, inside any folder:

```bash
claude
```

- Follow the prompt to **log in** (`/login`) with your Claude account or API key.
- Try it: *"What files are in this folder? Don't change anything yet."*

✅ Check: Claude responds and can **list your files.** That means the agent can see the repo — the whole point.

---

<!-- _class: lead -->

# Move 2 · The repo

### One folder to hold it all

---

# Step 5 — Create the monorepo

```bash
mkdir my-project && cd my-project
git init
mkdir code paper data results
printf "# My Project\n" > README.md
```

One folder now holds **code, the paper, data, and results** — side by side, so the AI (and future-you) see the whole picture.

✅ Check: `ls` shows `code  paper  data  results  README.md`.

---

# The canonical layout

```text
my-project/
├── README.md            # what this is, how to run it
├── CLAUDE.md            # house rules for the agent (Move + later)
├── .gitignore           # keeps data/ and secrets out of git
├── code/                # analysis scripts, notebooks
├── paper/
│   ├── main.tex         # the manuscript (from Overleaf)
│   ├── refs.bib         # auto-exported from Zotero
│   └── figures/         # plots your code writes here
├── results/             # tables, outputs
└── data/                # UNTRACKED — raw data lives here locally
```

> The figure that goes in the paper is generated by the code next to it. **One source of truth.**

---

# Step 6 — Data stays untracked

Data is often **big, private, or both.** It does **not** belong in git.

```bash
cat > .gitignore <<'EOF'
data/
!data/README.md
*.env
.DS_Store
__pycache__/
EOF
```

- Keep a **`data/README.md`** that says *where the real data lives* and how to get it.
- Large/shared data → a drive, S3 bucket, or **DVC / git-annex** (pointers in git, bytes elsewhere).
- Optional: commit a tiny **synthetic sample** so the repo runs for others.

> Track the **recipe**, not the **ingredients.**

---

<!-- _class: lead -->

# Move 3 · The paper

### Overleaf → LaTeX in VS Code

---

# Step 7 — LaTeX, locally

Your LaTeX install from pre-flight should be done by now.

- **LaTeX Workshop** extension (installed in Step 1) does the rest.
- Open `paper/main.tex` → it builds on save; PDF preview opens side-by-side.
- Under the hood it runs `latexmk`. No more "compile" button in a browser.

✅ Check: edit a word in `main.tex`, save, see the PDF update.

<!-- Speaker: if build fails, it's almost always a missing TeX package or latexmk not found — check the LaTeX Workshop output panel. -->

---

# Step 7b — Bring your Overleaf project over

You don't lose Overleaf — you **move the source into the repo.**

```bash
# Overleaf (premium): Menu → Git → copy the URL
git clone https://git.overleaf.com/<project-id> paper

# Free plan: Menu → Download → Source (.zip), unzip into paper/
```

- **Keep collaborating on Overleaf if you must** — its git bridge can sync both ways.
- The win: the **AI can now read and edit your manuscript** alongside the code.

> Co-authors on Overleaf? Sync via git for now. Move them over when *they're* ready.

---

<!-- _class: lead -->

# Move 4 · References

### Zotero → a live `.bib` in the repo

---

# Step 8 — Zotero → Better BibTeX

You **keep Zotero** as your library. You just point it at the repo.

1. Install the **Better BibTeX** plugin (zotero `.xpi`, then restart Zotero).
2. Right-click your collection → **Export Collection** → format **Better BibTeX**.
3. Save as **`paper/refs.bib`** and tick **"Keep updated."**

Now every reference you add in Zotero flows into `refs.bib` automatically.

```latex
% in main.tex
\bibliography{refs}     % or \addbibresource{refs.bib} with biblatex
```

> Zotero stays the source of truth; the repo gets a **always-fresh** copy the AI and LaTeX both read.

---

<!-- _class: lead -->

# Putting it together

### House rules · first loop · push

---

# Step 9 — Write a `CLAUDE.md`

A short file at the repo root that the agent reads every time. It makes output **consistent and yours.**

```markdown
# Project conventions
- Python 3.11, pandas. Plots with matplotlib → paper/figures/.
- Never modify files in data/. Treat it as read-only.
- Paper is LaTeX in paper/main.tex; cite from refs.bib.
- Explain your plan before writing code. Small steps.
```

> This is how you stop re-explaining yourself — and how a **lab** shares one standard.

---

# Step 10 — Your first in-repo loop

Open the project in VS Code, run `claude`, and try a **real** task end-to-end:

> *"Load `data/measurements.csv`, plot X vs Y, save it to `paper/figures/scatter.pdf`, and add a `\\includegraphics` for it in `main.tex`. Show me the plan first."*

Watch it touch **data → code → figure → paper** in one move. That's the whole reason for the monorepo.

✅ Check: the figure appears in your compiled PDF.

---

# Step 11 — Push to GitHub

```bash
git add -A
git commit -m "Initial project: code + paper + conventions"

# create the remote and push (GitHub CLI)
gh repo create my-project --private --source=. --push
```

✅ Check: refresh github.com — your repo is there, and **`data/` is not** (it's gitignored).

> Private by default. Your data never left your laptop.

---

# A gentle 3-week migration

Don't flip everything at once. Suggested ramp:

| Week | Do | Keep as backup |
|---|---|---|
| 1 | Set up the repo; vibe-code **one** small analysis in it | ChatGPT/Claude app for everything else |
| 2 | Move **one** paper's `.tex` + `.bib` in; compile locally | Overleaf (synced) for co-authors |
| 3 | Make the repo your default for new work | Old tools for legacy projects |

> Success = the day opening VS Code feels easier than opening four tabs.

---

# Troubleshooting (the usual suspects)

- **`claude: command not found`** → Node missing or npm global bin not on PATH. Re-check `node --version`.
- **LaTeX won't build** → distribution still installing, or a missing package; read LaTeX Workshop's output panel.
- **`refs.bib` not updating** → Better BibTeX "Keep updated" wasn't ticked on export.
- **Agent can't see a file** → you opened the wrong folder. Open the **repo root** in VS Code.
- **Pushed data by accident** → it was in git before `.gitignore`; ask the agent to help `git rm --cached` it.

<!-- Speaker: keep this slide up during the hands-on free-for-all. Most questions are here. -->

---

# Safety — before you commit

1. **Data confidentiality** — patient/embargoed data stays in `data/` (untracked). Don't paste it into a cloud chat.
2. **No secrets in git** — API keys, tokens → a `.env` file that's gitignored.
3. **Private repos** for unpublished work; check your institution's policy.
4. **Provenance** — commit the code and `CLAUDE.md`; the repo *is* your reproducibility story.

> Your name is on the paper. The repo is what makes the result **defensible.**

---

# Cheat sheet — the whole setup

```bash
# 1. Editor + agent
brew install git node
npm install -g @anthropic-ai/claude-code

# 2. The repo
mkdir my-project && cd my-project && git init
mkdir code paper data results
echo "data/" > .gitignore

# 3. Paper: clone/unzip Overleaf into paper/, open main.tex
# 4. Refs: Zotero → Better BibTeX → export paper/refs.bib (keep updated)

# 5. Work
claude                       # ask it to build something, plan first
gh repo create my-project --private --source=. --push
```

---

<!-- _class: lead -->

# You now direct from one place.

Code, paper, references, data — **one workspace**, with the AI inside it.

### Old tools still there. You just don't *need* the tabs anymore.

Pick one real project this week and move it in.
