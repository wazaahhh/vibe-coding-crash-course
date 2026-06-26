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
