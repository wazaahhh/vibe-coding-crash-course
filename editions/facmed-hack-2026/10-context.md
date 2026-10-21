<!-- ====== CONTEXT 1 — Divider ====== -->
<!-- _class: ink divider -->

<span class="clock">20 min</span>

<span class="kicker">17:05 · Part 1 · Objective 1 · Imagine</span>

# Where this comes from

From an artificial neuron in 1943 to an agent that edits your analysis code. What these tools are, what scientists do with them, and where they fail.

---

<!-- ====== CONTEXT 2 — It started in your field ======
For a neuroscience audience: the idea of artificial neural networks came from
neuroscience. Keep it to two minutes; the point is the lineage.
Sources: McCulloch & Pitts 1943 (Bull. Math. Biophys.); Rosenblatt 1958;
Hopfield 1982 (PNAS); Rumelhart, Hinton & Williams 1986 (Nature);
Krizhevsky, Sutskever & Hinton 2012 (AlexNet); Nobel Prize in Physics 2024.
-->

<span class="kicker">A short history · part 1</span>

## It started in your field

| Year | What happened |
|---|---|
| 1943 | **McCulloch &amp; Pitts** model a neuron as a logic unit: the first artificial neuron |
| 1958 | **Rosenblatt's perceptron**: a network of artificial neurons that learns from examples |
| 1982 | **Hopfield networks**: memories stored as stable states of a network |
| 1986 | **Backpropagation** popularised (Rumelhart, Hinton &amp; Williams): how multi-layer networks learn |
| 2012 | **Deep learning** wins image recognition by a wide margin (AlexNet): GPUs + big data + depth |
| 2024 | **Nobel Prize in Physics** to John Hopfield and Geoffrey Hinton, for the foundations of machine learning with artificial neural networks |

---

<!-- ====== CONTEXT 3 — From next word to agents ======
Sources: Vaswani et al. 2017 "Attention is all you need"; Brown et al. 2020
(GPT-3, 175 billion parameters); GitHub Copilot preview June 2021; ChatGPT
30 Nov 2022; OpenAI o1, Sept 2024; Claude Code (Feb 2025 preview) and OpenAI
Codex (2025); Karpathy coins "vibe coding", Feb 2025.
-->

<span class="kicker">A short history · part 2</span>

## From predicting the next word to editing your code

| Year | What happened |
|---|---|
| 2017 | **The Transformer** ("Attention is all you need"): the architecture behind every modern language model |
| 2020 | **GPT-3**: 175 billion parameters; scale alone produces surprising abilities |
| 2021 | **GitHub Copilot** autocompletes code inside the editor |
| Nov 2022 | **ChatGPT**: language models reach everyone, through a chat window |
| 2023–24 | Claude, GPT-4, open-weight models (Llama, Qwen…); **"reasoning" models** that work step by step before answering |
| 2025 | **Coding agents** (Claude Code, OpenAI Codex, Copilot agent mode) work inside your project; Andrej Karpathy names **"vibe coding"** |
| 2026 | Agents in research labs: model fitting, analysis pipelines, lab AI policies (this week's two pre-reads) |

---

<!-- ====== CONTEXT 4 — What an LLM is ======
Plain language. LLM = large language model. The consequences column is the
part to land: fluent is not the same as true.
-->

<span class="kicker">Under the hood, in plain words</span>

## What a large language model (LLM) actually is

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 4px;">
<div>

1. A very large **neural network** trained to **predict the next word piece** ("token") on a huge share of the written web, books and code.
2. Then **tuned** with examples and human feedback to follow instructions and be helpful.
3. It holds no database of facts: it generates the most **plausible continuation** of what it has been given.

</div>
<div>

| So… | In practice |
|---|---|
| Fluent ≠ true | It can invent a method, a number or a citation, in flawless prose |
| Training cut-off | It does not know what happened after its training data |
| Context window | It only "sees" what fits in its working memory: files, chat, instructions |
| Not deterministic | The same question can get different answers |

</div>
</div>

---

<!-- ====== CONTEXT 5 — From chatbot to agent ======
From module 03 (chat vs agent), with the agent loop made explicit.
-->

<span class="kicker">Module 03 · two modes</span>

## From chatbot to agent

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px;">
<div>

| **Chat** (browser, app) | **Agent** (editor + your project folder) |
|---|---|
| You paste code, data, an error; it answers | It **reads your files, runs code, edits in place** |
| Zero setup | One-time setup |
| **You** carry the context, message after message | It sees the whole project |
| A quick question, a snippet | A real, multi-file analysis |

</div>
<div>

<div class="card">
<h3>An agent is an LLM in a loop with tools</h3>
<p>You give a goal → it <b>plans</b> → it <b>acts</b> (reads a file, runs a script, searches) → it <b>looks at the result</b> or the error → it adjusts → … → it reports back.</p>
<br>
<p><b>You</b> approve the plan, watch the steps, and decide what to keep.</p>
</div>

</div>
</div>

---

<!-- ====== CONTEXT 6 — Why coding first, and what vibe coding means ======
From module 00 ("What vibe coding means"). Karpathy coined the term in a post
in February 2025.
-->

<span class="kicker">Module 00 · why coding came first</span>

## Code is where agents work best, and where "vibe coding" was born

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px;">
<div>

**Why coding first**
- Code is text, and there is a vast public corpus of it.
- Code can be **run**: errors and tests give the agent immediate feedback.
- The result can be **checked**, by the machine and by you.

</div>
<div>

**"Vibe coding"** (Andrej Karpathy, 2025)
- You describe **what you want** in plain language; the model writes the code.
- Tool-agnostic: Claude Code, Codex, Copilot, Cline, or paste-into-chat.

> The honest version for scientists: the vibe is in **how you produce** code, never in whether it's correct.

</div>
</div>

---

<!-- ====== CONTEXT 7 — One sentence in ======
From module 00 ("In practice"). The EEG line speaks to most of the room.
-->

<span class="kicker">Module 00 · in practice</span>

## One sentence in, a working analysis out

- **Neuro / EEG**: *"Load this `.edf`, band-pass 8–12 Hz, plot alpha power per channel as a topomap."* → it wires up MNE, filters, renders the scalp map.
- **Genomics**: *"Here's my RNA-seq counts table: give me a volcano plot, label the top 10 genes by adjusted p-value."* → it reads the file, runs the statistics, returns a labelled figure **and** the code.
- **Climate / field data**: *"30 years of daily rainfall: fit a trend, test it, plot it with a 12-month rolling mean."*
- **Imaging**: *"Count the nuclei in every image in `data/dapi/`, one CSV row per file."* → it plans, writes, runs on 200 images. **You** notice the dense clusters look undercounted, ask for three overlays: touching nuclei had merged.

> The question stays yours. The **plumbing** stops being the bottleneck. Looking, doubting, correcting: that last step is the whole job.

---

<!-- ====== CONTEXT 8 — How scientists use it ======
Sources: Jumper et al. 2021 (AlphaFold 2), Nobel Prize in Chemistry 2024
(Hassabis, Jumper; with Baker); Google "AI co-scientist" (Feb 2025);
Lu et al. 2024 "The AI Scientist" (Sakana, arXiv 2408.06292).
-->

<span class="kicker">How scientists use it today</span>

## Six everyday uses, and a few frontier ones

<div class="cols" style="grid-template-columns: 1.2fr 1fr; gap: 30px;">
<div>

| Everyday | What it does for you |
|---|---|
| **Literature** | find, summarise, compare papers |
| **Analysis code** | cleaning, statistics, figures, pipelines |
| **Modelling** | from a word model to a fitted model in hours |
| **Writing** | editing, restructuring, translating |
| **Learning** | explaining unfamiliar code or methods |
| **Tools** | small apps, dashboards, lab utilities |

</div>
<div>

<div class="card">
<h3>At the frontier</h3>
<p><b>AlphaFold</b> predicts protein structures (Nobel Prize in Chemistry 2024) · <b>AI "co-scientists"</b> propose hypotheses (Google, 2025) · <b>automated research pipelines</b> draft whole studies (The AI Scientist, 2024), with mixed quality</p>
</div>

</div>
</div>

---

<!-- ====== CONTEXT 9 — In neuroscience ======
Sources: Luo et al. 2024, "Large language models surpass human experts in
predicting neuroscience results", Nature Human Behaviour (BrainBench);
DePasquale 2026 and Schuck 2026, The Transmitter (the two pre-reads).
-->

<span class="kicker">And in neuroscience</span>

## Already happening in our field

<div class="cols3" style="margin-top: 6px;">
<div class="card">
<h3>Predicting results</h3>
<p>On a benchmark of real neuroscience abstracts, LLMs predicted which result was the true one better than human experts (Luo et al., <i>Nature Human Behaviour</i>, 2024).</p>
</div>
<div class="card">
<h3>Models in an afternoon</h3>
<p>Experimentalists without a modelling collaborator can get a fitted model, with an explanation, in an afternoon (DePasquale, pre-read 1).</p>
</div>
<div class="card">
<h3>A pipeline in a day</h3>
<p>A cognitive-neuroscience lab prototyped a complex decoding pipeline for its own data within a day, then wrote a lab AI policy (Schuck, pre-read 2).</p>
</div>
</div>

<br>

> Which of these would change *your* week first?

---

<!-- ====== CONTEXT 10 — POLL 1 · Where first ======
Opinion, no right answer. Zoom: multiple choice, up to two. Show the result
right away. Push: ask someone who picked the least-chosen option to defend it.
Most current evidence of real change is in A (the pre-read's argument) and C;
B is where the money is going (autonomous labs); D and E are where the policy
fights are.
-->

<span class="qnum">Poll 1 of 6 · Where first</span>

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

<span class="small" style="display:block; margin-top: 10px;">Zoom poll now · results right after.</span>

---

<!-- ====== CONTEXT 11 — Opportunities ======
From module 01 ("Why it matters"), plus two lines for research.
-->

<span class="kicker">Module 01 · the opportunities</span>

## Code was friction between a question and an answer

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 26px; margin-top: 6px;">
<div class="card"><h3>The plumbing stops being the bottleneck</h3><p>Hours of searching forums and documentation become minutes.</p></div>
<div class="card"><h3>Exploration gets cheap</h3><p>Five model specifications, three plots, two normalisations, in the time of one.</p></div>
<div class="card"><h3>The barrier drops for the whole lab</h3><p>The student who "can't code" can build a working pipeline; experimentalists can model.</p></div>
<div class="card"><h3>Scripts over clicks</h3><p>An analysis written as code can be re-run, reviewed and shared: better for reproducibility.</p></div>
</div>

<br>

> ⚠️ It is also trivially easy to produce **plausible · beautiful · wrong**.

---

<!-- ====== CONTEXT 11b — Pre-read 1: DePasquale, the opportunities ======
DePasquale (Boston University), The Transmitter, 16 June 2026. Starting point:
Larry Abbott's "Theoretical neuroscience rising" (Neuron, 2008): models can be
explored and rejected faster than experiments. In practice the engineering
(word model → equations → code → fit to data) throttled that speed. Agentic
coding removes much of the bottleneck, in four directions.
-->

<span class="kicker">Pre-read 1 · DePasquale, <i>Models at the speed of thought</i> · the opportunities</span>

## "Models at the speed of thought": four directions

<div class="cols" style="grid-template-columns: repeat(4, 1fr); gap: 14px; margin-top: 6px;">
<div class="card"><h3>1 · Experimentalists model</h3><p>Fit a model to your own data without waiting months for a modelling collaborator.</p></div>
<div class="card"><h3>2 · Theorists iterate</h3><p>Try, test and reject new models in hours, at last at the speed theory promised.</p></div>
<div class="card"><h3>3 · Search model space</h3><p>AI-guided search (AlphaEvolve-style) explores many candidate models at scale.</p></div>
<div class="card"><h3>4 · Maths opens up</h3><p>Mathematically heavy models become reachable for people stronger at code than at the blackboard.</p></div>
</div>

<br>

> *"Major new discoveries are likely to come from humans generating insights, just as they have always done…"* <span class="small">Larry Abbott, Columbia, in his response</span>

---

<!-- ====== CONTEXT 11c — Pre-read 1: the challenges, and seven responses ======
Verbatim quotes from the essay and its seven responses (checked on the page).
Use this slide to open a two-minute discussion: which risk worries you most?
-->

<span class="kicker">Pre-read 1 · the challenges · and the field answers back</span>

## "Prolific but shallow"?

<div class="cols" style="grid-template-columns: 1fr 1.25fr; gap: 26px;">
<div>

> *"The field risks becoming prolific but shallow—generating models faster than we can generate insights."*
> <span class="small">Brian DePasquale</span>

- The struggle of turning an idea into equations and code is *"a form of disciplined thinking"*, especially for trainees.
- AI-guided search will also produce *"artifacts of the search process"*.
- His advice: keep stepping away from the AI to exercise your own judgment.

</div>
<div>

| Respondent | The worry, in their words |
|---|---|
| **Dan Goodman**, Imperial | Code that seems to test your idea but hides errors: *"This isn't a theoretical risk; it's something that seems to crop up very regularly in practice."* |
| **Julijana Gjorgjieva**, TUM | Expertise is needed *"to recognize when an AI system is inventing concepts that do not actually exist."* |
| **Kim Stachenfeld**, DeepMind | LLMs are *"a flashlight as opposed to a laser pointer"* |
| **Anthony Zador**, CSHL | *"LLMs are like genies: They can grant you almost any wish, but you have to be very careful about what you ask for."* |

</div>
</div>

---

<!-- ====== CONTEXT 12 — Pitfalls ======
From module 02 ("Where it shines, where it bites" and "A 30-second horror
story") and module 09 (safety rules).
-->

<span class="kicker">Modules 02 &amp; 09 · the pitfalls</span>

## Strongest on syntax, weakest on truth

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 30px;">
<div>

| Trust, but skim | Slow down: it fails quietly here |
|---|---|
| Plotting, formatting | **Domain correctness**: units, time zones, scales |
| Boilerplate, file reading | **Statistics**: the wrong-but-plausible test, leakage |
| Explaining code | **Your specific method** |
| Translating languages | **Ground truth**: data meaning, citations |

</div>
<div>

**The failure is never a crash, it's a clean run with a wrong number:**
- `df.dropna()` silently deletes 40% of rows
- test data leaks into training → a 0.98 that evaporates
- a hallucinated citation nobody checked

**And beyond the code:** patient data pasted into cloud tools · skills that never develop · a field that becomes *"prolific but shallow"* (DePasquale)

</div>
</div>

---

<!-- ====== CONTEXT 13 — What the science says ======
From module 02 ("What the science says", both slides). Kosmyna et al. is a
preprint under active debate: cite as suggestive.
-->

<span class="kicker">Module 02 · what the science says</span>

## The danger is a confident answer that switches your checking off

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 26px;">
<div>

- **Automation bias &amp; complacency**: we over-trust automated output and stop checking it *(Parasuraman &amp; Manzey, 2010)*.
- **Cognitive offloading**: the more knowledge workers trust generative AI, the less critical thinking they report *(Lee et al., CHI 2025)*.
- **Illusion of explanatory depth**: fluent output makes you *feel* you understand what you couldn't rebuild *(Rozenblit &amp; Keil, 2002)*.

</div>
<div>

- **"Cognitive debt"**: heavy LLM use while writing went with weaker memory of one's own text and more homogeneous prose *(Kosmyna et al., 2025, preprint)*.
- **Generation effect**: you understand and retain what *you* produce far better than what you only read *(Slamecka &amp; Graf, 1978)*.

> Offload the typing. **Never offload the understanding** your name depends on.

</div>
</div>

---

<!-- ====== CONTEXT 14 — POLL 2 · Reality check ======
The one poll with an answer: D. Share the result right away, then the next
slide.
-->

<span class="qnum">Poll 2 of 6 · A reality check</span>

## In a 2025 randomised trial, experienced open-source developers worked on their own projects with and without AI tools. With AI, they were…

<div class="opts">
<div class="opt"><b>A</b>about 40% faster</div>
<div class="opt"><b>B</b>about 20% faster</div>
<div class="opt"><b>C</b>no faster and no slower</div>
<div class="opt"><b>D</b>about 19% slower</div>
</div>

<span class="small" style="display:block; margin-top: 10px;">Zoom poll now · the answer is on the next slide.</span>

---

<!-- ====== CONTEXT 15 — The perception gap ======
Caveat to say out loud: early-2025 tools, experts in large mature repositories
they knew intimately. METR says the result may not hold for small new projects
or unfamiliar code, which is closer to a 32-hour hack. The lesson is the
perception gap.
-->

<span class="kicker">Poll 2 · the answer</span>

## D: about 19% slower, while feeling 20% faster

<div class="cols" style="grid-template-columns: 1fr 1.3fr; gap: 30px; align-items: center;">
<div>

<div class="card"><div style="font-size:2.6em; font-weight:800; color:var(--accent); line-height:1">+19%</div><p>time taken with AI tools, measured</p></div>
<br>
<div class="card"><div style="font-size:2.6em; font-weight:800; color:var(--science); line-height:1">−20%</div><p>time the same developers <i>believed</i> AI had saved them, afterwards</p></div>

</div>
<div>

- 16 experienced developers, 246 real tasks on their own projects, early-2025 tools.
- METR's own caveat: experts in large codebases they knew by heart; it may not hold for small new projects, closer to a hackathon.
- **The lesson is the gap**: your feeling of speed is a poor measurement. That is thinking fast and slow, in one number.

<span class="small">METR (Model Evaluation &amp; Threat Research), "Measuring the impact of early-2025 AI on experienced open-source developer productivity", July 2025.</span>

</div>
</div>

---

<!-- ====== CONTEXT 16 — The thesis ======
From module 00 ("The thesis"). Bridge to Part 2.
-->
<!-- _class: ink -->

<span class="kicker">Module 00 · the thesis we'll repeat</span>

# You move from **author** of code to **director** of code.

Your job becomes **intent · judgment · verification**. The syntax is the agent's.

<br>

<span class="small">Next: how to do that job well.</span>
