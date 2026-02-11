# Github README.md

Owner: Fray

---

# Executive Intelligence System — Repo README

A reproducible pipeline that turns meeting artifacts (agendas, notes, SOPs, handwritten takeaways, transcripts) into a forwardable, operator-grade Executive Intelligence Brief microsite.

This repo contains ingestion, analysis, knowledge indexing, visualization, and the microsite code. The canonical runtime/data platform is **Supabase**; GitHub is the canonical code + CI platform.

---

## Table of Contents

- [Project overview](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Repo layout](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Architecture & data flow](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Prerequisites](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Quick start (developer)](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Supabase setup](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Local development tasks](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
    - [Run ingestion on a file](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
    - [Build knowledge index (topics)](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
    - [Extract dealer commitments](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
    - [Regenerate charts / visuals](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
    - [Run the microsite locally](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [CI / GitHub Actions](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Database schema overview](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [LLM / Embeddings configuration](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Design & Figma workflow](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Notion / Editorial workflow (optional)](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Security & governance](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Troubleshooting](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Contributing & code style](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)
- [Contacts & onboarding checklist](Github%20README%20md%203040fd35ad00802a860cf5e1605a7dbb.md)

---

## Project overview

This project turns raw documents from NADA 20 Group GC06 (and other meetings) into:

1. `chunks` + `chunk_vectors` (embeddings) stored in Supabase
2. A `knowledge_index` of canonical topics with traceability to source files
3. A `commitments` table mapping dealer codes → execution themes
4. Aggregated `metrics` and charts exported as SVG/JSON assets
5. A single-page microsite (Next.js/Framer) that renders the Executive Intelligence Brief

The goal is repeatable, auditable intelligence that can be updated when new meeting artifacts are added.

---

## Repo layout

```
/project-root
  /ingest                # ingestion scripts (ingest.py, helpers)
  /analysis              # ETL + index builder scripts
  /notebooks             # Jupyter notebooks for EDA
  /supabase
    /migrations          # SQL migrations for schema
  /app                   # Next.js microsite
  /design                # Figma exports, tokens, SVG examples
  /assets                # generated assets (optional)
  /docs                  # architecture docs, runbooks
  .github/
    workflows/
      ci.yml
      ingest-on-upload.yml
      deploy.yml
  README.md
  requirements.txt
```

---

## Architecture & data flow

1. Upload raw files to Supabase Storage (`raw-docs/`) or to the `ingest/upload/` directory.
2. `ingest.py` parses files, OCRs images (handwritten takeaways), chunks text, and inserts `raw_files`, `chunks`.
3. `ingest.py` requests embeddings for chunks and upserts into `chunk_vectors`.
4. `index_builder.py` (LLM-driven) consumes representative chunks and builds `knowledge_topics` with evidence pointers.
5. `normalize_commitments.py` maps OCR’d takeaways to canonical themes and stores `commitments`.
6. `charts_generator.py` creates visual assets (SVG/Plotly), uploads them to Supabase `assets/`.
7. Microsite reads sanitized tables/views and renders the Executive Intelligence Brief.
8. Periodic automation (Edge functions / GitHub Actions) triggers ingestion and index updates on new uploads or on schedule.

---

## Prerequisites

- Git & GitHub account
- Node.js 18+ (for the microsite)
- Python 3.10+ (for ingestion & analysis)
- Supabase account & project (service role key)
- An embeddings provider (OpenAI or other): API key
- Optional: Docker (for local Supabase dev)
- Optional: Figma account for design work

---

## Quick start (developer)

1. Clone the repo:
    
    ```bash
    git clone git@github.com:your-org/executive-intel.git
    cd executive-intel
    ```
    
2. Create a Python virtual environment and install:
    
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    
3. Install Node deps for the site:
    
    ```bash
    cd app
    npm install
    cd ..
    ```
    
4. Create a `.env.local` (see the example `.env.example`) and fill in:
    
    ```
    SUPABASE_URL=https://your-supabase-url.supabase.co
    SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
    SUPABASE_ANON_KEY=your_anon_key
    OPENAI_API_KEY=sk-...
    NEXT_PUBLIC_SUPABASE_URL=...
    NEXT_PUBLIC_SUPABASE_ANON_KEY=...
    ```
    
5. Apply DB migrations (see Supabase Setup below).

---

## Supabase setup

> **Note:** You must have a Supabase project and the service role key to run ingestion.
> 

### 1. Create project & enable extensions

- Create a Supabase project from app.supabase.io.
- If pgvector is supported in your plan, enable it.

### 2. Create storage buckets

- `raw-docs` (private) — upload raw meeting files here
- `assets` (private/public) — charts and images

### 3. Apply migrations

Using the Supabase CLI (recommended):

```bash
# from repo root
supabase login
supabase link --project-ref your-project-ref
supabase db push   # or run the SQL migrations in /supabase/migrations
```

(Or run the SQL files in `/supabase/migrations` via the SQL editor if you prefer.)

### 4. Create RLS policies

- Keep `raw_files` private.
- Expose sanitized views for the microsite (e.g., `public_knowledge_topics`) that strip PII.

---

## Local development tasks

### Run ingestion on a file

Upload a file to Supabase Storage manually or run a local ingestion:

```bash
# upload a file (or use the UI)
python ingest/ingest.py --file ./sample-data/gc06-agenda.pdf
```

What `ingest.py` does:

- Adds a row to `raw_files`
- Extracts text (PDF/DOCX/Images -> OCR)
- Chunks text (with overlap)
- Stores `chunks` table
- Requests embeddings and stores `chunk_vectors`

**Tip:** Use `--dry-run` for debug mode.

---

### Build knowledge index (topics)

Run the index builder which uses LLM prompts to produce canonical topics:

```bash
python analysis/index_builder.py --sample 200
```

Outputs:

- `knowledge_topics` table populated with {topic, definition, evidence}
- `sources_map` entries for traceability

---

### Extract dealer commitments

Process the handwritten takeaways and map to canonical themes:

```bash
python analysis/normalize_commitments.py --images ./sample-data/handwritten_takeaways.jpg
```

Review the `commitments` table and fix any low-confidence mappings in the admin UI or via the `--review` flag.

---

### Regenerate charts / visuals

Charts are generated from DB queries and saved as SVGs to `assets`:

```bash
python analysis/charts_generator.py --out-dir ./assets
# or upload directly to supabase
python analysis/charts_generator.py --upload
```

Common charts:

- Topic gravity map (bubble chart)
- Theme density bar
- Variance small multiples
- Execution loop SVG

---

### Run the microsite locally (Next.js)

```bash
cd app
npm run dev
# Open http://localhost:3000
```

The site reads sanitized endpoints from Supabase. For server-side rendering, ensure `NEXT_PUBLIC_SUPABASE_ANON_KEY` is set.

---

## CI / GitHub Actions

The repo includes the following workflows:

- `ci.yml` — Lint, unit tests, and a sample ingestion smoke test on PRs
- `ingest-on-upload.yml` — Triggered by Supabase webhook when a file is uploaded; runs ingestion job (or calls an Edge Function)
- `deploy.yml` — Builds and deploys the microsite (Vercel) on merges to `main`

Secrets (store in GitHub Settings → Secrets):

- `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `SUPABASE_ANON_KEY`
- `OPENAI_API_KEY`
- `VERCEL_TOKEN` (if deploying to Vercel via Actions)

---

## Database schema overview

Key tables (see `/supabase/migrations` for SQL):

- `raw_files` — metadata for uploaded files
- `chunks` — text chunks extracted from files
- `chunk_vectors` — embeddings for chunks (pgvector)
- `knowledge_topics` — canonical topics + evidence pointers
- `commitments` — dealer code -> theme mappings
- `metrics` — aggregated numeric ranges / medians
- `sources_map` — traceability (insight -> source files/chunk ids)
- `assets` — chart URLs / SVGs stored in Supabase Storage

---

## LLM / Embeddings configuration

- We use an embedding provider (OpenAI by default). Configure `OPENAI_API_KEY`.
- Embedding dimensionality must match the DB `vector(...)` size. Default: 1536 is common for many models.
- Prompt templates are in `/analysis/prompts/` and are versioned. Changing prompts should be done via PR and reviewed.

**Important**: Keep prompt changes small and documented; include tests demonstrating behavior before merging.

---

## Design & Figma workflow

- Figma file: `GC06 – Executive Intelligence System` (component library).
- Designers produce components & export tokens (colors, type scales) into `/design/tokens.json`.
- Export example SVGs / placeholders into `/design/exports/` used during front-end implementation.
- Front-end should mirror Figma tokens via Tailwind config or CSS variables.

---

## Notion / Editorial workflow (optional)

- Use Notion as a human editorial surface (meeting notes and copy editing).
- A simple sync script (`scripts/notion_sync.py`) can pull approved copy and write sanitized entries to Supabase.
- If using Notion-first approach, enforce a manual approval step before pushing to Supabase.

---

## Security & governance

- Protect raw uploads via Row Level Security (RLS). Use sanitized views for the public microsite.
- Never commit API keys. Use GitHub Secrets.
- Keep PII in `raw_files` private; public site must never expose emails/phone numbers.
- Keep `sources_map` for auditability but protect it behind RLS.

---

## Troubleshooting

**Common issues**

- *Embeddings failing*: Check `OPENAI_API_KEY` and quotas. For large batches, throttle requests.
- *OCR poor quality*: Switch OCR engine (Tesseract → AWS Textract) or pre-process images.
- *Vector sizes mismatch*: Ensure embedding model and `vector` column dimension match.
- *Supabase RLS blocking reads*: Debug with service role locally; define explicit policies for read-only public views.

**Useful commands**

- View Supabase tables: `supabase db remote connect` or via Supabase Studio
- Re-run a failed ingestion: `python ingest/ingest.py --file path --force`

---

## Contributing & code style

- All work via forks/branches → PRs → code review.
- Tests required for ingestion normalization logic and prompt regressions.
- Python: follow `black` + `flake8`. Node: follow `eslint`.
- Update `/docs/changes.md` with prompt template changes and key decisions.

---

## Contacts & onboarding checklist (intern friendly)

**Primary contacts**

- Project lead: Frazier Horn — `fhorn@...` (for product and ops decisions)
- Engineering lead: (name) — PR review and infra
- Design: (name) — Figma components

**Intern onboarding checklist**

1. Fork & clone the repo.
2. Create a Python venv and install `requirements.txt`.
3. Create `.env.local` from `.env.example` and fill keys (ask lead for dev Supabase service key).
4. Run `supabase start` (dev) or link to dev Supabase project.
5. Run a single-file ingestion:
    
    ```bash
    python ingest/ingest.py --file sample-data/gc06-agenda.pdf
    ```
    
6. Inspect `chunks` in Supabase.
7. Run `python analysis/index_builder.py --sample 50` and review `knowledge_topics`.
8. Generate one chart `python analysis/charts_generator.py --out-dir ./assets`.
9. Run the microsite locally `cd app && npm run dev`.
10. Make a small change, open PR, and get it reviewed.

---

Action Items:

- A `README.dev.md` for an intern with the exact commands and environment variables pre-filled.
- A sample `ci.yml` and `ingest-on-upload.yml` for GitHub Actions.
- A minimal Dockerfile and Docker Compose setup that runs a dev Supabase locally plus the ingestion worker for offline development.

Which of those would help you most next?