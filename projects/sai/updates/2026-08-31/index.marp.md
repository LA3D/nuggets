---
marp: true
theme: ai4c2
paginate: true
footer: "SAI · Scientific AI"
title: "WikiMemory"
description: "How agents rediscovered an old medium for persistent scientific memory"
author: "Charles F. Vardeman II"
date: 2026-08-31
categories: [WikiMemory, Agentic Memory, Scientific AI]
draft: false
publish_agentic_notes: true
---

<!-- _class: title -->

<div class="eyebrow">SAI · Scientific AI</div>

# WikiMemory

<p class="subtitle">How agents rediscovered an old medium for persistent scientific memory</p>

<div class="meta">
Charles F. Vardeman II<br>
Center for Research Computing, University of Notre Dame<br>
August 31, 2026
</div>

<!--
AGENTIC LEARNING NOTES

Slide ID — wikimemory-title
Learning objective — Frame WikiMemory as the rediscovery of an external medium for cumulative scientific memory.
Core claim — The new capability is not model recall; it is an agent that can help maintain an inspectable knowledge environment over time.
Explain — Open on the contemporary rediscovery, give away the architecture immediately, and then ask why such a simple pattern works. The historical arc supplies the answer; the final section asks what scientific use demands beyond a personal second brain.
Misconception — “Memory” here does not mean that an LLM remembers like a person or that a larger context window solves scientific continuity.
Check — In one sentence, what has the agentic community rediscovered?
Source routes — Use the next two slides for the motivating observation and system architecture; use the historical section to explain why the pattern works.
Transition — First give the audience a copy-ready way to explore the deck with an agent.
-->

---

<div class="eyebrow">Start here · agent-assisted walkthrough</div>

## Open the deck with your friendly neighborhood agent

<div class="agent-start">
  <div class="agent-deck-url"><small>PRESENTATION</small><a href="https://la3d.github.io/nuggets/projects/sai/updates/2026-08-31/">la3d.github.io/nuggets/projects/sai/updates/2026-08-31/</a></div>
  <div class="agent-prompt-card">
    <div class="prompt-label">Copy and paste into ChatGPT or Codex</div>
    <pre><code>Open this presentation in your browser:
https://la3d.github.io/nuggets/projects/sai/updates/2026-08-31/

Before helping me, inspect the page's raw HTML. Find the embedded
W3C Web Annotation JSON-LD and load its per-slide learning context.

I will navigate the deck myself and may skip around. When I ask a question,
use the slide number or title I provide to select the matching annotation.
Respond conversationally and only to what I ask. Draw on the core claim,
caveats, and sources when useful. Do not lecture through the deck, advance,
or quiz me automatically. If I do not identify the slide, ask which one I am
viewing.</code></pre>
  </div>
</div>

<!--
AGENTIC LEARNING NOTES

Slide ID — agentic-walkthrough-bootstrap
Learning objective — Start a learner-controlled agentic dialogue by giving the agent the presentation URL, its embedded learning context, and rules for responding to non-linear questions.
Core claim — The student controls navigation and inquiry; the agent retrieves the relevant slide annotation and responds on demand rather than delivering a linear lecture.
Explain — Invite the learner to copy the prompt and then browse freely. They may skip slides, linger, return, or ask no question at all. When a question includes a slide number or title, the agent selects the matching annotation and uses only the relevant claim, caveat, sources, or check. If the target is ambiguous, the agent asks which slide is in view.
Misconception — The comprehension checks and transitions are optional dialogue resources, not instructions to quiz the learner or advance after every slide.
Check — What information should the learner provide so the agent can ground a question in the correct slide?
Source routes — Open the linked Nuggets presentation and inspect its embedded W3C Web Annotation JSON-LD in the page source.
Transition — Begin the narrative with the Karpathy–Elvis exchange that turned a memory complaint into an agentic design pattern.
-->

---

<div class="eyebrow">March 25 → April 4, 2026</div>

## A memory complaint became an agentic design pattern

<div class="pkg-flow">
  <div class="pkg-node"><small>KARPATHY · MAR 25</small><b>Memory distracts</b><span>an incidental question resurfaces as a permanent “interest”</span></div>
  <div class="pkg-link">→</div>
  <div class="pkg-node"><small>ELVIS SARAVIA · MAR 25</small><b>Use simple files</b><span>but tune relevance, discovery, structure, and context</span></div>
  <div class="pkg-link">→</div>
  <div class="pkg-node teal-node"><small>KARPATHY · APR 2–4</small><b>Let an agent maintain a wiki</b><span>compile sources, answer questions, file outputs, and lint</span></div>
</div>

<p class="thesis-line">The surprise was not that a model could remember—it was that an agent could maintain external memory.</p>

<p class="microcopy"><a href="https://x.com/karpathy/status/2036836816654147718">Karpathy on distracting memory</a> · <a href="https://x.com/omarsar0/status/2036848785653895623">Elvis Saravia on methodical file-based memory</a> · <a href="https://x.com/karpathy/status/2039805659525644595">Karpathy, “LLM Knowledge Bases”</a> · <a href="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f">the “LLM Wiki” idea file</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — karpathy-elvis-rediscovery
Learning objective — Reconstruct how a complaint about distracting memory led to an agent-maintained wiki pattern.
Core claim — The important step was moving from indiscriminate remembered facts to methodical maintenance of external files, indexes, and relevance.
Explain — Tell this as a rediscovery, not an invention story. Karpathy begins with a failure mode: personalization memories are over-selected and distract the model. Elvis Saravia replies that simple Obsidian files plus metadata work when memory is tuned methodically. A week later Karpathy describes a working pattern: immutable raw sources, an LLM-maintained Markdown wiki, index-guided question answering, outputs filed back into the corpus, and periodic linting. The April 4 gist turns the observation into a portable idea file that another agent can instantiate.
Misconception — Putting facts in files is not sufficient; selection, discovery, structure, context, and maintenance determine whether external memory helps or distracts.
Check — What changed between “use simple files” and the later LLM Wiki pattern?
Source routes — Follow the three linked X threads and Karpathy’s linked “LLM Wiki” gist on this slide.
Transition — Now reveal the full architecture so the audience can recognize its components throughout the history.
-->

---

<div class="eyebrow">The LLM Wiki · TL;DR</div>

## Compile knowledge once; improve the artifact over time

<div class="compile-flow">
  <div class="compile-layer raw-layer"><small>RAW /</small><b>immutable sources</b><span>papers · notes · transcripts · code</span></div>
  <div class="compile-arrow"><span>agent reads + integrates</span>→</div>
  <div class="compile-layer wiki-layer"><small>WIKI /</small><b>persistent synthesis</b><span>pages · links · contradictions · index</span></div>
  <div class="compile-arrow"><span>agent searches + traverses</span>→</div>
  <div class="compile-layer answer-layer"><small>WORK</small><b>questions + artifacts</b><span>answers feed back into the wiki</span></div>
</div>

<div class="schema-strip"><span class="tag amber">SCHEMA / AGENTS.md</span><b>Instructions define ingest, query, citation, maintenance, and linting.</b></div>

<p class="microcopy"><a href="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f">Andrej Karpathy, “LLM Wiki”</a> · <a href="https://www.langchain.com/blog/wiki-memory">Harrison Chase, “Wiki Memory”</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — llm-wiki-architecture
Learning objective — Explain the roles of raw sources, persistent synthesis, work products, and behavioral instructions in the LLM Wiki loop.
Core claim — Knowledge compounds when an agent repeatedly compiles recoverable evidence into a maintained artifact and files reviewed work back into it.
Explain — Give away the system before the history. Raw is the independently recoverable source of truth. The wiki is the compiled, persistent artifact maintained by the agent. The schema or AGENTS.md is a behavioral contract for ingest, querying, citation, maintenance, and linting. Questions produce files, comparisons, diagrams, or slides that can be reviewed and filed back, so work compounds instead of disappearing into chat history.
Misconception — The wiki is not a replacement for raw evidence; it is a revisable synthesis whose claims must remain traceable to that evidence.
Check — For a newly encountered paper, what belongs in RAW, what belongs in WIKI, and what might be produced as WORK?
Source routes — Follow Karpathy’s linked “LLM Wiki” gist and Harrison Chase’s linked “Wiki Memory” essay.
Transition — The architecture solves a continuity problem that becomes sharper in scientific work.
-->

---

<div class="eyebrow">The continuity problem</div>

## Every model call begins now; science began long ago

<p class="lede">Research advances by carrying evidence, failed attempts, critique, decisions, and learned procedures across people and time.</p>

<div class="grid three">
  <div class="card"><h3>Models are episodic</h3><p>The active context is powerful but temporary. A new call does not inherit a research history by default.</p></div>
  <div class="card amber-border"><h3>Science is cumulative</h3><p>Claims gain meaning through sources, revisions, contradictions, methods, and negative results.</p></div>
  <div class="card teal"><h3>The system must bridge them</h3><p>Continuity has to live somewhere inspectable outside the model invocation.</p></div>
</div>

<!--
AGENTIC LEARNING NOTES

Slide ID — scientific-continuity-problem
Learning objective — Distinguish episodic model context from the cumulative state required by science.
Core claim — Scientific continuity must be preserved in an inspectable environment outside any single model invocation.
Explain — Widen Karpathy’s practical observation into the scientific continuity problem. Research state includes evidence, failed attempts, critique, decisions, procedures, and uncertainty. The engineering task is to preserve that state across calls, sessions, agents, collaborators, and time.
Misconception — A long context window is not automatically institutional memory: it does not by itself provide durable ownership, revision history, provenance, or maintenance.
Check — Name three kinds of scientific state that should survive after the current model call ends.
Source routes — This is the deck’s conceptual framing; connect it backward to the LLM Wiki architecture and forward to the historical continuity systems.
Transition — Ask which earlier knowledge systems already addressed parts of this problem.
-->

---

<div class="eyebrow">A longer history</div>

## WikiMemory is a convergence—not a sudden invention

<div class="lineage-map">
  <div class="lineage-row amber-lineage"><b>Augment thought</b><span>Memex</span><i>→</i><span>NLS / Augment</span><i>→</i><span>read–write Web</span></div>
  <div class="lineage-row teal-lineage"><b>Maintain shared knowledge</b><span>WikiWikiWeb</span><i>→</i><span>Wikipedia</span><i>→</i><span>living wiki</span></div>
  <div class="lineage-row rose-lineage"><b>Own a second brain</b><span>personal wiki</span><i>→</i><span>Markdown vault</span><i>→</i><span>knowledge graph</span></div>
  <div class="lineage-convergence">↓</div>
  <div class="convergence-box"><strong>Agentic WikiMemory</strong><span>A model can now navigate, write, refactor, audit, and learn through the medium.</span></div>
</div>

<p class="microcopy">Our synthesis: three historical lineages converge in a harness-operable knowledge substrate.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — wikimemory-convergence
Learning objective — Identify the three historical lineages that contribute to agentic WikiMemory.
Core claim — WikiMemory is a convergence of associative hypertext, collaborative wiki maintenance, and file-native personal knowledge—not a sudden invention.
Explain — Read the three rows as complementary historical traditions, not one literal lineage. Memex was Bush’s imagined personal device for following associative trails; NLS/Augment was Engelbart’s integrated environment for structured text, links, tools, and collaboration; the read–write Web treats the Web as a medium people can both browse and edit. Wikis add shared maintenance. The “second brain” row adds personal ownership: in a Markdown vault, notes are nodes, links are edges, and metadata can type consequential relationships, so linked notes already form a knowledge graph. Agentic WikiMemory converges these affordances.
Misconception — The arrows organize related developments; they do not claim a single direct genealogy or that each later system consciously inherited every earlier design principle. A graph view is optional: linked notes already form a graph.
Check — What does Memex, NLS/Augment, the read–write Web, wiki maintenance, and the personal Markdown graph each contribute?
Source routes — Treat this as a synthesis map; the next sequence of slides supplies the historical evidence for each row.
Transition — Start with Bush’s idea that associative trails matter more than filing hierarchies.
-->

---

<div class="eyebrow">1945 · associative memory</div>

## Bush imagined trails—not a better filing cabinet

<div class="quote-layout">
  <div class="quote-card">
    <span class="quote-mark">“</span>
    <p>The process of tying two items together is the important thing.</p>
    <small>Vannevar Bush · <em>As We May Think</em></small>
  </div>
  <div class="trail-demo" aria-label="A diagram showing a person moving along an associative trail between evidence, an idea, a contradiction, and a new question">
    <div class="trail-node"><small>EVIDENCE</small><b>paper</b></div><span>→</span>
    <div class="trail-node amber-node"><small>IDEA</small><b>claim</b></div><span>→</span>
    <div class="trail-node rose-node"><small>TENSION</small><b>conflict</b></div><span>→</span>
    <div class="trail-node teal-node"><small>NEXT</small><b>question</b></div>
  </div>
</div>

<p class="microcopy">Vannevar Bush, <a href="https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/">“As We May Think”</a>, 1945.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — bush-associative-trails
Learning objective — Explain why Bush’s associative trail is more relevant to WikiMemory than a simple filing cabinet metaphor.
Core claim — An associative trail is a saved, revisit-able, branchable, and shareable path through sources, ideas, tensions, and questions—not merely a place to store them.
Explain — In plain language, a trail records how inquiry moved: paper → supported claim → conflicting experiment → resulting question. Bush wrote amid concern that information was growing faster than people could organize and reuse it. His durable design principle was to preserve and pass on paths of association so scientific thought could continue; wiki links later provide a cheap, editable implementation.
Misconception — Bush did not describe the modern Web or modern AI; the Memex matters as an early framing of continuity through associative paths, not as a feature-by-feature prediction.
Check — Construct a four-step associative trail for a research question you know.
Source routes — Follow the linked 1945 Vannevar Bush essay “As We May Think,” especially its discussion of associative indexing and trails.
Transition — Engelbart expands the trail into an entire environment for augmented knowledge work.
-->

---

<div class="eyebrow">1960s · augmented knowledge work</div>

## Hypertext was designed as a cognitive environment

<div class="grid two bridge-cards">
  <div class="card amber-border"><span class="tag amber">Engelbart · NLS</span><h3>Augment the whole workshop</h3><p>Structured text, links, views, collaborative editing, tools, and working procedures formed one environment for improving knowledge work.</p></div>
  <div class="card teal"><span class="tag teal-tag">Nelson · Xanadu</span><h3>Make relationships first-class</h3><p>Hypertext, bidirectional links, versioning, transclusion, and visible provenance challenged the document as an isolated page.</p></div>
</div>

<p class="microcopy"><a href="https://dougengelbart.org/content/view/155/">Doug Engelbart Institute, NLS / Augment</a> · <a href="https://www.xanadu.com.au/general/faq.html">Project Xanadu history</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — engelbarts-cognitive-environment
Learning objective — Distinguish a hypertext feature from a whole cognitive environment for knowledge work.
Core claim — Augmentation emerges from the combination of structured information, tools, collaboration, views, and working procedures.
Explain — Engelbart bridges the history to the harness framing. NLS/Augment was not merely an information store: it designed the surrounding cognitive environment and the procedures through which humans and tools worked together. Nelson’s Xanadu similarly treated relationships, versioning, transclusion, and provenance as first-class concerns.
Misconception — Hypertext is not only clickable text; its knowledge value depends on the larger environment and practices around the links.
Check — Which capabilities surrounding links make NLS/Augment a cognitive environment rather than a document viewer?
Source routes — Follow the linked Doug Engelbart Institute NLS/Augment overview and Project Xanadu history.
Transition — Move from individual augmentation to CERN’s organizational continuity problem.
-->

---

<div class="eyebrow">March 1989 · Information Management: A Proposal</div>

## The Web began as a continuity problem at CERN

<div class="www-origin">
  <figure class="proposal-map">
    <img src="assets/tbl-www-1989-information-management.png" alt="Tim Berners-Lee's 1989 circles-and-arrows diagram connecting linked information, hypertext, projects, documents, people, software, and CERN systems">
    <figcaption>Berners-Lee’s original “circles and arrows” map · converted from the W3C archival GIF.</figcaption>
  </figure>
  <div class="www-origin-copy">
    <p class="lede">People rotated through. Projects evolved. Information existed—but could not be found.</p>
    <div class="memory-pressures">
      <div class="memory-pressure"><b>Turnover</b><span>expertise and project history left with short-term staff</span></div>
      <div class="memory-pressure"><b>Entanglement</b><span>real work crossed the formal organizational hierarchy</span></div>
      <div class="memory-pressure"><b>Change</b><span>books and trees became stale as dependencies shifted</span></div>
    </div>
    <p class="www-thesis">The proposal was for evolving organizational memory—not merely online publishing.</p>
  </div>
</div>

<p class="microcopy"><a href="https://www.w3.org/History/1989/proposal.html">Tim Berners-Lee, “Information Management: A Proposal”</a>, March 1989 / May 1990 · <a href="https://www.w3.org/History/1989/Image1.gif">original W3C diagram</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — web-continuity-problem
Learning objective — Read Berners-Lee’s 1989 proposal and diagram as a response to organizational memory failure at CERN.
Core claim — The Web began as a way to preserve evolving relationships among people, projects, systems, and documents despite turnover and change.
Explain — The proposal begins with high turnover, changing projects, duplicated effort, and technical information that had been recorded but could not be found. Berners-Lee says CERN’s observed working structure was a multiply connected web that evolved with time. The diagram is not a retrospective picture of websites; it maps the information-management problem the Web was meant to address. At this point the working name was “Mesh.”
Misconception — The 1989 diagram is not merely a collection of web pages connected by generic hyperlinks.
Check — Point to one node type and one semantically meaningful relationship in the diagram.
Source routes — Follow Berners-Lee’s linked 1989 proposal and the linked original W3C diagram; read the “Losing Information at CERN” and “Linked information systems” sections.
Transition — Look more closely at the proposal’s data model: the nodes and the links both had types.
-->

---

<div class="eyebrow">1989 · the proposed information model</div>

## Berners-Lee proposed typed nodes and links

<div class="web-typed-model">
  <div class="typed-panel node-panel">
    <small>NODES COULD BE</small>
    <div class="typed-cloud"><span>people</span><span>projects</span><span>concepts</span><span>documents</span><span>software</span><span>hardware</span></div>
  </div>
  <div class="typed-bridge"><span>linked by</span><strong>→</strong></div>
  <div class="typed-panel relation-panel">
    <small>LINKS COULD MEAN</small>
    <div class="typed-cloud"><span>depends on</span><span>part of</span><span>made</span><span>refers to</span><span>uses</span><span>example of</span></div>
  </div>
</div>

<div class="web-requirements">
  <span>remote</span><span>heterogeneous</span><span>non-centralized</span><span>connect existing data</span><span>machine-analyzable</span>
</div>

<p class="callout-line">Before the Web had pages at planetary scale, its proposal described a flexible, distributed knowledge graph.</p>

<p class="microcopy"><a href="https://www.w3.org/History/1989/proposal.html">Berners-Lee, “Information Management: A Proposal,” 1989</a> · sections: Linked information systems · CERN Requirements · Data analysis.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — web-typed-nodes-links
Learning objective — Distinguish typed node categories and typed link predicates in the original Web proposal.
Core claim — Before the Web operated at planetary scale, its proposal described a flexible, distributed, machine-analyzable graph of heterogeneous entities and relationships.
Explain — The proposal explicitly describes generic types of nodes and links, cross-system integration, personal annotations, and automatic analysis for anomalies and topology. This is richer than a collection of documents and anticipates the separation between a knowledge representation and the interfaces or agents that operate over it.
Misconception — Do not retroactively label the 1989 proposal RDF; it precedes RDF and does not specify the later formal model.
Check — Express one relationship from the original diagram as a subject–predicate–object triple.
Source routes — Follow the linked proposal sections “Linked information systems,” “CERN Requirements,” and “Data analysis.”
Transition — Isolate the predicate itself and ask what changes when a link says why two things are connected.
-->

---

<div class="eyebrow">1989 → 1999 · from links to relationships</div>

## A typed link says <em>why</em> two things are connected

<div class="typed-meaning-compare">
  <div class="meaning-card untyped-meaning"><small>UNTYPED WEB LINK</small><div><span>document</span><i>— href →</i><span>claim</span></div><p>Useful for navigation; the machine learns only “links to.”</p></div>
  <div class="meaning-shift">→</div>
  <div class="meaning-card typed-meaning"><small>NAMED RELATIONSHIP</small><div><span>paper</span><i>— supports →</i><span>claim</span></div><p>The predicate carries reusable intent.</p></div>
</div>

<div class="typed-payoffs">
  <div><b>Explain</b><span>Humans see whether a source supports, criticizes, defines, or depends on another page.</span></div>
  <div><b>Query</b><span>Ask “what supports this claim?” instead of searching for pages that mention its words.</span></div>
  <div><b>Infer</b><span>Direction and inverse relations expose dependencies, evidence paths, and affected neighbors.</span></div>
  <div><b>Govern</b><span>A shared predicate vocabulary can be documented, validated, linted, and evolved.</span></div>
</div>

<p class="microcopy"><a href="https://www.w3.org/1999/11/11-WWWProposal/thenandnow">Dan Brickley, “Nodes and Arcs 1989–1999: The WWW Proposal and RDF: Then and Now”</a> · informal W3C discussion, 1999.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — typed-links-why
Learning objective — Compare a navigational hyperlink with a named relationship whose predicate can be explained, queried, and governed.
Core claim — A stable predicate such as supports, criticizes, or depends on turns connectivity into reusable intent.
Explain — Brickley’s retrospective calls ordinary href semantics relatively meaningless because the relationship says only “links to.” His key move is to make the predicate a first-class, uniquely identified object. Once wrote, supports, or depends on has stable meaning, graph-pattern questions become possible and different systems can interpret the same edge consistently.
Misconception — A label alone does not make a link trustworthy; predicates still need shared definitions, provenance, validation, and governance. Also, Brickley labels the document a personal, informal interpretation rather than a formal W3C working-group publication.
Check — What question can a supports edge answer that an ordinary link cannot?
Source routes — Follow Dan Brickley’s linked 1999 “Nodes and Arcs” retrospective. Reserve its fuller nodes-and-arcs-to-RDF history for a future deck.
Transition — Return from the semantic model to the human interface: the original Web client supported writing as well as reading.
-->

---

<div class="eyebrow">1990 · WorldWideWeb implementation</div>

## The Web began as a read–write medium

<div class="readwrite-flow">
  <div class="rw-person"><span>human</span><strong>read</strong><strong>write</strong></div>
  <div class="rw-arrow">↔</div>
  <div class="rw-browser"><small>WORLDWIDEWEB · 1990</small><b>browser + editor</b><span>follow links · create pages · create links</span></div>
  <div class="rw-arrow">↔</div>
  <div class="rw-space"><span>shared</span><strong>information space</strong></div>
</div>

<p class="callout-line">Wikis did not invent read–write hypertext; they recovered an ambition the mainstream Web largely left behind.</p>

<p class="microcopy"><a href="https://www.w3.org/History/1989/proposal.html">1989 client/server proposal</a> · <a href="https://www.w3.org/People/Berners-Lee/WorldWideWeb.html">W3C, “WorldWideWeb: the first web client”</a> · <a href="https://www.w3.org/People/Berners-Lee/1997/Directions.html">Berners-Lee, “Realising the Full Potential of the Web”</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — web-read-write-medium
Learning objective — Explain the original Web’s read–write ambition and the later separation of browsing from editing.
Core claim — The first WorldWideWeb client was a browser-editor; wikis later recovered easy shared editing within the mainstream browser experience.
Explain — Be precise: Berners-Lee invented the Web, not the wiki. The first client could follow links, create pages, and create links. As passive browsers spread, intuitive editing became separated from reading. Wikis later made shared editing simple in an ordinary browser.
Misconception — WikiWikiWeb did not invent read–write hypertext, although it made collaborative maintenance radically accessible.
Check — Which affordance did mainstream browsing lose that wikis later made ordinary again?
Source routes — Follow the linked 1989 client/server proposal, W3C history of the first WorldWideWeb client, and Berners-Lee’s 1997 “Realising the Full Potential of the Web.”
Transition — The wiki’s larger contribution was not merely editing; it was a social process for continuous knowledge maintenance.
-->

---

<div class="eyebrow">1995 · WikiWikiWeb</div>

## Wiki made knowledge maintenance a social process

<div class="principle-wheel">
  <div class="principle"><b>Open</b><span>readers may repair</span></div>
  <div class="principle"><b>Incremental</b><span>link what is not written yet</span></div>
  <div class="principle"><b>Organic</b><span>structure grows with use</span></div>
  <div class="principle center-principle"><strong>WIKI</strong><small>write · link · refactor</small></div>
  <div class="principle"><b>Observable</b><span>changes can be reviewed</span></div>
  <div class="principle"><b>Convergent</b><span>duplication is reconciled</span></div>
  <div class="principle"><b>Mundane</b><span>few conventions suffice</span></div>
</div>

<p class="microcopy">Ward Cunningham, <a href="https://c2.com/doc/wikisym/WikiSym2006.pdf">“Design Principles of Wiki”</a>, WikiSym 2006.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — wiki-social-maintenance
Learning objective — Explain wiki as a social and procedural system for continuous knowledge maintenance.
Core claim — A wiki is a corpus plus a culture of writing, linking, reviewing, and refactoring—not merely a markup syntax.
Explain — The key shift is procedural. Openness lets readers repair; observability lets collaborators review; convergence reconciles duplication. “Incremental” is especially important because citing an unwritten page creates an affordance for future elaboration.
Misconception — Installing wiki software or using wiki syntax does not by itself create a maintained knowledge commons.
Check — Which wiki principle turns a missing page into useful future work, and how?
Source routes — Follow Ward Cunningham’s linked “Design Principles of Wiki.”
Transition — At social scale, link syntax must be joined by revision and governance infrastructure.
-->

---

<div class="eyebrow">2001 · wiki at social scale</div>

## Links became infrastructure for collective memory

<div class="wiki-scale">
  <div class="wiki-stage"><small>EARLY WIKI</small><b>CamelCase</b><span>lightweight page creation</span></div>
  <div class="wiki-step">→</div>
  <div class="wiki-stage amber-stage"><small>FREE LINKS</small><b>[[any phrase]]</b><span>concepts become addressable</span></div>
  <div class="wiki-step">→</div>
  <div class="wiki-stage teal-stage"><small>MEDIAWIKI</small><b>history + watchlists</b><span>revision becomes governable</span></div>
</div>

<div class="tag-row wiki-tags"><span class="tag">namespaces</span><span class="tag">backlinks</span><span class="tag">discussion</span><span class="tag">recent changes</span><span class="tag">revert</span><span class="tag teal-tag">maintenance reports</span></div>

<p class="microcopy"><a href="https://www.mediawiki.org/wiki/MediaWiki_history">MediaWiki history</a> · Wikipedia launched in January 2001; double-bracket “free links” emerged in the early Wikipedia toolchain.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — wiki-collective-memory
Learning objective — Explain how free links and revision infrastructure made links usable for collective memory.
Core claim — Arbitrary concept naming made knowledge easier to address, while history, watchlists, discussion, and revert made maintenance governable.
Explain — Ward’s first wiki used WikiWords. Double-bracket free links later allowed arbitrary phrases to become page identities without distorting prose. MediaWiki surrounded those links with namespaces, backlinks, discussion, recent changes, watchlists, history, and revert.
Misconception — Double-bracket links were not part of the original WikiWikiWeb, and link syntax alone did not produce Wikipedia’s collective memory.
Check — Why does arbitrary link text matter, and which governance feature makes the resulting edits accountable?
Source routes — Follow the linked MediaWiki history and its account of the early Wikipedia toolchain.
Transition — The next convergence makes this knowledge portable: a single plain-text file can carry both prose and structure.
-->

---

<div class="eyebrow">2001–2008 · file-native knowledge</div>

## Plain text became both prose and data

<div class="file-convergence">
  <div class="file-card yaml-card"><small>YAML · 2001</small><strong>human-readable structure</strong><code>status: contested</code></div>
  <div class="plus">+</div>
  <div class="file-card md-card"><small>MARKDOWN · 2004</small><strong>readable source text</strong><code>## A claim</code></div>
  <div class="plus">+</div>
  <div class="file-card git-card"><small>JEKYLL + GIT · 2008</small><strong>versioned content workflow</strong><code>diff → review → publish</code></div>
</div>

<div class="file-result"><b>A note can be read as prose, queried as structure, reviewed as a change, and moved without losing its meaning.</b></div>

<p class="microcopy"><a href="https://yaml.org/spec/1.2.2/">YAML specification history</a> · <a href="https://daringfireball.net/2004/03/introducing_markdown">Gruber, “Introducing Markdown”</a> · <a href="https://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker">Preston-Werner, “Blogging Like a Hacker”</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — plain-text-prose-data
Learning objective — Explain why YAML, Markdown, and Git together create a useful file-native knowledge substrate.
Core claim — A note can be human-readable prose, machine-queryable structure, and a reviewable versioned artifact at the same time.
Explain — YAML predates Markdown. Jekyll popularized their combination with Git for publishing. The technical result is a portable, tool-friendly, inspectable artifact that can be read directly, processed by scripts, compared as a diff, and moved among tools without surrendering its basic meaning.
Misconception — Jekyll did not start personal knowledge graphs, and YAML-flavored Markdown did not by itself cause the PKG movement.
Check — Name one human operation and one machine operation supported by the same Markdown-plus-YAML note.
Source routes — Follow the linked YAML specification history, Gruber’s “Introducing Markdown,” and Preston-Werner’s “Blogging Like a Hacker.”
Transition — Personal knowledge tools use this cheap, portable substrate to build graph-shaped second brains.
-->

---

<div class="eyebrow">2004–2020 · personal networked thought</div>

## The wiki became a personal knowledge graph

<div class="pkg-flow">
  <div class="pkg-node"><small>2004</small><b>TiddlyWiki</b><span>personal nonlinear notebook</span></div>
  <div class="pkg-link">→</div>
  <div class="pkg-node"><small>2019</small><b>Roam</b><span>networked thought + backlinks</span></div>
  <div class="pkg-link">→</div>
  <div class="pkg-node teal-node"><small>2020</small><b>Obsidian</b><span>local Markdown + graph</span></div>
</div>

<div class="grid two pkg-clarifier">
  <div class="card"><h3>PKM “knowledge graph”</h3><p>Notes, backlinks, tags, graph views, and emergent associations.</p></div>
  <div class="card amber-border"><h3>Academic personal KG</h3><p>Structured entities, attributes, and relations personally relevant to an individual.</p></div>
</div>

<p class="microcopy"><a href="https://tiddlywiki.com/static/The%2520Story%2520of%2520TiddlyWiki.html">The Story of TiddlyWiki</a> · <a href="https://roamresearch.com/">Roam Research</a> · <a href="https://obsidian.md/about">Obsidian</a> · <a href="https://www.tomkenter.nl/pdf/Personal%20Knowledge%20Graphs%20-%20ICTIR%202019.pdf">Balog &amp; Kenter, 2019</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — personal-knowledge-graph
Learning objective — Distinguish graph-shaped personal knowledge management from the more formal academic idea of a personal knowledge graph.
Core claim — Personal wikis evolved toward local, linked notes and backlinks, while academic PKGs usually require more explicit entities, attributes, and relations.
Explain — TiddlyWiki, Roam, and Obsidian illustrate the popular second-brain lineage: nonlinear notes, bidirectional links, local files, and graph views. The research literature uses overlapping language but generally assumes a more explicit knowledge representation about entities personally relevant to an individual.
Misconception — A graph visualization of linked notes is not automatically a formal knowledge graph.
Check — Would an Obsidian vault with only untyped wikilinks satisfy the academic PKG definition? What is missing?
Source routes — Follow the linked TiddlyWiki, Roam, and Obsidian histories, then compare them with Balog and Kenter’s 2019 paper.
Transition — Zettelkasten supplies an older and more disciplined account of how a personal note network generates thought.
-->

---

<div class="eyebrow">1950s–1990s · Zettelkasten</div>

## Luhmann built a network of arguments—not a filing system

<div class="pkg-flow">
  <div class="pkg-node"><small>ADDRESS</small><b>1/1a2</b><span>every note has a stable place</span></div>
  <div class="pkg-link">→</div>
  <div class="pkg-node"><small>BRANCH</small><b>insert nearby</b><span>extend an argument without reorganizing it</span></div>
  <div class="pkg-link">→</div>
  <div class="pkg-node teal-node"><small>REFER</small><b>cross-link</b><span>connect distant trains of thought</span></div>
</div>

<div class="grid two pkg-clarifier">
  <div class="card"><h3>Entry points, not a master taxonomy</h3><p>A selective keyword index and overview cards opened routes into the collection.</p></div>
  <div class="card amber-border"><h3>Serendipity by construction</h3><p>Following references resurfaced ideas in new contexts and helped generate manuscripts.</p></div>
</div>

<p class="microcopy">Johannes F. K. Schmidt, <a href="https://pub.uni-bielefeld.de/download/2942475/2942530">“Niklas Luhmann’s Card Index”</a> · <a href="https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_niklas-luhmanns-card-index_-sociologica_2018_12-1.pdf">“The Fabrication of Serendipity”</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — luhmann-zettelkasten
Learning objective — Identify the mechanisms that made Luhmann’s Zettelkasten a network of arguments rather than a filing taxonomy.
Core claim — Stable addresses, branching insertion, cross-references, selective entry points, and repeated traversal made the card index generative.
Explain — Luhmann’s two card indexes contained roughly 90,000 cards. A permanent address allowed nearby insertion without global reorganization; cross-references connected distant trains of thought; indexes opened selective routes; repeated traversal during writing resurfaced ideas in new contexts.
Misconception — “One idea per note” is a later simplification, not the complete historical definition of Luhmann’s method.
Check — Which mechanism creates serendipity without requiring a master taxonomy?
Source routes — Follow Schmidt’s linked account of Luhmann’s card index and “The Fabrication of Serendipity.”
Transition — Translate the mechanics into file-native form without pretending the furniture itself is the method.
-->

---

<div class="eyebrow">Zettelkasten → personal knowledge graph</div>

## A digital PKG preserves the mechanics—not the furniture

<div class="mapping-grid">
  <div class="mapping-head">Card-index mechanism</div><div class="mapping-head">File-native implementation</div>
  <div>Card + permanent slip address</div><div>Markdown note + stable filename, ID, or URI</div>
  <div>Branch beside an existing thought</div><div>Link a note into the argument it extends</div>
  <div>Cross-reference distant cards</div><div><code>[[wikilink]]</code>—ideally with the reason for the relation</div>
  <div>Keyword index + overview cards</div><div>Index notes, Maps of Content, properties, and queries</div>
  <div>Separate bibliographic apparatus</div><div>Source notes with citation and provenance metadata</div>
  <div>Re-encounter by following trails</div><div>Backlinks, local graph, search, and deliberate resurfacing</div>
</div>

<p class="callout-line">The graph view displays a network; the linking practice creates one worth traversing.</p>

<p class="microcopy"><a href="https://niklas-luhmann-archiv.de/bestand/zettelkasten/tutorial">Niklas Luhmann Archive</a> · <a href="https://obsidian.md/help/links">Obsidian internal links</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — zettelkasten-to-digital-pkg
Learning objective — Map functional Zettelkasten mechanics onto a file-native personal knowledge graph.
Core claim — Digital tools preserve the method when they support stable identity, contextual insertion, cross-reference, entry points, provenance, and deliberate resurfacing.
Explain — This is an analogy, not a claim that a digital graph reproduces Luhmann’s system. Folders and visualization can help, but neither replaces contextual insertion. The important operation is deciding where a thought participates and recording why. A formal PKG can additionally type consequential relations such as supports, contradicts, derived-from, supersedes, or uses-method.
Misconception — Recreating a card cabinet as folders or displaying a graph does not reproduce the reasoning practice.
Check — Choose one card-index mechanism and show its closest Obsidian implementation plus one way the digital version differs.
Source routes — Follow the linked Niklas Luhmann Archive tutorial and Obsidian internal-links documentation.
Transition — Obsidian provides a particularly inspectable implementation substrate for these mechanics.
-->

---

<div class="eyebrow">The file-native substrate</div>

## Obsidian makes the substrate inspectable

<div class="substrate-grid">
  <div class="substrate-item"><span class="tag teal-tag">pages</span><b>Markdown files</b><p>Human-readable, local, portable, scriptable.</p></div>
  <div class="substrate-item"><span class="tag amber">edges</span><b>[[wikilinks]]</b><p>Cheap references, backlinks, and unfinished destinations.</p></div>
  <div class="substrate-item"><span class="tag">schema</span><b>YAML properties</b><p>Types, status, dates, provenance, and controlled vocabulary.</p></div>
  <div class="substrate-item"><span class="tag rose-tag">views</span><b>Folders + queries + graph</b><p>Hierarchy, indexes, neighborhoods, and task-specific projections.</p></div>
</div>

<p class="callout-line">The vault supplies the medium; linking and maintenance practices turn it into memory.</p>

<p class="microcopy"><a href="https://obsidian.md/help/links">Obsidian internal links</a> · <a href="https://obsidian.md/help/properties">Obsidian properties</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — obsidian-substrate
Learning objective — Enumerate the file, link, metadata, and view affordances that make an Obsidian vault inspectable by humans and agents.
Core claim — Local Markdown, wikilinks, YAML properties, and multiple views provide a portable substrate; maintenance practices determine whether it becomes memory.
Explain — Pages give concepts editable local representations; wikilinks create cheap references and backlinks; properties expose machine-selectable state; folders, queries, and graph views offer task-specific projections. The same files can therefore support several memory profiles and toolchains.
Misconception — The graph view is a projection, not the memory method, and Obsidian alone does not supply trustworthy agentic rules or lifecycle semantics.
Check — Which affordance most directly supports auditability, and which supports machine selection?
Source routes — Follow Obsidian’s linked documentation for internal links and properties.
Transition — Add a new actor to this familiar substrate: an agent that performs maintenance work.
-->

---

<div class="eyebrow">2026 · a new division of labour</div>

## The new actor is not another reader—it is a maintainer

<div class="labour-shift">
  <div class="labour-side human-side"><small>PERSONAL WIKI</small><h3>The human</h3><span>writes</span><span>files</span><span>links</span><span>refactors</span><span>reviews</span></div>
  <div class="labour-arrow">→</div>
  <div class="labour-side shared-side"><small>AGENTIC WIKI</small><h3>Human + agent</h3><span>source</span><span>compile</span><span>cross-link</span><span>lint</span><span>challenge</span></div>
</div>

<p class="thesis-line">WikiMemory is not a new storage idea. It is a new actor in an old medium.</p>

<p class="microcopy">The shift became widely visible through <a href="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f">Karpathy’s “LLM Wiki”</a>, April 2026.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — agent-as-maintainer
Learning objective — Describe the division of labor between a human researcher and an agent maintaining a wiki.
Core claim — The novel actor is an agent that maintains useful structure and continuity within a human-governed medium.
Explain — The agent can find related sources, create or repair links, flag contradictions, summarize what a trail means, and keep paths connected as new evidence arrives. It can also file its execution trajectory so later work can inspect prior attempts rather than restart from scratch. The human remains source selector, question asker, editor, and epistemic judge.
Misconception — Maintenance does not transfer scientific authority to the agent: it may propose, connect, and flag, but it must not silently promote guesses into trusted claims or eliminate human review.
Check — Name one structural task to delegate, one trajectory detail to preserve, and one judgment that should remain explicitly human.
Source routes — Revisit Karpathy’s linked “LLM Wiki” idea file and compare its agent instructions with the earlier personal-wiki lineage.
Transition — Compare maintained synthesis with the dominant query-time retrieval architecture.
-->

---

<div class="eyebrow">Compiled memory</div>

## RAG retrieves fragments; WikiMemory preserves synthesis

<div class="compare-two">
  <div class="compare-panel rag-panel"><span class="tag">RAG</span><h3>Rediscover at query time</h3><div class="mini-flow"><span>chunks</span><i>→</i><span>retrieve</span><i>→</i><span>answer</span></div><p>Relationships assembled for one response usually disappear with it.</p></div>
  <div class="compare-panel wiki-panel"><span class="tag teal-tag">WikiMemory</span><h3>Compile and maintain</h3><div class="mini-flow"><span>sources</span><i>→</i><span>wiki</span><i>↻</i><span>work</span></div><p>Entities, tensions, and cross-source synthesis become reusable structure.</p></div>
</div>

<p class="caveat-line"><strong>Not a replacement:</strong> raw-source retrieval remains essential for evidence, verification, and details lost in compilation.</p>

<p class="microcopy"><a href="https://arxiv.org/abs/2605.07068">WiCER</a> finds blind compilation can discard critical facts; one or two evaluate–refine iterations recover much of the lost quality.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — rag-vs-wikimemory
Learning objective — Compare query-time retrieval with persistent, maintained synthesis without treating them as mutually exclusive.
Core claim — RAG grounds a response in retrieved evidence; WikiMemory preserves reusable synthesis, while retaining retrieval beneath it for verification and lost detail.
Explain — Avoid the false binary. A strong architecture keeps raw evidence and may use search or RAG beneath the wiki. The wiki stores maintained entities, relationships, tensions, and synthesis. Retrieval grounds claims and restores details that compilation may discard. WiCER makes that compilation risk empirical.
Misconception — WikiMemory neither replaces RAG nor guarantees that compiled pages preserve every important fact.
Check — When a compiled page omits a critical experimental detail, which layer should recover it and which layer should be repaired afterward?
Source routes — Follow the linked WiCER paper, especially its compilation and evaluate–refine findings.
Transition — Ask what structural affordances make a folder of files operable enough to support this maintenance loop.
-->

---

<div class="eyebrow">Why wiki affordances matter</div>

## Structure turns a folder into an operable knowledge space

<div class="affordance-grid">
  <div class="affordance"><b>Stable identity</b><span>A page gives a concept an address that agents and humans can revisit.</span></div>
  <div class="affordance"><b>Traversable relations</b><span>Links create explicit paths for search, context expansion, and synthesis.</span></div>
  <div class="affordance"><b>Structured metadata</b><span>Properties expose type, status, provenance, ownership, and lifecycle.</span></div>
  <div class="affordance"><b>Hierarchical scope</b><span>Folders and indexes bound domains and support progressive disclosure.</span></div>
  <div class="affordance"><b>Revision</b><span>Diffs and history make memory editable without becoming unaccountable.</span></div>
  <div class="affordance"><b>Human legibility</b><span>The same artifact can be inspected, challenged, and repaired directly.</span></div>
</div>

<p class="microcopy">Design synthesis. Plain links remain the navigation baseline; add typed predicates when the relation changes query, validation, explanation, or workflow.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — wiki-affordances
Learning objective — Explain how identity, relations, metadata, scope, revision, and legibility turn files into an operable knowledge space.
Core claim — Wiki affordances make knowledge revisitable, traversable, selectable, reviewable, and directly repairable by both humans and agents.
Explain — Stable pages provide addresses; links provide paths; metadata exposes status and provenance; hierarchy bounds scope; revision makes edits accountable; plain text keeps the artifact inspectable. Typed predicates add value when the distinction changes a query, validation rule, explanation, or workflow.
Misconception — A collection of links is not automatically a sound knowledge graph, and indiscriminate typing can replace link ambiguity with schema noise.
Check — Give one relation that deserves a typed predicate and one ordinary navigational link that does not.
Source routes — This is a design synthesis grounded in the preceding history; connect each affordance to the system that contributed it.
Transition — Hierarchical scope becomes especially important when an agent cannot load the entire corpus into context.
-->

---

<div class="eyebrow">Progressive disclosure</div>

## `index.md` turns hierarchy into a context budget

<div class="note-anatomy">
  <pre><code>&#35; Scientific WikiMemory

- [Claims](claims/)
  Synthesized claims, evidence, and status.
- [Methods](methods/)
  Procedures, assumptions, and validation.
- [Experiments](experiments/)
  Runs, outcomes, failures, and decisions.
- [Sources](sources/)
  Papers, data, code, and conversations.</code></pre>
  <div class="anatomy-labels">
    <div><b>Survey</b><span>see the available scopes cheaply</span></div>
    <div><b>Select</b><span>choose a branch for the present task</span></div>
    <div><b>Expand</b><span>open its index, then relevant pages</span></div>
    <div><b>Ground</b><span>reopen raw sources only when needed</span></div>
  </div>
</div>

<p class="callout-line">Context grows with relevance—not with the size of the corpus.</p>

<p class="microcopy">Google Cloud, <a href="https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#8-index-files">Open Knowledge Format v0.2, §8 “Index files”</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — index-context-budget
Learning objective — Use index.md files as routing layers for progressive disclosure under a limited context budget.
Core claim — A hierarchy becomes agent-operable when each index cheaply reveals available scopes and lets context expand only where the task requires it.
Explain — OKF permits index.md at any directory level. It groups links to concepts or subdirectories and recommends carrying each target’s short description, so a human or agent can see what is available before opening individual documents. The specification calls this progressive disclosure. Our harness interpretation is to survey, select, recursively expand, ground in raw sources when necessary, and stop when the task is sufficiently supported.
Misconception — An index is not an exhaustive table of contents that should always be loaded together with every descendant page.
Check — After reading a root index, what condition tells the agent to stop expanding rather than open another branch?
Source routes — Follow the linked Open Knowledge Format v0.2 specification, section 8 “Index files.”
Transition — Optionally move from hierarchical routing into the local typed neighborhood that an index helps reveal.
-->

---

<div class="eyebrow">A maintained neighborhood</div>

## A WikiMemory document is a typed node—not an isolated page

<div class="neighborhood-frame" aria-label="A typed WikiMemory neighborhood with a highlighted inquiry trail from a paper through a claim, conflicting experiment, question, and revised experiment">
  <div class="neighborhood-trail">
    <div class="trail-state source-state"><small>SOURCE · PAPER</small><b>paper-17</b><span>reported result</span></div>
    <div class="trail-edge"><b>supports</b><i>→</i></div>
    <div class="trail-state claim-state"><small>CLAIM</small><b>claim-7</b><span>contestable assertion</span></div>
    <div class="trail-edge rose-edge"><b>contradicts</b><i>→</i></div>
    <div class="trail-state run-state"><small>EXPERIMENT · RUN</small><b>run-042</b><span>conflicting result</span></div>
    <div class="trail-edge"><b>motivates</b><i>→</i></div>
    <div class="trail-state question-state"><small>OPEN QUESTION</small><b>question-3</b><span>what changed?</span></div>
    <div class="trail-edge"><b>revises</b><i>→</i></div>
    <div class="trail-state revised-state"><small>NEXT ACTION · RUN</small><b>run-043</b><span>revised experiment</span></div>
  </div>
  <div class="neighborhood-context">
    <div class="neighborhood-role"><small>METHOD · PROTOCOL</small><b>protocol-03</b><span><em>tests</em> the runs under a declared procedure</span></div>
    <div class="concept-hub"><small>CONCEPT NOTE · HUB</small><b>Compilation gap</b><span>organizes meaning, scope, and navigation across the neighborhood</span><em>concerns ↑ the highlighted trail</em></div>
    <div class="claim-boundary"><small>ASSERTION BOUNDARY</small><b>Claims stay separate</b><span>Contestable assertions keep their own evidence, contradictions, maturity, and review lifecycle.</span></div>
  </div>
</div>

<p class="microcopy">Design synthesis: typed note roles and edges make the inquiry path inspectable; the concept note coordinates the neighborhood rather than absorbing every assertion.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — wikimemory-neighborhood
Learning objective — Interpret WikiMemory documents as typed nodes in a maintained neighborhood and identify an inquiry trail as one path through that graph.
Core claim — A concept note organizes meaning and navigation, while sources, claims, runs, methods, questions, and next actions retain distinct roles, evidence, and lifecycles.
Explain — Read the highlighted path as a Bush-style inquiry trail: paper-17 supports claim-7; run-042 contradicts it; the conflict motivates question-3; the question leads to revised run-043. Protocol-03 records how runs are tested. The concept note connects this neighborhood without swallowing its contestable assertions; those remain in claim notes where provenance, contradictions, maturity, and review can stay inspectable.
Misconception — A central concept note is not the single source of truth, and drawing many links to it does not make its claims better supported.
Check — Optional exploration: which node should change when run-043 produces a new result, and which neighboring nodes should be reviewed rather than overwritten?
Source routes — Treat this as the deck’s design synthesis of Bush-style trails, typed links, note roles, and scientific provenance; route backward to slides 7 and 22 or forward to the claim-note and typed-edge slides.
Transition — Optional route: zoom into the claim node to separate lifecycle maturity from epistemic status.
-->

---

<div class="eyebrow">Claim-note zoom · illustrative fields</div>

## A claim note keeps maturity separate from epistemic status

<div class="claim-note-zoom">
  <pre class="claim-frontmatter"><code><span class="code-comment">---</span>
<span class="code-key">type:</span> <span class="code-type">claim</span>
<span class="code-key">maturity:</span> <span class="code-type">draft</span>
<span class="code-key">epistemic_status:</span> <span class="code-type">contested</span>
<span class="code-key">creator:</span> <span class="code-type">researcher-or-agent-id</span>
<span class="code-key">context:</span> <span class="code-type">inquiry/compilation-gap</span>
<span class="code-key">supported_by:</span> [<span class="code-type">"[[paper-17]]"</span>]
<span class="code-key">contradicted_by:</span> [<span class="code-type">"[[run-042]]"</span>]
<span class="code-key">review_after:</span> <span class="code-type">2026-10-01</span>
<span class="code-comment">---</span></code></pre>
  <div class="claim-readable">
    <div><small>CLAIM</small><b>Compiled knowledge reduces rediscovery.</b></div>
    <div><small>EVIDENCE</small><span><code>paper-17</code> supports the claim under the reported study conditions.</span></div>
    <div class="tension-block"><small>TENSIONS</small><span><code>run-042</code> contradicts the expected effect in a new evaluation.</span></div>
    <div><small>OPEN QUESTION</small><span>Which omitted details explain the disagreement?</span></div>
    <div><small>NEXT INQUIRY</small><span>Revise the protocol, run <code>run-043</code>, then review this claim.</span></div>
  </div>
</div>

<p class="claim-distinction"><strong>Maturity</strong> asks how developed the note is. <strong>Epistemic status</strong> asks how well the claim is currently supported.</p>

<p class="microcopy">Illustrative Obsidian-compatible claim note—not a canonical schema for llm-wiki-colab or every vault.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — wikimemory-page-anatomy
Learning objective — Read an illustrative claim note that separates lifecycle maturity from epistemic status while preserving provenance, supporting and contradictory evidence, review timing, and next inquiry.
Core claim — A claim becomes inspectable when machine-readable relations and lifecycle fields remain paired with readable evidence, tensions, questions, and next actions.
Explain — The example labels type, maturity, epistemic status, creator and creation context, supporting paper, contradictory run, and review timing. The prose sections then state the claim, evidence, tension, open question, and next inquiry. Keeping maturity separate from epistemic status prevents “well edited” from being mistaken for “well supported,” while typed relations keep both support and contradiction traversable.
Misconception — These fields are illustrative rather than a universal llm-wiki-colab schema, and structured frontmatter cannot turn an unsupported assertion into dependable knowledge.
Check — Optional exploration: which field should change after an editorial cleanup, which after contradictory evidence, and which after a successful replication?
Source routes — Treat the card as an illustrative claim-note specialization; route backward to the typed neighborhood or forward to the governed transaction and typed-edge slides.
Transition — Optional route: ask how an agent chooses the next useful note among the outgoing links in this neighborhood.
-->

---

<div class="eyebrow">Agentic graph navigation · Markov analogy</div>

## The neighborhood is the transition space; the realized sequence is the trail

<div class="navigation-layout">
  <div class="navigation-state-panel">
    <div class="query-chip"><small>TASK / QUERY</small><b>Which evidence challenges claim-7?</b></div>
    <div class="current-note"><small>CURRENT STATE · NOTE</small><b>claim-7</b><span>outgoing typed links define locally available transitions</span></div>
    <div class="transition-options">
      <div><code>supported_by</code><span>paper-17</span></div>
      <div class="selected-transition"><code>contradicted_by</code><span>run-042</span><b>selected</b></div>
      <div><code>tested_by</code><span>protocol-03</span></div>
      <div><code>motivates</code><span>question-3</span></div>
    </div>
  </div>
  <div class="navigation-policy-panel">
    <div class="policy-box"><small>QUERY-CONDITIONED POLICY / WEIGHTING</small><b>score(next note | task, context, edge semantics, evidence state)</b><span>choose a useful transition—not merely the most linked node</span></div>
    <div class="realized-trail"><small>REALIZED TRAIL / TRAJECTORY</small><div><span>concept</span><i>→</i><span>claim-7</span><i>→</i><span>run-042</span><i>→</i><span>question-3</span></div></div>
  </div>
</div>

<p class="caveat-line navigation-caveat"><strong>Markov-chain connection:</strong> notes can be modeled as states and typed links as possible transitions. This is a design analogy—not a claim that the current plugin implements one particular Markov algorithm.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — agentic-neighborhood-navigation
Learning objective — Connect graph navigation to a Markov-style state-transition model without assuming a specific implemented algorithm.
Core claim — A note’s local neighborhood is the available transition space, while a task-conditioned policy or weighting realizes one useful sequence as a trail or execution trajectory.
Explain — Treat notes as states and outgoing typed links as possible transitions. The task, current context, link meaning, provenance, and evidence status can weight which neighboring note is useful next. In the example, a query about challenges favors the contradicted_by edge to run-042, yielding a realized path through the graph. This framing connects to Markov-chain work while remaining implementation-neutral.
Misconception — Link count, centrality, or proximity alone does not establish relevance or truth, and the current llm-wiki-colab materials do not document a single canonical Markov navigation algorithm.
Check — Optional exploration: for a replication-planning query, which outgoing relation should receive more weight, and what evidence-status signal could change that choice?
Source routes — This is a conceptual bridge to state-transition and Markov-chain reasoning; use the deck’s linked llm-wiki-colab sources for implemented graph and lifecycle behavior, not as evidence of a specific navigation algorithm.
Transition — Optional route: move from read-side navigation to the harness that governs graph-changing writes.
-->

---

<div class="eyebrow">Harness externalization</div>

## The harness turns a writable vault into a memory system

<div class="harness-memory">
  <div class="hm-layer model-layer"><span class="tag">MODEL</span><b>interpret · propose · synthesize</b></div>
  <div class="hm-arrow">↕</div>
  <div class="hm-layer harness-layer"><span class="tag amber">HARNESS</span><b>select · authorize · validate · observe · rollback</b></div>
  <div class="hm-arrow split-arrow">↓ <span>↓</span> ↓</div>
  <div class="hm-outputs">
    <div><span class="tag teal-tag">MEMORY</span><b>state + knowledge</b></div>
    <div><span class="tag amber">SKILLS</span><b>reusable procedure</b></div>
    <div><span class="tag rose-tag">PROTOCOLS</span><b>interaction rules</b></div>
  </div>
</div>

<p class="callout-line">Persistence is an externalized capability; reliability comes from how the harness governs it.</p>

<p class="microcopy"><a href="https://arxiv.org/html/2604.08224v1">Zhou et al., “Externalization in LLM Agents”</a> · <a href="https://openreview.net/attachment?id=e64EcfHp8L&amp;name=pdf">“The Living Wiki”</a> treats the vault schema as a procedural Skill.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — harness-memory-system
Learning objective — Apply the harness-externalization frame to a writable knowledge vault.
Core claim — Persistence comes from external files, but reliability comes from a harness that selects context, authorizes changes, validates evidence, observes outcomes, and can roll back.
Explain — Files alone do not decide when an agent writes, which evidence is required, whether a change is accepted, or what must be preserved. Provenance keeps claims tied to sources; controlled write scopes and review bound authority; validation tests proposed changes; logs preserve actions and outcomes; rollback reverses changes that fail. Rules, skills, tools, permissions, and gates encode those responsibilities.
Misconception — A persistent folder is not automatically a dependable memory system, and a capable model cannot substitute for lifecycle governance or turn an unsupported guess into a trusted claim.
Check — Optional exploration: for an agent proposing to change a contested claim, name one responsibility at each of select, authorize, validate, observe, and rollback.
Source routes — Follow Zhou et al.’s linked “Externalization in LLM Agents” and the linked “Living Wiki” treatment of vault schema as a procedural skill.
Transition — Optional route: express a write as a governed graph change set and distinguish the generic plugin lifecycle from a stronger vault specialization.
-->

---

<div class="eyebrow">Governed write · graph change set</div>

## A WikiMemory write changes a neighborhood—not just one file

<div class="transaction-grid">
  <div class="tx-step"><small>01 · INTAKE</small><b>New evidence</b><span>paper · data · run · conversation</span></div>
  <div class="tx-step"><small>02 · ORIENT</small><b>Deduplicate + route</b><span>find the existing neighborhood and note role</span></div>
  <div class="tx-step"><small>03 · WRITE</small><b>Create or revise typed notes</b><span>preserve evidence and contestable claims</span></div>
  <div class="tx-step"><small>04 · INTEGRATE</small><b>Add typed + reciprocal links</b><span>repair both sides of consequential relations</span></div>
  <div class="tx-step"><small>05 · COORDINATE</small><b>Update concept · index · log</b><span>keep navigation and change history coherent</span></div>
  <div class="tx-step"><small>06 · VERIFY</small><b>Check provenance + structure</b><span>scope · links · evidence · structure</span></div>
  <div class="tx-step"><small>07 · AUTHORIZE</small><b>Review + commit</b><span>apply the profile’s write and Git controls</span></div>
  <div class="tx-step"><small>08 · DERIVE</small><b>Rebuild graph · permit rollback</b><span>when the profile defines derived RDF / SHACL</span></div>
</div>

<div class="transaction-profiles">
  <div class="generic-profile"><small>GENERIC · <code>llm-wiki-colab</code></small><b>Governed wiki lifecycle</b><span>orientation · explicit ingest skills · verification gate · index/log integration · Git coordination</span></div>
  <div class="vault-profile"><small>SPECIALIZATION · VAULT <code>/encode</code></small><b>Stronger typed transaction</b><span>type routing · maturity + epistemic state · creator/context provenance · review · commit · RDF/SHACL rebuild</span></div>
</div>

<p class="microcopy"><a href="https://github.com/LA3D-LLM-Agents/llm-wiki-colab">LA3D-LLM-Agents, <code>llm-wiki-colab</code></a> · <a href="https://doi.org/10.5281/zenodo.21213175">Saboia Moreira et al., “Beyond Memory”</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — llm-wiki-colab-lifecycle
Learning objective — Trace a WikiMemory write as a governed graph change set and distinguish llm-wiki-colab’s generic lifecycle from the vault /encode specialization.
Core claim — A dependable write integrates evidence across notes, links, indexes, logs, verification, authorization, and rollback rather than treating one edited file as the whole transaction.
Explain — The common change-set pattern is to orient and deduplicate, route evidence to an appropriate note role, create or revise typed notes, repair consequential links, update the concept neighborhood plus index and log, verify provenance and structure, authorize and commit, then rebuild derived graph artifacts where the profile defines them. llm-wiki-colab provides a governed wiki lifecycle through orientation, skills, verification, logs, and Git coordination. The vault /encode lane is a stronger specialization with explicit type routing, separate maturity and epistemic state, creator/context provenance, reciprocal integration, review, commit, and RDF/SHACL rebuild.
Misconception — The two lanes do not share one universal schema: llm-wiki-colab is a portable governed lifecycle, while /encode adds repository-specific transaction semantics and derived-graph checks.
Check — Optional exploration: which steps belong to any governed wiki write, and which are specifically stronger commitments of the vault /encode profile?
Source routes — Follow the linked llm-wiki-colab repository and “Beyond Memory” for the generic lifecycle; treat the clearly labeled /encode lane as the author-supplied vault specialization rather than a claim about the plugin’s canonical schema.
Transition — Optional route: zoom into typed-edge compilation as one method used inside a governed change set.
-->

---

<div class="eyebrow">Our implementation · typed edges</div>

## Readable predicates compile into an operable graph

<div class="edge-method">
  <div class="edge-authoring">
    <small>AUTHOR IN ORDINARY MARKDOWN</small>
    <div class="edge-form"><b>Page-level · YAML</b><pre><code><span class="code-key">supports:</span> <span class="code-type">"[[Claim-X]]"</span>
<span class="code-key">dependsOn:</span> <span class="code-type">"[[Dataset-Y]]"</span></code></pre></div>
    <div class="edge-form"><b>Contextual · visible inline annotation</b><pre><code>[Claim X](Claim-X)
([*supports*](Edge-Types#supports))</code></pre></div>
  </div>
  <div class="edge-compile-flow">
    <small>COMPILE + CHECK</small>
    <div><b>Markdown + YAML</b><span>forward predicates + plain mentions</span></div><i>↓ extract</i>
    <div><b>JSON-LD / RDF</b><span>stable page and predicate IRIs</span></div><i>↓ materialize</i>
    <div><b>Graph operations</b><span>inverse edges · SHACL · SPARQL</span></div>
  </div>
</div>

<div class="edge-vocabulary">
  <div><b>Evidence</b><span>source · supports · criticizes</span></div>
  <div><b>Semantics</b><span>concept · defines · related · mentions</span></div>
  <div><b>Structure</b><span>up · partOf · outOfScopeFor</span></div>
  <div><b>Evolution</b><span>extends · precedes · incorporatedInto</span></div>
  <div><b>Dependency</b><span>dependsOn · feedsInto · resolvedBy</span></div>
</div>

<p class="microcopy"><a href="https://github.com/LA3D-LLM-Agents/llm-wiki-colab/blob/main/codex/plugins/llm-wiki/core/Edge-Types.md.template"><code>Edge-Types.md</code> vocabulary</a> · <a href="https://github.com/LA3D-LLM-Agents/llm-wiki-colab/tree/main/codex/plugins/llm-wiki/core/scripts/kg">KG build pipeline</a> · forward predicates are authored; inverses are materialized.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — typed-edge-compilation
Learning objective — Trace a readable relation from Markdown authoring through extraction, RDF representation, validation, and graph querying.
Core claim — Consequential relationships can be promoted to governed predicates while ordinary links remain a low-cost navigation baseline.
Explain — This is progressive formalization. Page-level relations live in YAML; local claims can use a visible GitHub-wiki-compatible predicate annotation; an ordinary link is recorded as mentions. The extractor deduplicates the forms, maps them through a JSON-LD context, materializes inverse edges, validates with SHACL, and supports SPARQL queries such as supports-versus-criticizes.
Misconception — Authors and agents should not assert both directions of a relation; the build owns inverse edges so the two directions cannot silently disagree. Not every mention deserves promotion to a typed predicate.
Check — Where would you author a page-wide dependsOn relation, where would you author a local supports claim, and what does a plain link become?
Source routes — Follow the linked Edge-Types vocabulary and KG build pipeline in llm-wiki-colab.
Transition — Typed edges are one method; skills make the wider scientific maintenance procedures explicit and executable.
-->

---

<div class="eyebrow">Our implementation · executable methodology</div>

## Skills make scientific maintenance explicit

<div class="grid three">
  <div class="card teal"><span class="tag teal-tag">wiki-source</span><h3>Integrate external evidence</h3><p>Create a source summary, update the existing conceptual neighborhood, record typed relations, repair backlinks, and verify before commit.</p></div>
  <div class="card amber-border"><span class="tag amber">wiki-experiment</span><h3>File results honestly</h3><p>Preserve configuration, measured metrics, comparison, surprise, negative results, affected claims, code paths, and commit identity.</p></div>
  <div class="card rose"><span class="tag rose-tag">wiki-lint</span><h3>Maintain corpus integrity</h3><p>Surface orphans, dead links, stale claims, missing metadata, one-way references, index gaps, and naming drift.</p></div>
</div>

<div class="schema-strip"><span class="tag">SUPPORTING SKILLS</span><b>bootstrap: <code>wiki-init</code> · diagnose: <code>wiki-doctor</code> · collaborate: <code>wiki-ask</code> / <code>wiki-enroll</code></b></div>

<p class="microcopy"><a href="https://github.com/LA3D-LLM-Agents/llm-wiki-colab/tree/main/codex/plugins/llm-wiki/skills">Skills in <code>llm-wiki-colab</code></a> · each write procedure delegates to a shared Verification Gate.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — executable-wiki-skills
Learning objective — Differentiate the epistemic obligations of source ingest, experiment filing, and corpus linting.
Core claim — Scientific maintenance becomes inspectable when distinct operations are encoded as explicit skills that converge on a shared verification gate.
Explain — “The agent maintains the wiki” is too vague. Source ingest must integrate external evidence and provenance; experiment ingest must preserve configuration, metrics, comparison, surprise, negative results, code, and commit identity; linting diagnoses structural integrity. Writes integrate rather than append and may update the new page, existing claims, reciprocal links, the index, and the log.
Misconception — One generic maintenance prompt is not equivalent to procedures with different evidence obligations; wiki-lint is diagnostic first rather than permission to rewrite everything automatically.
Check — Which skill should record a negative experimental result, and what information must it preserve that a source summary need not?
Source routes — Follow the linked skills directory in llm-wiki-colab and inspect the shared Verification Gate delegated to by write procedures.
Transition — These local project memories can remain owned by their projects while a federation makes expertise discoverable.
-->

---

<div class="eyebrow">Our implementation · LA3D-LLM-Agents</div>

## A federation keeps memory local—and expertise reachable

<div class="compile-flow">
  <div class="compile-layer raw-layer"><small>PROJECT AGENT</small><b>repo + wiki + Agent Card</b><span>source of truth for one research domain</span></div>
  <div class="compile-arrow"><span>publish capability metadata</span>→</div>
  <div class="compile-layer wiki-layer"><small>FEDERATION INDEX</small><b>discover who knows what</b><span>topics · capabilities · contact</span></div>
  <div class="compile-arrow"><span>select + consult</span>→</div>
  <div class="compile-layer answer-layer"><small>PEER AGENT</small><b>ask · message · post</b><span>cross-project collaboration through files</span></div>
</div>

<p class="callout-line">Share an honest capability description; consult the source wiki; avoid copying every project into private context.</p>

<p class="microcopy"><a href="https://github.com/LA3D-LLM-Agents">LA3D LLM Agents organization profile</a> · <a href="https://la3d-llm-agents.github.io/">federation index</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — federated-project-memory
Learning objective — Explain how local project ownership and federated discovery can coexist.
Core claim — Projects should maintain their own source-of-truth wikis and publish honest capability metadata so peers can discover and consult expertise without copying every corpus into private context.
Explain — Each organization member is a research-project repository paired with a curated wiki and a published Agent Card. The federation index supports discovery. Ask is a synchronous clone-and-consult operation; message is an asynchronous direct mailbox; post is a topical broadcast. Transparent file-based primitives connect expertise while memory stays with the project that owns it.
Misconception — Federation does not require centralizing all project wikis or treating an Agent Card as evidence that every claimed capability is correct.
Check — When should an agent use ask, message, or post, and where should the resulting durable knowledge ultimately be maintained?
Source routes — Follow the linked LA3D LLM Agents organization profile and federation index.
Transition — Place our implementation inside the wider 2026 research cluster now exploring different parts of this system.
-->

---

<div class="eyebrow">A field crystallizes · 2026</div>

## Recent work is filling in different parts of the system

<div class="field-map">
  <div class="field-row"><b>Representation</b><span>Karpathy</span><span>Living Wiki</span><em>persistent, linked, inspectable synthesis</em></div>
  <div class="field-row"><b>Compilation</b><span>WiCER</span><span>DeepRefine</span><em>diagnose loss; iteratively repair the artifact</em></div>
  <div class="field-row"><b>Navigation</b><span>LLM-Wiki</span><span>WikiLoop</span><em>search, read, traverse, and learn from downstream use</em></div>
  <div class="field-row"><b>Provenance</b><span>TrajWiki</span><span>Beyond Memory</span><em>preserve evolution, failures, and source-grounded revision</em></div>
  <div class="field-row"><b>Learning</b><span>WikiSkill</span><span>skills</span><em>compile experience into reusable procedures</em></div>
</div>

<p class="microcopy"><a href="https://www.langchain.com/blog/wiki-memory">Chase, 2026</a> · <a href="https://arxiv.org/abs/2605.07068">WiCER</a> · <a href="https://arxiv.org/abs/2605.25480">LLM-Wiki</a> · <a href="https://arxiv.org/abs/2607.26604">WikiLoop</a> · <a href="https://arxiv.org/abs/2608.00967">TrajWiki</a> · <a href="https://arxiv.org/abs/2607.24759">Beyond Memory</a> · <a href="https://arxiv.org/html/2608.27454v1">WikiSkill</a>.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — wikimemory-research-field
Learning objective — Map recent WikiMemory work onto representation, compilation, navigation, provenance, and learning.
Core claim — The 2026 research cluster is filling complementary system dimensions; no single paper or implementation supplies the whole stack.
Explain — The term is no longer only a viral pattern. Work appearing between April and August 2026 addresses persistent representation, compilation loss and refinement, navigation and downstream learning, provenance and revision, and the conversion of experience into reusable procedure. The composition matters more than declaring one winning architecture.
Misconception — A strong result in one row does not solve the other dimensions or establish end-to-end scientific trustworthiness.
Check — Match WiCER, TrajWiki, and WikiSkill to the primary system dimension each contributes.
Source routes — Follow the linked contemporary sources on this slide: Chase, WiCER, LLM-Wiki, WikiLoop, TrajWiki, Beyond Memory, and WikiSkill.
Transition — Before celebrating persistent memory, examine how the same compounding mechanism can amplify error.
-->

---

<div class="eyebrow">Memory needs epistemology</div>

## An agent-maintained wiki can compound error, too

<div class="risk-loop">
  <div class="risk-node"><b>Weak source</b><span>enters the corpus</span></div><i>→</i>
  <div class="risk-node amber-risk"><b>Unsupported claim</b><span>looks more settled than its evidence</span></div><i>→</i>
  <div class="risk-node amber-risk"><b>Concept synthesis</b><span>drops the qualification</span></div><i>→</i>
  <div class="risk-node rose-risk"><b>Central page</b><span>gains links and apparent authority</span></div><i>→</i>
  <div class="risk-node"><b>Later agents</b><span>repeat and reinforce it</span></div>
</div>

<div class="grid four risk-controls">
  <div class="card"><h3>Evidence</h3><p>Claim-level provenance + explicit contradictory evidence.</p></div>
  <div class="card teal"><h3>State + review</h3><p>Maturity ≠ epistemic status · scheduled re-examination.</p></div>
  <div class="card amber-border"><h3>Revision</h3><p>Supersession + controlled writes preserve what changed and why.</p></div>
  <div class="card rose"><h3>Evaluation</h3><p>Probes detect entrenchment; failed changes can roll back.</p></div>
</div>

<p class="microcopy"><a href="https://arxiv.org/abs/2604.12034">“Memory as Metabolism”</a> highlights entrenchment and contradictory evidence · <a href="https://arxiv.org/abs/2608.00967">TrajWiki</a> uses immutable snapshots plus ADD / REVISE / DEPRECATE operations.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — memory-entrenchment-risk
Learning objective — Explain how an agent-maintained wiki can entrench weak claims and identify controls that interrupt the loop.
Core claim — Persistence and centrality can amplify an unsupported claim when concept synthesis drops qualifications and later agents treat links as authority.
Explain — The failure chain is explicit: a weak source supports an inadequately qualified claim; concept synthesis loses the caveat; the concept page becomes central; later agents repeat it and reinforce the same neighborhood. Controls map to the chain: claim-level provenance and contradictory evidence expose weak support; separate maturity and epistemic status plus scheduled review keep uncertainty visible; supersession and controlled writes preserve revision; evaluation detects downstream repetition; rollback reverses harmful changes.
Misconception — A mature, central, or frequently traversed note is not necessarily true, and a concept note must not absorb contested assertions without their provenance and contradictions.
Check — Optional exploration: choose one arrow in the error loop and name the control that would detect, interrupt, or reverse it before the next agent repeats the claim.
Source routes — Follow the linked “Memory as Metabolism” discussion of entrenchment and contradictory evidence and TrajWiki’s immutable snapshots with ADD, REVISE, and DEPRECATE operations.
Transition — Optional route: with these controls in place, examine how trajectories can be distilled into candidate procedures without treating the distillation as automatically trustworthy.
-->

---

<div class="eyebrow">From memory to learning</div>

## WikiSkill compiles experience into validated procedure

<div class="wikiskill-loop">
  <div class="ws-node raw-ws"><small>RAW</small><b>execution traces</b><span>successes + failures</span></div>
  <div class="ws-arrow">→</div>
  <div class="ws-node wiki-ws"><small>WIKI</small><b>persistent patterns</b><span>diagnoses + history</span></div>
  <div class="ws-arrow">→</div>
  <div class="ws-node skill-ws"><small>SKILLS</small><b>candidate procedure</b><span>instructions + resources</span></div>
  <div class="ws-arrow gate-arrow">→<small>validate</small></div>
  <div class="ws-gate"><b>accept</b><span>or rollback</span></div>
</div>

<p class="result-line"><strong>Key result:</strong> persistent wiki knowledge materially improves skill evolution; accepted skills can transfer across models.</p>

<p class="microcopy">Tang et al., <a href="https://arxiv.org/html/2608.27454v1">“WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution”</a>, Google Research, Aug. 2026.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — wikiskill-learning-loop
Learning objective — Distinguish an intellectual trail from an execution trajectory, then trace how trajectories are distilled and validated as candidate procedures.
Core claim — A persistent wiki can help procedures evolve, but distilled experience becomes dependable knowledge only after an outer-loop harness validates it on tasks and can roll it back.
Explain — An intellectual trail records movement through evidence and ideas; an execution trajectory records what an agent tried, which tools or steps it used, and the resulting outcomes and failures. Both preserve continuity, but they are different artifacts. The wiki can distill raw trajectories into candidate reusable lessons, instructions, and resources. Task-level evaluation must then demonstrate improvement, record outcomes, and roll back candidates that fail.
Misconception — A trajectory, plausible wiki summary, or well-written candidate skill is not itself a dependable procedure; distillation can erase context or promote a coincidental success unless validation tests the resulting behavior.
Check — Why is rollback necessary, and what evidence should the acceptance gate inspect?
Source routes — Follow Tang et al.’s linked WikiSkill preprint, especially the ablations on persistent knowledge and cross-model skill transfer; compare this execution path with Bush’s associative trail as a continuity analogy, not a prediction of AI.
Transition — Generalize from learned procedures to a definition of scientific memory that preserves evidence, knowledge, and contestable method.
-->

---

<div class="eyebrow">Scientific WikiMemory</div>

## Scientific memory must preserve why we believe—or doubt

<div class="science-stack">
  <div class="science-layer evidence-layer"><span>RAW EVIDENCE</span><b>papers · data · code · runs · conversations</b><small>immutable or independently recoverable</small></div>
  <div class="science-up">↑ grounded by</div>
  <div class="science-layer knowledge-layer"><span>WIKI KNOWLEDGE</span><b>claims · entities · methods · tensions · provenance</b><small>maintained, linked, revisioned</small></div>
  <div class="science-up">↑ operationalized as</div>
  <div class="science-layer procedure-layer"><span>SCIENTIFIC PROCEDURE</span><b>workflows · checks · skills · decision protocols</b><small>tested, gated, and inspectable</small></div>
</div>

<p class="thesis-line small-thesis">A scientific second brain should not only remember conclusions; it should preserve the routes by which conclusions remain contestable.</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — scientific-wikimemory-definition
Learning objective — Define Scientific WikiMemory as a layered relationship among recoverable evidence, maintained knowledge, and validated procedure.
Core claim — Scientific memory must preserve why claims are believed or doubted so conclusions remain traceable, revisable, and contestable.
Explain — Raw evidence includes papers, data, code, runs, and conversations that remain immutable or independently recoverable. Wiki knowledge maintains claims, entities, methods, tensions, provenance, and revision. Scientific procedures operationalize that knowledge as workflows, checks, skills, and decision protocols that can be tested and inspected.
Misconception — A conclusion-only second brain is not sufficient for science; provenance, negative results, uncertainty, competing interpretations, reproducibility, and human judgment are core memory semantics rather than optional metadata.
Check — Where should a negative result live in the three-layer stack, and how should it affect an existing claim and procedure?
Source routes — This is the deck’s proposed synthesis; route backward to raw/wiki/work, harness externalization, entrenchment controls, and WikiSkill.
Transition — End by turning the definition into an empirical and governance research agenda.
-->

---

<div class="eyebrow">SAI research agenda</div>

## What would make WikiMemory scientifically trustworthy?

<div class="grid six compact-six question-grid">
  <div class="card"><h3>Representation</h3><p>Which page types and relations earn their complexity?</p></div>
  <div class="card teal"><h3>Compilation</h3><p>What is safe to synthesize—and what must remain raw?</p></div>
  <div class="card amber-border"><h3>Retrieval</h3><p>When should an agent traverse the wiki or reopen evidence?</p></div>
  <div class="card"><h3>Maintenance</h3><p>How do we detect staleness, contradiction, and conceptual drift?</p></div>
  <div class="card rose"><h3>Governance</h3><p>Which writes are autonomous, reviewed, gated, or prohibited?</p></div>
  <div class="card"><h3>Evaluation</h3><p>Does the system improve work without hiding failure?</p></div>
</div>

<p class="lede closing-question">Can an inspectable wiki become the shared memory substrate through which scientists and agents learn together?</p>

<!--
AGENTIC LEARNING NOTES

Slide ID — sai-research-agenda
Learning objective — Translate WikiMemory’s promise into testable research questions about representation, compilation, retrieval, maintenance, governance, and evaluation.
Core claim — Scientific trustworthiness is an empirical and governance program, not a product feature conferred by using Markdown, graphs, or agents.
Explain — Close with a research program rather than a product pitch. A concrete next experiment is to build a scientific WikiMemory profile, compare it with a RAG-only baseline, and evaluate provenance, answer quality, context cost, recovery from error, and visibility of failure.
Misconception — The deck has not established that WikiMemory is already scientifically trustworthy; it has motivated the architecture and the questions required to test it.
Check — Which research question should be tested first, and what observable metric would distinguish improvement from hidden failure?
Source routes — Use the preceding field map and risk slides to design the evaluation; the six cards define the agenda’s major dimensions.
Transition — Invite the audience to choose a first experiment through which scientists and agents can learn together.
-->
