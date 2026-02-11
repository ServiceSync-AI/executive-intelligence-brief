# NADA Jan 2026 Data Inventory

**Total Files:** 73  
**Last Updated:** 2026-02-11

---

## Processing Priority

### Priority 1: Primary Sources (Process These)
These are the canonical files to ingest - no duplicates.

#### Meeting Documents
- `GC06 2026 01 Agenda.pdf` - Main meeting agenda
- `FW NADA 20 Group Meeting Agenda  GC06 January 1113 Atlanta.pdf` - Email with agenda
- `🧩 NADA 20 Group – Jan 2026 Service Mger Meeting.docx` - Meeting notes (use DOCX, skip TXT)
- `Fireflies AI NADA Meeting Transcript Summaries.docx` - AI transcripts (use DOCX, skip TXT)
- `Notes from GC06 January meeting.docx` - Additional notes (use DOCX, skip TXT)
- `GPT NADA Service & Parts Leadership Meeting Minutes.docx` - GPT summary (use DOCX, skip TXT)

#### Strategic Documents
- `GPT Married - Fireflies + Personal notes.docx` - Combined analysis
- `GPT Married Internal.docx` - Internal analysis
- `GPT NADA Meeting - Strategic Direction For SS_.docx` - ServiceSync strategy
- `GPT ServiceSync – Internal Product & Strategy Notes.docx` - Product notes

#### Hot Topics
- `Hot Topics - NADA January Service managers.pdf` - Main hot topics
- `Hot Topics.pdf` - Hot topics (use PDF, skip TXT)

#### Dealer-Specific Documents (PDFs only)
- `A Smarter Way to Attract and Retain Technicians.pdf`
- `Emich Chevrolet Menu + SOP process + initiatives implemented to increase sales-gross.pdf`
- `New service advisor, orientation, and training.pdf`
- `Pine belt Chevrolet process and hangcards.pdf`
- `Service advisor, best practices, checklist.pdf`
- `Turn Bottlenecks Into Opportunities.pdf`
- `greg email.pdf`

#### Dealer Processes (Use TXT for easier parsing)
- `Chevyland service GM Twenty group in ADA meeting packet service performance overview [TEXT].txt`
- `Mohawk Chevrolet SOR Process [TEXT].txt`
- `New Service Advisor Orientation Tool 080624 [TEXT].txt`
- `Parkway Chevrolet GM ordering process [TEXT].txt`
- `Puklich Chevrolet agreement for repayment of loan [TEXT].txt`
- `Riverton Chevrolet parts special order process [TEXT].txt`
- `Sales to Service Handoff Scrip GM [TEXT].txt`
- `Service Advisor Best Practices Check List [TEXT].txt`
- `Sharing your GBP with Vistadash_Detail Instructions [TEXT].txt`
- `Steps to increase hours per RO [TEXT].txt`
- `Take A Way's [TEXT].txt` - **IMPORTANT: Handwritten commitments**
- `Top Ten Reasons to Service at Dealership 110225 [TEXT].txt`

#### Performance Data (Use CSV for structured data)
- `Absorption for service and parts [DATA].csv`
- `November Proficiceny numbers [DATA].csv`
- `Ourisman Chevrolet Service Summary Trends [DATA].csv`
- `Ourisman Chevrolet strategic growth and operational realignment statement [DATA].csv`
- `PAM AI - Parkway Chevrolet [DATA].csv`
- `Parts inventory $ turn [DATA].csv`
- `Used vehicle days to breakeven after recon [DATA].csv`
- `GC06_Fixed_1125.xlsx` - Excel data

#### Images
- `NADA Group Roster.png` - Roster image (needs OCR)

#### Generated Indexes
- `KNOWLEDGE_INDEX.md` - Pre-built knowledge index
- `SOURCE_TRACEABILITY.md` - Source mapping
- `README.md` - Data folder readme

---

## Priority 2: Skip These (Duplicates)

### TXT versions (when DOCX exists)
- `🧩 NADA 20 Group – Jan 2026 Service Mger Meeting [TEXT].txt` ❌ Use DOCX
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` ❌ Use DOCX
- `GPT NADA Service & Parts Leadership Meeting Minutes [TEXT].txt` ❌ Use DOCX
- `Notes from GC06 January meeting [TEXT].txt` ❌ Use DOCX

### PDF versions (when TXT exists)
- `Chevyland service GM Twenty group in ADA meeting packet service performance overview.pdf` ❌ Use TXT
- `Mohawk Chevrolet SOR Process.pdf` ❌ Use TXT
- `Parkway Chevrolet GM ordering process.pdf` ❌ Use TXT
- `Puklich Chevrolet agreement for repayment of loan.pdf` ❌ Use TXT
- `Riverton Chevrolet parts special order process.pdf` ❌ Use TXT
- `Steps to increase hours per RO.pdf` ❌ Use TXT
- `Take A Way's.pdf` ❌ Use TXT

### PDF versions (when CSV exists)
- `Absorption for service and parts.pdf` ❌ Use CSV
- `November Proficiceny numbers.pdf` ❌ Use CSV
- `Ourisman Chevrolet strategic growth and operational realignment statement.pdf` ❌ Use CSV
- `PAM AI - Parkway Chevrolet.pdf` ❌ Use CSV
- `Parts inventory $ turn.pdf` ❌ Use CSV
- `Used vehicle days to breakeven after recon.pdf` ❌ Use CSV
- `GC06_Fixed_1125 [PDF].pdf` ❌ Use XLSX

### Extra TXT versions (when CSV exists)
- `Ourisman Chevrolet strategic growth and operational realignment statement [TEXT].txt` ❌ Use CSV
- `PAM AI - Parkway Chevrolet [TEXT].txt` ❌ Use CSV

---

## File Count Summary

**To Process:** 45 files
- 13 DOCX files
- 15 TXT files
- 7 CSV files
- 1 XLSX file
- 8 PDF files (unique)
- 1 PNG file

**To Skip:** 28 duplicate files

---

## Processing Order

### Phase 1: Text Documents (Meeting Context)
1. Meeting agendas and notes (6 DOCX + 2 PDF)
2. Strategic documents (4 DOCX)
3. Hot topics (2 PDF)

### Phase 2: Dealer Processes (Best Practices)
4. Dealer-specific TXT files (12 files)
5. Unique PDF processes (8 files)

### Phase 3: Performance Data (Metrics)
6. CSV files (7 files)
7. Excel file (1 file)

### Phase 4: Images (OCR)
8. Roster image (1 PNG)

### Phase 5: Generated Indexes
9. Knowledge index and traceability (3 MD files)

---

## Special Handling

### High Priority
- **Take A Way's [TEXT].txt** - Contains handwritten dealer commitments (needs manual QA)
- **NADA Group Roster.png** - Needs OCR for dealer list
- **GC06_Fixed_1125.xlsx** - Performance data spreadsheet

### Data Quality Notes
- TXT files are pre-extracted for easier parsing
- CSV files contain structured metrics
- Some PDFs may have embedded images/charts
- Handwritten notes require OCR validation

---

## Next Steps

1. Create `data/nada-jan-2026/to-process/` folder
2. Symlink or copy 45 priority files
3. Update ingestion script to use this list
4. Process in order above
