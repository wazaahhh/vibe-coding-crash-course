---
marp: true
paginate: true
size: 16:9
title: "FacMed Hack #1 — Crash Course #2, 22 October 2026"
author: Faculty of Medicine, UNIGE
style: |
  /* FacMed Hack edition of Vibe Coding for Scientists. FacMed hackathon design system — tokens verbatim from
     apps/facmed-hack/workers/api/src/site/styles.ts, as in Crash Course #1.
     Ink ground for the title and the moments the room does the work
     (opening question, quiz); light ground for everything else. */
  :root {
    --ink: #11233F;
    --accent: #96004B;        /* UNIGE burgundy */
    --science: #4FA5B8;       /* teal */
    --energy: #6E7CF6;        /* periwinkle */
    --accent-soft: #EBCFDC;
    --science-soft: #D9F0F4;
    --energy-soft: #E3E7FF;
    --bg-soft: #F7F9FC;
    --bg-inset: #EEF4FA;
    --fg-muted: #4D5B73;
    --fg-faint: #7C8AA1;
    --line: #D7E1EC;
    --on-ink: #F2F6FB;
    --on-ink-muted: #A9B8CE;
  }
  section {
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 25px;
    background: #ffffff;
    color: var(--ink);
    line-height: 1.4;
    padding: 46px 64px 54px;
    display: block !important;
  }
  p { margin: 0 0 0.6em; }
  ul, ol { margin: 0 0 0.6em; padding-left: 1.2em; }
  li { margin-bottom: 0.28em; }
  h1, h2, h3 { color: var(--ink); letter-spacing: -0.018em; line-height: 1.16; margin: 0; }
  h1 { font-size: 1.9em; font-weight: 800; }
  h2 {
    display: inline-block; font-size: 1.45em; font-weight: 700;
    border-bottom: 3px solid var(--accent);
    padding-bottom: 6px; margin-bottom: 0.55em;
  }
  h3 { font-size: 1.0em; font-weight: 700; margin-bottom: 0.25em; }
  strong { color: var(--accent); }
  a { color: var(--accent); text-decoration: none; }
  .kicker {
    display: block; font-size: 0.62em; font-weight: 700; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--fg-faint); margin-bottom: 6px;
  }
  .small { font-size: 0.74em; color: var(--fg-muted); }
  .muted { color: var(--fg-muted); }
  blockquote {
    margin: 0.3em 0 0.7em; padding: 14px 22px; border: 0;
    border-left: 5px solid var(--accent); background: var(--bg-soft);
    border-radius: 0 12px 12px 0; color: var(--ink); font-size: 1.05em;
  }
  blockquote p { margin: 0; }

  /* House table: uppercase faint headers over hairline rules, no fills. */
  table, thead, tbody, tr { background: transparent !important; color: inherit; }
  table { border-collapse: collapse; font-size: 0.78em; width: 100%; display: table; }
  th, td { border: 0; border-bottom: 1px solid var(--line); padding: 8px 12px 8px 0; text-align: left; vertical-align: top; background: transparent !important; }
  th { font-size: 0.72em; letter-spacing: 0.08em; text-transform: uppercase; color: var(--fg-faint); font-weight: 700; }
  tr:last-child td { border-bottom: 0; }

  /* Layout helpers */
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 34px; }
  .card { background: var(--bg-soft); border: 1px solid var(--line); border-radius: 14px; padding: 16px 20px; }
  .card h3 { margin-bottom: 0.3em; }
  .card p { font-size: 0.8em; margin: 0; color: var(--fg-muted); }
  .clock {
    position: absolute; top: 40px; right: 64px;
    font-size: 0.8em; font-weight: 700; color: var(--accent);
    background: var(--accent-soft); padding: 4px 14px; border-radius: 8px;
  }
  footer { color: var(--fg-faint); font-size: 0.5em; left: 64px; }
  section::after { color: var(--fg-faint); font-size: 0.55em; }

  /* Quiz: four answer cards in a 2 × 2 grid, letter badge on the left. */
  .opts { display: grid; grid-template-columns: 1fr 1fr; gap: 14px 22px; margin-top: 6px; }
  .opt {
    display: flex; align-items: center; gap: 16px;
    background: var(--bg-soft); border: 1px solid var(--line); border-radius: 14px;
    padding: 14px 18px; font-size: 0.86em; line-height: 1.3;
  }
  .opt b {
    flex: none; width: 40px; height: 40px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    background: var(--accent); color: #fff; font-size: 1.05em;
  }
  .qnum { font-size: 0.62em; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--accent); }

  /* Ink slides: title, opening question, quiz cover */
  section.ink {
    background: radial-gradient(900px 520px at 88% 8%, rgba(110,124,246,0.38), transparent 60%),
                radial-gradient(760px 460px at 4% 100%, rgba(79,165,184,0.30), transparent 60%),
                var(--ink);
    color: var(--on-ink);
  }
  section.ink h1, section.ink h2, section.ink h3 { color: #fff; }
  section.ink h2 { border-bottom-color: #F08BB4; }
  section.ink strong { color: #F6A9C8; }
  section.ink .kicker, section.ink .small, section.ink .muted { color: var(--on-ink-muted); }
  section.ink .clock { background: rgba(240,139,180,0.18); color: #F6A9C8; }
  section.ink .card { background: rgba(255,255,255,0.06); border-color: rgba(255,255,255,0.14); }
  section.ink .card p { color: var(--on-ink-muted); }
  section.ink blockquote { background: rgba(255,255,255,0.06); border-left-color: #F08BB4; color: var(--on-ink); }
  section.ink footer, section.ink::after { color: var(--on-ink-muted); }

  .cols3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 22px; }
  .cols4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
  pre { font-size: 0.62em; background: var(--bg-inset); border: 1px solid var(--line); border-radius: 12px; padding: 14px 18px; line-height: 1.35; }
  code { font-size: 0.9em; background: var(--bg-inset); border-radius: 6px; padding: 1px 6px; }
  pre code { background: transparent; padding: 0; }
  section.ink pre, section.ink code { background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.14); color: var(--on-ink); }
  .divider h1 { font-size: 2.3em; margin-bottom: 0.3em; }
  .logos {
    display: flex; flex-wrap: nowrap; align-items: center; justify-content: flex-start;
    gap: 20px; background: #fff; border-radius: 14px; padding: 14px 24px; margin-top: 18px;
  }
  .logos img { height: 24px; width: auto; }
  .logos img.tall { height: 38px; }
footer: "FacMed Hack #1 · Digital Phenotyping of Mental Health · Crash Course #2 · 22 Oct 2026"
---

<!-- ====== SLIDE 1 — Title ====== -->
<!-- _class: ink -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="cols" style="grid-template-columns: 1.6fr 1fr; align-items: center;">
<div>

<span class="kicker">Crash Course #2 · Thursday 22 October 2026 · 17:00 → 19:00 · on Zoom</span>

# Vibe coding &amp; AI-assisted development
## Direct the agent. Check the result.

Tonight you open your challenge repository, put an AI agent to work in it, and learn to catch it when it is confidently wrong.

<span class="small">FacMed Hack #1 · Digital Phenotyping of Mental Health · Fri 6 – Sat 7 November 2026 · Campus Biotech · in English</span>

</div>
<div style="text-align:center">

<div class="card" style="text-align:left">
<h3>The road to 6 November</h3>
<p><b>Thu 8 Oct</b> · B1 · Digital phenotyping &amp; the Swiss data rules</p>
<p><b>Today</b> · B2 · Vibe coding &amp; AI-assisted development</p>
<p><b>Thu 29 Oct</b> · B3 · Grant writing for pop-up projects, with the RGO</p>
<p><b>Fri 6 – Sat 7 Nov</b> · the hackathon, 32 hours</p>
</div>

</div>
</div>

<div class="logos">
<img class="tall" src="assets/unige-facmed.png" alt="UNIGE Faculty of Medicine" />
<img class="tall" src="assets/synapsy.png" alt="Synapsy" />
<img src="assets/wyss-center.png" alt="Wyss Center for Bio and Neuroengineering" />
<img src="assets/neuro-campusbiotech.svg" alt="Neuro @ Campus Biotech" />
<img src="assets/hug.png" alt="HUG" />
<img src="assets/epfl.png" alt="EPFL" />
<img src="assets/cisa.png" alt="CISA" />
<img src="assets/sparkboard.png" alt="Sparkboard" />
</div>

---

<!-- ====== SLIDE 2 — Opening question ======
Facilitator: read the question aloud, then silence. 90 seconds for everyone to type
one or two lines in the Zoom chat (ask them to hold Enter until you say "send", so
early answers don't anchor the rest). Read 4–5 aloud, picking ones far apart
(clinic vs. theory vs. lab bench vs. publishing). Save the chat: at 18:50 we sort
the answers into the places the session showed agents change today vs. the places
that are still imagination.
-->
<!-- _class: ink -->

<span class="clock">4 min</span>

<span class="kicker">Before anything else · 90 seconds · one or two lines in the Zoom chat</span>

# Where do you imagine vibe coding and agentic coding will change science? Name one place, and what changes there.

<span class="small" style="display:block; margin-top: 10px;">Your own field or any other. A method, an instrument, a job in the lab, a stage of publishing: be specific.</span>

<br>

> *"What would you do if you had all the models of the brain you wanted?"*
> <span class="small">Grace Lindsay, NYU, responding to this week's pre-read (DePasquale, <i>The Transmitter</i>, June 2026)</span>

---

<!-- ====== SLIDE 3 — Quiz cover ====== -->
<!-- _class: ink -->

<span class="clock">8 min</span>

<span class="kicker">Six questions about where this is going</span>

## Five have no right answer. One does.

<div class="cols" style="margin-top: 10px;">
<div class="card">
<h3>How</h3>
<p>One question per slide, about a minute each. A Zoom poll pops up with each one. Anonymous. Answer with what you actually expect for your field.</p>
</div>
<div class="card">
<h3>Why</h3>
<p>The split in the room is the material for tonight. We keep the results, set them against what researchers in the field are saying, and come back to them before 19:00.</p>
</div>
</div>

<br>

<span class="small">No poll on your screen? Type your letter in the chat.</span>

---

<!-- ====== SLIDE 4 — Q1: where first? ======
Opinion, no right answer. Zoom: multiple choice, up to two.
Push: whichever wins, ask someone who picked the least-chosen option to defend it.
Most current evidence of real change is in A (analysis and modelling: the
pre-read's argument) and C (literature tools); B is where the money is going
(autonomous labs). D and E are where the policy fights are.
Comes back: live build (17:15) shows A for real; hands-on (17:40) tries it on
the challenge repositories.
-->

<span class="qnum">Question 1 of 6 · Where first</span>

## Where will agentic coding change research practice most in the next five years? *Pick up to two.*

<div class="opts">
<div class="opt"><b>A</b>Analysing data and building models</div>
<div class="opt"><b>B</b>Designing and running experiments: automated labs</div>
<div class="opt"><b>C</b>Reading and synthesising the literature</div>
<div class="opt"><b>D</b>Writing papers and grants</div>
</div>
<div class="opts" style="grid-template-columns: 1fr; margin-top: 14px;">
<div class="opt"><b>E</b>Peer review and replication</div>
</div>

---

<!-- ====== SLIDE 5 — Q2: the scarce skill ======
Opinion, no right answer. Links straight to the opening question.
Push: if C or D wins, ask the PIs in the room how they hire for it today, and
how a PhD student practises it. The course's thesis sits between C and D
(director of the code: intent, judgment, verification).
Voices: Stachenfeld (DeepMind/Columbia) calls LLMs "a flashlight as opposed to a
laser pointer", useful near known ideas, unlikely to find very unusual ones (C).
Gjorgjieva (TUM): expertise is needed "to recognize when an AI system is
inventing concepts that do not actually exist" (D).
Comes back: review hunt (18:15) is D, practised.
-->

<span class="qnum">Question 2 of 6 · The scarce skill</span>

## In 2031, the scarcest skill in a neuroscience lab will be…

<div class="opts">
<div class="opt"><b>A</b>Programming</div>
<div class="opt"><b>B</b>Statistics and methods</div>
<div class="opt"><b>C</b>Choosing the question worth asking</div>
<div class="opt"><b>D</b>Judging whether a result is true</div>
</div>
<div class="opts" style="grid-template-columns: 1fr; margin-top: 14px;">
<div class="opt"><b>E</b>Collecting good data from real people</div>
</div>

---

<!-- ====== SLIDE 6 — Q3: prolific but shallow? ======
Opinion. Checks the pre-read without making it a test.
DePasquale: "The field risks becoming prolific but shallow—generating models
faster than we can generate insights."
B is Dan Goodman's point (Imperial): the field already rewards producing models
over understanding them, and vibe modelling could make that worse.
C is the hopeful reading of DePasquale's own four directions.
Push: ask a D voter what evidence would change their mind, and by when.
Comes back: close (18:50).
-->

<span class="qnum">Question 3 of 6 · Depth</span>

## This week's pre-read warns that AI coding could make theoretical neuroscience *"prolific but shallow"*. For your own field, you think…

<div class="opts">
<div class="opt"><b>A</b>It is already happening</div>
<div class="opt"><b>B</b>It will happen unless incentives change</div>
<div class="opt"><b>C</b>The opposite: faster coding frees time to think</div>
<div class="opt"><b>D</b>Too early to say</div>
</div>

<br>

<span class="small">B. DePasquale, "Models at the speed of thought: How AI coding is reshaping theoretical neuroscience", <i>The Transmitter</i>, 16 June 2026.</span>

---

<!-- ====== SLIDE 7 — Q4: training the next generation ======
Opinion, and the one where PhD students and PIs tend to split. After the
results, ask in the chat: "PhD students: does this match what you'd want? PIs:
is this what you do?"
DePasquale's argument: the struggle of turning an idea into equations and code
is "a form of disciplined thinking"; skip it and you never know your own model.
Schuck's lab policy (second pre-read) answers it in practice: trainees do by hand
the work that builds core skills (questions, models, arguments) and hand off what
they don't need to learn; they draft text themselves before any AI editing.
Talmo Pereira (Salk) worries about losing the craft of scientific software.
The counter: if directing agents is the job, learn it from day one (A).
Comes back: hands-on (17:40), where pairs direct an agent in a challenge repo.
-->

<span class="qnum">Question 4 of 6 · Training</span>

## A first-year PhD student can now get working analysis code from an agent in minutes. In their first year, they should…

<div class="opts">
<div class="opt"><b>A</b>Use agents freely: directing them is the skill that matters now</div>
<div class="opt"><b>B</b>Write their core analyses by hand first, agents later</div>
<div class="opt"><b>C</b>Use agents, but explain every line at lab meeting</div>
<div class="opt"><b>D</b>Keep agents away from thesis-critical analyses</div>
</div>

---

<!-- ====== SLIDE 8 — Q5: the literature ======
Opinion. The futures question with the widest spread.
Push: A and C are the same technology with opposite incentives. Who would pay
for the checking? (Funders, journals, an AI reviewer, nobody?)
Voice from the pre-read: Dan Goodman (Imperial College London) argues that
publication incentives already reward producing models over understanding them,
and that vibe modelling could make this worse. That is C and D; A needs someone
to reward the checking.
Comes back: how the hack runs (18:35): every team's repository is re-runnable
by the jury, which is A, at the scale of one weekend.
-->

<span class="qnum">Question 5 of 6 · The literature</span>

## Soon an agent can re-run any published analysis from its repository in minutes. What happens to your field's literature?

<div class="opts">
<div class="opt"><b>A</b>Replication becomes routine and the literature gets cleaner</div>
<div class="opt"><b>B</b>A wave of corrections and retractions, then a cleaner literature</div>
<div class="opt"><b>C</b>Little changes: nobody is rewarded for checking</div>
<div class="opt"><b>D</b>AI-generated papers multiply faster than anyone can check them</div>
</div>

---

<!-- ====== SLIDE 9 — Q6: a reality check ======
The one question with an answer: D. Reveal it now, right after the poll closes.
Tasks took 19% longer with AI. Before starting, the developers forecast a 24%
speed-up; afterwards they still estimated AI had made them ~20% faster.
Caveat to say out loud: early-2025 tools, experts in large mature repositories
they knew intimately. METR says the result may not hold for small new projects
or unfamiliar code, which is closer to a 32-hour hack.
Why it closes the quiz: five minutes of imagining the future, then evidence
that our sense of what AI does for us can be wrong in sign. Imagine boldly;
measure before you believe.
Comes back: review hunt (18:15).
-->

<span class="qnum">Question 6 of 6 · A reality check</span>

## In a 2025 randomised trial, experienced open-source developers worked on their own projects with and without AI tools. With AI, they were…

<div class="opts">
<div class="opt"><b>A</b>about 40% faster</div>
<div class="opt"><b>B</b>about 20% faster</div>
<div class="opt"><b>C</b>no faster and no slower</div>
<div class="opt"><b>D</b>about 19% slower</div>
</div>

<br>

<span class="small">METR (Model Evaluation &amp; Threat Research), "Measuring the impact of early-2025 AI on experienced open-source developer productivity", July 2025 · 16 developers, 246 real tasks.</span>

---

<!-- ====== SLIDE 10 — Tonight's three objectives ======
Facilitator: the quiz has just shown the room is split on where this goes.
These three objectives are the answer to "so what do we do tonight".
Objective 3 matters most for anyone who arrived without tools installed: say
explicitly that this is fine, and that the hack offers the HPE / NVIDIA
environment to everyone, with or without their own setup.
-->

<span class="kicker">Tonight · three objectives</span>

## By 19:00 you should…

<div class="cols3" style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap: 22px; margin-top: 8px;">
<div class="card">
<span class="qnum">1 · Imagine</span>
<h3>See your place in agentic science</h3>
<p>Your contribution to science, your career and your purpose, once agents write much of the code. What becomes yours to do?</p>
</div>
<div class="card">
<span class="qnum">2 · Understand</span>
<h3>Know how vibe coding works</h3>
<p>Think fast and slow: let the agent go fast, check slowly. Try, fail and retry cheaply. GitHub as the safety net. Working as a team, with agents in the loop.</p>
</div>
<div class="card">
<span class="qnum">3 · Prepare</span>
<h3>Know how it runs at the hack</h3>
<p>Whether you already have the tools or not, both paths are covered: your own setup, or the HPE / NVIDIA environment, open to every team to build and test on.</p>
</div>
</div>

<br>

<span class="small">Objective 2 follows the course <i>Vibe Coding for Scientists</i> (github.com/wazaahhh/vibe-coding-crash-course): modules 01–04 were this week's pre-work; tonight draws on modules 02, 03, 05, 06 and 08.</span>

---

<!-- ====== SLIDE 11 — Tonight's programme ====== -->

<span class="kicker">Tonight · 17:00 → 19:00</span>

## Hold your answers: each one comes back tonight

| Time | Block | Obj. | Quiz |
|---|---|---|---|
| 17:00 | Opening question and quiz | 1 | — |
| 17:15 | **Live build**: a sleep and mood analysis on phenotyping data, from question to pull request | 2 | Q1&nbsp;Q6 |
| 17:40 | **Hands-on in pairs** (breakout rooms), in a challenge you voted for: explain, plan, commit, pull request | 2 | Q4 |
| 18:15 | **Review hunt**: find the planted errors in an AI-written analysis | 2 | Q2&nbsp;Q6 |
| 18:35 | **How the hack runs**: with or without your own tools, the HPE / NVIDIA environment, data rules | 3 | Q5 |
| 18:50 | **Your place**: the room's answers, voices from the field, back to the opening question | 1 | Q1&nbsp;Q3 |


---

<!-- ====== LIVE BUILD 1 — Divider ====== -->
<!-- _class: ink divider -->

<span class="clock">25 min</span>

<span class="kicker">17:15 · Objective 2 · Understand</span>

# Live build: from a question to a pull request

A real analysis on digital-phenotyping data, directed live, with an agent in the editor.

**Your job while you watch:** type in the chat whenever you see a pillar being skipped.

---

<!-- ====== LIVE BUILD 2 — The pre-work in one slide ======
From module 02 (the mindset). 2 minutes, no more: they read it.
The thesis from module 01 sits on top: you move from author of code to director of code.
-->

<span class="kicker">The pre-work in one slide · module 02</span>

## You direct; the agent writes. Four disciplines keep it honest.

<div class="cols4" style="margin-top: 6px;">
<div class="card"><h3>Diverge</h3><p>Generation is nearly free: ask for three approaches with trade-offs, then choose.</p></div>
<div class="card"><h3>Think critically</h3><p>Every output is a pull request from a brilliant, overconfident intern. <i>How would I know if this is wrong?</i></p></div>
<div class="card"><h3>Fast and slow</h3><p>The agent is System 1: fast, fluent, sometimes wrong. You supply System 2. The more it matters, the slower you read.</p></div>
<div class="card"><h3>Try and fail</h3><p>Attempts cost minutes. Branch, try, throw away. Git makes failure reversible.</p></div>
</div>

<br>

> Trust the vibe to **write** it; never trust the vibe that it's **right**.

---

<!-- ====== LIVE BUILD 3 — Tonight's question ======
The dataset is synthetic but shaped like a challenge dataset: say so.
The move to name: this is what teams do on 6 November. Start from a need or a
breakthrough-app opportunity on the challenge page, turn it into one testable question.
-->

<span class="kicker">The demo</span>

<div class="cols" style="grid-template-columns: 1.15fr 1fr; align-items: start;">
<div>

## Does last night's sleep predict today's mood?

40 participants · 21 nights, 12 Oct → 1 Nov 2026 · phone sleep detection, wearable steps, a four-item mood questionnaire every evening.

Synthetic, and messy on purpose, like the plant dataset in the pre-work: the traps teach the mindset.

<span class="small">Repository: <code>editions/facmed-hack-2026/demo-phenotyping/</code> in the course repo. Fork it and follow along, or just watch.</span>

</div>
<div>

```text
data/
├── README.md          ← the codebook: read it
├── participants.csv   age, PHQ-9 at baseline
├── sleep.csv          bedtime, wake time
├── steps.csv          steps, minutes worn
└── ema.csv            mood_1 … mood_4 (1–7)
```

<span class="small">On 6 Nov the same move starts from your challenge page: a need, a breakthrough-app opportunity, one testable question.</span>

</div>
</div>

---

<!-- ====== LIVE BUILD 4 — The arc ======
From module 04's demo arc, re-cut for this dataset. Facilitator script in
demo-phenotyping/README.md. Name the pillar out loud at each move.
-->

<span class="kicker">The arc · six moves</span>

## Watch for where it goes fast, and where we slow down

| # | Move | What we type | Pillar |
|---|---|---|---|
| 1 | Orient by asking | *"Brief me on `data/` and the codebook. What problems do you see?"* | Fast |
| 2 | Plan before code | *"Plan how you'd relate sleep to next-day mood. Don't write code yet."* | Diverge |
| 3 | Let it run | sleep per night → mean per night → a plot | Fast |
| 4 | Slow down at the picture | *one night looks strange: why?* | **Slow** |
| 5 | Fix with intent | *"Localise to Europe/Zurich, convert to UTC, then subtract. Show me before and after."* | Critical |
| 6 | Review and commit | `git diff` → commit → a line in `NOTES.md` → pull request | Try and fail |

---

<!-- ====== LIVE BUILD 5 — Three dials ======
From module 06 (edit modes, models and steering). One slide; point at the
editor while saying it.
Tools named for the hack: Claude Code or Codex with your own subscription;
GitHub Copilot (free for students through GitHub Education); Cline with the open
models served on the HPE / NVIDIA environment at the hack.
-->

<span class="kicker">Module 06 · the controls</span>

## Three dials, whichever agent you use

<div class="cols3" style="margin-top: 6px;">
<div class="card">
<h3>1 · Edit mode: how much rope</h3>
<p><b>Plan first</b> for anything big · <b>edit</b> with every diff approved for results that matter · <b>agent / auto</b> only on a throwaway branch, because git makes it reversible.</p>
</div>
<div class="card">
<h3>2 · Model: the right brain</h3>
<p>A frontier or "thinking" model for statistics, study design and subtle bugs; a fast one for boilerplate. Escalate when it is stuck.</p>
</div>
<div class="card">
<h3>3 · Steering: hand on the wheel</h3>
<p>Interrupt the moment it drifts · correct with specifics · paste the traceback · small steps · clear a thread that goes in circles.</p>
</div>
</div>

<br>

<span class="small">Same dials in Claude Code, Codex, GitHub Copilot and Cline. At the hack: your own agent, or Cline on the open models served on the HPE / NVIDIA environment.</span>

---

<!-- ====== LIVE BUILD 6 — The git loop ======
From module 05. The vibe loop is the git loop. The agent can run all of this
through `gh`; the human reads the diff and merges.
-->

<span class="kicker">Module 05 · the safety net</span>

<div class="cols" style="grid-template-columns: 1fr 1fr; align-items: start;">
<div>

## The vibe loop is the git loop

- `git diff` is how you review the agent's work: the diff is the intern's pull request.
- **Commit before a big prompt**: a guaranteed way back.
- **Branches** make the risky attempt cheap. `main` stays known-good.
- The agent can run git and `gh` for you. **You read the diff; you merge.**

</div>
<div>

```bash
# the agent changed something
git status        # what did it touch?
git diff          # read exactly what changed
# good: snapshot it
git commit -am "sleep in UTC: DST night fixed, checked by plot"
# bad: back to the last commit
git restore .

# try the risky thing on a branch
git switch -c thomas/mixed-model
```

</div>
</div>

---

<!-- ====== LIVE BUILD 7 — What just happened ======
Show after the demo. Numbers from demo-phenotyping/check_answers.py.
Callback to quiz Q6: the run felt fast and finished cleanly; the number was
wrong for one night and nothing complained.
-->

<span class="kicker">What just happened</span>

## A clean run with a wrong number

<div class="cols" style="grid-template-columns: 1fr 1.2fr; gap: 30px; align-items: center;">
<div>

<div class="card"><div style="font-size:2.6em; font-weight:800; color:var(--accent); line-height:1">5.9 h</div><p>mean sleep on the night of 24 → 25 October, subtracting clock times</p></div>
<br>
<div class="card"><div style="font-size:2.6em; font-weight:800; color:var(--science); line-height:1">6.9 h</div><p>the same night in UTC, and every other night</p></div>

</div>
<div>

- No error, no warning: the clocks went back an hour at 03:00 on Sunday.
- The agent was **mostly right**, the dangerous kind of wrong.
- Found by a **plot** and the **calendar**: domain knowledge.
- Recorded in `NOTES.md`: *verified: DST night, by plot · trusted: pandas time-zone handling*.

> Quiz Q6: it felt fast. The question is whether it was right.

</div>
</div>


---

<!-- ====== HANDS-ON 1 — Divider ======
Facilitator: open breakout rooms of two (Zoom: assign automatically, 35 min,
let participants return early off). Pair people who voted for the same
challenge where possible; mix seniorities (a PI with a PhD student works well).
Put the challenge repository links and the demo link in the main chat before
opening the rooms, and broadcast a message at 17:57 ("switch roles") and 18:10
("pull request now").
-->
<!-- _class: ink divider -->

<span class="clock">35 min</span>

<span class="kicker">17:40 · Objective 2 · Understand, by doing it</span>

# Hands-on in pairs

Zoom breakout rooms of two, in the repository of a challenge one of you voted for.

**Goal by 18:15:** one small change, reviewed, committed, in a pull request with a note on what you checked.

---

<!-- ====== HANDS-ON 2 — Roles ======
From module 08 (working in a lab): pair on the prompts, one drives, one plays
skeptic. The skeptic role is the one most people skip; insist on it.
Objective 3 starts here: nobody without tools is left out.
-->

<span class="kicker">Module 08 · pair on the prompts</span>

## Two roles, switch at 17:57

<div class="cols" style="margin-top: 6px;">
<div class="card">
<h3>Driver</h3>
<p>Shares their screen and talks to the agent. Says out loud what they are about to ask, and why.</p>
</div>
<div class="card">
<h3>Skeptic</h3>
<p>Never touches the keyboard. After every answer: <i>how would we know if this is wrong?</i> Decides when to slow down.</p>
</div>
</div>

<br>

| Your situation | What to do |
|---|---|
| One of you has an agent installed | That person drives first |
| Neither has an agent yet | Drive in **chat mode** (module 03): paste the README and code into any AI chat, never data |
| No access to a challenge repository yet | Use the demo: `editions/facmed-hack-2026/demo-phenotyping/` |

---

<!-- ====== HANDS-ON 3 — Four quests ======
The quests mirror the hack workflow (AGENTS.md rules: branch, small commits,
pull request with NOTES.md). Most pairs reach quest 3; that's fine.
-->

<span class="kicker">Four quests · do them in order</span>

## From "what is this?" to a pull request

| # | Quest | The move | ~min |
|---|---|---|---|
| 1 | **Explain** | Ask the agent to brief you on the repository and the challenge brief. What is missing from its answer? | 5 |
| 2 | **Plan** | Pick one need or breakthrough-app opportunity from the challenge page. Ask for a plan for a first, tiny analysis or prototype. No code yet. Approve or correct it | 10 |
| 3 | **Change** | On a branch (`firstname/topic`), let the agent make the first small step. Run it. Read the `git diff` together. Commit | 12 |
| 4 | **Pull request** | Push, open a pull request, and add two lines to `NOTES.md`: *verified: …* and *trusted: …* | 5 |

<br>

<span class="small">At 18:15, back in the main room: paste your pull-request link (or your furthest quest) in the chat.</span>

---

<!-- ====== HANDS-ON 4 — Prompt cards ======
From module 03 (how to ask) and the course handout. Leave this slide shared
in the main room while breakouts run, and paste the five prompts in the chat.
-->

<span class="kicker">Module 03 · how to ask</span>

## Five prompts worth stealing

<div class="cols" style="grid-template-columns: 1.25fr 1fr; gap: 30px;">
<div>

1. *"Explain what this code does before you change anything."*
2. *"Outline your plan, then wait for my OK."*
3. *"Write a test that would fail if this result were wrong."*
4. *"What could make this conclusion wrong? Argue against yourself."*
5. *"Summarise in plain language what you changed and what you assumed."*

</div>
<div>

<div class="card">
<h3>Give it context</h3>
<p>The goal, the data's structure, the constraints, what you tried. Vague in, generic out.</p>
</div>
<br>
<div class="card">
<h3>Data stays out</h3>
<p>The agent may see column names and made-up rows. It never sees records from a challenge dataset.</p>
</div>

</div>
</div>


---

<!-- ====== REVIEW HUNT 1 — Divider ======
Facilitator: reopen the same breakout rooms for 15 minutes. Paste in the chat
the link to demo-phenotyping/analysis.py and data/README.md first.
Answer key: demo-phenotyping/ANSWER_KEY.md (five problems). Don't hint.
-->
<!-- _class: ink divider -->

<span class="clock">20 min</span>

<span class="kicker">18:15 · Objective 2 · The slow part</span>

# Review hunt

An agent wrote this analysis. It runs, it reads well, and it reaches a confident conclusion.

**Would you put your name on it?**

---

<!-- ====== REVIEW HUNT 2 — The task, with the output ======
Output is verbatim from `python analysis.py` (seed 2026).
-->

<span class="kicker">15 min in your pairs · then post your list in the chat</span>

<div class="cols" style="grid-template-columns: 1fr 1.2fr; gap: 30px; align-items: start;">
<div>

## List everything you would not sign

1. Open `demo-phenotyping/analysis.py` and the codebook `data/README.md`.
2. Run it (or read the output on the right).
3. Hunt: the code, the data, the method, the summary.
4. For each problem: **what tipped you off?**

<span class="small">Allowed: plots, the codebook, a second AI, your own judgment. The prompt the agent got is at the top of the file.</span>

</div>
<div>

```text
Analysed 743 participant-days from 40 participants.

1. Associations with next-day mood (Pearson r)
   sleep duration : r = +0.39
   daily steps    : r = +0.25

2. Low-mood day classifier (random forest,
   30% held-out test set)
   AUC = 0.77

Summary
   Physical activity is the stronger correlate
   of mood (r = +0.25 vs +0.39 for sleep).
   Wearable data flag low-mood days with high
   accuracy (AUC = 0.77), supporting passive
   sensing as an early-warning signal for
   depressive episodes.
```

</div>
</div>

---

<!-- ====== REVIEW HUNT 3 — Where it bites ======
From module 02. Optional while rooms are open; useful to leave shared for
people who return early.
-->

<span class="kicker">Module 02 · aim your checking</span>

## Strongest on syntax, weakest on truth

| Trust, but skim | Slow down: it fails quietly here |
|---|---|
| Plotting, formatting, refactoring | **Domain correctness**: units, time zones, reverse-keyed items |
| Boilerplate, glue, file reading | **Statistics**: the wrong-but-plausible test, leakage |
| Explaining unfamiliar code | **What the outcome really measures** |
| Translating between languages | **Anything needing ground truth**: codebooks, citations |

> The bug that ends a paper compiles, runs, and looks beautiful.

---

<!-- ====== REVIEW HUNT 4 — Reveal ======
Show only after reading 3–4 lists from the chat. Numbers from check_answers.py.
Ask: which of these would a second AI have caught? (Usually 1 and 3 when given
the codebook; rarely 4 and 5.)
Callback to quiz Q2: judging whether a result is true is the skill this block
practises. Schuck (second pre-read): "AI output sounds confident even when wrong,
so know how you can falsify what a model produces": write scripts that check the
output rather than asking the model to check itself (check_answers.py is one).
-->

<span class="kicker">The answer key</span>

## Five problems, and the headline flips

| # | Problem | Effect | What catches it |
|---|---|---|---|
| 1 | `mood_3` reverse-keyed, averaged as is | mood spread halves; r(sleep) +0.45 → +0.39 | the codebook |
| 2 | Non-wear days kept as 0 steps | fake steps–mood link: r +0.15 → +0.28 | a histogram: spike at 0 |
| 3 | Same participants in train and test | AUC 0.89 → **0.69** on new people | "would it work on a new patient?" |
| 4 | Summary contradicts its numbers | "activity is stronger": 0.25 < 0.39 | numbers before prose |
| 5 | Overclaim | a low-mood *day* is no depressive *episode* | what does the outcome measure? |

<span class="small">Fixed: sleep predicts next-day mood (r ≈ +0.45), steps add little (r ≈ +0.15), the classifier generalises modestly (AUC ≈ 0.69).</span>

---

<!-- ====== REVIEW HUNT 5 — Peer review matters more ======
From module 08. Bridge to objective 3: at the hack, every pull request gets a
second pair of eyes, and NOTES.md records what was verified.
-->
<!-- _class: ink -->

<span class="kicker">Module 08 · working together</span>

## When code is cheap, review is the work

Peer review matters **more** when generation is cheap: the failure mode is unreviewed AI code flowing straight into results.

<div class="cols3" style="margin-top: 14px;">
<div class="card"><h3>Show how you checked</h3><p>Demo what you built and how you verified it.</p></div>
<div class="card"><h3>A second pair of eyes</h3><p>No AI-written analysis reaches a claim without a human reading the reasoning.</p></div>
<div class="card"><h3>Keep the record</h3><p>Whose prompt, which model, what was verified and what was trusted.</p></div>
</div>


---

<!-- ====== HACK 1 — Divider ====== -->
<!-- _class: ink divider -->

<span class="clock">15 min</span>

<span class="kicker">18:35 · Objective 3 · Prepare</span>

# How it runs at the hack

Friday 6 – Saturday 7 November · Campus Biotech · 32 hours.

---

<!-- ====== HACK 2 — Two paths ======
The message to land: arriving without tools is fine. Both paths reach the same
team repository, and both can run work on the HPE / NVIDIA environment.
Source: vibe_coding_environment/implementation_plan.md (corp repo).
-->

<span class="kicker">With or without your own tools</span>

## Two ways in, one team repository

<div class="cols" style="margin-top: 6px;">
<div class="card">
<h3>You already have the tools</h3>
<p>VS Code on your laptop with your own agent: Claude Code or Codex on your own plan, GitHub Copilot, or Cline. Clone your team's repository and work as tonight.</p>
</div>
<div class="card">
<h3>You don't, or you'd rather not install</h3>
<p>A ready-made VS Code in the browser on the HPE / NVIDIA environment: nothing to install, an agent already set up on open models served there, your team's repository already cloned.</p>
</div>
</div>

<br>

> **Either way, every team can build and test on the HPE / NVIDIA environment**: GPUs for heavy jobs, and the challenge datasets, which stay there.

---

<!-- ====== HACK 3 — Your team's repository ======
From the agents' rules (AGENTS.md, implementation plan §3.5). For credit
candidates, the contribution history is the assessment (LNDS syllabus,
Module C, A2).
-->

<span class="kicker">The workflow you rehearsed tonight</span>

## Your team's repository

| Rule | Why |
|---|---|
| One repository per team, in the hack's GitHub organisation | One place for code, notes and the demo |
| A branch per person and task: `firstname/topic` | `main` stays working while you try things |
| **Commit small and often**, under your own name | For credit candidates, the contribution history is the assessment |
| Merge through a pull request, with `NOTES.md` updated: *verified* and *trusted* | The record of what was checked, by whom |
| Tag `demo` on `main` before the final presentations | The jury looks at exactly what you showed |

<br>

<span class="small">Each repository comes with an <code>AGENTS.md</code>: the same rules, written for your agent, so it branches, commits and opens pull requests the way the team does.</span>

---

<!-- ====== HACK 4 — Data rules ======
Recap of B1 (Swiss data rules) in agent terms. Source: implementation plan §5.
-->

<span class="kicker">Data rules · the short version of Crash Course #1</span>

## The agent sees the structure of the data, never the records

<div class="cols3" style="margin-top: 6px;">
<div class="card"><h3>Real data stays put</h3><p>Challenge datasets live on the HPE / NVIDIA environment, read-only. Analyses run there.</p></div>
<div class="card"><h3>Laptops get samples</h3><p>Each repository has a small synthetic sample in <code>examples/</code>, so code runs anywhere.</p></div>
<div class="card"><h3>Nothing sensitive in git</h3><p>A pre-commit check blocks data files and secrets. Never paste records into a chat tool.</p></div>
</div>

---

<!-- ====== HACK 5 — Before 6 November ======
[CONFIRM before the session] where participants register their GitHub username,
and the challenge-voting link.
-->

<span class="kicker">Before 6 November</span>

## Five things to do

| | What | When |
|---|---|---|
| 1 | **Vote** on the challenges you want to work on | Now: voting is open |
| 2 | A **GitHub account** with two-factor authentication, and your username sent to us | This week |
| 3 | *Optional:* VS Code + one agent on your laptop; try the demo repository | Before 6 Nov |
| 4 | **Crash Course #3**: grant writing for pop-up projects, with the RGO | Thu 29 Oct, 17:00 |
| 5 | Come with one idea for **your** challenge: a need, an opportunity, a question | 6 Nov, 11:00 |


---

<!-- ====== YOUR PLACE 1 — Divider ====== -->
<!-- _class: ink divider -->

<span class="clock">10 min</span>

<span class="kicker">18:50 · Objective 1 · Imagine</span>

# Your place in agentic science

Back to where we started: what you imagined at 17:00, and what you saw tonight.

---

<!-- ====== YOUR PLACE 2 — The room vs. the field ======
Before this slide, open the six poll results in Zoom's Polls/Quizzes panel and
share them. Put the room's majority next to each voice; the question where the
room disagrees most with the voice gets the remaining minutes.
-->

<span class="kicker">The room's answers</span>

## What you imagined, and voices to argue with

| Q | The room | A voice from the field |
|---|---|---|
| 1 · Where first | *poll* | Agentic coding is already removing the engineering bottleneck in modelling (DePasquale) |
| 2 · Scarce skill | *poll* | LLMs are *"a flashlight as opposed to a laser pointer"* (Kim Stachenfeld, DeepMind) |
| 3 · Depth | *poll* | *"Prolific but shallow—generating models faster than we can generate insights"* (DePasquale) |
| 4 · Training | *poll* | Struggling to turn an idea into code is *"a form of disciplined thinking"* (DePasquale) |
| 5 · Literature | *poll* | Incentives already reward producing models over understanding them; vibe modelling could make it worse (Dan Goodman, Imperial) |
| 6 · Reality | **D** · 19% slower | …while feeling 20% faster (METR, 2025) |

---

<!-- ====== YOUR PLACE 3 — Back to the opening question ======
Facilitator: paste back 6–8 answers from the 17:00 chat and sort them live
into the two columns, asking the room. Then the last prompt, in the chat.
Save the chat: it is the B2 record for objective 1.
-->

<span class="kicker">The opening question, revisited</span>

## Where will agentic coding change science?

<div class="cols" style="margin-top: 6px;">
<div class="card">
<h3>What we saw tonight</h3>
<p>Analysis and modelling in minutes · a plan before the code · review as the real work · a pull request as the record of what was checked</p>
</div>
<div class="card">
<h3>Still imagination</h3>
<p>Your answers from 17:00 that nothing tonight showed yet: where your own research, career or field could go</p>
</div>
</div>

<br>

> **Last line in the chat:** *"When agents write the code, the part of my research that stays mine is …"*

---

<!-- ====== YOUR PLACE 4 — Close ======
From module 11 (close). End on time.
-->
<!-- _class: ink -->
<!-- _footer: "" -->

<span class="kicker">See you on 6 November</span>

# Director, not author.

The agent brings **speed and breadth**. You bring **the question, the judgment and the responsibility**. That division of labour is the skill.

<div class="cols3" style="margin-top: 18px;">
<div class="card"><h3>The course</h3><p>github.com/wazaahhh/vibe-coding-crash-course · fork it, star it, open a pull request</p></div>
<div class="card"><h3>Read</h3><p>DePasquale, <i>Models at the speed of thought</i> · Schuck, <i>How, when and why to use agentic AI in our neuroscience labs</i> · both in The Transmitter, 2026</p></div>
<div class="card"><h3>Next</h3><p>Vote on challenges · GitHub account · Crash Course #3 on Thu 29 Oct</p></div>
</div>

<span class="small">Vibe Coding for Scientists · CC BY-NC 4.0 · Thomas Maillart</span>
