# Quick Reference - Executive Intelligence Brief

## 🎯 What This Is

Transform 72 NADA meeting documents into an Executive Intelligence Brief showing the execution gap in automotive service operations. Reveals where knowledge exists but continuity breaks down.

**Key Insight:** The industry doesn't lack best practices. Execution breaks between meetings, departments, and shifts. The system doesn't remember.

---

## 📍 Locations

**GitHub:** https://github.com/ServiceSync-AI/executive-intelligence-brief  
**Local:** `/Users/frazierhorn/Development/GitHubRepos/Professional/executive-intelligence-brief`  
**Data:** `data/nada-jan-2026/` (72 files, not in git)

## 🚀 Quick Commands

```bash
# Navigate to project
cd /Users/frazierhorn/Development/GitHubRepos/Professional/executive-intelligence-brief

# Activate Python environment
source venv/bin/activate

# Test configuration
python ingest/ingest_smoke.py

# Run ingestion (when implemented)
python ingest/ingest.py --directory data/nada-jan-2026

# Build knowledge index
python analysis/index_builder.py --sample 200

# Generate charts
python analysis/charts_generator.py --upload

# Run microsite
cd app && npm run dev
```

## 📚 Key Documents

- **README.md** - Start here
- **docs/DEV_SETUP.md** - Developer onboarding
- **PROJECT_SUMMARY.md** - Complete overview
- **data/nada-jan-2026/README.md** - Data inventory

## 🔑 Environment Setup

```bash
cp .env.example .env.local
# Add:
# - SUPABASE_URL
# - SUPABASE_SERVICE_ROLE_KEY
# - SUPABASE_ANON_KEY
# - OPENAI_API_KEY
```

## 📊 Data Summary

**Location:** `data/nada-jan-2026/`

- **Total Files:** 72
- **PDFs:** 25 (agendas, handouts, homeworks, follow-ups)
- **DOCX:** 13 (notes, summaries, strategic docs)
- **Extracted Data:** 27 (text files, CSVs)
- **Images:** 1 (roster)
- **Markdown:** 2 (knowledge index, traceability)

All files included in repository for team access and processing.

## 🎯 Current Phase

✅ Phase 1: Foundation - COMPLETE  
⏳ Phase 2: Ingestion - Next

## 👥 Team Access

Share this with team:
```bash
git clone git@github.com:ServiceSync-AI/executive-intelligence-brief.git
cd executive-intelligence-brief
# Follow docs/DEV_SETUP.md
```
