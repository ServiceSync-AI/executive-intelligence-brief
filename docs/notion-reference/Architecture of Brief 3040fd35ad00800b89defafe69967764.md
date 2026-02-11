# Architecture of Brief

Owner: Fray

Start with:

> Structured data → patterns → visuals → narrative → site
> 

In that order.

## 🔹 Tool: Notion (Company Knowledge Base)

Use Notion as your **canonical memory layer**. Create databases:

### 1. Meetings Database

- Meeting name
- Date
- Participants
- Raw documents (file links)
- Status (indexed / analyzed / briefed)

### 2. Insights Database

- Insight title
- Category (Execution, Flow, Pricing, Retention, etc.)
- Source meeting
- Supporting documents
- Confidence level
- Status (Observed / Pattern / Validated / Hypothesis)

### 3. Dealer Commitments Database

- Dealer code
- Theme
- Commitment statement
- Follow-up needed
- Next meeting check-in

### 4. Metrics / Signals Database

- Metric name
- Range observed
- Source
- Update timestamp

This gives you:

> A living knowledge graph without building software.
> 

# LAYER 2 — ANALYSIS & VISUALIZATION

## 🔹 Primary Tool: Python (Jupyter or VS Code)

- Parse documents
- Create structured datasets
- Generate:
    - Topic frequencies
    - Commitment matrices
    - Theme clustering
    - Variance visualizations

Libraries:

- pandas
- matplotlib
- seaborn (for internal use)
- plotly (for web-ready charts)
- altair (great for clean declarative visuals)

This gives:

- Reproducible analysis
- Easy updates when new data comes in
- Actual audit trail

## 🔹 Visual Design Layer: Figma

Use Figma only for:

- Layout
- Typography
- Component system
- Polished visual hierarchy

Charts should ideally be:

- Exported as SVG from Python
- Or recreated cleanly in Figma from structured data

Avoid:

- Designing charts manually
- “Eyeballing” numbers

# LAYER 3 — MICROSITE BUILD

## Framer

Why:

- Fast
- Clean
- Can embed interactive charts
- No heavy engineering overhead
- Easy export

Can:

- Import SVG charts
- Embed Plotly charts
- Use your Figma layouts as reference

Best for:

- Executive-facing artifacts
- Speed

# CONTINUOUS FLOW SYSTEM (MOST IMPORTANT PART)

How to prevent this from becoming a one-off.

## The Update Workflow

### Step 1 — New Meeting Files Arrive

Intern:

- Uploads to Notion Meeting entry
- Adds raw files to structured folder

### Step 2 — Run Analysis Notebook

Python script:

- Recalculate:
    - Topic clusters
    - Commitment matrix
    - Metric ranges
- Output updated JSON + charts

### Step 3 — Sync to Knowledge DB

- Update Insights database
- Mark new patterns
- Flag deltas since last meeting

### Step 4 — Regenerate Brief

- Replace charts
- Update narrative
- Publish new version

No rethinking.

No re-design.

Just updates.

# TOOL STACK SUMMARY (RECOMMENDED)

| Layer | Tool |
| --- | --- |
| Knowledge | Notion |
| Raw Data | Google Drive or GitHub |
| Analysis | Python (VS Code / Jupyter) |
| Charts | Plotly / Altair |
| Design System | Figma |
| Microsite | Framer (initially) |