# AI Project Prompt

Owner: Fray

# 1. Base Prompt

<aside>
💡

You are kiro-cli acting as a full-stack product builder + analyst. Build a complete, deployable “Executive Intelligence Brief” microsite for a NADA 20 Group (GC06) meeting using the files in a nested folder structure.

GOAL
Create a single-page, scroll-based microsite (no login) that feels like an internal operator intelligence brief (not a SaaS landing page). It must be forwardable, non-salesy, and confidentiality-safe. It should make the reader feel: “This person understands what happens between meetings.”

INPUT FILES
All source documents live in: <PATH_TO_ROOT_FOLDER>
There are subfolders within subfolders. Recursively scan and ingest:

- PDFs (agendas, handouts, SOPs, dealer packets)
- DOCX (notes, meeting minutes, transcript summaries)
- Images / PNGs (rosters screenshots, handwritten takeaways, etc.)

IMPORTANT CONSTRAINTS (CONFIDENTIALITY + TONE)

- Do NOT publish emails, phone numbers, or personal contact info anywhere on the site.
- Do NOT name or rank individual dealerships by performance.
- It’s OK to show dealer numbers (codes) only, and anonymous dots.
- Never attribute a quote or takeaway to a named person; use anonymized language.
- The site must not look like a pitch deck, marketing site, or dashboard product demo.
- No hype words (“revolutionary”, “game-changing”). Use calm, operator language.
- Prefer “insight feels inevitable” design: minimalist, whitespace, muted palette.

OUTPUTS

1. A complete web project with:
    - A single-page site (index route) matching the storyboard below
    - Responsive layout (desktop first, mobile support)
    - Charts/visuals rendered as SVG/Canvas and accessible (aria labels, captions)
    - Build + run instructions in [README.md](http://readme.md/)
2. A JSON “data layer” generated from the documents:
    - topics.json (topic clusters + counts + supporting evidence pointers)
    - commitments.json (dealer code -> themes commitments)
    - metrics.json (any extracted metric ranges that are safe to show, aggregated/anonymized)
    - sources_map.json (which file(s) contributed to which section; no sensitive info)
3. A “content layer”:
    - copy.json with final page copy per section (use exact copy below as baseline; only lightly adjust if needed based on evidence)
4. A static export option (generate /export to produce a shareable PDF snapshot of the page)

TECH STACK (choose one and implement fully)
Preferred: Next.js (App Router) + TypeScript + TailwindCSS + Chart rendering via:

- Vega-Lite (recommended) OR D3 (simple)
Use local file ingestion scripts in Node/TS (or Python if easier) but the final site must be TS/Next.

SITE STORYBOARD (SECTIONS)
A) HERO

- Title: “Two Days. 40+ Operators. One Pattern.”
- Subhead: “An executive synthesis of what surfaced in the room — and where fixed operations quietly break down.”
- Metadata: “January 2026 · NADA 20 Group GC06 · Atlanta”
- No images. Minimal.

B) THE ROOM (LEGITIMACY WITHOUT NAMES)

- Visual: “Dealer Footprint Matrix” (anonymous dots). Use roster sources to infer # of dealer orgs; do NOT display contact data.
- Copy: “19 dealer organizations · single-point and multi-rooftop · mixed markets” (if evidence supports).
- Caption: “Insights drawn from a structurally diverse operator group.”

C) WHAT THE ROOM AGREED ON

- Visual: Topic Gravity Map (bubble/dot sized by frequency).
- Derive topics from transcript summaries + notes + meeting minutes + hot topics docs.
- Show 6–10 topics max, operator language labels.
- Copy: include bullet list and final line “The group is aligned on what matters.”

D) WHAT THE PLAYBOOKS ALREADY COVER

- Visual: Playbook Cards grid/scroll (SOPs, onboarding, checklists, scripts, etc.)
- Each card has a title + 3–4 bullet fragments. Clicking expands to show a short excerpt (safe, no proprietary or personal info).
- Copy emphasizes: “Knowledge is not the constraint.”

E) WHERE PERFORMANCE STILL VARIES

- Visual: “Variance Panels” small multiples (dot plots).
- Only show SAFE, anonymized distributions. Prefer ranges and medians; no labels tied to stores.
- Use any available proficiency numbers, parts turns, recon days to breakeven, etc. If data is too specific, aggregate further or omit.
- Copy: “Same knowledge. Different outcomes.”

F) WHAT EACH DEALERSHIP COMMITTED TO (TAKEAWAYS MATRIX)

- Visual: Dealer Commitment Matrix (rows=themes, columns=dealer codes). Use the handwritten “Take A Way’s” pages.
- Themes (rows) exactly:
    1. Hours per RO & Throughput
    2. Video MPI & Inspections
    3. Dispatch & Flow Control
    4. Onboarding & Training
    5. Sales → Service Handoff
    6. AI & Automation
- Columns: dealer codes found in roster + takeaways pages. If a dealer code has no takeaways, omit its column.
- Cell states: empty / filled / strong (multiple commitments).
- Secondary visual: Theme Density Bars (# dealers selecting each theme).
- Copy: “Post-meeting execution priorities captured directly from the room. Numbers indicate dealership codes.”

G) WHERE EXECUTION QUIETLY BREAKS (CORE)

- Visual: Execution Loop Diagram:
Decision → Owner → Action → Measurement → Follow-up (loop)
- Highlight breakpoints:
    - After meetings
    - Between departments
    - Between shifts
    - Between systems
- Copy includes: “Most failures occur between steps, not within them. The system doesn’t remember. People are forced to.”

H) WHAT THIS GROUP IS ACTUALLY READY FOR

- Visual: Before/After compression timeline:
Before: Decision — Drift — Next Meeting
After: Decision → Reinforcement → Adjustment
- Copy: “The next advantage won’t come from more meetings or more tools. It will come from shortening the distance between intent and execution.”

I) CLOSING

- “Prepared by Frazier Horn”
- “Turning operational conversations into decision-ready intelligence.”
- No CTA button. Optional: tiny footer note “Shared in the spirit of clarity, not critique.”

EXACT BASELINE COPY (USE THIS; ONLY TWEAK IF EVIDENCE REQUIRES)
HERO:
Two Days. 40+ Operators. One Pattern.
An executive synthesis of what surfaced in the room — and where fixed operations quietly break down.
January 2026 · NADA 20 Group GC06 · Atlanta
Prepared independently from meeting materials, shared SOPs, and discussion transcripts.

SECTION: What the Room Agreed On
Across two full days of discussion — hot topics, composites, dealer case studies, and open dialogue — alignment was not the issue.
The same themes surfaced repeatedly, regardless of store size, market, or performance tier:

- Phones and customer communication are breaking first
- Scheduling is constrained more by capacity than demand
- Video MPIs work — when they are executed consistently
- Technician productivity is limited more by flow than skill
- Advisors struggle less with knowledge than with reinforcement
- Parts readiness directly controls technician output
- Reconditioning speed dictates used car profitability
- Retention is the real profit engine — not acquisition
These topics did not appear once. They reappeared across sessions, speakers, and roles.
The group is aligned on what matters.

SECTION: What the Playbooks Already Cover
The room did not lack answers.
Shared during the meeting were: service advisor onboarding frameworks, best-practice checklists, sales-to-service handoff scripts, technician training/retention programs, parts SOPs, menu structures, dispatch models, recon workflows, and digital profile guidance.
Individually, these documents are strong. Collectively, they demonstrate something important:
The industry already knows how to run a high-performing service operation.
Processes are documented. Best practices are proven. Tools exist.
Knowledge is not the constraint.

SECTION: Where Performance Still Varies
Despite shared knowledge and intent, outcomes vary widely.
Across the group, metrics revealed large spreads.
These gaps are not explained by market size, labor rates, access to tools, or awareness.
The same ideas are present — but results differ.
That variance is the signal.

SECTION: Where Execution Quietly Breaks
Decision → Owner → Action → Measurement → Follow-Up
Breakdowns commonly occur after meetings, between departments, between shifts, and between systems.
High-performing stores compensate with whiteboards, daily huddles, scoreboards, paper dispatch books, radios, and constant leadership presence.
These methods work — but only with sustained energy.
The system does not remember. People are forced to.
That is where value leaks.

SECTION: What This Group Is Actually Ready For
This group does not need more meetings, more ideas, or another checklist.
It is ready for shortening the distance between decision, execution, and reinforcement.
That means making ownership visible, follow-up automatic, drift obvious, and accountability lighter.
The opportunity is not new data. It is continuity.

CLOSING:
Fixed operations performance does not break because teams don’t care.
It breaks because conversations fade, context evaporates, reinforcement weakens, and execution becomes optional by default.
The strongest operators in the room are already fighting this — manually.
The next advantage will come from making that effort permanent, not heroic.

DATA EXTRACTION / INGESTION TASKS

- Recursively enumerate all files under <PATH_TO_ROOT_FOLDER>.
- For each file, extract text:
    - PDFs: parse text; if scanned, use OCR only when needed.
    - DOCX: extract headings and paragraphs.
    - Images: OCR only for handwritten takeaways and roster screenshots.
- Build topic clusters from transcript summaries + minutes:
    - output: topics.json with {topic, count, evidence_snippets[], source_files[]}
- Build commitments.json from handwritten takeaways:
    - Map each dealer code to 0–n commitments in the 6 themes.
    - Where a line is ambiguous (e.g., “Dive into EXP’s”), place into “Hours per RO & Throughput” unless evidence suggests otherwise; store original phrase.
- Build metrics.json:
    - Extract only safe numeric ranges and medians (no dealer identifying labels).
    - If a metric is tied to a specific named store, aggregate it or omit it.
- Create sources_map.json linking each section to the files used (filenames only).

DESIGN REQUIREMENTS

- Minimalist, operator-credible.
- No gradients; subtle borders; lots of whitespace.
- One accent color max.
- Charts should look like internal analysis, not marketing.

DELIVERABLE QUALITY BAR

- The site must build and run with one command.
- Provide README with:
    - install
    - ingest step
    - dev
    - build
    - export PDF
- Include sample screenshots in /docs/screenshots generated via Playwright.

PROJECT STRUCTURE (CREATE THIS)
/
ingest/
ingest.ts
parsers/
outputs/
topics.json
commitments.json
metrics.json
sources_map.json
app/ (Next.js)
page.tsx
components/
sections/
public/
docs/
screenshots/
[README.md](http://readme.md/)

NOW DO IT

1. Scan files recursively.
2. Generate JSON outputs.
3. Generate the full site with the above storyboard, visuals, and copy.
4. Ensure confidentiality constraints.
5. Provide a final summary of what data was used where (from sources_map.json).
</aside>

# 2. Fresh Eyes Prompt

<aside>
💡

You are an independent strategist, systems thinker, and product designer.

I am giving you a folder (with nested subfolders) containing:

- Meeting agendas
- Follow-up emails
- Handwritten notes
- SOPs and best practices from multiple dealerships
- Dealer-level “homework” and operating processes
- Performance snapshots and metrics
- Rosters
- AI-generated transcript summaries
- Human-written notes and summaries

These materials all come from a multi-day NADA 20 Group meeting focused on Service & Parts (Fixed Operations).

Your task is NOT to follow any prior outline or instructions.
Your task is to approach this as if you were seeing it for the first time.

GOAL
After reviewing all files, propose:

- What you think is ACTUALLY happening in this group
- What the materials imply about how the industry works between meetings
- What kinds of artifacts, experiences, or outputs would be most valuable — even if they were never explicitly requested

Think like:

- A systems designer
- An operator psychologist
- A product founder trying to see whitespace
- Someone who understands how executive trust is built

WHAT TO DO

1. Recursively explore all files in the folder and subfolders.
2. Build a mental model of:
    - The people in the room
    - The incentives they operate under
    - The gaps between intent, process, and execution
3. Identify:
    - Repeated patterns
    - Contradictions
    - Things people keep circling but never naming
    - Where effort is being wasted
    - Where leverage clearly exists

WHAT TO PRODUCE
Do NOT jump straight to solutions.

Instead, output the following sections:

SECTION A — “What This Group Is Really Wrestling With”
Describe the core problems or tensions you believe exist, even if they are not stated directly.

SECTION B — “What’s Unusual or Telling About These Materials”
Call out anything that stands out as odd, revealing, or unintentionally insightful (e.g., why people rely on whiteboards, why SOPs are shared, why handwritten takeaways matter).

SECTION C — “Where Value Is Quietly Being Created (or Lost)”
Explain where real value seems to be created or destroyed — especially in the gaps between departments, time periods, or tools.

SECTION D — “Artifacts That Might Actually Matter”
Propose 5–10 possible artifacts, outputs, or experiences that could be created from this material.
These can include:

- Documents
- Visual systems
- Ongoing processes
- Internal tools
- Briefs
- Rituals
- New meeting formats
- Or things that don’t yet have a name

Do NOT constrain yourself to websites or dashboards.
If something sounds strange but useful, include it.

SECTION E — “What You’d Build First (and Why)”
Pick ONE idea from Section D and explain:

- Why it’s the highest leverage
- Who would care most
- How it would quietly change behavior

RULES

- Do not assume I want to sell software.
- Do not assume I want to automate everything.
- Do not use startup buzzwords.
- Do not optimize for novelty alone — optimize for credibility and usefulness.
- Be honest if something feels fragile, political, or trust-sensitive.

Tone: thoughtful, calm, incisive.
Audience: someone serious about operations and influence.

</aside>