<!-- _class: lead -->

# 5 · Git &amp; GitHub — your safety net

### When the AI edits your files fast, version control is what lets you say *undo*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`

<!-- Speaker: this is the conceptual bridge into the install fest. Frame git as the thing that makes vibe coding SAFE, not as bureaucracy. The demo (04) just showed the AI being confidently wrong — git is how you survive that. -->

---

# Where we've been — and what's next

**Covered so far**
- **01 · Why it matters** — author → director.
- **02 · The mindset** — four pillars; you are System 2.
- **03 · How you actually do it** — chat vs. agent; intent is the lever.
- **04 · Live demo** — we caught the bug the AI missed.

**This module · 05 — Git &amp; GitHub**
- **Local git** vs. **GitHub** — two different jobs
- Why version control is **non-negotiable** when an AI edits your code
- **Private vs. public**, and **connecting the agent to GitHub**

---

# The problem vibe coding creates

An agent can edit **ten files in thirty seconds** — confidently, and sometimes wrong (you just watched it).

- Without a safety net, a bad edit **silently overwrites** work that ran yesterday.
- "Undo" in your editor won't save you across many files, runs, and sessions.
- You need a **known-good state** you can always return to — and a **record** of what changed, when, and why.

> Generation got cheap (**Pillar 4: try &amp; fail**). Cheap experiments are only safe if failure is **reversible.** That's git.

---

# Local git vs. GitHub — two different jobs

| **Local git** (on your laptop) | **GitHub** (in the cloud) |
|---|---|
| A **time machine** for one folder | A **backup + sharing** copy of it |
| Save points (**commits**) you can revert to | Off-machine copy — laptop dies, work survives |
| Works fully **offline**, no account | Needs an account; you **push** / **pull** to sync |
| *Your* history, private by default | **Collaboration** — co-authors, PRs, review |

> **Local git protects you from yourself. GitHub protects you from the world** (and shares with your lab).

You can use git **with no GitHub at all** — but you lose backup and collaboration.

---

# The one loop that makes it safe

The vibe-coding loop **is** the git loop:

```bash
# 1. AI makes a change (you prompt; it edits files)
git status                 # what did it touch?
git diff                   # read EXACTLY what changed  ← System 2 checkpoint
# 2. Good? snapshot it.       Bad? throw it away.
git add -A && git commit -m "clean units, fix mm rows"
git restore .              # <- the undo button: back to last commit
```

- `git diff` is **how you review the AI's work** — the diff is the PR from your overconfident intern.
- Every commit is a **save point** you can return to with `git restore` / `git revert`.

> **Commit early, commit often.** A commit before a big prompt = a guaranteed way back.

---

# Branches — try the risky thing safely

Want the AI to attempt a big refactor or a second analysis path? Do it on a **branch.**

```bash
git switch -c try-mixed-model    # a parallel sandbox
#  ... let the agent go wild; test the result ...
git switch main                  # untouched, still works
git merge try-mixed-model        # keep it — or just delete the branch
```

- `main` stays **known-good** while you experiment.
- Bad experiment? **Delete the branch** — zero trace, zero regret.

> Branches turn "I hope this doesn't break everything" into "let's just try it."

---

# Private vs. public — choose per repo

GitHub repos are **private by default here — and that's the right default for research.**

| **Private** | **Public** |
|---|---|
| Only you + invited collaborators | Anyone can read (and fork) |
| Unpublished results, sensitive work | Published methods, open source, teaching |
| **Start here** while the work is live | Flip to public **at publication** for reproducibility |

- You can **start private and go public later** — one click. The reverse leaks.
- ⚠️ **Public = permanent.** A secret or dataset pushed public may be **cloned/indexed before you delete it**. Assume it's out there.
- **Data still stays out of git** (Install fest · Code) — public/private governs the *code*, not permission to upload private data.

> Default **private**. Go public **deliberately**, at publication, after checking what's in the history.

---

# Connect the AI agent to GitHub

Let the agent do the git/GitHub plumbing for you — through the **`gh` CLI** it can run:

```bash
gh auth login            # one-time: authorize gh in your browser (HTTPS + token)
#   the agent can now run git & gh on your behalf:
#   "commit this with a sensible message, push, and open a PR"
```

- **How it connects:** `gh auth login` stores a **token** locally; the agent calls `git`/`gh` like any command — no password typing.
- The agent can **commit, push, open pull requests, read CI logs** — you still **review the diff** before it lands.
- **GitHub MCP** (advanced) lets the agent read issues/PRs directly. Same rule: **grant the least it needs.**

> ⚠️ Authorize on **your** machine, scope tokens tight, and **never** let auto-accept push to `main` unreviewed. The agent drafts; **you merge.**

---

# End of Module 5 — recap, discussion &amp; support

**Module 05 recap — Git &amp; GitHub**
- **Local git** = your time machine / undo; **GitHub** = backup, sharing, review.
- The vibe loop *is* the git loop: **prompt → `git diff` → commit or restore.** Branches make risk cheap.
- **Private by default**, public at publication; the agent can drive git/GitHub via `gh` — **you review, you merge.**

**Open question — let's discuss:** *If every AI edit is a commit you review, what should a "good" commit-sized change look like — and how small is too small?*

★ Support this course → `github.com/wazaahhh/vibe-coding-crash-course`
