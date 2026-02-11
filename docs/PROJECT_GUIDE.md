# Project Guide - Executive Intelligence Brief

**Complete step-by-step guide from setup to deployment**

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Phase 1: Setup (Complete)](#phase-1-setup)
3. [Phase 2: Ingestion Pipeline](#phase-2-ingestion-pipeline)
4. [Phase 3: Knowledge Extraction](#phase-3-knowledge-extraction)
5. [Phase 4: Visualizations](#phase-4-visualizations)
6. [Phase 5: Microsite](#phase-5-microsite)
7. [Phase 6: Deployment](#phase-6-deployment)
8. [Reference Documentation](#reference-documentation)

---

## Project Overview

**Goal:** Transform 72 NADA meeting documents into an operator-grade Executive Intelligence Brief microsite.

**Deliverable:** Single-page interactive website showing:
- Conversation heatmap (topics × time)
- Dealer commitment matrix (themes × dealers)
- Knowledge topics with evidence
- Performance variance analysis
- Execution gap insights

**Timeline:** 6-8 weeks (6 phases)

---

## Phase 1: Setup ✅ COMPLETE

**Status:** Done  
**Duration:** 1 day  
**Owner:** Frazier

### Completed:
- ✅ GitHub repository created
- ✅ Project structure established
- ✅ Documentation written
- ✅ Database schema defined
- ✅ All 72 NADA files committed
- ✅ Team can clone and start

### Next Action:
→ Move to Phase 2

---

## Phase 2: Ingestion Pipeline

**Status:** Ready to start  
**Duration:** 1-2 weeks  
**Owner:** Developer/Intern

### Goal:
Process all 72 NADA files into structured data in Supabase.

### Tasks:

#### 2.1 Supabase Setup (Day 1)
```bash
# Create Supabase project
# → https://app.supabase.io

# Apply schema
supabase login
supabase link --project-ref YOUR_REF
supabase db push

# Create storage buckets:
# - raw-docs (private)
# - assets (public)
```

**Deliverable:** Supabase project with schema applied

---

#### 2.2 PDF Parser (Days 2-3)
**File:** `ingest/parsers/pdf_parser.py`

```python
# Implement:
- Extract text from PDFs using pdfplumber
- Handle multi-page documents
- Preserve metadata (filename, page numbers)
- Return structured text
```

**Test with:** `data/nada-jan-2026/Meeting Handouts/GC06 2026 01 Agenda.pdf`

**Deliverable:** Working PDF parser

---

#### 2.3 DOCX Parser (Day 4)
**File:** `ingest/parsers/docx_parser.py`

```python
# Implement:
- Extract text from DOCX using python-docx
- Preserve headings and structure
- Handle tables
- Return structured text
```

**Test with:** `data/nada-jan-2026/Meeting Notes and Summaries/*.docx`

**Deliverable:** Working DOCX parser

---

#### 2.4 Image OCR (Day 5)
**File:** `ingest/parsers/image_parser.py`

```python
# Implement:
- OCR using pytesseract
- Handle handwritten notes
- Clean up OCR artifacts
- Return text
```

**Test with:** `data/nada-jan-2026/NADA Group Roster.png`

**Deliverable:** Working OCR parser

---

#### 2.5 Text Chunking (Day 6)
**File:** `ingest/chunker.py`

```python
# Implement:
- Split text into 800-token chunks
- 200-token overlap between chunks
- Preserve context
- Track chunk metadata (file, position)
```

**Deliverable:** Chunking logic

---

#### 2.6 Embeddings Generation (Day 7)
**File:** `ingest/embedder.py`

```python
# Implement:
- Call OpenAI embeddings API
- Batch processing (avoid rate limits)
- Store vectors in Supabase
- Handle errors gracefully
```

**Deliverable:** Embedding generation

---

#### 2.7 Main Ingestion Script (Days 8-9)
**File:** `ingest/ingest.py`

```python
# Implement:
- Process directory of files
- Route to correct parser (PDF/DOCX/image)
- Chunk text
- Generate embeddings
- Store in Supabase (raw_files, chunks, chunk_vectors)
- Track processing status
```

**Run:**
```bash
python ingest/ingest.py --directory data/nada-jan-2026
```

**Deliverable:** All 72 files processed and in Supabase

---

#### 2.8 Validation (Day 10)
```bash
# Check Supabase tables:
# - raw_files: 72 rows
# - chunks: ~500-1000 rows
# - chunk_vectors: same as chunks
```

**Deliverable:** Verified data in Supabase

---

## Phase 3: Knowledge Extraction

**Status:** Waiting on Phase 2  
**Duration:** 1 week  
**Owner:** Developer/Intern

### Goal:
Extract canonical topics, dealer commitments, and metrics from processed data.

### Tasks:

#### 3.1 Topic Extraction (Days 1-2)
**File:** `analysis/index_builder.py`

```python
# Implement:
- Query representative chunks from Supabase
- Use LLM to extract 10-15 canonical topics
- Map evidence to source files/chunks
- Store in knowledge_topics table
```

**Prompt template:** `analysis/prompts/topic_extraction.txt`

**Run:**
```bash
python analysis/index_builder.py --sample 200
```

**Deliverable:** knowledge_topics table populated

---

#### 3.2 Commitment Extraction (Days 3-4)
**File:** `analysis/normalize_commitments.py`

```python
# Implement:
- OCR "Take A Way's" PDF
- Parse dealer codes and statements
- Map to 6 canonical themes:
  1. Hours per RO & Throughput
  2. Video MPI & Inspections
  3. Dispatch & Flow Control
  4. Onboarding & Training
  5. Sales → Service Handoff
  6. AI & Automation
- Manual QA for ambiguous mappings
- Store in commitments table
```

**Run:**
```bash
python analysis/normalize_commitments.py \
  --images data/nada-jan-2026/Meeting\ Follow\ Up\ Email\ Attachments/Take\ A\ Way\'s.pdf \
  --review
```

**Deliverable:** commitments table populated

---

#### 3.3 Metrics Aggregation (Day 5)
**File:** `analysis/metrics_aggregator.py`

```python
# Implement:
- Extract numeric data from CSVs
- Calculate ranges, medians
- Anonymize (no dealer names)
- Store in metrics table
```

**Process:**
- Proficiency numbers
- Absorption rates
- Parts inventory turn
- Recon days

**Deliverable:** metrics table populated

---

#### 3.4 Source Traceability (Day 6)
**File:** `analysis/traceability.py`

```python
# Implement:
- Map each topic to source files
- Map each commitment to evidence
- Populate sources_map table
```

**Deliverable:** Complete traceability

---

#### 3.5 Validation (Day 7)
```bash
# Check Supabase:
# - knowledge_topics: 10-15 rows
# - commitments: ~20-30 rows
# - metrics: ~10-15 rows
# - sources_map: complete
```

**Deliverable:** Verified knowledge extraction

---

## Phase 4: Visualizations

**Status:** Waiting on Phase 3  
**Duration:** 1 week  
**Owner:** Developer

### Goal:
Generate all charts and visualizations for the microsite.

### Tasks:

#### 4.1 Conversation Heatmap (Days 1-2)
**File:** `analysis/charts/heatmap.py`

**Visual:** Topics (x-axis) × Meeting Parts (y-axis), color = discussion density

**Reference:** `docs/notion-reference/gpt heatmap caption*.md`

**Output:** SVG or interactive Plotly chart

---

#### 4.2 Topic Gravity Map (Day 3)
**File:** `analysis/charts/topic_gravity.py`

**Visual:** Bubble chart, size = frequency

**Output:** SVG

---

#### 4.3 Commitment Matrix (Day 4)
**File:** `analysis/charts/commitment_matrix.py`

**Visual:** Themes (rows) × Dealer codes (columns), filled cells = commitments

**Output:** SVG or interactive

---

#### 4.4 Variance Panels (Day 5)
**File:** `analysis/charts/variance_panels.py`

**Visual:** Small multiples showing performance distributions

**Output:** SVG

---

#### 4.5 Execution Loop Diagram (Day 6)
**File:** `analysis/charts/execution_loop.py`

**Visual:** Decision → Owner → Action → Measurement → Follow-up (with breakpoints)

**Output:** SVG

---

#### 4.6 Chart Upload (Day 7)
```bash
python analysis/charts_generator.py --upload
```

**Deliverable:** All charts in Supabase assets bucket

---

## Phase 5: Microsite

**Status:** Waiting on Phase 4  
**Duration:** 2 weeks  
**Owner:** Developer

### Goal:
Build the single-page Executive Intelligence Brief website.

### Reference:
- **Storyboard:** `docs/notion-reference/Microsite storyboard*.md`
- **Design:** Minimalist, operator-credible, no marketing fluff

### Tasks:

#### 5.1 Next.js Setup (Day 1)
```bash
cd app
npm install
```

**Configure:**
- TypeScript
- TailwindCSS
- Supabase client

---

#### 5.2 Component Library (Days 2-3)
**Files:** `app/components/`

Create:
- `Hero.tsx` - Title and metadata
- `Section.tsx` - Reusable section wrapper
- `Chart.tsx` - Chart display component
- `TopicCard.tsx` - Topic display
- `CommitmentMatrix.tsx` - Matrix visualization

---

#### 5.3 Page Sections (Days 4-10)
**File:** `app/page.tsx`

Implement sections per storyboard:
1. Hero - "Two Days. 40+ Operators. One Pattern."
2. The Room - Dealer footprint (anonymous)
3. What the Room Agreed On - Topic alignment
4. What Playbooks Cover - Knowledge isn't the constraint
5. Where Performance Varies - Variance panels
6. Dealer Commitments - Commitment matrix
7. Where Execution Breaks - Execution loop diagram
8. What Group Is Ready For - Continuity insight
9. Closing - Attribution

---

#### 5.4 Supabase Integration (Days 11-12)
**File:** `app/lib/supabase.ts`

Implement:
- Fetch knowledge_topics
- Fetch commitments
- Fetch metrics
- Fetch chart URLs
- Use sanitized views (no PII)

---

#### 5.5 Responsive Design (Day 13)
- Desktop first
- Mobile support
- Tablet optimization

---

#### 5.6 Testing (Day 14)
- Cross-browser testing
- Performance optimization
- Accessibility check

**Deliverable:** Working microsite locally

---

## Phase 6: Deployment

**Status:** Waiting on Phase 5  
**Duration:** 3 days  
**Owner:** Developer

### Tasks:

#### 6.1 Vercel Setup (Day 1)
```bash
cd app
vercel login
vercel deploy
```

**Configure:**
- Environment variables
- Domain (if custom)

---

#### 6.2 CI/CD (Day 2)
**File:** `.github/workflows/deploy.yml`

Implement:
- Auto-deploy on push to main
- Run tests before deploy

---

#### 6.3 Final QA (Day 3)
- Security audit
- Performance testing
- Stakeholder review

**Deliverable:** Live microsite

---

## Reference Documentation

All planning docs from Notion are in `docs/notion-reference/`:

- **AI Project Prompt** - Original build instructions
- **Architecture of Brief** - System design
- **Microsite Storyboard** - Page layout and sections
- **Supabase Documentation** - Database setup
- **Github README** - Repository structure
- **Developer Guide** - Onboarding

---

## Quick Commands

```bash
# Navigate to project
cd /Users/frazierhorn/Development/GitHubRepos/Professional/executive-intelligence-brief

# Phase 2: Ingestion
python ingest/ingest.py --directory data/nada-jan-2026

# Phase 3: Knowledge
python analysis/index_builder.py --sample 200
python analysis/normalize_commitments.py --images data/nada-jan-2026/Meeting\ Follow\ Up\ Email\ Attachments/Take\ A\ Way\'s.pdf --review

# Phase 4: Charts
python analysis/charts_generator.py --upload

# Phase 5: Microsite
cd app && npm run dev

# Phase 6: Deploy
cd app && vercel deploy
```

---

## Current Status

✅ **Phase 1: Setup** - COMPLETE  
⏳ **Phase 2: Ingestion** - Ready to start  
⏳ **Phase 3: Knowledge** - Waiting  
⏳ **Phase 4: Visualizations** - Waiting  
⏳ **Phase 5: Microsite** - Waiting  
⏳ **Phase 6: Deployment** - Waiting

---

## Next Action

**Start Phase 2:** Implement ingestion pipeline

**First Task:** Set up Supabase project and apply schema

**Estimated Time:** 1-2 weeks for complete ingestion

---

**Questions?** See `docs/DEV_SETUP.md` or contact Frazier Horn
