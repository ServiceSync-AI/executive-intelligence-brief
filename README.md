# Executive Intelligence Brief

**Transform meeting artifacts into operator-grade intelligence**

A reproducible pipeline that turns NADA 20 Group meeting materials (agendas, notes, SOPs, transcripts) into a forwardable Executive Intelligence Brief microsite.

---

## 🎯 Project Overview

This system processes raw meeting documents and generates:
- Structured knowledge index with canonical topics
- Dealer commitment tracking mapped to execution themes
- Performance metrics and variance analysis
- Interactive visualizations (heatmaps, matrices, charts)
- Single-page microsite presenting executive intelligence

**Goal:** Establish credibility by surfacing patterns no one else extracted — not as a sales pitch, but as operational intelligence.

---

## 🏗️ Architecture

```
Raw Documents → Supabase Storage → Ingestion (Python) → 
Chunks + Embeddings → Knowledge Index (LLM) → 
Commitments + Metrics → Charts (Plotly) → Microsite (Next.js)
```

**Tech Stack:**
- **Database:** Supabase (PostgreSQL + pgvector)
- **Processing:** Python (ingestion, OCR, embeddings, analysis)
- **Frontend:** Next.js + TypeScript + TailwindCSS
- **Deployment:** Vercel
- **CI/CD:** GitHub Actions

---

## 📁 Repository Structure

```
/
├── ingest/              # Document parsing and ingestion
│   ├── ingest.py        # Main ingestion script
│   ├── ingest_smoke.py  # Configuration validation
│   └── parsers/         # PDF, DOCX, image parsers
├── analysis/            # Knowledge extraction and analytics
│   ├── index_builder.py         # LLM-driven topic extraction
│   ├── normalize_commitments.py # Dealer commitment mapping
│   ├── charts_generator.py      # Visualization generation
│   └── prompts/                 # LLM prompt templates
├── notebooks/           # Jupyter notebooks for EDA
├── supabase/
│   └── migrations/      # Database schema migrations
├── app/                 # Next.js microsite
│   └── components/
│       └── sections/    # Page sections per storyboard
├── data/
│   └── nada-jan-2026/   # 72 NADA meeting files (PDFs, DOCX, data)
├── design/              # Figma exports and design tokens
├── docs/                # Documentation
│   ├── DEV_SETUP.md     # Developer onboarding
│   ├── ROADMAP.md       # Project phases
│   └── WORKFLOWS.md     # CI/CD setup
├── .github/
│   └── workflows/       # CI/CD automation
├── sample-data/         # Test files
└── assets/              # Generated charts and visuals
```

---

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.10+
- Supabase account (get URL and service key)
- OpenAI API key

### Setup

1. **Clone and install:**
```bash
git clone git@github.com:ServiceSync-AI/executive-intelligence-brief.git
cd executive-intelligence-brief

# Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Node dependencies
cd app
npm install
cd ..
```

2. **Configure environment:**
```bash
cp .env.example .env.local
# Edit .env.local with your keys
```

3. **Set up Supabase:**
```bash
# Apply database migrations
supabase login
supabase link --project-ref YOUR_PROJECT_REF
supabase db push
```

4. **Run ingestion (test):**
```bash
python ingest/ingest.py --file ./sample-data/test-agenda.pdf
```

5. **Start microsite:**
```bash
cd app
npm run dev
# Open http://localhost:3000
```

---

## 📚 Documentation

- **[Developer Setup Guide](docs/DEV_SETUP.md)** - Step-by-step onboarding
- **[Architecture Overview](docs/ARCHITECTURE.md)** - System design and data flow
- **[Supabase Schema](supabase/migrations/)** - Database structure
- **[API Documentation](docs/API.md)** - Endpoints and data models

---

## 🔄 Workflows

### 1. Ingest Documents
```bash
# Process all NADA files
python ingest/ingest.py --directory data/nada-jan-2026
```
Parses 72 files (PDFs, DOCX, images), chunks text, generates embeddings, stores in Supabase.

### 2. Build Knowledge Index
```bash
python analysis/index_builder.py --sample 200
```
LLM extracts canonical topics with evidence traceability.

### 3. Extract Commitments
```bash
# Process handwritten takeaways
python analysis/normalize_commitments.py \
  --images data/nada-jan-2026/Meeting\ Follow\ Up\ Email\ Attachments/Take\ A\ Way\'s.pdf \
  --review
```
OCRs handwritten notes, maps to themes, manual QA.

### 4. Generate Charts
```bash
python analysis/charts_generator.py --upload
```
Creates visualizations, uploads to Supabase assets.

### 5. Deploy Site
```bash
cd app
npm run build
vercel deploy
```

---

## 🔐 Security & Confidentiality

**Repository Access:**
- Private repository within ServiceSync-AI organization
- All NADA meeting files included for team processing
- Controlled access via GitHub organization membership

**Critical Requirements for Public Brief:**
- ❌ No emails, phone numbers, or PII in public site
- ❌ No named dealer performance rankings
- ❌ No attributed quotes to specific people
- ✅ Dealer codes (numbers) only
- ✅ Anonymous performance distributions
- ✅ Aggregated metrics only

All sensitive data protected via Supabase RLS policies in final microsite.

---

## 🤝 Contributing

1. Create feature branch: `git checkout -b feat/your-feature`
2. Make changes with tests
3. Commit: `git commit -m "feat: description"`
4. Push: `git push origin feat/your-feature`
5. Open PR for review

**Code Style:**
- Python: `black` + `flake8`
- TypeScript: `eslint` + `prettier`
- Conventional commits

---

## 📞 Team & Support

**Project Lead:** Frazier Horn - frazier@servicesync.io

**Key Resources:**
- [Notion Documentation](https://notion.so/servicesync)
- [Supabase Project](https://app.supabase.io)
- [Figma Design System](https://figma.com)

---

## 📄 License

Proprietary - ServiceSync AI  
© 2026 ServiceSync AI. All rights reserved.

---

**Built for NADA 20 Group GC06 - January 2026**
