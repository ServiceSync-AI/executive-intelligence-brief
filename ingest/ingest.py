"""Main ingestion script to process all NADA files into Supabase."""

import os
import sys
from pathlib import Path
from supabase import create_client
from datetime import datetime
import argparse

# Import parsers
from parsers.pdf_parser import parse_pdf
from parsers.docx_parser import parse_docx
from parsers.image_parser import parse_image
from chunker import chunk_text
from embedder import generate_embeddings


def load_env():
    """Load environment variables from .env.local"""
    env_path = Path(__file__).parent.parent / ".env.local"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, val = line.strip().split('=', 1)
                    os.environ[key] = val


def get_supabase_client():
    """Initialize Supabase client"""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    
    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY required")
    
    return create_client(url, key)


def parse_file(file_path: Path):
    """Parse a file based on its extension"""
    ext = file_path.suffix.lower()
    
    if ext == '.pdf':
        return parse_pdf(str(file_path))
    elif ext == '.docx':
        return parse_docx(str(file_path))
    elif ext in ['.png', '.jpg', '.jpeg']:
        return parse_image(str(file_path))
    elif ext == '.txt':
        # Read text files directly
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return {
            "file_name": file_path.name,
            "file_type": "txt",
            "text": text
        }
    elif ext == '.csv':
        # Read CSV as text for now
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return {
            "file_name": file_path.name,
            "file_type": "csv",
            "text": text
        }
    else:
        print(f"⚠️  Skipping unsupported file type: {file_path}")
        return None


def ingest_file(file_path: Path, supabase, dry_run=False):
    """Process a single file: parse, chunk, embed, store"""
    print(f"\n📄 Processing: {file_path.name}")
    
    # Parse file
    try:
        parsed = parse_file(file_path)
        if not parsed:
            return False
    except Exception as e:
        print(f"❌ Parse error: {e}")
        return False
    
    print(f"   ✓ Parsed ({len(parsed['text'])} chars)")
    
    # Chunk text
    chunks = chunk_text(parsed['text'])
    print(f"   ✓ Created {len(chunks)} chunks")
    
    if dry_run:
        print(f"   🔍 DRY RUN - would process {len(chunks)} chunks")
        return True
    
    # Store raw file record
    file_record = {
        "file_name": parsed['file_name'],
        "file_type": parsed['file_type'],
        "file_path": str(file_path),
        "content": parsed['text'],
        "metadata": {
            "num_chunks": len(chunks),
            "processed_at": datetime.utcnow().isoformat()
        }
    }
    
    try:
        result = supabase.table("raw_files").insert(file_record).execute()
        file_id = result.data[0]['id']
        print(f"   ✓ Stored file record (id: {file_id})")
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False
    
    # Generate embeddings for all chunks
    chunk_texts = [c['text'] for c in chunks]
    try:
        embeddings = generate_embeddings(chunk_texts)
        print(f"   ✓ Generated {len(embeddings)} embeddings")
    except Exception as e:
        print(f"❌ Embedding error: {e}")
        return False
    
    # Store chunks with embeddings
    chunk_records = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        chunk_records.append({
            "file_id": file_id,
            "chunk_index": i,
            "content": chunk['text'],
            "num_tokens": chunk['num_tokens'],
            "embedding": embedding
        })
    
    try:
        supabase.table("chunks").insert(chunk_records).execute()
        print(f"   ✓ Stored {len(chunk_records)} chunks")
    except Exception as e:
        print(f"❌ Chunk storage error: {e}")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(description="Ingest NADA files into Supabase")
    parser.add_argument("--directory", required=True, help="Directory containing files to process")
    parser.add_argument("--dry-run", action="store_true", help="Parse and chunk without storing")
    parser.add_argument("--limit", type=int, help="Limit number of files to process")
    
    args = parser.parse_args()
    
    # Load environment
    load_env()
    
    # Get directory
    data_dir = Path(args.directory)
    if not data_dir.exists():
        print(f"❌ Directory not found: {data_dir}")
        sys.exit(1)
    
    # Find all files
    files = []
    for ext in ['.pdf', '.docx', '.txt', '.csv', '.png', '.jpg']:
        files.extend(data_dir.rglob(f"*{ext}"))
    
    # Resolve symlinks and filter out broken ones
    resolved_files = []
    for f in files:
        try:
            resolved = f.resolve()
            if resolved.exists():
                resolved_files.append(resolved)
        except:
            pass
    
    files = resolved_files
    
    if args.limit:
        files = files[:args.limit]
    
    print(f"\n🚀 Starting ingestion")
    print(f"   Directory: {data_dir}")
    print(f"   Files found: {len(files)}")
    print(f"   Dry run: {args.dry_run}")
    
    if not args.dry_run:
        supabase = get_supabase_client()
        print(f"   ✓ Connected to Supabase")
    else:
        supabase = None
    
    # Process files
    success_count = 0
    for i, file_path in enumerate(files, 1):
        print(f"\n[{i}/{len(files)}]", end=" ")
        if ingest_file(file_path, supabase, dry_run=args.dry_run):
            success_count += 1
    
    # Summary
    print(f"\n\n✅ Ingestion complete!")
    print(f"   Processed: {success_count}/{len(files)} files")
    if success_count < len(files):
        print(f"   Failed: {len(files) - success_count} files")


if __name__ == "__main__":
    main()
