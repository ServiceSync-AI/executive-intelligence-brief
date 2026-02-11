#!/bin/bash
# Organize priority files for processing

BASE_DIR="/Users/frazierhorn/Development/GitHubRepos/Professional/executive-intelligence-brief/data/nada-jan-2026"
PROCESS_DIR="$BASE_DIR/to-process"

# Meeting Documents
ln -sf "$BASE_DIR/GC06 2026 01 Agenda.pdf" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/FW NADA 20 Group Meeting Agenda  GC06 January 1113 Atlanta.pdf" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/🧩 NADA 20 Group – Jan 2026 Service Mger Meeting.docx" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/Fireflies AI NADA Meeting Transcript Summaries.docx" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/Notes from GC06 January meeting.docx" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/GPT NADA Service & Parts Leadership Meeting Minutes.docx" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/GPT Married - Fireflies + Personal notes.docx" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/GPT Married Internal.docx" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/GPT NADA Meeting - Strategic Direction For SS_.docx" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/GPT ServiceSync – Internal Product & Strategy Notes.docx" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/Hot Topics - NADA January Service managers.pdf" "$PROCESS_DIR/meeting-docs/"
ln -sf "$BASE_DIR/Hot Topics.pdf" "$PROCESS_DIR/meeting-docs/"

# Dealer Processes (TXT)
ln -sf "$BASE_DIR/Chevyland service GM Twenty group in ADA meeting packet service performance overview [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Mohawk Chevrolet SOR Process [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/New Service Advisor Orientation Tool 080624 [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Parkway Chevrolet GM ordering process [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Puklich Chevrolet agreement for repayment of loan [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Riverton Chevrolet parts special order process [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Sales to Service Handoff Scrip GM [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Service Advisor Best Practices Check List [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Sharing your GBP with Vistadash_Detail Instructions [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Steps to increase hours per RO [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Take A Way's [TEXT].txt" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Top Ten Reasons to Service at Dealership 110225 [TEXT].txt" "$PROCESS_DIR/dealer-processes/"

# Dealer Processes (PDF - unique)
ln -sf "$BASE_DIR/A Smarter Way to Attract and Retain Technicians.pdf" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Emich Chevrolet Menu + SOP process + initiatives implemented to increase sales-gross.pdf" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/New service advisor, orientation, and training.pdf" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Pine belt Chevrolet process and hangcards.pdf" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Service advisor, best practices, checklist.pdf" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/Turn Bottlenecks Into Opportunities.pdf" "$PROCESS_DIR/dealer-processes/"
ln -sf "$BASE_DIR/greg email.pdf" "$PROCESS_DIR/dealer-processes/"

# Performance Data
ln -sf "$BASE_DIR/Absorption for service and parts [DATA].csv" "$PROCESS_DIR/performance-data/"
ln -sf "$BASE_DIR/November Proficiceny numbers [DATA].csv" "$PROCESS_DIR/performance-data/"
ln -sf "$BASE_DIR/Ourisman Chevrolet Service Summary Trends [DATA].csv" "$PROCESS_DIR/performance-data/"
ln -sf "$BASE_DIR/Ourisman Chevrolet strategic growth and operational realignment statement [DATA].csv" "$PROCESS_DIR/performance-data/"
ln -sf "$BASE_DIR/PAM AI - Parkway Chevrolet [DATA].csv" "$PROCESS_DIR/performance-data/"
ln -sf "$BASE_DIR/Parts inventory $ turn [DATA].csv" "$PROCESS_DIR/performance-data/"
ln -sf "$BASE_DIR/Used vehicle days to breakeven after recon [DATA].csv" "$PROCESS_DIR/performance-data/"
ln -sf "$BASE_DIR/GC06_Fixed_1125.xlsx" "$PROCESS_DIR/performance-data/"

# Images
ln -sf "$BASE_DIR/NADA Group Roster.png" "$PROCESS_DIR/images/"

# Indexes
ln -sf "$BASE_DIR/KNOWLEDGE_INDEX.md" "$PROCESS_DIR/indexes/"
ln -sf "$BASE_DIR/SOURCE_TRACEABILITY.md" "$PROCESS_DIR/indexes/"
ln -sf "$BASE_DIR/README.md" "$PROCESS_DIR/indexes/"

echo "✅ Organized 45 priority files into to-process/"
echo "📁 Structure:"
echo "   - meeting-docs: 12 files"
echo "   - dealer-processes: 19 files"
echo "   - performance-data: 8 files"
echo "   - images: 1 file"
echo "   - indexes: 3 files"
