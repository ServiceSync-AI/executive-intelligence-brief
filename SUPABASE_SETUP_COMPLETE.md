# Supabase Setup Complete! ✅

## ✅ Configuration Done

Your `.env.local` files have been created with:
- Supabase URL: `https://easyazauclbtxgkxyfbe.supabase.co`
- Anon key: Configured
- Service role key: Configured

---

## 📋 Next Steps (5 minutes)

### Step 1: Apply Database Schema (2 min)

**Option A: Via Supabase Dashboard (Easiest)**

1. Go to: https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe/sql/new

2. Copy ALL the SQL from: `supabase/migrations/20260211_initial_schema.sql`

3. Paste into the SQL editor

4. Click "Run"

5. You should see: "Success. No rows returned"

**Option B: Via Supabase CLI**

```bash
# Install CLI (if not installed)
brew install supabase/tap/supabase

# Link project
supabase link --project-ref easyazauclbtxgkxyfbe

# Apply schema
supabase db push
```

---

### Step 2: Create Storage Buckets (2 min)

1. Go to: https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe/storage/buckets

2. Click "New bucket"
   - Name: `raw-docs`
   - Public: OFF (private)
   - Click "Create bucket"

3. Click "New bucket" again
   - Name: `assets`
   - Public: ON (public)
   - Click "Create bucket"

---

### Step 3: Add OpenAI API Key (1 min)

Edit `.env.local` and add your OpenAI key:

```bash
OPENAI_API_KEY=sk-proj-your_key_here
```

---

### Step 4: Install Dependencies (Optional - if not done)

```bash
cd /Users/frazierhorn/Development/GitHubRepos/Professional/executive-intelligence-brief

# Python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Node
cd app
npm install
cd ..
```

---

### Step 5: Test Configuration

```bash
source venv/bin/activate
python ingest/ingest_smoke.py
```

Should see:
```
✓ Environment variables configured
✓ Supabase connection successful
✓ OpenAI API connection successful
```

---

## 🚀 Then You're Ready!

### Process the NADA data:
```bash
source venv/bin/activate
python ingest/ingest.py --directory data/nada-jan-2026
```

### Run the microsite locally:
```bash
cd app
npm run dev
# Open http://localhost:3000
```

### Deploy to AWS Amplify:
See: `docs/AWS_AMPLIFY_SETUP.md`

---

## 📊 Verify Setup

Check your Supabase project:
- Tables: https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe/editor
- Storage: https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe/storage/buckets

You should see:
- ✅ 9 tables created (raw_files, chunks, chunk_vectors, etc.)
- ✅ 2 storage buckets (raw-docs, assets)

---

## 🆘 Need Help?

If anything doesn't work:
1. Check `.env.local` has all values filled
2. Verify schema was applied (check Tables in Supabase)
3. Verify storage buckets exist
4. Run smoke test: `python ingest/ingest_smoke.py`

---

**Project:** https://github.com/ServiceSync-AI/executive-intelligence-brief  
**Supabase:** https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe
