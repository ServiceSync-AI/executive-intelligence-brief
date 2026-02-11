# Executive Intelligence Brief

**Transform meeting artifacts into operator-grade intelligence**

**🌐 Live Site:** http://gc06-servicesync.s3-website-us-east-1.amazonaws.com  
**🔗 Custom Domain:** https://gc06.servicesync.io (configure Cloudflare DNS)

**Status:** ✅ DEPLOYED - All 6 phases complete!

---

## 🎯 What Is This?

**The Problem:**  
You attended a NADA 20 Group meeting with 40+ automotive service managers. Two days of discussions, best practices, dealer presentations, and commitments. Tons of valuable insights... but they fade after the meeting. Knowledge doesn't stick. Execution drifts.

**What We're Building:**  
A single-page interactive website (Executive Intelligence Brief) that extracts and visualizes the patterns NO ONE ELSE SAW from those 72 meeting documents.

**The Insight:**  
The automotive service industry doesn't lack knowledge. Every dealer knows the best practices:
- Video MPIs increase hours per RO
- Stall discipline improves tech productivity  
- Sales-to-service handoffs retain customers
- Daily huddles drive accountability

**The Real Problem:**  
Execution breaks down BETWEEN meetings, BETWEEN departments, BETWEEN shifts. The system doesn't remember. People are forced to manually maintain accountability.

**What This Brief Shows:**
1. **What the room agreed on** - Topics that surfaced repeatedly (alignment exists)
2. **What playbooks already cover** - Knowledge isn't the constraint
3. **Where performance still varies** - Same knowledge, different outcomes
4. **Where execution quietly breaks** - Between meetings, departments, systems
5. **What this group is ready for** - Continuity, not more meetings

**The Goal:**  
Establish ServiceSync as "the people who see the system" by delivering intelligence that makes Greg (the moderator) and service managers say: *"This person understands what happens between meetings."*

Not a sales pitch. Not a recap. **Operational intelligence that reveals the execution gap.**

---

## 🏭 The Industry Context

**NADA 20 Groups:**  
Peer groups of 15-20 automotive dealerships that meet quarterly to share performance data, best practices, and operational challenges. Facilitated by consultants like Greg Joutras.

**Key Metrics They Track:**
- **Service Absorption** - % of dealership overhead covered by service department (target: 70-90%)
- **Hours per RO** - Billable labor hours per customer visit (Quick Lane: 1.6, Main Shop: 3.2)
- **Technician Proficiency** - Actual hours worked vs available (range: 76-169%)
- **Parts Inventory Turn** - How fast parts sell (optimal: 40-60%)
- **Service Retention** - % of customers returning (target: 90%, actual: 70-85%)

**Pain Points We Discovered:**
- Phone handling and scheduling (AI adoption starting)
- Video MPI implementation (tech resistance)
- Postponed service follow-up (tracking breaks down)
- Reconditioning speed (service/used car trust issues)
- Daily accountability (manual whiteboards and huddles)

**The Pattern:**  
High-performing stores compensate with constant leadership presence, whiteboards, radios, and manual follow-up. **That effort should be permanent, not heroic.**

---

## 📊 What We're Extracting from 72 Files

**Source Materials:**
- 25 PDFs (agendas, handouts, performance data)
- 13 DOCX (meeting notes, transcripts, strategic docs)
- 27 extracted data files (metrics, commitments)
- 1 roster image
- 2 knowledge indexes

**What We're Building:**

### 1. Conversation Heatmap
Visual showing which topics consumed the most discussion time across the 2-day meeting.  
**Insight:** "Some issues consumed disproportionate mental energy."

### 2. Dealer Commitment Matrix
Grid showing which dealers committed to which execution themes post-meeting.  
**Insight:** "Execution priorities captured directly from the room."

### 3. Knowledge Topics Index
10-15 canonical topics with evidence traceability back to source documents.  
**Insight:** "What the industry already knows how to do."

### 4. Performance Variance Analysis
Anonymous distributions showing outcome spreads despite shared knowledge.  
**Insight:** "Same ideas present, but results differ. That variance is the signal."

### 5. Execution Gap Diagram
Visual showing where the system breaks: Decision → Owner → Action → Measurement → Follow-up.  
**Insight:** "Most failures occur between steps, not within them."

---

## 🎯 The Deliverable

**Format:** Single-page scroll-based microsite  
**Tone:** Internal analyst, not marketing  
**Design:** Minimalist, operator-credible, lots of whitespace  
**Confidentiality:** Anonymous (dealer codes only, no names/PII in public version)

**Sections:**
1. Hero - "Two Days. 40+ Operators. One Pattern."
2. The Room - Who was there (anonymous footprint)
3. What the Room Agreed On - Alignment on topics
4. What Playbooks Cover - Knowledge exists
5. Where Performance Varies - Execution gap
6. Dealer Commitments - Post-meeting priorities
7. Where Execution Breaks - System failures
8. What Group Is Ready For - The opportunity
9. Closing - Attribution

**Target Audience:**
- Greg Joutras (consultant/moderator) - Can forward as "additional context"
- Service managers - See themselves without being exposed
- Dealer principals - Understand the execution gap

**Success Metric:**  
Greg forwards it. Dealers reference it. ServiceSync gets pilot conversations.

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
- OpenAI API key (business account - ask Frazier)
- AWS account (optional, for hosting)

### Supabase Project (Already Set Up ✅)

**Project:** executive-intelligence-brief  
**URL:** https://easyazauclbtxgkxyfbe.supabase.co  
**Dashboard:** https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe

Credentials are in `.env.local` - ask Frazier for the OpenAI API key!

### Supabase Project (Already Set Up)

**Project:** executive-intelligence-brief  
**URL:** https://easyazauclbtxgkxyfbe.supabase.co  
**Project Ref:** easyazauclbtxgkxyfbe  
**Dashboard:** https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe

**Credentials are in `.env.local`** - Do not commit this file!

### Setup Steps

1. **Install dependencies:**
```bash
# Python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Node (for microsite)
cd app && npm install && cd ..
```

2. **Add OpenAI API key to `.env.local`:**
```bash
# Ask Frazier for the business account API key
OPENAI_API_KEY=sk-proj-...
```

3. **Verify Supabase connection:**
```bash
python ingest/ingest_smoke.py
```

4. **Check storage buckets exist:**
   - Go to https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe/storage/buckets
   - Should see: `raw-docs` (private) and `assets` (public)
   - If not, create them in Supabase Studio → Storage

5. **Start processing data:**
```bash
source venv/bin/activate
python ingest/ingest.py --directory data/nada-jan-2026
```

6. **Set up AWS hosting:**
   - See [AWS Amplify Setup Guide](docs/AWS_AMPLIFY_SETUP.md)
   - Or use Vercel: `cd app && vercel deploy`

### Manual Setup

If you prefer manual setup, see [Developer Setup Guide](docs/DEV_SETUP.md).

---

## 📚 Documentation

- **[README.md](README.md)** - Project overview and quick start
- **[STATUS.md](STATUS.md)** - Current progress and next actions
- **[data/nada-jan-2026/DATA_INVENTORY.md](data/nada-jan-2026/DATA_INVENTORY.md)** - File processing priority (45 files to process, 28 duplicates to skip)
- **[docs/PROJECT_GUIDE.md](docs/PROJECT_GUIDE.md)** - Complete phase-by-phase implementation guide
- **[docs/DEV_SETUP.md](docs/DEV_SETUP.md)** - Developer onboarding (30-60 min)
- **[docs/ROADMAP.md](docs/ROADMAP.md)** - Project phases and milestones
- **[docs/WORKFLOWS.md](docs/WORKFLOWS.md)** - CI/CD setup instructions
- **[docs/NOTION_TRACKER.md](docs/NOTION_TRACKER.md)** - Notion project management template
- **[docs/notion-reference/](docs/notion-reference/)** - Original Notion planning docs
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick commands and paths
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project summary

**GitHub Resources:**
- **Issues:** https://github.com/ServiceSync-AI/executive-intelligence-brief/issues
- **Project Board:** https://github.com/orgs/ServiceSync-AI/projects/1
- **Supabase Dashboard:** https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe

---

## 🔄 Workflows

### Current: Phase 2 - Data Ingestion

**Goal:** Process 45 priority files from `data/nada-jan-2026/to-process/`

**Steps:**
1. Set up Supabase storage buckets (Issue #1)
2. Build parsers for PDF, DOCX, images (Issues #2-4)
3. Implement chunking and embeddings (Issues #5-6)
4. Run ingestion pipeline (Issue #7)
5. Validate data (Issue #8)

**See:** [DATA_INVENTORY.md](data/nada-jan-2026/DATA_INVENTORY.md) for file processing order

### Future Workflows

#### 2. Build Knowledge Index
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
