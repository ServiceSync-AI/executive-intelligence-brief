# Supabase Documentation

Owner: Fray

Supabase gives you a real Postgres backing (so everything is queryable and versionable), hosted storage for documents and assets, Edge Functions / cron for automation, and the ability to add vector search (pgvector) for embeddings. Below is a **concrete, ordered plan** to build the full “meeting → knowledge → site” pipeline in Supabase, plus schemas, code snippets, recommended libraries, and the exact sequencing that ties back to the prompt pipeline we designed earlier.

I. Big picture (one-sentence)

- Put **raw files** into Supabase Storage → run an ingestion worker that parses & chunks files → create/store **chunks + embeddings** (vectors) + metadata → build a **Knowledge Index** table of topics/definitions/traceability → generate commitments/metrics JSON → produce visuals and the microsite which reads structured data from Supabase → keep everything updated with scheduled re-ingestion and event-driven updates.

---

## ORDER OF STEPS (high level)

1. **Supabase setup**: project, storage bucket, database, enable pgvector (if available), service key.
2. **Create DB schema**: tables for files, chunks, vectors, knowledge_index, insights, commitments, metrics, processed_files, decisions, citations.
3. **Wire storage**: create `raw-docs/` bucket. Add upload policy and roles.
4. **Ingest worker**: script (Python/Node) to watch bucket or run on demand → parse files → OCR for images/handwriting → chunk → embed → store chunks + embeddings.
5. **Knowledge index builder**: an LLM-driven process that consumes chunks and builds canonical topics with traceability.
6. **Commitments extraction**: parse handwritten takeaways + notes -> map dealer codes to themes -> store `commitments` table.
7. **Analytics & visuals**: Python notebooks generate charts (SVG/Plotly) from Supabase queries; store visuals in `assets/` bucket.
8. **Microsite**: build Next.js (or Framer) app that reads from Supabase (public read role or secure API) and renders the storyboard with charts & JSON.
9. **Automation**: schedule re-ingest (cron / Supabase Edge Function), webhooks for new uploads, and periodic knowledge-index refreshes.
10. **QA & auditing**: lineage via `sources_map`, snapshot exports, backups, tests.

---

## REQUIRED TABLE SCHEMAS (SQL you can paste)

> Note: adjust types and naming to your conventions. I include `pgvector` usage for embeddings.
> 

```sql
-- enable pgvector if not already (may require Supabase support)
-- CREATE EXTENSION IF NOT EXISTS vector;

-- raw files metadata
CREATE TABLE raw_files (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  path text NOT NULL,          -- storage path
  filename text,
  file_type text,
  size bigint,
  uploaded_at timestamptz DEFAULT now(),
  uploaded_by text,
  processed boolean DEFAULT false,
  processing_error text
);

-- chunked content
CREATE TABLE chunks (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  file_id uuid REFERENCES raw_files(id) ON DELETE CASCADE,
  chunk_index int,
  text text,
  created_at timestamptz DEFAULT now()
);

-- vector table (pgvector)
CREATE TABLE chunk_vectors (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  chunk_id uuid REFERENCES chunks(id) ON DELETE CASCADE,
  embedding vector(1536),   -- size depends on embedding model
  metadata jsonb,
  created_at timestamptz DEFAULT now()
);

-- canonical topics / knowledge index
CREATE TABLE knowledge_topics (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  topic text UNIQUE,
  definition text,
  status text,   -- observed / agreed / committed / unresolved
  evidence jsonb, -- [{file:..., chunk_ids: [...] }]
  confidence numeric,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

-- commitments: dealer_code -> themes
CREATE TABLE commitments (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  dealer_code text,
  theme text,
  statement text,
  evidence jsonb, -- filenames, page refs, original text snippet
  captured_at timestamptz DEFAULT now()
);

-- numeric metrics aggregated or ranges
CREATE TABLE metrics (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text,
  median numeric,
  low numeric,
  high numeric,
  units text,
  evidence jsonb,
  updated_at timestamptz DEFAULT now()
);

-- decisions & action log for persistence
CREATE TABLE decision_log (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  context text,
  decision text,
  owner text,
  due_date date,
  status text,
  created_at timestamptz DEFAULT now()
);

-- mapping of insight -> source files (traceability)
CREATE TABLE sources_map (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  insight_id uuid,
  source_files jsonb,
  created_at timestamptz DEFAULT now()
);

-- processed files / audit
CREATE TABLE processed_files (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  file_id uuid REFERENCES raw_files(id),
  status text,
  details jsonb,
  processed_at timestamptz DEFAULT now()
);
```

---

## INGESTION WORKFLOW (detailed)

**Tools & libs** (recommended)

- Python 3.10+
- `supabase-py` or `supabase-js`
- `pdfplumber`, `PyPDF2`, `pytesseract`, `python-docx` for parsing
- `langchain` (optional) for orchestration and chunking helpers
- `openai` (or other embedding provider)
- `numpy`, `pandas`
- `psycopg2` / `asyncpg` or `supabase` client
- If handwriting: `Tesseract` + `easyocr` or a handwriting OCR service
- Docker for local testing

**High-level ingestion steps (Python pseudocode)**

```python
# pseudocode (not full)
from supabase import create_client
import pdfplumber, docx, pytesseract
from openai import OpenAI

SUPABASE_URL = "..."
SUPABASE_KEY = "..."
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
openai = OpenAI(api_key="...")

def upload_file_to_supabase(filepath):
    # upload file to storage/raw-docs/... and create raw_files row
    storage_path = f"raw-docs/{filename}"
    supabase.storage.from_('raw-docs').upload(storage_path, open(filepath,'rb'))
    res = supabase.table('raw_files').insert({...}).execute()

def parse_file(file_path):
    if file is pdf:
        text = extract_text_with_pdfplumber(file_path)
    elif file is docx:
        text = extract_with_docx(file_path)
    elif file is image:
        text = pytesseract.image_to_string(...)
    # add OCR for handwritten pages specially
    return text

def chunk_text(text, chunk_size=800, overlap=200):
    # split text into chunks with overlap
    return chunks

def create_embeddings(chunks):
    embeddings = []
    for c in chunks:
        emb = openai.embeddings.create(input=c)["data"][0]["embedding"]
        embeddings.append(emb)
    return embeddings

def store_chunks_and_vectors(file_id, chunks, embeddings, metadata):
    for idx,(chunk,emb) in enumerate(zip(chunks, embeddings)):
        chunk_row = supabase.table('chunks').insert({...}).execute()
        vector_row = supabase.table('chunk_vectors').insert({
             'chunk_id': chunk_row['id'],
             'embedding': emb,
             'metadata': {...}
        }).execute()
```

**Notes & tips**

- **Chunk size**: 500–900 tokens is a common sweet spot. Keep overlap ~100–200 tokens.
- **Batch embeddings**: send chunks in batches to embedding API.
- **Store original snippets** in chunk metadata for traceability.
- For **handwritten takeaways**, use an OCR pass directed at those specific images; then clean up using prompt-engineered LLM steps.

---

## VECTOR SEARCH & TOPIC EXTRACTION

**Vector search (SQL example with pgvector)**:

```sql
-- find top 5 similar chunks to a query embedding:
SELECT chunk_id, chunks.text, (1 - (embedding <=> query_embedding)) as similarity
FROM chunk_vectors
JOIN chunks ON chunks.id = chunk_vectors.chunk_id
ORDER BY chunk_vectors.embedding <-> query_embedding
LIMIT 5;
```

(`<->` is pgvector distance operator)

**Topic extraction** using LLM:

- Run a batch query to gather representative chunks (e.g., high-frequency terms)
- Feed them to LLM with a prompt: “Extract canonical topics/themes (5–10) we should track and return {topic: definition, example_snippets:[], supporting_files:[] }”

Store outputs into `knowledge_topics`.

---

## BUILDING THE KNOWLEDGE INDEX (process & prompt guidance)

**Process**

1. Gather a sample of high-signal chunks (most-cited chunks, topic clusters).
2. Prompt LLM to propose canonical topics and definitions using evidence pointers.
3. LLM returns JSON; insert into `knowledge_topics` with `evidence` referencing file ids & chunk ids.

**Example prompt to LLM**

> “You are a sensible operator analyst. Given these text snippets (with file names and chunk ids), propose up to 10 canonical topics in operator language. For each: topic name, one-sentence definition, 2–3 evidence snippets, confidence (0–1). Output as valid JSON.”
> 

---

## EXTRACTION: DEALER COMMITMENTS (handwritten pages)

- Use OCR to get the raw handwritten lines (use separate OCR model like AWS Textract or Tesseract).
- Normalize phrases via a small mapping (heuristic + LLM): map phrasing to the 6 themes.
- Validate: produce a table (dealer_code, original_text, mapped_theme, confidence).
- Insert into `commitments`.

**Prompt to normalize**

> “Given this list of short handwritten phrases, map each phrase to one of the canonical themes: [list]. If ambiguous, return 'uncertain' and include the original phrase.”
> 

Have the intern **manually approve** ambiguous mappings during first passes.

---

## VISUALS & MICROSITE

**Visual generation**

- Use Python (Plotly or Altair) to query Supabase metrics and outputs and generate SVGs or interactive Plotly graphs.
- Save SVGs to Supabase storage `assets/` bucket and store URLs in a `charts` table.

**Microsite stack (recommendation)**

- **Frontend**: Next.js (App Router) + TypeScript + TailwindCSS
- **Data**: Read from Supabase via `@supabase/supabase-js`
- **Charts**: Plotly for interactive or use static SVGs
- **Deploy**: Vercel or Supabase Hosting
- **Reads**: Public read role or JWT-secured for auth; keep contact info & raw emails out of public pages.

**Page architecture**

- Fetch `knowledge_topics`, `commitments`, `metrics`, and chart URLs from Supabase and render per the storyboard we designed earlier.

---

## AUTOMATION & CONTINUOUS UPDATES

**Event-driven**

- Create a Supabase Edge Function or webhook that fires when new files are uploaded to `raw-docs/` bucket.
- Function pushes a job to your ingestion worker (or directly runs ingestion for small files).

**Scheduled**

- CRON (Supabase has scheduler or use GitHub Actions) to:
    - Re-run topic extraction weekly
    - Recompute metrics after new data
    - Regenerate visuals and export snapshots

**Delta updates**

- Keep `processed_files` table to avoid re-processing.
- When new chunks are added, run an incremental topic/update pipeline rather than full rebuild.

**Notifications**

- On significant changes (new topic, big commitment changes), post to Slack or email a short summary. Use Supabase Edge Functions to send.

---

## ACCESS CONTROL & SECURITY

- Use Supabase Row Level Security (RLS) for tables holding sensitive metadata.
- Keep `raw_files` or `raw-docs` bucket non-public.
- The microsite should only expose anonymized data. Use server-side rendering (Next.js), or if public, only read from sanitized tables/views.
- Maintain an audit trail: who uploaded, who mapped commitments, who approved mappings.

---

## DEV/PROD & BACKUPS

- Use separate Supabase projects for dev and prod.
- Export periodic backups of DB (automated) and assets.
- Keep schema migrations managed with a migration tool (e.g., `sqitch`, `pg-migrate`, or Supabase migrations).

---

## RECOMMENDED INFRASTRUCTURE / LIBRARIES

- **Python**: `supabase-py`, `openai`, `langchain`, `pdfplumber`, `python-docx`, `pytesseract`, `numpy`, `pandas`, `plotly`, `altair`
- **Node**: `@supabase/supabase-js`, `openai`, Next.js for site
- **Vector**: `pgvector` (native in Supabase if available) or external vector DB (Pinecone/Weaviate) if not
- **OCR**: `pytesseract` or managed OCR (AWS Textract, Google Vision) — handwriting accuracy will vary
- **CI/Automation**: GitHub Actions, Supabase Edge functions

---

## HOW THIS MAPS TO YOUR PROMPT PIPELINE

Use Supabase at every stage:

1. **Inventory (Prompt 1)**
    - Query `raw_files` and `processed_files`. Return a table of ingestion_status.
2. **Knowledge Index Builder (Prompt 2)**
    - Read `chunks` + `chunk_vectors` and create `knowledge_topics`.
3. **Commitments Map (Prompt 3)**
    - Read `commitments` table; export `commitments.json`.
4. **Fresh Eyes / Ideation (Prompt 4)**
    - Feed `knowledge_topics` + representative chunk snippets to LLM in your “fresh eyes” prompt.
5. **Artifact Prioritization (Prompt 5)**
    - Use metrics and `commitments` in DB to rank artifacts.
6. **Build (Prompt 6)**
    - Site reads sanitized views from DB. Use `charts` and `assets` table for visuals.
7. **Memory Update**
    - Append to `decision_log` and update `knowledge_topics` status, and store the delta.

---

## A PRACTICAL STEP-BY-STEP FOR THE INTERN (concrete)

1. **Get Supabase access** (project URL + service key + storage access).
2. **Create DB tables** (paste SQL above).
3. **Create storage buckets**: `raw-docs/`, `assets/`.
4. **Small test file**: upload one meeting agenda PDF to `raw-docs`.
5. **Run local ingestion script** on that one file:
    - parse text → chunk → create embeddings → insert `chunks` & `chunk_vectors`.
6. **Write a simple query**: fetch top 10 chunks similar to “video MPI adoption”.
7. **Build a knowledge-index prototype**: run LLM prompt on 30 top chunks.
8. **Extract commitments**: OCR the handwritten takeaways image, normalize with LLM to themes, store in `commitments`.
9. **Make one visualization** (e.g., theme density bar) and save as SVG to `assets/`.
10. **Build a one-page Next.js site** that reads `knowledge_topics`, `commitments`, and renders the theme density chart.
11. **Document**: write README about how to run ingestion and rebuild visuals.
12. **Automate**: add a Supabase Edge Function or GitHub Action to re-run ingestion when new files are added.
13. **QA**: review outputs, check `sources_map` for traceability, and have you sign-off.

---

## QUICK SAMPLE: Python snippet to upsert chunk & vector to Supabase (very small)

```python
from supabase import create_client
import numpy as np
import json

supabase = create_client(url, key)

def upsert_chunk_vector(chunk_id, embedding, chunk_text):
    supabase.table('chunks').insert({
        'id': chunk_id,
        'text': chunk_text
    }).execute()
    supabase.table('chunk_vectors').insert({
        'chunk_id': chunk_id,
        'embedding': embedding,   # depends on driver; some clients support passing list for vector column
        'metadata': {'snippet': chunk_text[:200]}
    }).execute()
```

Note: how to insert a vector depends on `supabase-py` version. If needed, convert embedding list into vector literal like `ARRAY[...]` or use parameterized SQL.

---

## FINAL NOTES & UX TIPS

- **Constrain personally-identifying info** at ingestion: drop emails/phones when saving public records and keep them only behind RLS.
- **Manual QA loop** at first: the intern flags ambiguous OCR results and theme mappings.
- **Keep the Knowledge Index human-editable** (use a simple admin view or small internal app) so you can correct topics/status quickly.
- **A/B check**: small sample manual mapping vs LLM mapping to calibrate confidence thresholds.
- **Logs & traceability** matter more than fancy UI in early days — make sure `sources_map` is always populated.

---

Action Items for AI:

- Produce a **ready-to-run ingestion repo skeleton** (Python) with sample environment variables and a simple Dockerfile.
- Or generate the **SQL with migrations** for Supabase and an Edge Function template to trigger ingestion on new uploads.