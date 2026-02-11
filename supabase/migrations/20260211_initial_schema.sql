-- Enable pgvector extension for embeddings
CREATE EXTENSION IF NOT EXISTS vector;

-- Raw files metadata
CREATE TABLE raw_files (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  file_name text NOT NULL,
  file_type text,
  file_path text,
  content text,
  metadata jsonb,
  created_at timestamptz DEFAULT now()
);

-- Chunked content with embeddings
CREATE TABLE chunks (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  file_id uuid REFERENCES raw_files(id) ON DELETE CASCADE,
  chunk_index int,
  content text,
  num_tokens int,
  embedding vector(1536),
  created_at timestamptz DEFAULT now()
);

-- Create index for vector similarity search
CREATE INDEX ON chunks USING ivfflat (embedding vector_cosine_ops);

-- Canonical topics / knowledge index
CREATE TABLE knowledge_topics (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  topic text UNIQUE,
  definition text,
  status text,
  evidence jsonb,
  confidence numeric,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

-- Dealer commitments
CREATE TABLE commitments (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  dealer_code text,
  theme text,
  statement text,
  evidence jsonb,
  captured_at timestamptz DEFAULT now()
);

-- Aggregated metrics
CREATE TABLE metrics (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text,
  median numeric,
  low numeric,
  high numeric,
  units text,
  evidence jsonb,
  updated_at timestamptz DEFAULT now()
);

-- Decision log for persistence
CREATE TABLE decision_log (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  context text,
  decision text,
  owner text,
  due_date date,
  status text,
  created_at timestamptz DEFAULT now()
);

-- Source traceability
CREATE TABLE sources_map (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  insight_id uuid,
  source_files jsonb,
  created_at timestamptz DEFAULT now()
);

-- Processing audit
CREATE TABLE processed_files (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  file_id uuid REFERENCES raw_files(id),
  status text,
  details jsonb,
  processed_at timestamptz DEFAULT now()
);

-- Create indexes for common queries
CREATE INDEX idx_chunks_file_id ON chunks(file_id);
CREATE INDEX idx_commitments_dealer_code ON commitments(dealer_code);
CREATE INDEX idx_commitments_theme ON commitments(theme);
CREATE INDEX idx_knowledge_topics_status ON knowledge_topics(status);
