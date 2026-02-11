# Developer Setup Guide

**Complete onboarding for new developers and interns**

---

## ⏱️ Time Estimate

- Initial setup: 30-60 minutes
- First ingestion test: 20-40 minutes
- Full pipeline run: 1-2 hours

---

## 📋 Prerequisites

Before starting, ensure you have:

- [ ] GitHub account with access to ServiceSync-AI organization
- [ ] macOS, Linux, or Windows with WSL
- [ ] Node.js 18+ installed
- [ ] Python 3.10+ installed
- [ ] Git configured with SSH keys
- [ ] Code editor (VS Code recommended)

**Get from project lead:**
- [ ] Supabase project URL
- [ ] Supabase service role key
- [ ] Supabase anon key
- [ ] OpenAI API key

---

## 🛠️ Installation

### 1. Install System Dependencies

**macOS:**
```bash
brew install python node tesseract
brew tap supabase/tap
brew install supabase
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip nodejs npm tesseract-ocr
npm install -g supabase
```

**Windows (WSL):**
Use Ubuntu commands above in WSL terminal.

### 2. Clone Repository

```bash
cd ~/Development/GitHubRepos/Professional  # or your preferred location
git clone git@github.com:ServiceSync-AI/executive-intelligence-brief.git
cd executive-intelligence-brief
```

### 3. Python Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Node Dependencies

```bash
cd app
npm install
cd ..
```

### 5. Environment Configuration

```bash
cp .env.example .env.local
```

Edit `.env.local` with your credentials:

```env
# Supabase
SUPABASE_URL=https://YOUR_PROJECT.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here
SUPABASE_ANON_KEY=your_anon_key_here

# OpenAI
OPENAI_API_KEY=sk-your_key_here

# Configuration
EMBEDDING_MODEL=text-embedding-3-small
VECTOR_DIM=1536

# Next.js (for microsite)
NEXT_PUBLIC_SUPABASE_URL=https://YOUR_PROJECT.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key_here
```

**⚠️ Security:** Never commit `.env.local` - it's in `.gitignore`

---

## 🗄️ Supabase Setup

### 1. Link to Project

```bash
supabase login
supabase link --project-ref YOUR_PROJECT_REF
```

### 2. Create Storage Buckets

In Supabase Studio (app.supabase.io):
- Create bucket: `raw-docs` (private)
- Create bucket: `assets` (public or private)

### 3. Apply Database Migrations

```bash
supabase db push
```

This creates all required tables:
- `raw_files` - uploaded document metadata
- `chunks` - text segments from documents
- `chunk_vectors` - embeddings for semantic search
- `knowledge_topics` - canonical topics with evidence
- `commitments` - dealer commitments mapped to themes
- `metrics` - aggregated performance data
- `sources_map` - traceability
- `processed_files` - ingestion audit log

### 4. Verify Setup

```bash
# Check tables exist
supabase db remote connect
# In psql: \dt
```

---

## ✅ Validation Tests

### Test 1: Python Environment

```bash
python ingest/ingest_smoke.py
```

Expected: "✓ Supabase connection successful"

### Test 2: Single File Ingestion

```bash
python ingest/ingest.py --file ./sample-data/test-agenda.pdf --dry-run
```

Expected: Parsed text output, no errors

### Test 3: Microsite

```bash
cd app
npm run dev
```

Open http://localhost:3000 - should see placeholder page

---

## 🔄 Development Workflow

### Daily Workflow

1. **Activate environment:**
```bash
source venv/bin/activate
```

2. **Pull latest changes:**
```bash
git pull origin main
```

3. **Create feature branch:**
```bash
git checkout -b feat/your-feature-name
```

4. **Make changes and test**

5. **Commit and push:**
```bash
git add .
git commit -m "feat: description of changes"
git push origin feat/your-feature-name
```

6. **Open PR on GitHub**

---

## 📝 Common Tasks

### Ingest a Document

```bash
python ingest/ingest.py --file path/to/document.pdf
```

Flags:
- `--dry-run` - Test without writing to database
- `--force` - Reprocess even if already processed

### Build Knowledge Index

```bash
python analysis/index_builder.py --sample 200
```

Flags:
- `--sample N` - Use N representative chunks
- `--output file.json` - Save to file for review

### Extract Commitments

```bash
python analysis/normalize_commitments.py \
  --images ./sample-data/takeaways.jpg \
  --review
```

The `--review` flag opens interactive QA for ambiguous mappings.

### Generate Charts

```bash
python analysis/charts_generator.py --upload
```

Flags:
- `--upload` - Upload to Supabase assets
- `--out-dir ./assets` - Save locally only

### Run Microsite Locally

```bash
cd app
npm run dev
```

### Build for Production

```bash
cd app
npm run build
npm run start
```

---

## 🐛 Troubleshooting

### Python Import Errors

```bash
pip install -r requirements.txt --force-reinstall
```

### Supabase Connection Failed

- Verify `.env.local` has correct URL and keys
- Check Supabase project is active
- Test with service role key (not anon key) for ingestion

### Embeddings API Errors

- Check `OPENAI_API_KEY` is valid
- Verify API quota/billing
- Try smaller batch sizes

### OCR Poor Quality

- Ensure Tesseract is installed: `tesseract --version`
- For handwriting, consider AWS Textract or manual review

### Vector Dimension Mismatch

- Ensure `VECTOR_DIM` in `.env.local` matches embedding model
- Default: 1536 for `text-embedding-3-small`

### Microsite Shows No Data

- Check `NEXT_PUBLIC_*` variables in `.env.local`
- Verify Supabase RLS policies allow anon key reads
- Check browser console for errors

---

## 🧪 Running Tests

```bash
# Python tests
pytest

# Linting
black .
flake8

# Node tests
cd app
npm test
```

---

## 📚 Next Steps

After setup is complete:

1. **Read [ARCHITECTURE.md](ARCHITECTURE.md)** - Understand system design
2. **Review sample data** - Explore `sample-data/` folder
3. **Run full pipeline** - Process one complete document
4. **Explore Supabase** - Inspect tables and data
5. **Review storyboard** - See microsite design in Notion

---

## 🆘 Getting Help

**Stuck?** Contact:
- **Project Lead:** Frazier Horn - frazier@servicesync.io
- **GitHub Issues:** Open an issue with error details
- **Slack:** #executive-intelligence channel

**Before asking:**
1. Check this guide
2. Search GitHub issues
3. Review error messages carefully
4. Try `--dry-run` or `--help` flags

---

## ✨ Tips for Success

- **Commit often** - Small, focused commits
- **Test locally** - Always test before pushing
- **Document changes** - Update docs when changing behavior
- **Ask questions** - No question is too small
- **Review PRs** - Learn from others' code

---

**Welcome to the team! 🚀**
