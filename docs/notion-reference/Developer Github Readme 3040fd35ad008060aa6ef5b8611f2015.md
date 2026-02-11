# Developer Github Readme

Owner: Fray

This is an explicit step-by-step runbook (commands, env vars, tips, troubleshooting). It assumes the repo layout we agreed on and uses the script names we discussed (`ingest.py`, `index_builder.py`, `normalize_commitments.py`, `charts_generator.py`, etc.).

---

# Developer Readme — Intern Onboarding (DEV)

> **Goal:** Get you from zero → running the ingestion → index → charts → microsite flow.
> 
> 
> Follow the steps exactly. If you get stuck, capture the error and ping Frazier (`fhorn@hornhausventures.com`).
> 

---

## Quick summary (timeline)

1. Setup local environment, Supabase access, and keys (~30–60m)
2. Run one-file ingestion (parse, chunk, embed) (~20–40m)
3. Build knowledge index (topics) (~20–60m)
4. Normalize commitments from handwritten takeaways (~20–60m)
5. Generate charts and upload to Supabase assets (~30–60m)
6. Run the microsite locally and validate (~20–40m)

---

## Prereqs (ask for access before starting)

- GitHub repo access (this repo)
- Supabase project URL & **SERVICE_ROLE_KEY** (ask Frazier)
- Supabase anon key (for local microsite)
- OpenAI API key (or other embedding provider)
- Node 18+ and npm / pnpm / yarn
- Python 3.10+
- (Optional but recommended) Docker & Supabase CLI for a local dev DB
- Install Tesseract if you will OCR handwritten images

---

## Tools to install locally

**macOS**

```bash
# Homebrew
brew install python node tesseract
brew tap supabase/cli
brew install supabase/tap/supabase
```

**Ubuntu / Debian**

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip nodejs npm tesseract-ocr
# Install supabase CLI via npm
npm install -g supabase
```

**Windows**

- Use WSL (Ubuntu) — follow the Ubuntu commands above.

**VS Code**

- Recommended editor with Python & Node plugins.

---

## Repo bootstrap

Clone the repo and install dependencies:

```bash
git clone git@github.com:your-org/executive-intel.git
cd executive-intel
```

### Python

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows (PowerShell)
pip install --upgrade pip
pip install -r requirements.txt
```

### Node / Microsite

```bash
cd app
npm install
cd ..
```

---

## Environment variables

Create a `.env.local` in the project root (copy from `.env.example` if present). Fill in values with secrets provided by Frazier.

```
# Supabase
SUPABASE_URL=https://<your-project-ref>.supabase.co
SUPABASE_SERVICE_ROLE_KEY=service_role_key_here
SUPABASE_ANON_KEY=anon_key_here

# OpenAI (or embeddings provider)
OPENAI_API_KEY=sk-...

# Local microsite (Next.js)
NEXT_PUBLIC_SUPABASE_URL=https://<your-project-ref>.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=anon_key_here

# Optional: other config
EMBEDDING_MODEL=text-embedding-3-small
VECTOR_DIM=1536
```

**Security note:** Never commit `.env.local`. Add it to `.gitignore`.

---

## Supabase setup (one-time / if not done)

If you already have a Supabase project, skip to creating buckets and running migrations.

**If you want a local dev instance (optional)**:

```bash
# start local Supabase (if you installed supabase CLI)
supabase start
# follow instructions to link local project
```

**Create storage buckets (Supabase Studio > Storage)**:

- `raw-docs` (private) — put raw PDFs, images here
- `assets` (private/public) — PNG/SVG charts

**Apply DB migrations** (if provided):

```bash
supabase login
supabase link --project-ref <your-project-ref>
supabase db push    # or run SQL files in /supabase/migrations
```

Open Supabase Studio to inspect tables: `raw_files`, `chunks`, `chunk_vectors`, `knowledge_topics`, `commitments`, `metrics`, `assets`, `processed_files`.

---

## Useful developer commands (run this first)

Make sure your venv is active and `.env.local` is set.

```bash
# Linting / formatting (optional)
black .
flake8 .

# Run small smoke test to validate config
python ingest/ingest_smoke.py   # script that validates keys and Supabase connectivity
```

---

## 1) Ingest one file (parse, chunk, embed)

**Upload sample file** to Supabase `raw-docs` via UI OR put it in `/sample-data/`.

**Run ingestion** locally (single file):

```bash
python ingest/ingest.py --file ./sample-data/gc06-agenda.pdf
```

Flags:

- `-dry-run` (does everything except write to DB)
- `-force` (reprocess even if processed)
- `-file` (path to a local file; script handles upload + processing)

**What to expect**

- New row in `raw_files` (Supabase)
- New rows inserted into `chunks`
- `chunk_vectors` inserted with embeddings
- `processed_files` entry created

**Check** the Supabase tables in Studio to confirm.

---

## 2) Build the knowledge index (topics)

Run the index builder to generate canonical topics (LLM-driven):

```bash
python analysis/index_builder.py --sample 200
```

Flags:

- `-sample N` (use N representative chunks)
- `-dry-run` (print output to console, don’t insert)
- `-output ./tmp/topics.json` (save for review)

**Review**

- Check `knowledge_topics` table in Supabase
- Verify `evidence` includes file names & chunk ids

If any topics feel off, rerun with a different sample or edit prompts in `/analysis/prompts/`.

---

## 3) Extract dealer commitments (handwritten takeaways)

OCR and normalize handwritten takeaways:

```bash
python analysis/normalize_commitments.py --images ./sample-data/takeaways-page1.jpg --review
```

Flags:

- `-review` opens a simple CLI review to confirm ambiguous mappings
- `-output ./tmp/commitments.json`

**Manual QA**

- Inspect `commitments` table
- For low-confidence lines, correct the mapping in the review step
- Finalized commitments are inserted into `commitments` table.

---

## 4) Regenerate charts (SVG / Plotly)

Generate the visuals used on the microsite:

```bash
python analysis/charts_generator.py --upload
```

This script:

- Queries Supabase `knowledge_topics`, `commitments`, `metrics`
- Generates SVG or Plotly charts (bubble map, density bars, small multiples)
- Uploads SVGs to Supabase `assets` bucket
- Updates `assets` table with URLs

**Local-only version** (no upload):

```bash
python analysis/charts_generator.py --out-dir ./assets
```

---

## 5) Run the microsite locally

Open a new terminal:

```bash
cd app
npm run dev
# open http://localhost:3000
```

The site fetches sanitized views from Supabase. If anything appears missing, check the `public_` views or confirm RLS policies allow the anon key to read the sanitized tables.

**Build for production**

```bash
npm run build
npm run start
```

---

## 6) Tests & CI

Run Python tests (if present):

```bash
pytest -q
```

Lint and format:

```bash
black .
flake8
```

**PR workflow**:

1. Create a feature branch: `git checkout -b feat/ingest-fix`
2. Commit changes following conventional commits
3. Push and open a PR
4. Assign reviewer (engineering lead)
5. CI runs; address failures, then merge

---

## 7) Common troubleshooting

**Embeddings failing**

- Check `OPENAI_API_KEY` or embedding provider key
- Rate limit: cut into smaller batches

**OCR poor results**

- Try `-preprocess` flag in OCR script (grayscale, threshold)
- If handwriting is messy, run manual corrections using the `-review` step

**Supabase errors**

- RLS issues: try with the SERVICE_ROLE_KEY locally to debug
- Vector dimension mismatch: ensure `VECTOR_DIM` in `.env` matches DB vector size

**Microsite shows blank**

- Check `NEXT_PUBLIC_SUPABASE_ANON_KEY` and `NEXT_PUBLIC_SUPABASE_URL`
- Check sanitized views exist and have rows

---

## 8) Fast checklist (one-liner commands)

```bash
# Setup
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cd app && npm install && cd ..

# Ingest sample file
python ingest/ingest.py --file ./sample-data/gc06-agenda.pdf

# Build index (topics)
python analysis/index_builder.py --sample 200

# Normalize commitments
python analysis/normalize_commitments.py --images ./sample-data/takeaways-page1.jpg --review

# Generate charts and upload
python analysis/charts_generator.py --upload

# Run site locally
cd app && npm run dev
```

---

## 9) Notes on manual QA & review

- The `-review` flags exist on critical scripts to allow you to confirm ambiguous LLM outputs (especially for handwriting). Use them always the first few times.
- Keep `sources_map` filled: every insight must have evidence. If not, flag as `single-source` or `uncertain`.

---

## 10) Where to get help

- **Product lead:** Frazier Horn — `fhorn@hornhausventures.com`
- **Engineering lead / PR reviewer:** (Name / GitHub handle)
- **Design lead:** (Name / Figma file link)

---

## 11) Clean up & handoff

Before opening a PR for a completed feature:

- Ensure `processed_files` shows success for files you processed
- Confirm `sources_map` has traceability
- Update `docs/changes.md` with prompt edits or normalization heuristics you changed
- Add a short demo video/GIF of the microsite update

---

Action Items:

- Create a `.env.example` file with placeholders for these vars
- Add a `scripts/` folder with simple wrapper scripts (`run_ingest.sh`, `build_index.sh`) to make the intern’s life even easier

Would you like the `.env.example` and wrapper scripts next?