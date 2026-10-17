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
