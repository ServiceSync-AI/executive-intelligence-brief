# Operational Friction Index — Full Breakdown
**Project:** ServiceSync AI — Car Dealership Service Analytics  
**Analyst:** Service Data Analytics  
**Data Source:** NADA 20 Group Meeting, January 2026 (Atlanta, GA)  
**Scoring:** 0–100 | Higher = Less Friction  

---

## Scoring Rubric

Each metric is scored across 4 dimensions (0–25 each):

| Dimension | Question |
|---|---|
| Visibility (Vis) | Is data being captured? |
| Ownership (Own) | Is someone accountable? |
| Measurement (Meas) | Are targets/benchmarks defined? |
| Actionability (Act) | Are documented steps/tools available? |

**Score per dimension:**
- 0 = Not present
- 10 = Mentioned informally / anecdotal
- 20 = Documented but inconsistent
- 25 = Fully implemented and consistent

### Visibility (0–25)
Is this metric being captured anywhere?

| Score | Criteria |
|---|---|
| 0 | Not tracked, only mentioned as a pain point |
| 10 | Mentioned in meeting notes/transcripts only |
| 20 | Exists in a CSV/spreadsheet but inconsistently |
| 25 | Structured data file with multi-dealer, multi-period data |

---

### Ownership (0–25)
Does a named person or role have accountability for it?

| Score | Criteria |
|---|---|
| 0 | No one owns it |
| 10 | Discussed in meeting but no assignment |
| 20 | Named in Take A Way's (dealer committed to it) |
| 25 | Named owner + documented process/role |

---

### Measurement (0–25)
Is there a target, benchmark, or comparison point?

| Score | Criteria |
|---|---|
| 0 | No numbers exist |
| 10 | Anecdotal numbers mentioned in conversation |
| 20 | Group average or range exists, no clear target |
| 25 | Defined target with group benchmark to compare against |

---

### Actionability (0–25)
Are there documented steps, tools, or processes to improve it?

| Score | Criteria |
|---|---|
| 0 | No action path exists |
| 10 | General idea discussed in meeting |
| 20 | Tool or process exists but adoption is inconsistent |
| 25 | Step-by-step process documented + multiple dealers implementing |

---

---

## Full Index Summary

| Metric | Vis | Own | Meas | Act | Score | Status |
|---|---|---|---|---|---|---|
| Technician Proficiency | 25 | 20 | 25 | 20 | **90** | ✅ Low Friction |
| Labor Rate | 20 | 25 | 20 | 25 | **90** | ✅ Low Friction |
| Stall Discipline / Tech Utilization | 20 | 25 | 20 | 25 | **90** | ✅ Low Friction |
| Hours per RO | 20 | 20 | 20 | 25 | **85** | ✅ Low Friction |
| Call Handling / Response Time | 20 | 20 | 20 | 20 | **80** | ✅ Low Friction |
| Service Advisor Training / Onboarding | 20 | 20 | 10 | 25 | **75** | ✅ Low Friction |
| Service Absorption | 25 | 10 | 25 | 10 | **70** | ✅ Low Friction |
| Parts Inventory Turn | 25 | 10 | 20 | 10 | **65** | ⚠️ Moderate |
| Reconditioning Time | 20 | 10 | 25 | 10 | **65** | ⚠️ Moderate |
| Personnel Expense % | 25 | 10 | 20 | 10 | **65** | ⚠️ Moderate |
| Lost Sales Tracking | 10 | 10 | 10 | 20 | **50** | ⚠️ Moderate |
| Appointment Scheduling | 10 | 10 | 10 | 20 | **50** | ⚠️ Moderate |
| Postponed / Declined Repairs | 10 | 10 | 10 | 10 | **40** | 🔶 High Friction |
| Video MPI Adoption | 10 | 10 | 0 | 10 | **30** | 🔴 Critical Gap |
| Service Retention | 10 | 0 | 10 | 10 | **30** | 🔴 Critical Gap |

---

## Detailed Breakdown by Metric

---

### 1. Technician Proficiency — 90/100

**Where found:**
- `November Proficiceny numbers [DATA].csv`
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt`
- `KNOWLEDGE_INDEX.md`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 25 | Full CSV with every dealer's proficiency % (76%–169%), multi-dealer structured data |
| Ownership | 20 | Shop foreman explicitly owns stall allocation; Josh and Alex named in transcripts as managing it daily |
| Measurement | 25 | Clear range (76–169%), peak of 159% in December documented, group benchmarks exist |
| Actionability | 20 | Stall discipline process is documented and working, but cultural adoption varies — Meeting 4 notes say some dealers still struggle |

**Note:** Not 25 on actionability because the transcript explicitly flags technician resistance and inconsistent adoption across dealers.

---

### 2. Labor Rate — 90/100

**Where found:**
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` (Meeting 3 notes)
- `KNOWLEDGE_INDEX.md`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 20 | Referenced in transcripts with specific numbers ($160→$225), but no group-wide CSV |
| Ownership | 25 | Service manager directly owns this — multiple named dealers committed and already raised rates |
| Measurement | 20 | Specific dollar examples given, but no group benchmark table comparing all dealers |
| Actionability | 25 | The action is literally "raise the rate" — simplest lever, multiple dealers already did it and documented the gross profit impact |

---

### 3. Stall Discipline / Tech Utilization — 90/100

**Where found:**
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` (Meeting 4)
- `Steps to increase hours per RO [TEXT].txt`
- `KNOWLEDGE_INDEX.md`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 20 | Daily power sheets and scoreboards mentioned; tracked daily but no standalone CSV |
| Ownership | 25 | Shop foreman explicitly named as owner — Josh's approach documented in detail in transcripts |
| Measurement | 20 | Tied directly to proficiency %, daily tracking mentioned, but no separate stall utilization metric |
| Actionability | 25 | Clear documented process: allocate stalls by output, remove stalls from underperformers, daily huddles — multiple dealers confirmed it works |

---

### 4. Hours per RO — 85/100

**Where found:**
- `Steps to increase hours per RO [TEXT].txt`
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt`
- `Take A Way's [TEXT].txt`
- `KNOWLEDGE_INDEX.md`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 20 | Quick lane 1.6 hrs/RO and main shop 3.2 hrs/RO documented, but no group-wide CSV tracking it per dealer |
| Ownership | 20 | Colleen (Dealer 28) and Laurie (Dealer 26) named in Take A Way's as committed owners |
| Measurement | 20 | Benchmarks exist (1.6 vs 3.2), but no hard group target like "every dealer must hit X" |
| Actionability | 25 | Only metric with a full 7-step documented process in its own dedicated file |

**Note:** Not 25 on visibility because there's no CSV with every dealer's hrs/RO — only two reference points.

---

### 5. Call Handling / Response Time — 80/100

**Where found:**
- `PAM AI - Parkway Chevrolet [DATA].csv`
- `PAM AI - Parkway Chevrolet [TEXT].txt`
- `Hot Topics [TEXT].txt` (#01 Respond To Calls)
- `KNOWLEDGE_INDEX.md`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 20 | PAM AI CSV has 7,892 calls tracked with booking rate, handle rate, resolution rate — but only one dealer (Parkway) |
| Ownership | 20 | Named advisors (Kevin Brumley, Jordan) in the CSV; BDC ownership mentioned for others |
| Measurement | 20 | Booking rate 69.42%, handle rate 66.74%, resolution 97% — strong benchmarks for Parkway only |
| Actionability | 20 | AI tools exist (PAM, Matador, Toma) and one dealer implemented — but group-wide adoption is inconsistent |

**Note:** Capped at 20 across the board because this is a single-dealer case study, not group-wide data.

---

### 6. Service Advisor Training / Onboarding — 75/100

**Where found:**
- `New Service Advisor Orientation Tool 080624 [TEXT].txt`
- `Service Advisor Best Practices Check List [TEXT].txt`
- `Sales to Service Handoff Scrip GM [TEXT].txt`
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` (Meeting 3)

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 20 | Three dedicated documents exist covering orientation, best practices, and handoff scripts |
| Ownership | 20 | Named in action items (Brandy, Mike, Colleen) in transcripts; structured onboarding being embedded |
| Measurement | 10 | No pass/fail metric, no completion tracking, no score for advisor readiness |
| Actionability | 25 | Most complete process documentation in the dataset — orientation tool, checklist, and script all exist |

**Note:** Measurement is the weak link — there's no way to know if advisors are actually completing or passing training.

---

### 7. Service Absorption — 70/100

**Where found:**
- `Absorption for service and parts [DATA].csv`
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` (Meeting 1)
- `KNOWLEDGE_INDEX.md`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 25 | Full CSV with all dealers, today vs yesterday comparison, group-wide data |
| Ownership | 10 | Discussed broadly in meeting but no single named owner per dealer — it's a GM/principal-level metric |
| Measurement | 25 | Target 70–90% documented, group average 42–76%, top performer 169% — very clear benchmarks |
| Actionability | 10 | Capacity expansion and team management discussed, but no step-by-step process like hrs/RO has |

**Note:** Strong data, weak execution path. The meeting talked about what absorption is, not how to systematically improve it.

---

### 8. Parts Inventory Turn — 65/100

**Where found:**
- `Parts inventory $ turn [DATA].csv`
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt`
- `KNOWLEDGE_INDEX.md`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 25 | Full CSV with all dealers (16%–60% range), structured data |
| Ownership | 10 | Tara (Dealer 26) owns bin counts in Take A Way's, but most dealers have no named owner |
| Measurement | 20 | Range 16–60% documented, optimal 40–60% referenced — but no hard group target |
| Actionability | 10 | Discussed in meeting but no documented improvement process found in any file |

**Note:** Classic "we have the data but nobody's doing anything with it" situation.

---

### 9. Reconditioning Time — 65/100

**Where found:**
- `Used vehicle days to breakeven after recon [DATA].csv`
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` (Meeting 5)
- `KNOWLEDGE_INDEX.md`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 20 | CSV exists with recon days and days-to-breakeven per dealer, but many entries are blank |
| Ownership | 10 | "Trust between service and used car teams" mentioned — no named individual owner |
| Measurement | 25 | 3-day target is explicit, days-to-breakeven calculated (3–33 days range), clearest target in the dataset |
| Actionability | 10 | Trust-building discussed in Meeting 5, but no formal SOP or process document found |

**Note:** The target is crystal clear (3 days) but the path to get there is "build trust" — which is not actionable.

---

### 10. Personnel Expense % — 65/100

**Where found:**
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` (Meeting 2)
- `Ourisman Chevrolet Service Summary Trends [DATA].csv`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 25 | Page 31 group composite data reviewed in meeting, full range 37–70% visible |
| Ownership | 10 | GM/dealer principal level — service manager has limited control over this |
| Measurement | 20 | Range 37–70%, target ~35% absorption referenced, but no hard per-dealer target |
| Actionability | 10 | Meeting conclusion was essentially "monitor it and question anomalies" — no action steps |

**Note:** This metric is visible but largely outside a service manager's control, which tanks ownership and actionability.

---

### 11. Lost Sales Tracking — 50/100

**Where found:**
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` (Meeting 4 — "Inventory Tracking: Regular checks on lost sales")

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 10 | Only mentioned in one meeting summary bullet — no dedicated CSV or tracking file |
| Ownership | 10 | Referenced but no named owner in any document |
| Measurement | 10 | No numbers, no targets, no lost sales rate tracked anywhere |
| Actionability | 20 | CDK and Reynolds DMS systems mentioned as capable of tracking this — tools exist, just not being used |

**Note:** Boss's example baseline (42). The 8-point gap vs his score is the actionability credit for DMS tools. Drop actionability to 10 if tools aren't actively configured.

---

### 12. Appointment Scheduling — 50/100

**Where found:**
- `Hot Topics [TEXT].txt` (#05 and #06 — listed twice, showing high pain)
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` (Meeting 5 — mobile scheduling, 2-minute abandonment stat)
- `PAM AI - Parkway Chevrolet [TEXT].txt`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 10 | Hot topic twice but no scheduling fill rate, lead time, or no-show rate CSV |
| Ownership | 10 | BDC mentioned but "centralized but ineffective" per knowledge index |
| Measurement | 10 | No scheduling metrics tracked — only anecdotal "users abandon after 2 minutes" |
| Actionability | 20 | Tools exist (Xtime, DealerFX, mobile scheduling) and are in use — but inconsistently |

**Note:** High pain, low measurement. The tools are there but nobody's measuring whether they're working.

---

### 13. Postponed / Declined Repairs — 40/100

**Where found:**
- `Hot Topics [TEXT].txt` (#11 Track Postpone Repairs)
- `KNOWLEDGE_INDEX.md`

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 10 | Listed as a hot topic — dealers know it's a problem but nothing is being captured |
| Ownership | 10 | Mentioned in meeting, no named owner in any document |
| Measurement | 10 | No declined repair rate, no dollar value of deferred work tracked anywhere |
| Actionability | 10 | General awareness only — no tools, no process, no follow-up system documented |

**Note:** Boss's example baseline (38). Essentially the same — pure awareness-only metric right now.

---

### 14. Video MPI Adoption — 30/100

**Where found:**
- `Hot Topics [TEXT].txt` (#04 and #17 — listed twice)
- `Take A Way's [TEXT].txt` (Mike, Dealer 28)
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` (multiple meetings)
- `KNOWLEDGE_INDEX.md` (flagged UNRESOLVED)

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 10 | Mentioned repeatedly but no adoption rate, compliance %, or usage data tracked |
| Ownership | 10 | Mike (Dealer 28) committed in Take A Way's, but knowledge index explicitly flags cultural resistance |
| Measurement | 0 | No metric exists — no "% of ROs with video" or compliance score anywhere in the data |
| Actionability | 10 | The concept is understood but tech resistance is the documented blocker — no solution path found |

**Note:** The only metric with a 0 in any dimension. There is literally no measurement of whether anyone is actually doing video MPI.

---

### 15. Service Retention — 30/100

**Where found:**
- `Hot Topics [TEXT].txt` (#02 Svc Retention)
- `KNOWLEDGE_INDEX.md` (flagged UNRESOLVED)
- `Fireflies AI NADA Meeting Transcript Summaries [TEXT].txt` (Meeting 5)

| Dimension | Score | Reasoning |
|---|---|---|
| Visibility | 10 | Hot topic but no retention rate CSV or tracking data found in any file |
| Ownership | 0 | No named owner in any document across the entire dataset |
| Measurement | 10 | Anecdotal range mentioned (1st year 70–85%, target 90%) but not tracked per dealer |
| Actionability | 10 | Knowledge index says "AI/automation needed" — acknowledged but no solution implemented |

**Note:** The only metric with a 0 in ownership. Nobody owns customer retention in this group right now.

---

## Key Patterns

### Tier 1 — Well-Managed (70–90)
Metrics where someone named owns it AND a documented process exists.
> Proficiency, Labor Rate, Stall Discipline, Hrs/RO, Call Handling, Advisor Training, Absorption

### Tier 2 — Data-Rich but Action-Poor (65)
Metrics with good CSVs but no owner and no improvement process.
> Parts Inventory Turn, Reconditioning Time, Personnel Expense %

### Tier 3 — Critical Gaps (30–50)
Pain points raised in meetings with no data, no owner, and no process.
> Service Retention, Video MPI, Declined Repairs, Scheduling, Lost Sales

**The biggest opportunity:** Tier 2 metrics already have the data — they just need an ownership layer and a process on top. That's the ServiceSync product wedge.

---

*Generated from NADA Jan 2026 meeting data | executive-intelligence-brief repository*
