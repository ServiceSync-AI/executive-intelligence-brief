# Notion Main Page — Executive Intelligence System (GC06) — HQ

Owner: Fray

Great — below is a **ready-to-paste Notion main page** (and a bundle of subpage contents) you can drop into Notion as the project home for *everything we’ve built in this chat*.

I made it explicit and copy-paste friendly: create the main page, then create each linked subpage using the titles below and paste the corresponding content into them. I’ve also included the most important code snippets, schemas, and the Dev README excerpt (including the Homebrew install block you edited).

---

**Page title:** `Executive Intelligence System — GC06 HQ`

**Page icon:** 🧭

**Cover (optional):** a calm abstract or simple photo of a conference room

---

## Page body (copy into Notion)

### Quick summary

This workspace is the single place to find the system that turns GC06 meeting artifacts into forwardable executive intelligence. It links to all operational docs, code, design specs, and runbooks. Use the links below to navigate. For operational changes or prompt edits, update the relevant subpage and record changes in `docs/changes.md`.

---

### How to use this page

1. Pick a topic from **Quick Links** below.
2. Open the linked page to see full docs, code, and actionables.
3. For a fresh run: see **Dev → Runbook (intern)**.
4. For audits: open **Data → Supabase** and `sources_map`.

---

### Quick Links (create as Notion links to the subpages below)

- **Project Overview** — short project description and architecture diagram
- **Runbook — Dev (Intern)** — `README.dev.md` step-by-step onboarding (primary day-to-day)
- **Supabase Docs & Schema** — SQL schema, tables, RLS guidance, and automation
- **Ingestion & Indexing** — ingestion pipeline, chunking, embedding, OCR, scripts
- **Knowledge Index** — canonical topic schema & examples (how to edit)
- **Commitments & Dealer Matrix** — how takeaways map to themes + matrix spec
- **Visual System (Figma)** — component library spec, tokens, Figma workflow
- **Wireframe & Storyboard** — full site storyboard and wireframe boxes
- **Microsite (App)** — Next.js / Framer build instructions + data contract
- **CI / GitHub Actions** — Actions workflows (ingest-on-upload, CI, deploy)
- **Prompts & Prompt Pipeline** — ingestion, inventory, fresh-eyes prompts, enforcement snippets
- **Notion Editorial Flow** — workflows when you want editors to update copy
- **Change Log & Audit Trail** — `sources_map`, `processed_files`, `decision_log` guidance
- **Useful Snippets** — Homebrew dev install, CLI examples, embed generation tips

---

### Short Project Roadmap

- Phase 0 — Supabase schema + single-file ingestion (done)
- Phase 1 — Knowledge Index + commitments pipeline (done)
- Phase 2 — Charts generation + Figma components (done)
- Phase 3 — Microsite MVP and public-forwardable PDF export (done)
- Ongoing — automation, Notion sync, incremental improvements

---

### Owners & Contacts

- **Project lead:** Frazier Horn — `fhorn@hornhausventures.com`
- **Engineering lead:** (YOUR ENG HERE)
- **Design lead:** (YOUR DESIGNER)
- For urgent infra help: Supabase support center

---

### Suggested Notion Properties for linked pages

For any subpage you create, add these top properties as a Notion database item (if you want to track everything centrally):

- `Status` (Draft / In Review / Approved)
- `Owner` (person)
- `Last updated` (date)
- `Related files` (link to GitHub / Supabase)
- `Tags` (e.g., ingestion, design, site, prompt)

---

## Next step

Create the subpages listed in **Quick Links** and paste the content from the subpage sections below.

---

# Subpage contents (create each as a separate Notion page and paste the corresponding content)

> **How to create:** In Notion, create a new page and paste the matching markdown/content below. Then come back to this HQ page and create an internal link to that subpage (type `@` or use “Link to page”).
> 

---

## 1) Project Overview

**Title:** `Project Overview — Executive Intelligence System`

**Content (paste):**

**Goal**

Turn meeting artifacts (agendas, notes, SOPs, handwritten takeaways, transcripts) into an auditable, forwardable single-page Executive Intelligence Brief that highlights where execution breaks down and what dealers committed to.

**Core principle**

Make insight feel inevitable, not impressive — operator language, non-salesy, privacy-safe.

**Architecture (one-paragraph)**

Supabase is the canonical runtime/data platform (storage, Postgres, pgvector, assets). GitHub houses all code (ingestion, analysis, site). Python handles ingestion, LLM orchestration, and chart generation. Figma is used for visual system; Framer/Next.js hosts the microsite. Notion serves as the optional editorial surface.

**High-level diagram (copy into your page or link a PNG)**

- Raw files → Supabase Storage
- Ingest worker (Python) → chunks & embeddings (Supabase)
- LLM workflows → knowledge_index & commitments (Supabase)
- Charts (Python) → assets (Supabase)
- Microsite (app) → reads sanitized views & assets

**Success criteria**

- Repeatable ingestion of meeting artifacts
- Canonical knowledge index and traceability (`sources_map`)
- Dealer commitments mapped to the 6 themes and displayed cleanly
- Forwardable, non-personalized microsite that Greg and others can share

---

## 2) Runbook — Dev (Intern)

**Title:** `Runbook — Dev (Intern)`

**Content (paste):**

This is the intern step-by-step. Use the `README.dev.md` in repo root for all commands. Key steps (abbreviated):

1. Setup local environment
2. Upload 1 sample file to Supabase or drop in `/sample-data`
3. `python ingest/ingest.py --file ./sample-data/yourfile.pdf`
4. Confirm `raw_files`, `chunks`, `chunk_vectors` in Supabase Studio
5. `python analysis/index_builder.py --sample 200`
6. `python analysis/normalize_commitments.py --images ./sample-data/takeaways.jpg --review`
7. `python analysis/charts_generator.py --upload`
8. `cd app && npm run dev` to run microsite locally

**Important flags**

- `-dry-run` — simulate without writing data
- `-force` — reprocess a file

**Dev tips**

- Use `-review` for uncertain OCR outputs
- Inspect `sources_map` after each run for traceability
- Keep "low-confidence" commits flagged for a human review

*(You can paste the full `README.dev.md` content here for the intern)*

---

## 3) Supabase Docs & Schema

**Title:** `Supabase — Schema & Docs`

**Content (paste):**

**Purpose:** Canonical data store and runtime.

**Buckets**

- `raw-docs` (private)
- `assets` (charts, svgs, screenshots)

**Key tables**

Paste the SQL schema from the conversation (create page with code blocks):

- `raw_files`
- `chunks`
- `chunk_vectors`
- `knowledge_topics`
- `commitments`
- `metrics`
- `decision_log`
- `sources_map`
- `processed_files`
    
    (Insert the SQL create statements from the earlier message — see README or migration files.)
    

**RLS / Security**

- Keep `raw_files` and `sources_map` protected.
- Expose sanitized views for public microsite: `public_knowledge_topics`, `public_commitments` (these remove emails, phone numbers, or named individuals).

**Vector / embeddings**

- Use pgvector in Supabase (vector type) or external vector DB if not available.
- Embedding model dims should match `vector` column (1536 default).

**Automation**

- Edge functions for ingestion triggers
- Scheduled job for topic refresh & chart regen

**Audit tables**

- `processed_files` and `sources_map` must be filled for every ingestion and transform.

---

## 4) Ingestion & Indexing

**Title:** `Ingestion & Indexing Pipeline`

**Content (paste):**

**Overview**

- `ingest.py` — upload/parsing, OCR, chunking, embedding storage
- `index_builder.py` — LLM-driven canonical topic extraction & traceability
- `normalize_commitments.py` — OCR + LLM normalization for handwritten takeaways

**Chunking rules**

- 500–900 tokens per chunk
- Overlap 100–200 tokens

**Embedding flow**

- Batch embeddings to the provider, store vectors in `chunk_vectors`
- Store snippet & file metadata in `chunk_vectors.metadata` for traceability

**OCR**

- Use Tesseract for printed text, try AWS Textract or Google Vision for handwriting if accuracy needed

**Prompts**

- Keep LLM prompts versioned (folder `/analysis/prompts/`)
- Always return JSON that includes `evidence`: filenames + chunk_ids

**Error handling**

- If OCR/LLM reports low-confidence, mark the row in `processed_files` for human review

---

## 5) Knowledge Index (Topics)

**Title:** `Knowledge Index — Topics`

**Content (paste):**

**Data model**

- `topic` (text)
- `definition` (one-line operator language)
- `status` (observed / agreed / committed / unresolved)
- `evidence` (json: list of {file, chunk_ids})
- `confidence` (number 0–1)

**Process**

- LLM consumes high-signal chunks and returns up to 10 canonical topics
- Insert with evidence into `knowledge_topics`
- Human review step for finalization

**Editing**

- For quick edits, update `knowledge_topics` via a simple admin UI or Notion editorial page (sync back to Supabase)

---

## 6) Commitments & Dealer Matrix

**Title:** `Commitments — Dealer Takeaways`

**Content (paste):**

**Canonical themes (rows)**

1. Hours per RO & Throughput
2. Video MPI & Inspections
3. Dispatch & Flow Control
4. Onboarding & Training
5. Sales → Service Handoff
6. AI & Automation

**Process**

- OCR the `Take A Way's.pdf` pages
- LLM map phrases → themes; return {dealer_code, phrase, theme, confidence}
- Human review (`-review`) to confirm ambiguous mappings
- Store rows in `commitments` table with `evidence`

**Matrix**

- The Notion page should display a matrix (rows=themes, columns=dealer codes). Embed exported SVG or use a Notion table view.

---

## 7) Visual System (Figma)

**Title:** `Visual System — Figma`

**Content (paste):**

**Component Library**

- Color tokens (Surface / Background / Ink Primary / Secondary / Muted)
- Text styles (H1, H2, Body, Caption)
- Components: `Section Header`, `Matrix / Cell` (variants), `Dealer Column`, `Bar / Density`, `Execution Loop Diagram` etc.

**Figma pages**

- `Foundations` (colors, typography)
- `Components` (all components)
- `Examples` (assembled pages)

**How to use**

- Designers: build component and publish library
- Developers: export tokens (`design/tokens.json`) and SVG samples

(Include the Figma-ready specs content as a subpage here.)

---

## 8) Wireframe & Storyboard

**Title:** `Wireframe & Storyboard — Microsite`

**Content (paste):**

Paste the full storyboard/wireframe content we created: Hero, Room, What the Room Agreed On, Playbooks, Variance, Commitments, Execution Gap, What This Group Is Ready For, Closing. Include the scroll experience summary and the “do not use” design notes.

---

## 9) Microsite (App)

**Title:** `Microsite — App (Next.js / Framer)`

**Content (paste):**

**Tech stack**

- Next.js + TypeScript + Tailwind
- `@supabase/supabase-js` for data
- Plotly or Vega-Lite for charts

**Data contract**

- Front-end reads `public_knowledge_topics`, `public_commitments`, `assets` table
- Charts hosted in `assets` bucket; front-end reads SVGs or uses Plotly JSON

**Export PDF**

- Endpoint `/export` that server-renders the page and returns a PDF snapshot

**Deploy**

- Vercel recommended, or Supabase Hosting

---

## 10) CI / GitHub Actions

**Title:** `CI — GitHub Actions & Workflows`

**Content (paste):**

List workflows and short descriptions:

- `ci.yml` — lint + test + sample ingestion smoke test
- `ingest-on-upload.yml` — triggered by Supabase webhook, invokes ingestion job
- `deploy.yml` — build & deploy site to Vercel

Add note: Secrets in GitHub: `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `OPENAI_API_KEY`, `VERCEL_TOKEN`.

---

## 11) Prompts & Prompt Pipeline

**Title:** `Prompts — Pipeline & Enforcement`

**Content (paste):**

Include the major prompts:

- Ingestion Gatekeeper (inventory output requirement)
- Knowledge Tracking Requirement (persist to Knowledge Index)
- Fresh Eyes Prompt (ideation)
- Full kiro-cli build prompt (the big one)
- Evidence requirement snippets

Add the Prompt Loading Order (Inventory → Knowledge Index → Commitments → Fresh Eyes → Prioritization → Build → Persist).

---

## 12) Notion Editorial Flow (optional)

**Title:** `Editorial — Notion Flow`

**Content (paste):**

- Editors write meeting copy in Notion meeting pages
- After approval, run sync script to push approved copy to `knowledge_topics` or `public_*` views
- Keep manual approval step for anything LLM-normalized

---

## 13) Change Log & Audit Trail

**Title:** `Change Log & Audit Trail`

**Content (paste):**

- Use `sources_map` for traceability
- Use `processed_files` for ingestion audit
- Use `decision_log` to store decisions & owners
- For prompt changes, update `docs/changes.md` with before/after prompt and sample outputs

---

## 14) Useful Snippets

**Title:** `Useful Snippets & Install`

**Content (paste):**

**Homebrew dev install (edited)**

```bash
# Homebrew
brew install python node tesseract
brew tap supabase/cli
brew install supabase/tap/supabase
```

**Fast commands**

```bash
# Setup
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cd app && npm install && cd ..

# Ingest
python ingest/ingest.py --file ./sample-data/gc06-agenda.pdf

# Build index
python analysis/index_builder.py --sample 200

# Normalize commitments
python analysis/normalize_commitments.py --images ./sample-data/takeaways-page1.jpg --review

# Charts
python analysis/charts_generator.py --upload

# Run site
cd app && npm run dev
```

---

# Final notes for setting up Notion links and pages

1. Create the main page **Executive Intelligence System — GC06 HQ** and paste the Main Page content above.
2. For each subpage title in **Quick Links**, create a new Notion page and paste the matching content from the subpage blocks above.
3. Back on HQ page, highlight each subpage title text and create a link to the newly created Notion pages (type `@` then choose the page).
4. Add `Status`, `Owner`, and `Last updated` properties to each subpage if you want them managed as a Notion database row.
5. Use Notion’s database view if you prefer tracking dozens of meeting briefs over time.

---

Action Items

- Export all of these subpage contents as a single `.md` bundle for fast paste into Notion (one file per page).
- Or, if you give me the Notion workspace/page URL and invite me, I can auto-create the pages for you (note: I don’t have automatic access — you’d need to connect a Notion integration).

Would you like the `.md` bundle next so you can paste quickly?