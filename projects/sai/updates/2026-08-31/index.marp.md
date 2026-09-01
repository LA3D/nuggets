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
Open on a contemporary rediscovery, give away the architecture immediately, and
then ask why such a simple pattern works. The historical arc supplies the answer;
the final section asks what scientific use demands beyond a personal second brain.
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
Tell this as a rediscovery, not an invention story. Karpathy begins with a failure
mode: personalization memories are over-selected and distract the model. Elvis
Saravia replies that simple Obsidian files plus metadata work when memory is tuned
methodically. A week later Karpathy describes a working agentic pattern: immutable
raw sources, an LLM-maintained Markdown wiki, index-guided question answering,
outputs filed back into the corpus, and periodic linting. The April 4 gist turns
the observation into a portable “idea file” that another agent can instantiate.
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
Give away the system before the history. Raw is the independently recoverable
source of truth. The wiki is the compiled, persistent artifact owned by the agent.
The schema is a behavioral contract for the general-purpose coding agent. Queries
produce files, comparisons, diagrams, or slides that can be reviewed and filed
back, so work compounds instead of disappearing into chat history.
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
Now widen Karpathy’s practical observation into the scientific continuity problem.
“Memory” here is not anthropomorphic recall. It is the engineering problem of
preserving useful scientific state across model calls, sessions, agents, and
collaborators.
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
This is not a claim of direct descent. These traditions developed partly in
parallel. The useful historical claim is convergence: associative hypertext, wiki
maintenance, and file-native personal knowledge all supply pieces of WikiMemory.
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
The Memex is frequently flattened into “an early computer” or “a proto-Web.” The
stronger idea is the associative trail: a durable path through sources that can be
revisited and shared. Wiki links later give this idea a very cheap implementation.
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
Engelbart is the bridge to the harness framing. He was not merely proposing an
information store: he was designing the surrounding cognitive environment and the
procedures through which humans and tools worked together.
-->

---

<div class="eyebrow">1990 · the original Web</div>

## The Web began as a read–write medium

<div class="readwrite-flow">
  <div class="rw-person"><span>human</span><strong>read</strong><strong>write</strong></div>
  <div class="rw-arrow">↔</div>
  <div class="rw-browser"><small>WORLDWIDEWEB · 1990</small><b>browser + editor</b><span>follow links · create pages · create links</span></div>
  <div class="rw-arrow">↔</div>
  <div class="rw-space"><span>shared</span><strong>information space</strong></div>
</div>

<p class="callout-line">Wikis did not invent read–write hypertext; they recovered an ambition the mainstream Web largely left behind.</p>

<p class="microcopy"><a href="https://www.w3.org/People/Berners-Lee/WorldWideWeb.html">W3C, “WorldWideWeb: the first web client”</a> · <a href="https://www.w3.org/People/Berners-Lee/1997/Directions.html">Berners-Lee, “Realising the Full Potential of the Web”</a>.</p>

<!--
Be precise: Berners-Lee invented the Web, not the wiki. The first client was a
browser-editor. As passive browsers spread, intuitive editing became separated
from reading. Wikis later made shared editing simple in an ordinary browser.
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
The key shift is procedural. A wiki is not defined only by a markup syntax. It is
a corpus plus a maintenance culture. “Incremental” is especially important:
citing an unwritten page creates an affordance for future elaboration.
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
The double-bracket link is not original to Ward’s first wiki, which used WikiWords.
Its importance is representational: arbitrary concepts can be named without
distorting prose. MediaWiki then surrounded links with governance machinery.
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
YAML predates Markdown. Jekyll popularized their combination with Git for
publishing; it did not itself start personal knowledge graphs. The important
technical result is a portable, tool-friendly, inspectable knowledge artifact.
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
These meanings of “personal knowledge graph” overlap but are not identical. The
popular second-brain movement generally means graph-shaped notes and navigation;
the research literature usually assumes more explicit entities and relations.
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
Luhmann’s two card indexes contained roughly 90,000 cards. The popular slogan
“one idea per note” is a later simplification. The historically distinctive
mechanism is the combination of a permanent address, branching insertion,
cross-references, selective entry points, and repeated traversal during writing.
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
This is an analogy, not a claim that a digital graph reproduces Luhmann’s system.
Folders and visualization can help, but neither replaces contextual insertion.
The important operation is deciding where a thought participates and recording
why. A formal PKG can additionally type consequential relations such as supports,
contradicts, derived-from, supersedes, or uses-method.
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
The graph view is a projection, not the method. The same files can support many
memory profiles. Agentic rules, workflows, permissions, and lifecycle semantics
determine what kind of memory system the substrate becomes.
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
Personal wikis have existed for decades. Karpathy’s useful inversion is that the
human rarely performs the bookkeeping. The model becomes librarian and gardener;
the human remains source selector, question asker, reader, editor, and judge.
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
Avoid the false binary. A strong architecture retains raw evidence and may use
search or RAG beneath the wiki. The wiki stores maintained synthesis; retrieval
grounds claims and recovers detail. WiCER makes the compilation risk empirical.
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

<p class="microcopy">Design synthesis. Plain links + metadata + hierarchy are established affordances; richer typed-link semantics remain a research and design choice.</p>

<!--
Do not oversell the graph. A collection of links is not automatically a sound
knowledge graph. Typed edges can make operations clearer, but that claim should be
tested rather than asserted as intrinsic to Wikilinks.
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
OKF specifies that index.md may appear at any directory level. It groups links to
concepts or subdirectories and recommends carrying each target’s short description,
so a human or agent can see what is available before opening individual documents.
The specification calls this progressive disclosure. Treating the root index as a
small routing layer within the working-context budget is our harness interpretation:
survey, select, recursively expand, and stop when the task is sufficiently grounded.
-->

---

<div class="eyebrow">A WikiMemory page</div>

## One note can coordinate evidence, meaning, and action

<div class="note-anatomy">
  <pre><code><span class="code-comment">---</span>
<span class="code-key">type:</span> <span class="code-type">claim</span>
<span class="code-key">status:</span> <span class="code-type">contested</span>
<span class="code-key">sources:</span> [<span class="code-type">paper-17</span>, <span class="code-type">run-042</span>]
<span class="code-key">review_after:</span> <span class="code-type">2026-10-01</span>
<span class="code-comment">---</span>
&#35;&#35; Compiled knowledge reduces rediscovery
Supported by [[WiCER]]; limited by [[Compilation gap]].
Contradicts [[Full-context is always sufficient]].
&#35;&#35;&#35; Evidence
- [[run-042]] — matched evaluation
&#35;&#35;&#35; Open question
- Which details must remain in raw evidence?</code></pre>
  <div class="anatomy-labels">
    <div><b>Metadata</b><span>machine-selectable state</span></div>
    <div><b>Wikilinks</b><span>navigable relationships</span></div>
    <div><b>Sections</b><span>predictable reading contract</span></div>
    <div><b>Sources</b><span>path back to evidence</span></div>
  </div>
</div>

<p class="microcopy">Illustrative Obsidian-compatible note—not a proposed universal schema.</p>

<!--
Use this as the concrete “aha” slide. The note is simultaneously prose, a small
record, a graph node, and an instruction surface. Templates make recurring page
types predictable, while Markdown keeps exceptions expressible.
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
This imports the previous AI4C2 deck’s central frame. Files alone do not decide
when an agent writes, which evidence is required, or whether a change is accepted.
Those are harness responsibilities encoded through rules, skills, tools, and gates.
-->

---

<div class="eyebrow">Our implementation · llm-wiki-colab</div>

## We package the lifecycle—not just the files

<div class="substrate-grid">
  <div class="substrate-item"><span class="tag teal-tag">orient</span><b>Index + recent log</b><p>A session-start hook gives the agent a small, current map of project memory.</p></div>
  <div class="substrate-item"><span class="tag amber">operate</span><b>Explicit skills</b><p>Initialize, query, ingest evidence, file experiments, lint, and collaborate.</p></div>
  <div class="substrate-item"><span class="tag rose-tag">verify</span><b>Discipline gates</b><p>Re-read writes; check evidence, scope, structure, links, index, and log.</p></div>
  <div class="substrate-item"><span class="tag">coordinate</span><b>Git write protocol</b><p>Keep memory revisioned and handle concurrent wiki writers without silent loss.</p></div>
</div>

<p class="callout-line">The Markdown corpus is portable; the memory profile lives in the lifecycle around it.</p>

<p class="microcopy"><a href="https://github.com/LA3D-LLM-Agents/llm-wiki-colab">LA3D-LLM-Agents, <code>llm-wiki-colab</code></a> · <a href="https://doi.org/10.5281/zenodo.21213175">Saboia Moreira et al., “Beyond Memory”</a>.</p>

<!--
This is our implementation of the harness claim on the previous slide. The plugin
keeps the project repository ordinary and attaches its GitHub wiki at a gitignored
.llm-wiki/ path. A neutral core is packaged through agent-specific adapters. The
important contribution is not another Markdown schema; it is orientation, explicit
operations, pre-commit verification, auditable logs, and safe multi-writer updates.
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
This is more specific than “the agent maintains the wiki.” Source ingest and
experiment ingest have different epistemic obligations. Both integrate rather than
append: a typical write may touch the new page, existing claims, reciprocal links,
the index, and the log. wiki-lint is diagnostic first and asks which findings to
fix. Supporting skills bootstrap, diagnose, consult peers, and publish an Agent Card.
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
Each organization member is a research-project repository paired with a curated
wiki and a published Agent Card. The federation index supports discovery. “Ask” is
a synchronous clone-and-consult operation; “message” is an asynchronous direct
mailbox; “post” is a topical broadcast. Knowledge stays with the project that owns
and maintains it, while transparent file-based primitives connect the expertise.
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
The term is no longer only a viral pattern. A coherent research cluster appeared
between April and August 2026. No single source tells the full historical and
harness story; this slide shows how the contemporary contributions compose.
-->

---

<div class="eyebrow">Memory needs epistemology</div>

## An agent-maintained wiki can compound error, too

<div class="risk-loop">
  <div class="risk-node"><b>Weak source</b><span>enters the corpus</span></div><i>→</i>
  <div class="risk-node amber-risk"><b>Confident synthesis</b><span>loses qualification</span></div><i>→</i>
  <div class="risk-node rose-risk"><b>Central page</b><span>gains links and authority</span></div><i>→</i>
  <div class="risk-node"><b>Future answers</b><span>repeat the claim</span></div>
</div>

<div class="grid four risk-controls">
  <div class="card"><h3>Provenance</h3><p>Every important claim keeps a path to evidence.</p></div>
  <div class="card teal"><h3>Supersession</h3><p>Revision preserves what changed and why.</p></div>
  <div class="card amber-border"><h3>Evaluation</h3><p>Queries and probes reveal compilation failures.</p></div>
  <div class="card rose"><h3>Authority</h3><p>Sensitive writes require review, gates, or rollback.</p></div>
</div>

<p class="microcopy"><a href="https://arxiv.org/abs/2604.12034">“Memory as Metabolism”</a> highlights entrenchment and contradictory evidence · <a href="https://arxiv.org/abs/2608.00967">TrajWiki</a> uses immutable snapshots plus ADD / REVISE / DEPRECATE operations.</p>

<!--
This is the scientific objection slide. Links can turn repetition into apparent
authority. A scientific memory cannot silently overwrite uncertainty or negative
evidence. It needs epistemic status, source identity, temporal revision, and gates.
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
This is the payoff for the harness view. The wiki is not merely read during task
execution. It is an intermediate representation used by a maintainer and skill
proposer. The outer-loop harness records objective validation outcomes and rolls
back skill changes that do not improve performance.
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
This is our proposed definition. “Scientific” changes the requirements: provenance,
negative results, uncertainty, competing interpretations, reproducibility, and
human judgment are not optional metadata. They are core memory semantics.
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
Close with the research program, not a product pitch. The next iteration can end
on a narrower experiment: build a scientific WikiMemory profile, compare it with a
RAG-only baseline, and evaluate provenance, quality, context cost, and recovery.
-->
