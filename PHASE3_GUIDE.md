# Phase 3: Knowledge Extraction

**Status:** Ready to Start  
**Duration:** ~1 week  
**Dependencies:** Phase 2 Complete ✅

---

## Overview

Phase 3 transforms raw ingested data into structured intelligence:
- Extract canonical topics from 981 chunks
- Map dealer commitments to themes
- Aggregate performance metrics
- Build source traceability

---

## What We Have

✅ **167 files ingested**
- 83 PDFs (meeting docs, dealer processes)
- 40 TXT files (pre-extracted text)
- 26 DOCX files (strategic notes, transcripts)
- 14 CSV files (performance data)
- 4 images (roster, handwritten notes)

✅ **981 chunks with embeddings**
- 715,104 tokens processed
- 1536-dimension vectors for semantic search
- Average 5.9 chunks per file

✅ **Database ready**
- `raw_files` table populated
- `chunks` table with embeddings
- Empty tables ready: `knowledge_topics`, `commitments`, `metrics`

---

## Phase 3 Tasks

### Task 1: Topic Extraction (2-3 days)

**Goal:** Extract 10-15 canonical topics that represent what the industry knows

**Approach:**
1. Sample chunks from database (semantic clustering)
2. Use LLM to identify recurring themes
3. Generate topic definitions
4. Map evidence back to source chunks
5. Store in `knowledge_topics` table

**Script:** `analysis/index_builder.py`

**Output:**
```
Topic: Video MPI Implementation
Definition: Using video multi-point inspections to increase customer trust and RO value
Status: Widely discussed, variable adoption
Evidence: [chunk_ids with quotes]
Confidence: 0.85
```

---

### Task 2: Commitment Extraction (1-2 days)

**Goal:** Extract dealer commitments from "Take A Way's" handwritten notes

**Approach:**
1. OCR already done (ingestion phase)
2. Parse commitment statements
3. Map to 6 themes:
   - AI Phone & Scheduling
   - Video MPI
   - Postponed Service Follow-up
   - Reconditioning Speed
   - Daily Accountability
   - Tech Retention
4. Assign dealer codes
5. Store in `commitments` table

**Script:** `analysis/normalize_commitments.py`

**Output:**
```
Dealer: D01
Theme: Video MPI
Statement: "Implement video MPI in all service bays by Q2"
Evidence: {source: "Take A Way's.pdf", page: 1}
```

---

### Task 3: Metrics Aggregation (1 day)

**Goal:** Aggregate performance metrics from CSV files

**Approach:**
1. Parse CSV files (already ingested)
2. Extract key metrics:
   - Service Absorption (median, range)
   - Hours per RO (Quick Lane vs Main Shop)
   - Tech Proficiency (range)
   - Parts Inventory Turn
   - Service Retention
3. Calculate median, low, high
4. Store in `metrics` table

**Script:** `analysis/metrics_aggregator.py`

**Output:**
```
Metric: Service Absorption
Median: 82%
Low: 65%
High: 95%
Units: percentage
Evidence: [source files]
```

---

### Task 4: Source Traceability (1 day)

**Goal:** Map every insight back to source documents

**Approach:**
1. For each topic, track source chunks
2. For each commitment, track source page
3. For each metric, track source CSV
4. Store in `sources_map` table

**Script:** `analysis/traceability.py`

**Output:**
```
Insight: Topic "Video MPI Implementation"
Sources:
  - GC06 Agenda.pdf (page 3)
  - Hot Topics.pdf (page 1)
  - Emich Chevrolet SOP.pdf (pages 2-4)
  - 15 discussion chunks
```

---

## Deliverables

By end of Phase 3:

✅ **knowledge_topics table**
- 10-15 canonical topics
- Definitions and status
- Evidence mapped to chunks
- Confidence scores

✅ **commitments table**
- ~20-30 dealer commitments
- Mapped to 6 themes
- Dealer codes assigned
- Source traceability

✅ **metrics table**
- ~10-15 key metrics
- Median, low, high values
- Units and context
- Source files tracked

✅ **sources_map table**
- Complete traceability
- Every insight → source documents
- Ready for citation in brief

---

## Success Criteria

- [ ] All topics have evidence from multiple sources
- [ ] All commitments mapped to themes
- [ ] All metrics have valid ranges
- [ ] 100% source traceability
- [ ] Data ready for visualization (Phase 4)

---

## Next Phase Preview

**Phase 4: Visualizations**
- Conversation heatmap (topics × meeting parts)
- Topic gravity map (bubble chart)
- Commitment matrix (themes × dealers)
- Variance panels (performance distributions)
- Execution loop diagram

All visualizations will use Phase 3 extracted data.

---

## Getting Started

1. Review existing analysis scripts in `analysis/` folder
2. Check `analysis/prompts/` for LLM templates
3. Start with topic extraction (highest value)
4. Run validation after each task
5. Update STATUS.md as you progress

**Questions?** See `docs/PROJECT_GUIDE.md` or GitHub Issues.
