<!-- ====== CONTEXT 1 — Divider ====== -->
<!-- _class: ink divider -->

<span class="clock">25 min</span>

<span class="kicker">17:05 · Part 1 · Objective 1 · Imagine</span>

# Where this comes from

From an artificial neuron in 1943 to an agent that edits your analysis code. What these tools are, what scientists do with them, and where they fail.

---

<!-- ====== CONTEXT 2 — It started in your field ======
For a neuroscience audience: the idea of artificial neural networks came from
neuroscience. Keep it to two minutes; the point is the lineage.
Definitions (say them only if asked):
- Artificial neuron (McCulloch & Pitts): a unit that adds up its weighted inputs
  and "fires" (outputs 1) when the sum passes a threshold.
- Perceptron (Rosenblatt): one layer of such units whose weights are LEARNED from
  labelled examples: wrong answer → nudge the weights.
- Neural network (multi-layer): layers of units, every connection a weight; the
  hidden layers build intermediate features the output layer combines.
- Hopfield network: a recurrent network in which memories are stable states
  (energy minima) the network settles into.
- Backpropagation: computes how much each weight contributed to the error and
  adjusts all weights, layer by layer, from the output backwards.
- Deep learning: neural networks with many layers, trained on large data with GPUs.
Sources: McCulloch & Pitts 1943 (Bull. Math. Biophys.); Rosenblatt 1958;
Hopfield 1982 (PNAS); Rumelhart, Hinton & Williams 1986 (Nature);
Krizhevsky, Sutskever & Hinton 2012 (AlexNet); Nobel Prize in Physics 2024.
Diagrams: drawn for this deck.
-->

<span class="kicker">A short history · part 1</span>

## It started in your field

<div class="cols" style="grid-template-columns: 1.25fr 1fr; gap: 26px; align-items: start;">
<div>

| Year | What happened |
|---|---|
| 1943 | **McCulloch &amp; Pitts** model a neuron as a logic unit: the first artificial neuron |
| 1958 | **Rosenblatt's perceptron** learns its weights from examples |
| 1982 | **Hopfield networks**: memories as stable states of a network |
| 1986 | **Backpropagation** (Rumelhart, Hinton &amp; Williams): how multi-layer networks learn |
| 2012 | **Deep learning** wins image recognition (AlexNet): GPUs + data + depth |
| 2024 | **Nobel Prize in Physics** to Hopfield and Hinton |

</div>
<div>

<div class="fig"><img src="assets/perceptron.svg" alt="Perceptron diagram" style="height:190px"><div class="cap">Perceptron: weighted inputs → sum → threshold</div></div>
<div class="fig" style="margin-top:8px"><img src="assets/neural_network.svg" alt="Multi-layer neural network diagram" style="height:190px"><div class="cap">Multi-layer network, trained by backpropagation</div></div>

</div>
</div>

---

<!-- ====== CONTEXT 3 — From next word to agents ======
Definitions:
- Token: a piece of text, a word or part of a word ("neur" + "on").
- Parameter (weight): a number learned in training; GPT-3 has 175 billion.
- Transformer: the architecture behind every modern language model: a stack of
  layers, each with self-attention and a feed-forward network; processes all
  tokens of a text in parallel.
- Self-attention: lets every token weigh every other token when building its
  representation ("it" looks back at "neuron").
- GPT: "generative pre-trained transformer".
- Reasoning model: trained to work through intermediate steps before answering.
- Coding agent: a language model in a loop with tools (files, terminal, tests).
Sources: Vaswani et al. 2017 "Attention is all you need"; Brown et al. 2020
(GPT-3, 175 billion parameters); GitHub Copilot preview June 2021; ChatGPT
30 Nov 2022; OpenAI o1, Sept 2024; Claude Code (Feb 2025 preview) and OpenAI
Codex (2025); Karpathy coins "vibe coding", Feb 2025.
-->

<span class="kicker">A short history · part 2</span>

## From predicting the next word to editing your code

<div class="cols" style="grid-template-columns: 1.3fr 1fr; gap: 24px; align-items: start;">
<div>

| Year | What happened |
|---|---|
| 2017 | **The Transformer** ("Attention is all you need") |
| 2020 | **GPT-3**: 175 billion parameters; scale brings surprising abilities |
| 2021 | **GitHub Copilot** autocompletes code in the editor |
| Nov 2022 | **ChatGPT**: language models reach everyone |
| 2023–24 | Claude, GPT-4, open-weight models; **"reasoning" models** |
| 2025 | **Coding agents** work inside your project; Karpathy names **"vibe coding"** |
| 2026 | Agents in research labs (this week's two pre-reads) |

</div>
<div>

<div class="fig"><img src="assets/transformer.svg" alt="Transformer diagram with self-attention" style="width:100%"><div class="cap">A Transformer layer: each word attends to the others, then a feed-forward step; stacked dozens of times</div></div>

</div>
</div>

---

<!-- ====== CONTEXT 4 — How an LLM works ======
Walk through the five steps on the diagram. Then the four consequences: fluent
is not the same as true; it only knows its training data; it only "sees" what
fits in its context window; the same question can give different answers
(step 4 picks among probabilities).
-->

<span class="kicker">Under the hood, in plain words</span>

## How a large language model (LLM) writes, one token at a time

<div class="fig"><img src="assets/llm_schematic.svg" alt="Schematic: text to tokens to transformer layers to next-token probabilities, then append and repeat" style="width:100%"></div>

<div class="cols" style="grid-template-columns: repeat(4, 1fr); gap: 12px; margin-top: 6px;">
<div class="card"><h3>Fluent ≠ true</h3><p>It writes the most plausible continuation; it can invent a method or a citation.</p></div>
<div class="card"><h3>Training cut-off</h3><p>It knows nothing after its training data.</p></div>
<div class="card"><h3>Context window</h3><p>It only "sees" what fits in its working memory.</p></div>
<div class="card"><h3>Not deterministic</h3><p>Same question, possibly a different answer.</p></div>
</div>

---

<!-- ====== CONTEXT 5 — Two environments ======
From module 03 (chat vs agent). The pictures are faithful mock-ups of the two
typical set-ups (replace assets/env_chat.png and assets/env_agent.png with real
screenshots if you prefer). Point out in the agent picture: the project's files
on the left, the code in the middle, the agent on the right, and the terminal
showing the run and the saved history (git) at the bottom.
-->

<span class="kicker">Module 03 · two environments</span>

## From chatbot to agent

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 22px; margin-top: 2px;">
<div class="fig">
<img src="assets/env_chat.png" alt="A chat assistant in the browser: the user uploads sleep.csv and gets code to copy into a notebook" style="border-radius:10px; border:1px solid var(--line)">
<div class="cap"><b>Chat</b> (browser, app): you paste code, data and errors; it answers; <b>you</b> carry the context and copy the code back.</div>
</div>
<div class="fig">
<img src="assets/env_agent.png" alt="VS Code with an AI agent panel: project files, the edited script, the agent's plan, a run and saved history in the terminal" style="border-radius:10px; border:1px solid var(--line)">
<div class="cap"><b>Agent</b> (VS Code + your project folder): it reads your files, plans, edits, runs, sees the error, and saves; <b>you</b> approve.</div>
</div>
</div>

> An agent is an LLM **in a loop with tools**: goal → plan → act → look at the result → adjust → report.

---

<!-- ====== CONTEXT 6 — Why coding first ======
From module 00 ("What vibe coding means"). Source for the usage figures:
Anthropic Economic Index, launch report, 10 Feb 2025: "37.2% of queries sent to
Claude were in this category" (computer and mathematical, largely software
engineering); report of 24 Mar 2026: "Coding remains the most common use on our
platforms", 35% of Claude.ai conversations, and coding tasks "continue to
migrate ... to more automated workflows" in API traffic (incl. Claude Code).
Caveat (Anthropic's own): Claude is marketed as a coding model, so coding may be
over-represented.
-->

<span class="kicker">Module 00 · why coding came first</span>

## Software development is where agentic AI is used most

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 28px;">
<div>

**Why coding first**
- Code is text, and there is a vast public corpus of it.
- Code can be **run**: errors and tests give immediate feedback.
- The result can be **checked**, by the machine and by you.

<div class="card" style="margin-top:10px"><div style="font-size:2.3em; font-weight:800; color:var(--accent); line-height:1">37%</div><p>of conversations with one major assistant were software and maths tasks, by far the first use (Anthropic Economic Index, 2025); still first in 2026, and moving from chat to <b>autonomous agent workflows</b>.</p></div>

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

<!-- ====== CONTEXT 8 — LIVE QUIZ · How do you use AI? ======
Live quiz app, question "uses" (multi-select). Show the QR and link, give 60 s,
then open the presenter view's live results; the next slide sets them against
how scientists use it today.
-->
<!-- _class: ink -->

<span class="kicker">Live quiz · on your phone or laptop</span>

## What have you already used AI for in your research? *Tick all that apply.*

<div class="cols" style="grid-template-columns: 1.2fr 1fr; gap: 30px; align-items: center; margin-top: 10px;">
<div>

Finding and summarising papers · analysis code · modelling · writing and editing · learning or explaining code and methods · building small tools · **nothing yet**

<br>

<span class="small">Anonymous. Results appear live; we look at them together on the next slide.</span>

</div>
<div>

<div class="quizbox big" style="position:static; display:inline-flex;"><img src="assets/quiz_qr.svg" alt="QR code to the live quiz"><div><b>Live quiz</b><span>{{QUIZ_URL}}</span></div></div>

</div>
</div>

---

<!-- ====== CONTEXT 9 — How scientists use it today ======
Put the room's live results (presenter view) next to this list: where is the
room ahead, where behind?
-->

<span class="kicker">How scientists use it today · and how this room does</span>

## Six everyday uses

| Everyday use | What it does for you |
|---|---|
| **Literature** | find, summarise, compare papers |
| **Analysis code** | cleaning, statistics, figures, pipelines |
| **Modelling** | from a word model to a fitted model in hours |
| **Writing** | editing, restructuring, translating |
| **Learning** | explaining unfamiliar code or methods |
| **Tools** | small apps, dashboards, lab utilities |

<br>

> Compare with the room's answers on the quiz: which uses are we missing?

---

<!-- ====== CONTEXT 10 — At the frontier ======
Diagrams drawn for this deck, describing how each system works.
- AlphaFold 2 (Jumper et al., Nature 2021): predicts a protein's 3-D structure
  from its amino-acid sequence, with a per-residue confidence score (pLDDT,
  colours as in the AlphaFold database). Nobel Prize in Chemistry 2024 (Hassabis,
  Jumper; with Baker for protein design). Not a language model, but the same
  deep-learning family.
- AI co-scientist (Google, Feb 2025): several agents generate, review, debate,
  rank in a tournament and refine hypotheses for a scientist's goal.
- The AI Scientist (Lu et al., Sakana AI, 2024, arXiv 2408.06292): automates
  idea → code and experiments → paper → automated review, end to end. Its papers
  were of mixed quality.
-->

<span class="kicker">At the frontier</span>

## Beyond the chat window

<div class="cols3" style="margin-top: 4px;">
<div class="fig"><img src="assets/frontier_alphafold.svg" alt="AlphaFold: sequence to folded structure" style="width:100%"><div class="cap" style="font-size:0.7em"><b>AlphaFold</b> predicts protein structures from sequence · Nobel Prize in Chemistry 2024</div></div>
<div class="fig"><img src="assets/frontier_coscientist.svg" alt="AI co-scientist: agents generating, reviewing, debating and ranking hypotheses" style="width:100%"><div class="cap" style="font-size:0.7em"><b>AI "co-scientist"</b>: agents generate, debate and rank hypotheses · Google, 2025</div></div>
<div class="fig"><img src="assets/frontier_aiscientist.svg" alt="The AI Scientist: idea, code, paper, review loop" style="width:100%"><div class="cap" style="font-size:0.7em"><b>The AI Scientist</b> drafts whole studies end to end, with mixed quality · Sakana AI, 2024</div></div>
</div>

---

<!-- ====== CONTEXT 11 — BrainBench ======
Luo, X., …, Love, B. C. Large language models surpass human experts in
predicting neuroscience results. Nature Human Behaviour (2024).
doi:10.1038/s41562-024-02046-9 · arXiv 2403.03230. Numbers from arXiv v4.
Discussion prompt: predicting which result was published is not the same as
discovering; models learn the literature's patterns, including its biases.
-->

<span class="kicker">In neuroscience · Luo et al., <i>Nature Human Behaviour</i>, 2024</span>

## Can an LLM predict a neuroscience result better than you?

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 26px;">
<div>

**The approach: BrainBench**
- **200 test cases** from 2023 *Journal of Neuroscience* abstracts, across five fields.
- For each, experts wrote a **version with altered results**, coherent but wrong; background and methods unchanged.
- The task: **which abstract is the real one?**
- LLMs choose the version they find less surprising (lower perplexity); **171 neuroscience experts** took the same test.

</div>
<div>

**The results**

<div class="cols" style="grid-template-columns: 1fr 1fr; gap: 12px;">
<div class="card"><div style="font-size:2.2em; font-weight:800; color:var(--accent); line-height:1">81.4%</div><p>LLMs, on average</p></div>
<div class="card"><div style="font-size:2.2em; font-weight:800; color:var(--science); line-height:1">63.4%</div><p>human experts</p></div>
</div>

- Ahead in **every subfield**; well calibrated: more confident when right.
- **BrainGPT**, a small model further trained on neuroscience literature, did ~3 points better.
- No sign of memorisation; they integrate background and methods.

</div>
</div>

<span class="small">doi.org/10.1038/s41562-024-02046-9 · Predicting what was published is not discovering: models learn the literature's patterns, biases included.</span>

---

<!-- ====== CONTEXT 12 — Explore and reject fast: our example ======
Thomas's own work (AutismBrainBehavior, detection-repetitive-behaviors-asd,
June 2026). Unpublished: say "our work in progress"; no session IDs, no
clinical data on screen. The figure is the method schematic on a synthetic
signal. The point, with pre-read 1: when building and testing costs hours, you
find out fast whether an approach can work, and stop early.
[CONFIRM with Thomas: the slide follows what the repository shows (rebuild,
re-run, reproducibility audit, benchmark scaffold).]
-->
<!-- _class: dense -->

<span class="kicker">Models in an afternoon · our own example · pre-read 1: doi.org/10.53053/FVAU9567</span>

## Explore and reject fast: detecting repetitive movements in autism

<div class="cols" style="grid-template-columns: 1.15fr 1fr; gap: 26px; align-items: start;">
<div>

**The idea**: spot hand-flapping and rocking automatically in videos of free-play sessions (Geneva Autism Cohort), with a training-free kinematic method: body keypoints → joint angles along the arm → wavelet scalogram → episodes.

**With an agent, in a few working sessions**: the legacy code rebuilt as a tested package, re-run on the cohort, and a benchmark against a supervised deep-learning baseline (ASDMotion) scaffolded.

**What it showed, fast**: the method did not reproduce. Re-runs found extra episodes in every session checked; the recording behind the paper's figure was the wrong one; left and right arm signals were swapped. No easy path: fix the inputs before investing in the model.

</div>
<div>

<div class="fig"><img src="assets/asd_wavelet_method.png" alt="Method schematic: oscillating input signal, Morlet wavelet family, and the resulting scalogram" style="border-radius:8px; border:1px solid var(--line)"><div class="cap">The method on a synthetic signal: oscillation → wavelets → scalogram</div></div>

</div>
</div>

---

<!-- ====== CONTEXT 13 — A pipeline in a day: our example ======
Thomas's own work (AutismBrainBehavior, 4by4k-pipeline), Marie Schaer's group.
Facts from the repository's benchmarks and git history: whole pipeline built
on 18 Sep 2026 (10:46 → 18:29) with an agent; calibration solved before, in
situ with a checkerboard (Aug–Sep 2026); validated on a real 49-min session:
296,294 frames, 19.8 min from submission to 3-D, 99.89% agreement with the
reference pipeline; 2-D pose at 5.5× real time; audio sync 6–14 ms RMS.
Picture: stick figures from the room-4 reconstruction (gen_social), no video
frames, no faces. Do not name the session.
Governance point (bridge to pre-read 2): a guard in the code blocks the agent
from the participant data folders.
[CONFIRM] "hundreds of hours" (from Marie Schaer's crash course).
-->
<!-- _class: dense -->

<span class="kicker">A pipeline in a day · our own example · pre-read 2: doi.org/10.53053/NSSZ1001</span>

## Four 4K cameras, one 3-D scene, built in a day

<div class="cols" style="grid-template-columns: 1fr 1.05fr; gap: 24px; align-items: start;">
<div>

**Setting**: clinical assessment rooms, four 4K corner cameras, a child with a clinician (and a parent), 20–60 min sessions (Marie Schaer's group). Cameras calibrated beforehand, in the room, with a checkerboard.

**Day 1 with an agent** (18 Sep 2026): 2-D pose at 5.5× real time · audio sync across cameras (6–14 ms) · identities from geometry · metric 3-D · cluster automation · a quality-check app.

**Same day, a real 49-min session**: 296,294 frames → 3-D in **19.8 min**, **99.89%** agreement with the reference. Ready for the lab's archive: hundreds of hours (see Marie Schaer's crash course).

<span class="small">A guard in the code keeps the agent away from participant data.</span>

</div>
<div>

<div class="fig"><img src="assets/room4_3d.png" alt="3-D reconstruction of a clinical room: child, clinician and parent as stick figures, four corner cameras" style="border-radius:10px"><div class="cap">Four calibrated corner cameras → one metric 3-D scene · child (blue), clinician (orange), parent (green)</div></div>

</div>
</div>

---

<!-- ====== CONTEXT 14 — Live quiz · Where first ======
Opinion, no right answer. Live quiz app, multi-select (up to two). Show the
results right away. Push: ask someone who picked the least-chosen option to
defend it. Analysis and modelling is where the evidence of change is today
(pre-read 1, the two examples you just saw); automated labs are where the
money is going; writing and peer review are where the policy fights are.
-->

<span class="qnum">Poll 1 of 6 · Where first</span>

## Where has agentic coding changed, or will it change, research practice most in the next five years? *Pick up to two.*

<div class="opts" style="width: 64%;">
<div class="opt"><b>A</b>Analysing data and building models</div>
<div class="opt"><b>B</b>Designing and running experiments: automated labs</div>
<div class="opt"><b>C</b>Reading and synthesising the literature</div>
<div class="opt"><b>D</b>Writing papers and grants</div>
</div>
<div class="opts" style="grid-template-columns: 1fr; margin-top: 14px; width: 64%;">
<div class="opt"><b>E</b>Peer review and replication</div>
</div>

<div class="quizbox"><img src="assets/quiz_qr.svg" alt="QR code to the live quiz"><div><b>Vote live</b><span>{{QUIZ_URL}}</span></div></div>

---

<!-- ====== CONTEXT 15 — Opportunities ======
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

<!-- ====== CONTEXT 16 — Pre-read 1: DePasquale, the opportunities ======
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

<!-- ====== CONTEXT 17 — Pre-read 1: the challenges, and seven responses ======
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

<!-- ====== CONTEXT 18 — Pitfalls ======
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

<!-- ====== CONTEXT 19 — What the science says ======
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

<!-- ====== CONTEXT 20 — POLL 2 · Reality check ======
The one poll with an answer: D. Share the result right away, then the next
slide.
-->

<span class="qnum">Poll 2 of 6 · A reality check</span>

## In a 2025 randomised trial, experienced open-source developers worked on their own projects with and without AI tools. With AI, they were…

<div class="opts" style="width: 64%;">
<div class="opt"><b>A</b>about 40% faster</div>
<div class="opt"><b>B</b>about 20% faster</div>
<div class="opt"><b>C</b>no faster and no slower</div>
<div class="opt"><b>D</b>about 19% slower</div>
</div>

<div class="quizbox"><img src="assets/quiz_qr.svg" alt="QR code to the live quiz"><div><b>Vote live</b><span>{{QUIZ_URL}}</span></div></div>

---

<!-- ====== CONTEXT 21 — The perception gap ======
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

<!-- ====== CONTEXT 22 — The thesis ======
From module 00 ("The thesis"). Bridge to Part 2.
-->
<!-- _class: ink -->

<span class="kicker">Module 00 · the thesis we'll repeat</span>

# You move from **author** of code to **director** of code.

Your job becomes **intent · judgment · verification**. The syntax is the agent's.

<br>

<span class="small">Next: how to do that job well.</span>
