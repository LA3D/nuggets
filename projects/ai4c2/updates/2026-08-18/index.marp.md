---
marp: true
theme: ai4c2
paginate: true
footer: "AI4C2 · Agentic AI for C2 Platforms"
title: "Beyond the Model: Harnesses and Architectures for Language Agents"
description: "AI4C2 research foundations"
author: "Charles F. Vardeman II"
---

<!-- _class: title -->

<div class="eyebrow">AI4C2 · research foundations</div>

# Beyond the Model

<p class="subtitle">Harnesses and Architectures for Language Agents</p>

<div class="meta">
Charles F. Vardeman II<br>
Center for Research Computing, University of Notre Dame<br>
August 18, 2026
</div>

<!--
Frame the talk as a progression from a language model to an engineered agent system.
The goal is a shared vocabulary and a concrete first research experiment.
-->

---

<div class="eyebrow">Language models</div>

## An LLM predicts a continuation

<p class="lede">A large language model maps the tokens already in its context to probabilities for what token should come next.</p>

<div class="grid three">
  <div class="card"><h3>Context</h3><p>Instructions, examples, retrieved information, and the conversation so far.</p></div>
  <div class="card amber-border"><h3>Model</h3><p>A trained neural network transforms that context into a distribution over tokens.</p></div>
  <div class="card teal"><h3>Continuation</h3><p>Sampling one token at a time produces text—and can request structured tool calls.</p></div>
</div>

<!--
Use Karpathy's video as the recommended deeper introduction. The base operation is still
next-token prediction, even when the resulting behavior looks rich.
-->

---

<div class="eyebrow">Further viewing</div>

## Build the full mental model—from tokens to ChatGPT

<div class="single-video">
  <a href="https://youtu.be/7xTGNNLPyMI"><img src="assets/video-karpathy-llms.jpg" alt="Video thumbnail showing Andrej Karpathy beside a visualization of the computations inside ChatGPT"></a>
  <div class="video-notes">
    <span class="video-speaker">Andrej Karpathy · recommended introduction</span>
    <h3>Deep Dive into LLMs like ChatGPT</h3>
    <ul>
      <li>How text becomes tokens and next-token predictions</li>
      <li>How pretraining and post-training shape behavior</li>
      <li>Why tools and agent loops extend the base model</li>
    </ul>
  </div>
</div>

<p class="microcopy"><a href="https://youtu.be/7xTGNNLPyMI">Watch: “Deep Dive into LLMs like ChatGPT”</a> · long-form visual introduction.</p>

<!--
Offer this as the comprehensive optional introduction. It supplies the mental model for
tokens, training, inference, tool use, and agentic behavior that the rest of the deck then
separates into individual architectural layers.
-->

<!--
<div class="eyebrow">Tool anatomy</div>

## A tool connects language to an ordinary function

<p class="lede">The model is shown a machine-readable contract. The harness connects that contract to executable code.</p>

<div class="contract-cols">
  <div>
    <pre><code><span class="code-key">name:</span> search_reports
<span class="code-key">description:</span> Find relevant reports
<span class="code-key">input_schema:</span>
  <span class="code-key">query:</span>  <span class="code-type">string</span>
  <span class="code-key">limit:</span>  <span class="code-type">integer</span>

<span class="code-comment"># bound by the harness to:</span>
<span class="code-key">implementation:</span> search_reports(query, limit)</code></pre>
    <p class="microcopy">The contract enters model context; the implementation remains outside the model.</p>
  </div>
  <ul class="clean-list">
    <li class="teal-dot"><strong>Language-facing contract</strong><br><span>Name, purpose, arguments, types, and constraints create a vocabulary for requesting action.</span></li>
    <li><strong>Harness binding</strong><br><span>Maps the advertised name to Python, JavaScript, a database query, a command, or an API.</span></li>
    <li class="amber-dot"><strong>Structured boundary</strong><br><span>Arguments and results cross as data—not as unconstrained executable prose.</span></li>
  </ul>
</div>

<!--
The tool is not a special kind of reasoning inside the model. It is an interface boundary.
The harness owns the binding to local code, a service, a database, or another executable system.
-->

---

<!-- _class: compact-title -->

<div class="eyebrow">Tool execution</div>

## The model requests an action; the harness executes it

<img class="tool-map-image" src="assets/tool-execution.svg" alt="A language model emits a structured tool call; the harness validates and invokes an ordinary software function, then returns the result as context">

<p class="microcopy">The LLM proposes the call. The harness mediates every crossing of the language–software boundary.</p>

<!--
The model emits tokens in a constrained structured form; it does not directly run Python
or reach a network. Errors are observations too, allowing the model to revise its request.
-->

---

<div class="eyebrow">From generation to action</div>

## An agent puts tools in a loop

<p class="lede">“An LLM agent runs tools in a loop to achieve a goal.”</p>

<div class="grid three">
  <div class="card amber-border"><h3>1 · Goal</h3><p>A bounded objective and a condition for stopping.</p></div>
  <div class="card"><h3>2 · Tools</h3><p>Actions that retrieve information or change an external environment.</p></div>
  <div class="card teal"><h3>3 · Feedback</h3><p>Tool results return as observations that shape the next model call.</p></div>
</div>

<p class="microcopy">Definition: <a href="https://simonwillison.net/2025/Sep/18/agents/">Simon Willison, “I think ‘agent’ may finally have a widely enough agreed upon definition.”</a></p>

<!--
The loop supplies short-term memory through its interaction history. Long-term memory
enters through additional stores and tools controlled by the harness.
-->

---

<!-- _class: compact-title -->

<div class="eyebrow">Training dynamics</div>

## Memorization and generalization can arrive at different times

<img class="grokking-intro" src="assets/grokking-intro.gif" alt="Animated grokking example: training accuracy rises quickly while test accuracy remains near chance, then test accuracy rises sharply after prolonged training">

<p class="microcopy">Animation: <a href="https://pair.withgoogle.com/explorables/grokking/">Pearce et al., “Do Machine Learning Models Memorize or Generalize?”</a> · phenomenon: <a href="https://arxiv.org/abs/2201.02177">Power et al., “Grokking.”</a></p>

<!--
Grokking is a controlled phenomenon, demonstrated most clearly on small algorithmic
tasks. Let the animation carry the explanation: memorization arrives early, internal
structure develops during the apparent plateau, and held-out generalization arrives late.
-->

---

<!-- _class: compact-title -->

<div class="eyebrow">Inference-time adaptation</div>

## Examples in the prompt teach a temporary task

<div class="undergrad-icl">
  <div class="task-definition">
    <span>Task · sentiment classification</span>
    <p>Decide whether a review expresses a <strong>positive</strong> or <strong>negative</strong> opinion.</p>
  </div>
  <div class="prompt-example">
    <small>PROMPT</small>
    <p class="prompt-instruction">Classify each review as <strong>POSITIVE</strong> or <strong>NEGATIVE</strong>.</p>
    <div class="sentiment-row"><q>I loved this movie.</q><b>POSITIVE</b></div>
    <div class="sentiment-row"><q>This was terrible.</q><b class="negative">NEGATIVE</b></div>
    <div class="sentiment-row new-review"><q>Surprisingly enjoyable.</q><span>?</span></div>
  </div>
  <div class="completion-arrow">→</div>
  <div class="model-completion">
    <small>MODEL COMPLETION</small>
    <strong>POSITIVE</strong>
  </div>
</div>

<p class="icl-takeaway"><strong>No retraining:</strong> the examples shape behavior only while they remain in the prompt.</p>

<p class="microcopy">In-context learning: <a href="https://arxiv.org/abs/2005.14165">Brown et al., “Language Models are Few-Shot Learners”</a> · <a href="https://arxiv.org/abs/2208.01066">Garg et al., “What Can Transformers Learn In-Context?”</a></p>

<!--
Sentiment classification means deciding whether a statement expresses a positive or
negative opinion. The examples show both what the task is and how the answer should be
formatted. The model uses that information without updating its trained parameters.
-->

---

<!-- _class: compact-title -->

<div class="eyebrow">Inside the transformer</div>

## An induction head finds a pattern and continues it

<p class="induction-lede">An <strong>attention head</strong> is a small part of a transformer that decides which earlier words are useful for predicting the next one.</p>

<div class="induction-example">
  <div class="sequence-line">
    <small>EARLIER IN THE PROMPT</small>
    <span><mark>The code word is</mark> <b>BLUEBIRD</b>.</span>
  </div>
  <div class="copy-cue">look back at what followed the same words</div>
  <div class="sequence-line later">
    <small>LATER IN THE PROMPT</small>
    <span><mark>The code word is</mark> <i>→</i> <b>BLUEBIRD</b></span>
  </div>
</div>

<div class="induction-steps">
  <div><strong>1</strong><span>Find a familiar sequence</span></div>
  <div><strong>2</strong><span>See what followed it earlier</span></div>
  <div><strong>3</strong><span>Use that continuation again</span></div>
</div>

<p class="microcopy">Mechanistic evidence: <a href="https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html">Olsson et al., “In-context Learning and Induction Heads.”</a></p>

<!--
The repeated phrase is highlighted in amber; the copied continuation is teal. This
match-and-continue behavior is called induction. It helps explain some in-context learning,
but it is not a complete explanation of every capability in a modern language model.
-->

---

<div class="eyebrow">Continue learning</div>

## Three visual explanations worth watching

<div class="video-grid">
  <a class="video-card" href="https://youtu.be/VkHfRKewkWw">
    <img src="assets/video-backpropagation.jpg" alt="Welch Labs video thumbnail showing neural-network layers and a next-token prediction">
    <span class="video-topic">1 · How training works</span>
    <h3>The F=ma of Artificial Intelligence</h3>
    <p>Backpropagation and how training changes a model’s weights.</p>
  </a>
  <a class="video-card" href="https://youtu.be/qx7hirqgfuU">
    <img src="assets/video-generalization.jpg" alt="Welch Labs video thumbnail titled The Geometry of Depth">
    <span class="video-topic">2 · Why depth helps</span>
    <h3>Why Deep Learning Works Unreasonably Well</h3>
    <p>A visual account of deep networks and generalization.</p>
  </a>
  <a class="video-card" href="https://youtu.be/D8GOeCFFby4">
    <img src="assets/video-grokking.jpg" alt="Welch Labs video thumbnail showing geometric patterns around the word Grokking">
    <span class="video-topic">3 · Looking inside</span>
    <h3>The Most Complex Model We Actually Understand</h3>
    <p>Grokking and a rare mechanistic explanation of a learned algorithm.</p>
  </a>
</div>

<p class="resource-strip">All three videos: <strong>Welch Labs</strong> · companion <a href="https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/XpCnhaAQrssq8tJBG/rfpm8jhcd5kog1mqi8jn">grokking animation</a></p>

<!--
Offer these as an optional sequence rather than required preparation. The first explains
how weights change during training; the second builds intuition for deep learning and
generalization; the third connects grokking to mechanistic interpretability.
-->

---

<!-- _class: compact-title -->

<div class="eyebrow">Statistical-mechanics aside</div>

## Grokking may resemble slow glass relaxation—not a first-order transition

<p class="glass-lede">Treat the neural network as a physical system: its parameters are the degrees of freedom, and training loss plays the role of energy.</p>

<div class="glass-analogy">
  <div class="analogy-label"><strong>Glass physics</strong><span>atoms rearrange</span></div>
  <div class="analogy-state"><small>LIQUID</small><b>mobile configurations</b></div>
  <div class="analogy-arrow"><span>rapid quench</span>→</div>
  <div class="analogy-state amber-state"><small>NONEQUILIBRIUM GLASS</small><b>motion becomes sluggish</b></div>
  <div class="analogy-arrow"><span>slow relaxation</span>→</div>
  <div class="analogy-state teal-state"><small>STABLE CONFIGURATION</small><b>more equilibrated</b></div>

  <div class="analogy-label"><strong>Neural network</strong><span>parameters change</span></div>
  <div class="analogy-state"><small>EARLY TRAINING</small><b>many possible solutions</b></div>
  <div class="analogy-arrow"><span>fast optimization</span>→</div>
  <div class="analogy-state amber-state"><small>MEMORIZATION</small><b>low loss; poor test accuracy</b></div>
  <div class="analogy-arrow"><span>continued training</span>→</div>
  <div class="analogy-state teal-state"><small>GENERALIZATION</small><b>high test accuracy</b></div>
</div>

<div class="glass-finding">
  <strong>No entropy barrier observed</strong>
  <span>The sampled landscape is continuous between memorizing and generalizing states—evidence against a first-order transition in these experiments.</span>
</div>

<p class="microcopy">Zhang et al., <a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/117824">“Is Grokking a Computational Glass Relaxation?”</a> NeurIPS 2025 · scope: one-layer transformers on modular-arithmetic tasks.</p>

<!--
This is a statistical-mechanics analogy backed by an entropy-landscape calculation, not a
claim that every neural network literally undergoes a glass transition. The authors map
parameters to degrees of freedom and training loss to energy. They find no entropy barrier,
arguing against a first-order phase transition in their setup. Their Wang-Landau-inspired
WanD optimizer reaches generalization without the long grokking delay.
-->

---

<div class="eyebrow">From model to system</div>

## Capability is moving outward

<img class="architecture-image" src="assets/externalization-layers.svg" alt="Three layered stages of language-agent capability: model weights, assembled context, and harness infrastructure">

<p class="microcopy">Adapted from <a href="https://arxiv.org/html/2604.08224v1">Zhou et al., “Externalization in LLM Agents,” Fig. 2 and §2.</a></p>

<!--
The layers accumulate rather than replace one another. The question shifts from “what can
the model do?” toward “what environment lets the model act reliably over time?”
-->

---

<div class="eyebrow">Externalization</div>

## Reliable agency relocates recurring burdens

<div class="grid three">
  <div class="card teal"><span class="tag teal-tag">Memory</span><h3>Recall → recognition</h3><p>Persist state outside the model and retrieve what the present decision needs.</p></div>
  <div class="card amber-border"><span class="tag amber">Skills</span><h3>Generation → composition</h3><p>Package procedures so workflows need not be improvised from scratch.</p></div>
  <div class="card rose"><span class="tag rose-tag">Protocols</span><h3>Ad hoc → structured</h3><p>Turn ambiguous interaction into machine-readable, governable exchange.</p></div>
</div>

<p class="microcopy">Organizing principle: <a href="https://arxiv.org/html/2604.08224v1">Zhou et al., “Externalization in LLM Agents,” §1.</a></p>

<!--
Each artifact transforms the task presented to the model: retrieve rather than recall,
compose rather than reinvent, and fill a contract rather than negotiate an interface in prose.
-->

---

<div class="eyebrow">Externalized state</div>

## Memory carries continuity across time

<div class="grid four">
  <div class="card"><h3>Working context</h3><p>Plans, open files, hypotheses, and checkpoints for the active task.</p></div>
  <div class="card teal"><h3>Episodic experience</h3><p>Prior trajectories, decisions, failures, outcomes, and reflections.</p></div>
  <div class="card amber-border"><h3>Semantic knowledge</h3><p>Stable facts, project conventions, abstractions, and domain guidance.</p></div>
  <div class="card rose"><h3>Personalized memory</h3><p>User- or environment-specific preferences with distinct retention rules.</p></div>
</div>

<p class="microcopy">Sources: <a href="https://arxiv.org/html/2604.08224v1#S3">Zhou et al., §3 and Fig. 4</a> · <a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Anthropic, “Effective context engineering for AI agents.”</a></p>

<!--
Memory is not synonymous with a vector database. The harness decides what is recorded,
consolidated, forgotten, and loaded into the finite working context at each step.
-->

---

<div class="eyebrow">Externalized expertise</div>

## Skills make procedures reusable and inspectable

<div class="grid three">
  <div class="card amber-border"><h3>Operational procedure</h3><p>Steps, dependencies, recovery paths, and stopping conditions.</p></div>
  <div class="card"><h3>Decision heuristics</h3><p>Rules for choosing tools, strategies, or branches under recurring conditions.</p></div>
  <div class="card teal"><h3>Normative constraints</h3><p>Required checks, prohibited actions, quality standards, and escalation rules.</p></div>
</div>

<div class="tag-row skill-paths"><span class="tag">authored</span><span class="tag teal-tag">distilled</span><span class="tag amber">discovered</span><span class="tag rose-tag">composed</span><span class="path-arrow">→ registry → progressive disclosure → execution</span></div>

<p class="microcopy">Source: <a href="https://arxiv.org/html/2604.08224v1#S4">Zhou et al., §4 and Fig. 5.</a></p>

<!--
A skill is not merely a tool description. It packages expertise for a class of tasks.
Progressive disclosure keeps only a summary resident until the detailed procedure is needed.
-->

---

<div class="eyebrow">Externalized interaction</div>

## Protocols govern how capabilities cross boundaries

<div class="grid four">
  <div class="card teal"><h3>Invocation grammar</h3><p>Arguments, types, ordering, result shape, and validation.</p></div>
  <div class="card"><h3>Lifecycle semantics</h3><p>Allowed transitions, turn ownership, completion, and failure.</p></div>
  <div class="card rose"><h3>Permission and trust</h3><p>Who may act, what data may move, and which evidence is required.</p></div>
  <div class="card amber-border"><h3>Discovery metadata</h3><p>Registries and capability descriptions make interfaces findable.</p></div>
</div>

<p class="microcopy">Tools expose operations · skills encode how to use them · protocols govern interaction. <a href="https://arxiv.org/html/2604.08224v1#S5">Zhou et al., §5 and Fig. 6.</a></p>

<!--
Return to search_reports. Its schema is the invocation grammar, but a complete protocol may
also specify discovery, lifecycle, authorization, and error semantics.
-->

---

<div class="eyebrow">Harness engineering</div>

## The harness is a designed cognitive environment

<img class="architecture-image" src="assets/harness-cognitive-environment.svg" alt="A foundation model surrounded by memory, skills, protocols, permission, control, and observability within a harness">

<p class="microcopy">Adapted from <a href="https://arxiv.org/html/2604.08224v1#S6">Zhou et al., Fig. 7 and §6.</a></p>

<!--
Memory, skills, and protocols supply externalized cognitive content. Permission, control,
and observability govern how that content is accessed, constrained, and monitored.
-->

---

<div class="eyebrow">Harness design</div>

## Six dimensions define the operating envelope

<div class="grid six compact-six">
  <div class="card"><h3>Loop and control</h3><p>Steps, branches, recursion, termination, and costs.</p></div>
  <div class="card teal"><h3>Sandboxing</h3><p>Filesystem, network, state, and execution isolation.</p></div>
  <div class="card amber-border"><h3>Human oversight</h3><p>Approval gates, review points, and escalation triggers.</p></div>
  <div class="card"><h3>Observability</h3><p>Traces, metrics, causal links, errors, and outcomes.</p></div>
  <div class="card rose"><h3>Policy encoding</h3><p>Versioned permissions across user, project, and organization scopes.</p></div>
  <div class="card"><h3>Context budgets</h3><p>Retrieval, loading, compaction, eviction, and allocation.</p></div>
</div>

<p class="microcopy">Analytical framework from <a href="https://arxiv.org/html/2604.08224v1#S6.SS2">Zhou et al., §6.2.</a></p>

<!--
These dimensions are architectural variables, not a product checklist. They let us compare
systems using the same model but operating under different cognitive environments.
-->

---

<div class="eyebrow">At the model boundary</div>

## The harness structures model input—and output

<div class="boundary-grid">
  <div class="boundary-label">INPUT</div>
  <div class="card teal"><h3>Memory</h3><p>Selected historical and situational context.</p><span class="tag teal-tag">contextual input</span></div>
  <div class="card amber-border"><h3>Skills</h3><p>Procedures, examples, heuristics, and constraints.</p><span class="tag amber">instructional input</span></div>
  <div class="boundary-model">LLM</div>
  <div class="card rose"><h3>Protocols</h3><p>Typed calls constrain the generative action space.</p><span class="tag rose-tag">action schema</span></div>
  <div class="boundary-label output">OUTPUT</div>
</div>

<p class="microcopy">Separation makes retrieval, procedure, and interface failures independently debuggable. <a href="https://arxiv.org/html/2604.08224v1#S7.SS2">Zhou et al., §7.2.</a></p>

<!--
The prompt is no longer an undifferentiated buffer. These layers have distinct update rates,
governance requirements, and failure modes.
-->

---

<div class="eyebrow">Architectural bridge</div>

## CoALA organized cognition; externalization locates its machinery

<div class="grid two bridge-cards">
  <div class="card"><span class="tag">CoALA · 2023/2024</span><h3>Functional vocabulary</h3><p>Memory modules, internal and external actions, and a decision cycle explain what a language agent does.</p></div>
  <div class="card teal"><span class="tag teal-tag">Externalization · 2026</span><h3>Systems partition</h3><p>Memory, skills, and protocols explain where state, expertise, and interaction structure live—and how the harness governs them.</p></div>
</div>

<p class="microcopy">Sources: <a href="https://arxiv.org/abs/2309.02427">Sumers et al., “Cognitive Architectures for Language Agents”</a> · <a href="https://arxiv.org/html/2604.08224v1">Zhou et al., “Externalization in LLM Agents.”</a></p>

<!--
The newer paper is not a revised edition of CoALA; it identifies CoALA as its closest
conceptual bridge. Preserve the lineage while shifting attention to systems partitioning.
-->

---

<!-- _class: compact-title -->

<div class="eyebrow">Multi-step reinforcement learning</div>

## Agentic RL trains over trajectories—not single responses

<img class="rl-loop-image" src="assets/mai-agentic-rl-loop.svg" alt="Agentic reinforcement learning loop in which a policy model produces policy steps, an orchestration harness dispatches tool calls into a sandbox environment, observations return as environment steps, and the completed trajectory is graded for reward">

<p class="microcopy">Adapted from <a href="https://microsoft.ai/pdf/mai-thinking-1.pdf">Microsoft AI Team, <em>MAI-Thinking-1</em>, Fig. 18 and §3.3, p. 40.</a></p>

<!--
The unit of experience is a trajectory: policy step, action, environment observation, then
another policy step. The harness owns dispatch, context, budgets, termination, and the session.
-->

---

<div class="eyebrow">Harness reinforcement learning</div>

## RL can operate through—or on—the harness

<div class="grid two">
  <div class="card amber-border"><h3>RL through the harness</h3><p>The runtime owns the rollout while training changes the model policy that emits reasoning, tool calls, and final answers.</p></div>
  <div class="card teal"><h3>RL of the harness</h3><p>A controller learns structural choices—retrieve, branch, check, retry, compact, or stop—while the executor may remain frozen.</p></div>
</div>

<p class="microcopy">Sources: <a href="https://arxiv.org/abs/2608.17528">Agent Lightning v1.0</a> · <a href="https://arxiv.org/abs/2607.05458">Learning to Control LLM Agent Harnesses with Offline RL</a></p>

<!--
The target of learning matters: model behavior within a fixed runtime, structural runtime
decisions, or eventually both as a coupled system.
-->

---

<!-- _class: compact-title -->

<div class="eyebrow">Reasoning vocabulary</div>

## Two ways to move from evidence to a conclusion

<div class="reasoning-compare">
  <div class="reasoning-mode induction-mode">
    <span class="reasoning-label">Induction · examples → likely rule</span>
    <div class="reasoning-observations"><span>Copper expands when heated.</span><span>Aluminum expands when heated.</span><span>Steel expands when heated.</span></div>
    <div class="reasoning-down">↓</div>
    <strong>Metals probably expand when heated.</strong>
  </div>
  <div class="reasoning-mode deduction-mode">
    <span class="reasoning-label">Deduction · rule + fact → necessary conclusion</span>
    <div class="reasoning-observations"><span>Rule: All metals expand when heated.</span><span>Fact: Copper is a metal.</span></div>
    <div class="reasoning-down">↓</div>
    <strong>Copper will expand when heated.</strong>
  </div>
</div>

<p class="reasoning-takeaway"><strong>Useful division of labor:</strong> language models recognize patterns and propose possibilities; symbolic reasoners apply explicit rules and return checkable consequences.</p>

<!--
This is a pedagogical division of labor, not an absolute boundary. Language models can
produce deductive-looking arguments, but text generation alone does not guarantee logical
entailment. Deduction is conditional on the correctness of the supplied facts and rules.
-->

---

<div class="eyebrow">Recursive Language Models</div>

## A long prompt is not organized evidence

<p class="lede compact-lede">Imagine answering one question across a 500-page report archive. Reading everything into one conversation does not tell the model where to look—or how to keep intermediate results organized.</p>

<div class="grid three">
  <div class="card amber-border"><h3>Store it as data</h3><p>Keep the full archive outside the model’s immediate conversation.</p></div>
  <div class="card"><h3>Search before reading</h3><p>Inspect and select the portions relevant to the present question.</p></div>
  <div class="card teal"><h3>Ask smaller questions</h3><p>Solve bounded subproblems and combine their results in code.</p></div>
</div>

<p class="microcopy">Source: <a href="https://arxiv.org/abs/2512.24601">Zhang, Kraska, and Khattab, “Recursive Language Models,” v3.</a></p>

<!--
The hook is information organization, not merely context length. An RLM is an inference
paradigm and harness: the root model treats the original prompt as data in an external
programmatic environment.
-->

---

<div class="eyebrow">Recursive Language Models</div>

## An RLM turns the prompt into a working environment

<p class="mechanics-key"><strong>Root model</strong> = coordinator · <strong>REPL workspace</strong> = external notebook with variables and code</p>

<img class="architecture-image" src="assets/rlm-offloading.svg" alt="Context is offloaded into symbolic variables and programmatic sub-agent calls keep task-specific intermediate results outside the root model context">

<p class="microcopy">Adapted from <a href="https://alexzhang13.github.io/blog/2026/harness/">Zhang and Khattab, “Language model harnesses are compositional generalizers,” Fig. 5.</a></p>

<!--
Context offloading hides input-specific tokens behind an addressable variable. Programmatic
subcalls pass intermediate results through workspace variables rather than bloating the
coordinator’s conversation history.
-->

---

<div class="eyebrow">Inductive bias</div>

## Structure makes unfamiliar problems feel familiar

<p class="inductive-bias-definition"><strong>Inductive reasoning</strong> infers a pattern from examples. An <strong>inductive bias</strong> is built-in structure that makes some solutions easier to find.</p>

<img class="architecture-image" src="assets/locally-in-distribution.svg" alt="A complex out-of-distribution task is transformed by a structured harness into several small locally in-distribution observations for language-model calls">

<p class="microcopy">Concept and early evidence: <a href="https://alexzhang13.github.io/blog/2026/harness/">Zhang and Khattab, “Language model harnesses are compositional generalizers,” Figs. 1–5.</a></p>

<!--
Locally in-distribution is the authors' framing, not settled theory. Their experiments report
better transfer from short to 8–32× longer tasks and across domains when training an RLM.
-->

---

<div class="eyebrow">Symbolic reasoning as a tool</div>

## An RLM can ask a reasoner to derive what follows

<div class="reasoner-flow">
  <div class="reasoner-stage">
    <small>FACT</small>
    <code>:Socrates a :Man.</code>
  </div>
  <div class="reasoner-arrow">+</div>
  <div class="reasoner-stage">
    <small>RULE</small>
    <code>Man(x) → Mortal(x)</code>
  </div>
  <div class="reasoner-arrow">→</div>
  <div class="reasoner-stage reasoner-tool">
    <small>EYELENG TOOL</small>
    <strong>apply the rule</strong>
    <span>forward or backward reasoning</span>
  </div>
  <div class="reasoner-arrow">→</div>
  <div class="reasoner-stage reasoner-result">
    <small>DERIVED + PROOF</small>
    <code>:Socrates a :Mortal.</code>
  </div>
</div>

<p class="reasoner-caveat"><strong>The guarantee is conditional:</strong> the derivation is valid only if the translated facts and rules are correct.</p>

<p class="microcopy">Example and capabilities: <a href="https://github.com/eyereasoner/eyeleng">Eyeleng—hybrid forward materialization, backward proving, validation, and proof explanations.</a></p>

<!--
The RLM decides when deduction is useful, prepares formal input, calls the reasoner, and
interprets the returned closure or proof. The neural-to-symbolic translation is the risky
boundary: malformed facts or rules can yield a perfectly valid but irrelevant deduction.
-->

---

<div class="eyebrow">Neurosymbolic RLM</div>

## A neurosymbolic agent separates responsibilities

<div class="symbolic-stack">
  <div class="stack-layer neural"><span class="tag amber">Neural model</span><strong>Interpret language · recognize patterns · propose facts and actions</strong></div>
  <div class="stack-arrow">↓</div>
  <div class="stack-layer symbolic"><span class="tag teal-tag">RLM harness</span><strong>Manage context · choose tools · recurse · preserve provenance</strong></div>
  <div class="stack-arrow">↓</div>
  <div class="stack-layer verified"><span class="tag rose-tag">Symbolic reasoner</span><strong>Apply rules · validate constraints · return conclusions and proofs</strong></div>
</div>

<p class="microcopy">Design synthesis; tools and examples: <a href="https://github.com/eyereasoner/eyeleng">Eyeleng</a> · <a href="https://youtu.be/Sir59K8ZDPU">Coyle, “Why Agentic Systems Need Ontologies”</a> · <a href="https://arxiv.org/abs/2608.16794">Albinhassan et al.</a></p>

<!--
The layers exchange structured artifacts. The model supplies flexible interpretation; the
harness controls the workflow; the reasoner supplies explicit inference and validation.
None can repair incorrect domain knowledge automatically.
-->

---

<div class="eyebrow">Further viewing</div>

## Why agentic systems need ontologies

<div class="single-video">
  <a href="https://youtu.be/Sir59K8ZDPU"><img src="assets/video-ontologies.jpg" alt="Video thumbnail featuring Frank Coyle with the words Ontologies Keep Agents Honest"></a>
  <div class="video-notes">
    <span class="video-speaker">Frank Coyle · UC Berkeley · AI Engineer</span>
    <h3>Probabilistic reasoning inside.<br>Logical guardrails outside.</h3>
    <ul>
      <li><strong>4:23</strong> · neurosymbolic AI</li>
      <li><strong>9:19</strong> · RDFS and OWL inference</li>
      <li><strong>14:23</strong> · validation inside an agent loop</li>
      <li><strong>17:43</strong> · type safety vs. domain correctness</li>
    </ul>
  </div>
</div>

<p class="microcopy"><a href="https://youtu.be/Sir59K8ZDPU">Watch: “Why Agentic Systems Need Ontologies”</a> · 21 minutes.</p>

<!--
The talk provides the practical bridge from the conceptual stack to implementation:
probabilistic interpretation in the model, typed interfaces at the boundary, and ontology-
based inference and validation before consequential side effects are accepted.
-->

---

<!-- _class: compact-title -->

<div class="eyebrow">Case study · PRIME Agent</div>

## PRIME Agent makes an RLM persistent

<p class="prime-lede">The model can reorganize information, run code, delegate work, and retain useful lessons—without changing its weights during the task.</p>

<div class="prime-state-map">
  <div class="prime-zone model-zone">
    <span class="prime-zone-label">MODEL INVOCATION</span>
    <div class="prime-level"><small>L0</small><strong>Model weights</strong><span>learned before the task</span></div>
    <div class="prime-level"><small>L1</small><strong>Active context</strong><span>what the model sees now</span></div>
  </div>
  <div class="prime-boundary"><span>explicitly managed state begins here</span><b>→</b></div>
  <div class="prime-zone harness-zone">
    <span class="prime-zone-label">PRIME AGENT HARNESS</span>
    <div class="prime-level"><small>L2</small><strong>Persistent REPL + recursive agents</strong><span>compute, tools, and parallel subproblems</span></div>
    <div class="prime-level"><small>L3</small><strong>History + memories + skills</strong><span>retained, versioned, and reusable</span></div>
  </div>
</div>

<div class="prime-evidence">
  <div><small>REPORTED RESULT</small><strong>30% → 95.5%</strong><span>ARC-AGI-3 RHAE Best@1</span></div>
  <div><small>LONG HORIZON</small><strong>85.5 hours</strong><span>one autonomous nanoGPT run</span></div>
  <div class="prime-warning"><small>DESIGN WARNING</small><strong>Persistence remembers shortcuts, too</strong><span>least privilege, independent validation, and rollback still matter</span></div>
</div>

<p class="microcopy">Karten et al., <a href="https://arxiv.org/html/2608.23552v1">“Prime Agent: A Self-Improving RLM Harness”</a> (preprint, Aug. 2026) · <a href="https://github.com/PrimeIntellect-ai/prime-agent">open-source implementation</a>.</p>

<!--
PRIME Agent is a concrete implementation of the RLM ideas introduced earlier. L0 and L1
belong to the model invocation; L2 and L3 are explicitly managed by the harness. “Self-
improving” here means that trajectory evidence can update versioned prompts, memories,
skills, and subagent specifications while the model weights remain fixed.

Treat the headline evaluation numbers as system-level evidence, not as a clean causal
estimate for any single component. The authors note that some native-harness reruns fell
below published reference scores and that uncertainty intervals are unavailable for their
long-context table. Their Factorio case study also found that refinement preserved an
objective-gaming shortcut as a skill—an especially useful bridge back to ontology-based
validation, least-privilege tools, and auditable rollback.
-->

---

<div class="eyebrow">AI4C2 starting experiment</div>

## Compare externalization strategies—not only models

| System | What is externalized | Research question |
|---|---|---|
| Base LLM | Nothing beyond one assembled prompt | Where do quality and traceability degrade? |
| Retrieval workflow | Semantic memory and fixed retrieval policy | What is gained or lost through preselected evidence? |
| RLM harness | Context, workspace, decomposition, and subcalls | Does agent-directed decomposition improve evidence use? |
| RLM + reasoner | Plus formal facts, rules, constraints, and proof traces | When does explicit deduction improve robustness and auditability? |

<p class="microcopy">Public or synthetic C2-style artifacts · measures: quality, provenance, context cost, latency, failures, and recovery.</p>

<!--
Hold the base model constant where possible so the experiment measures system architecture.
Keep operational or proposal-sensitive materials out of the public deck and initial corpus.
-->

---

<!-- _class: compact-title -->

<div class="eyebrow">Research question</div>

## What contract should connect an LLM agent to a symbolic reasoner?

<p class="interface-question">How should an agent formalize evidence, invoke deduction, and consume proof-bearing results without hiding errors at the neural–symbolic boundary?</p>

<div class="interface-contract">
  <div class="interface-stage formalize-stage">
    <small>1 · FORMALIZE</small>
    <strong>Language → formal claims</strong>
    <span>Typed facts · rules · query · source provenance</span>
  </div>
  <div class="interface-arrow">→</div>
  <div class="interface-stage reason-stage">
    <small>2 · REASON</small>
    <strong>Derive what follows</strong>
    <span>Conclusion · proof · contradiction · invalid · unknown</span>
  </div>
  <div class="interface-arrow">→</div>
  <div class="interface-stage act-stage">
    <small>3 · ACT</small>
    <strong>Control downstream use</strong>
    <span>Validate provenance and policy before planning or tool use</span>
  </div>
</div>

<p class="interface-test"><strong>Test against an RLM-only baseline:</strong> Does the interface improve correctness, contradiction detection, and auditability at acceptable cost and latency?</p>

<p class="microcopy">Research target: the schema, provenance, failure semantics, and control policy at the neural–symbolic boundary.</p>

<!--
“Interface” means the complete contract between components—not merely an API endpoint or
user interface. The first risk is translation: the model may formalize the evidence
incorrectly. The reasoner should therefore return proof-bearing results and explicit
contradiction, invalid, and unknown states. The harness then decides whether those results
are trustworthy enough to influence a plan or authorize an external action.

The symbolic derivation is sound only relative to the supplied facts and rules. Evaluate
the full interface against an otherwise matched RLM-only system using correctness,
contradiction detection, provenance coverage, auditability, latency, and context cost.
-->
