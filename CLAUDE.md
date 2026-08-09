# ServiceSync AI — Executive Intelligence Brief

## What This Is
Interactive microsite transforming 72 NADA 20 Group meeting documents into an intelligence brief. Conversation heatmaps, dealer commitment matrices, performance variance analysis, execution gap diagrams. Goal: impress the group moderator and land pilot conversations.

## Stack
- Python (ingestion, OCR, embeddings) — analysis/, ingest/
- Next.js + TypeScript + Tailwind (frontend) — app/
- Supabase (PostgreSQL + pgvector + storage)
- OpenAI for embeddings and extraction
- AWS S3 for static hosting

## Current State
83% complete. Phases 1-5 done. Phase 6 (deployment) is next. Microsite is built, just needs to go live.

## Team
- Frazier Horn (lead)
- Kexin (intern, kexin@servicesync.io, GitHub @kkt-19)

## Supabase Tables
raw_files, chunks, chunk_vectors, knowledge_topics, commitments, metrics, sources_map, processed_files, decision_log

## Key Results
- 14 canonical topics extracted
- 5 dealer commitments mapped
- 4 key performance metrics
- 4 interactive visualizations in Supabase storage

## Confidentiality
No PII, no named dealers in public output. This data is from private 20 Group meetings.

## Don't
- Don't expose dealer names or PII
- Don't commit secrets or .env.local
- Don't modify Supabase data without understanding the evidence traceability chain
