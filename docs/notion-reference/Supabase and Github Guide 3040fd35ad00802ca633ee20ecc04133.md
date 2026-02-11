# Supabase and Github Guide

Owner: Fray

Use **Supabase** as your canonical runtime/data platform and **GitHub** as the canonical code + CI + collaboration platform. They play very different but complementary roles:

- **Supabase** = database, storage, embeddings/vectors, edge functions, scheduled jobs, RLS, assets.
- **GitHub** = code, notebooks, SQL migrations, CI/CD, actions, docs, PR review, collaboration.

Below is a compact, practical guide for how to use them together and what the intern should do. Treat it as the operating pattern you’ll reuse.

---

## WHY BOTH

- **Supabase** holds the *live data* (raw files, chunks, vectors, knowledge_index, commitments, metrics, charts). It is the system of record for the intelligence pipeline.
- **GitHub** holds the *code and process* that operate on your data: ingestion scripts, LLM prompt templates, analytic notebooks, site code, DB migrations, and automation pipelines. GitHub Actions runs jobs that call Supabase (or trigger Supabase Edge Functions).

They are *designed to be used together*, not as alternatives.

---

## HOW THEY FIT TOGETHER (WORKFLOW)

1. **Dev & Version Control (GitHub)**
    - Repository contains: `ingest/`, `analysis/`, `notebooks/`, `supabase/migrations/`, `app/` (site), `docs/`, `deploy/`.
    - All code, SQL migrations, README, prompt templates, and CI definitions live in GitHub.
2. **Run & Store (Supabase)**
    - `raw-docs/` bucket for uploaded meeting files; `assets/` for SVGs/screenshots.
    - Postgres tables for chunks, vectors, knowledge_topics, commitments, metrics, sources_map.
    - Supabase Edge Functions / Scheduled jobs to run ingestion or the knowledge-index builder if desired.
3. **CI & Automation (GitHub Actions)**
    - On push / PR: lint, tests, build the site, run unit tests for ingestion code.
    - On schedule (daily/weekly) or on-storage-upload webhook: run ingestion, indexing, regenerate charts, push updated JSON or assets to Supabase.
    - On release: deploy the microsite (Vercel) and/or commit snapshot exports back to GitHub for archival.
4. **Deployment (Vercel / Supabase / Framer)**
    - Site code in GitHub → Vercel (recommended for Next.js) or Framer integration.
    - Site reads sanitized data (or server-rendered components) from Supabase.

---

## REPO LAYOUT (one recommended pattern)

```
/project-root
  /ingest                # ingestion scripts (ingest.py, dockerfile)
  /analysis              # small ETL and notebook helpers
  /notebooks             # jupyter notebooks for EDA
  /supabase
    /migrations          # SQL migration files
    /seed                # sample seed data
  /app                   # Next.js or Framer site
  /design                # Figma export assets / tokens / svg examples
  /docs                  # README, architecture.md, dev-setup.md
  .github/
    workflows/
      ci.yml
      deploy.yml
      ingest-on-upload.yml
  README.md
```

---

## KEY TECHNICAL PIECES & EXAMPLE COMMANDS

**Local dev / setup**

- Use Supabase CLI:
    - `supabase login`
    - `supabase init`
    - `supabase start` (dev DB + auth locally)
    - `supabase db push` or migrations flow: `supabase migration new add_chunks_table`
- Use repo scripts:
    - `pip install -r requirements.txt` or `npm install`
    - `python ingest.py --file path/to/file` (test one file)
    - `python index_builder.py --sample 50`

**CI / Actions examples**

- `ci.yml` (on PR): run lint + unit tests + run a small sample ingestion test
- `deploy.yml` (on merge to main): build & deploy site to Vercel
- `ingest-on-upload.yml`: webhook-triggered action that calls a runner to ingest a new file or invokes a Supabase Edge Function

**Secrets / env**

- Put Supabase URL/KEY and OpenAI key in **GitHub Secrets** (e.g., `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `OPENAI_KEY`).
- Never commit keys or `.env` to the repo.

---

## DB MIGRATIONS & SCHEMA MANAGEMENT

- Keep your SQL migrations in `supabase/migrations/`.
- Use `supabase migration new` and `supabase db push` in CI.
- Migrations + tests should be run in CI before merging.

---

## AUTOMATION PATTERNS

1. **Event-driven ingestion**
    - File uploaded to Supabase storage → Supabase storage webhook → GitHub Action or Supabase Edge Function → runs ingestion job.
2. **Scheduled jobs**
    - GitHub Action or Supabase scheduled function (cron) calls `index_builder.py` weekly to refresh topics/metrics.
3. **Snapshot exports**
    - After index rebuild, export `knowledge_index.json` and commit to `data/` folder via an authenticated action (use a GitHub bot account).

---

## AUDITABILITY & TRACEABILITY

- `sources_map` table in Supabase is populated by ingestion + LLM steps. Always write the filenames + chunk ids used for each insight.
- Commit code changes + SQL migrations via PRs so reviewers can inspect prompt changes or normalization logic.

---

## SECURITY & Governance

- RLS on sensitive tables; keep raw files private. Only expose sanitized views to the public site.
- Use GitHub Secrets for CI; rotate keys.
- Use codeowners and PR reviews for critical folders (`/ingest`, `/supabase/migrations`).

---

## PRACTICAL GUIDANCE FOR THE INTERN

- **Clone** repo, install deps.
- **Set up** local Supabase using CLI and a dev project. Put dev keys in local `.env` (gitignored).
- **Run** a single-file ingestion locally, view `chunks` table in Supabase.
- **Open PR** when code ready; use Actions to run tests.
- **Test** site locally with `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_ANON_KEY` for read-only views (or use server-side rendering).
- **Document** every script in `docs/dev-setup.md`.

---

## OPTIONAL: Snapshotting the Knowledge Index in GitHub

If you want versioned, auditable snapshots of the knowledge index:

- Add a scheduled job that runs `curl` to your server to fetch `knowledge_index.json`, commits it to the repo (`data/`), and opens a PR or pushes to a snapshots branch. Use a bot account and GitHub Actions for the commit.

---

## Final recommendation (practical)

- **Yes — use both**.
- **Supabase** for living data and run-time.
- **GitHub** for all code, migrations, CI, workflows, and collaboration.
- Use **GitHub Actions** to orchestrate scheduled & event-driven pipelines that operate on Supabase.
- Protect secrets in GitHub and protect sensitive views inside Supabase.

If you want, I can:

1. Draft a sample `ci.yml` and `ingest-on-upload.yml` workflow (GitHub Actions).
2. Provide a `README.dev.md` for your intern with exact step-by-step commands and example `supabase` + repo setup.

Which one would you like first?