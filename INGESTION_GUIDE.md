# Running the Ingestion Pipeline

**Status:** Phase 2 Complete - Ready to ingest data! 🚀

---

## Prerequisites

✅ Supabase project configured  
✅ Storage buckets created (raw-docs, assets)  
✅ All parsers and scripts ready  
⏳ Database schema needs to be applied  
⏳ OpenAI API key needs to be added  

---

## Step 1: Apply Database Schema

**Option A: SQL Editor (Easiest)**

1. Go to: https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe/sql/new
2. Copy the entire contents of `supabase/migrations/20260211_initial_schema.sql`
3. Paste into the SQL editor
4. Click "Run"
5. Verify tables created: raw_files, chunks, knowledge_topics, commitments, metrics

**Option B: Supabase CLI**

```bash
supabase login
supabase link --project-ref easyazauclbtxgkxyfbe
supabase db push
```

---

## Step 2: Add OpenAI API Key

Edit `.env.local` and add your OpenAI business account key:

```bash
OPENAI_API_KEY=sk-proj-your-actual-key-here
```

---

## Step 3: Test Ingestion (5 files)

```bash
cd ingest
source ../venv/bin/activate
python ingest.py --directory ../data/nada-jan-2026 --limit 5
```

This will:
- Parse 5 files
- Chunk the text (800 tokens, 200 overlap)
- Generate embeddings via OpenAI
- Store in Supabase

Expected output:
```
🚀 Starting ingestion
   Directory: ../data/nada-jan-2026
   Files found: 5
   ✓ Connected to Supabase

[1/5] 📄 Processing: Hot Topics.pdf
   ✓ Parsed (571 chars)
   ✓ Created 1 chunks
   ✓ Generated 1 embeddings
   ✓ Stored file record (id: ...)
   ✓ Stored 1 chunks

...

✅ Ingestion complete!
   Processed: 5/5 files
```

---

## Step 4: Validate Data

```bash
python validate.py
```

Expected output:
```
🔍 Validating Ingestion Data

📁 Raw Files Table:
   ✓ Files stored: 5
   File types:
     - pdf: 3
     - docx: 2

📦 Chunks Table:
   ✓ Chunks stored: 15
   Total tokens: 12,000
   Avg tokens/chunk: 800.0

🔢 Embeddings:
   ✓ Embeddings present
   Dimension: 1536

🪣 Storage Buckets:
   ✓ raw-docs exists
   ✓ assets exists

✅ VALIDATION PASSED
```

---

## Step 5: Run Full Ingestion

Once test passes, process all 45 priority files:

```bash
python ingest.py --directory ../data/nada-jan-2026/to-process
```

This will process:
- 12 meeting docs (DOCX, PDF)
- 19 dealer processes (TXT, PDF)
- 8 performance data (CSV, XLSX)
- 1 roster image (PNG)
- 3 indexes (MD)

Expected time: ~10-15 minutes (depends on OpenAI API speed)

---

## Step 6: Final Validation

```bash
python validate.py
```

Expected results:
- Files: ~45
- Chunks: ~500-1000
- All embeddings present
- No issues

---

## Troubleshooting

**Error: "OPENAI_API_KEY not found"**
- Add key to `.env.local`
- Make sure no spaces around `=`

**Error: "column chunks.embedding does not exist"**
- Database schema not applied
- Go back to Step 1

**Error: "Rate limit exceeded"**
- OpenAI API rate limit hit
- Wait 1 minute and retry
- Or use `--limit` to process in smaller batches

**Error: "Supabase connection failed"**
- Check `.env.local` has correct SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY
- Verify project is active at https://supabase.com/dashboard

---

## What's Next?

After successful ingestion:

✅ Phase 2 Complete  
➡️ **Phase 3: Knowledge Extraction**
- Build topic index with LLM
- Extract dealer commitments
- Aggregate metrics
- Create source traceability

See `STATUS.md` for full roadmap.

---

## Quick Reference

```bash
# Dry run (no database writes)
python ingest.py --directory ../data/nada-jan-2026 --dry-run

# Process specific number of files
python ingest.py --directory ../data/nada-jan-2026 --limit 10

# Full ingestion
python ingest.py --directory ../data/nada-jan-2026/to-process

# Validate data
python validate.py
```

---

**Questions?** Check `STATUS.md` or GitHub Issues: https://github.com/ServiceSync-AI/executive-intelligence-brief/issues
