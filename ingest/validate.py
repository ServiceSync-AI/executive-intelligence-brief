"""Validation script to verify ingestion data quality."""

import os
from pathlib import Path
from supabase import create_client
from datetime import datetime


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


def validate_ingestion():
    """Validate ingestion data in Supabase"""
    print("\n🔍 Validating Ingestion Data\n")
    print("=" * 60)
    
    load_env()
    supabase = get_supabase_client()
    
    issues = []
    
    # Check raw_files table
    print("\n📁 Raw Files Table:")
    try:
        files = supabase.table("raw_files").select("*").execute()
        file_count = len(files.data)
        print(f"   ✓ Files stored: {file_count}")
        
        if file_count == 0:
            issues.append("No files found in raw_files table")
        
        # Check file types
        file_types = {}
        for f in files.data:
            ft = f.get('file_type', 'unknown')
            file_types[ft] = file_types.get(ft, 0) + 1
        
        print(f"   File types:")
        for ft, count in sorted(file_types.items()):
            print(f"     - {ft}: {count}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        issues.append(f"raw_files table error: {e}")
        file_count = 0
    
    # Check chunks table
    print("\n📦 Chunks Table:")
    try:
        chunks = supabase.table("chunks").select("id, file_id, chunk_index, num_tokens").execute()
        chunk_count = len(chunks.data)
        print(f"   ✓ Chunks stored: {chunk_count}")
        
        if chunk_count == 0:
            issues.append("No chunks found in chunks table")
        
        # Calculate stats
        if chunk_count > 0:
            total_tokens = sum(c.get('num_tokens', 0) for c in chunks.data)
            avg_tokens = total_tokens / chunk_count
            print(f"   Total tokens: {total_tokens:,}")
            print(f"   Avg tokens/chunk: {avg_tokens:.1f}")
            
            # Check for orphaned chunks
            file_ids = set(f['id'] for f in files.data)
            chunk_file_ids = set(c['file_id'] for c in chunks.data)
            orphaned = chunk_file_ids - file_ids
            if orphaned:
                issues.append(f"Found {len(orphaned)} orphaned chunks (no matching file)")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        issues.append(f"chunks table error: {e}")
        chunk_count = 0
    
    # Check embeddings
    print("\n🔢 Embeddings:")
    try:
        # Sample a few chunks to check embeddings
        sample = supabase.table("chunks").select("embedding").limit(5).execute()
        
        if sample.data:
            has_embeddings = all(c.get('embedding') for c in sample.data)
            if has_embeddings:
                embedding_dim = len(sample.data[0]['embedding'])
                print(f"   ✓ Embeddings present")
                print(f"   Dimension: {embedding_dim}")
                
                if embedding_dim != 1536:
                    issues.append(f"Unexpected embedding dimension: {embedding_dim} (expected 1536)")
            else:
                issues.append("Some chunks missing embeddings")
                print(f"   ⚠️  Some chunks missing embeddings")
        else:
            print(f"   ⚠️  No chunks to check")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        issues.append(f"embeddings check error: {e}")
    
    # Storage buckets
    print("\n🪣 Storage Buckets:")
    try:
        buckets = supabase.storage.list_buckets()
        bucket_names = [b.name for b in buckets]
        
        required = ['raw-docs', 'assets']
        for bucket in required:
            if bucket in bucket_names:
                print(f"   ✓ {bucket} exists")
            else:
                print(f"   ❌ {bucket} missing")
                issues.append(f"Missing storage bucket: {bucket}")
                
    except Exception as e:
        print(f"   ❌ Error: {e}")
        issues.append(f"storage buckets error: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("\n📊 Summary:")
    print(f"   Files: {file_count}")
    print(f"   Chunks: {chunk_count}")
    
    if file_count > 0:
        print(f"   Avg chunks/file: {chunk_count/file_count:.1f}")
    
    print(f"\n{'✅ VALIDATION PASSED' if not issues else '⚠️  VALIDATION ISSUES FOUND'}")
    
    if issues:
        print(f"\n🚨 Issues ({len(issues)}):")
        for i, issue in enumerate(issues, 1):
            print(f"   {i}. {issue}")
    
    print("\n" + "=" * 60)
    
    # Generate report
    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "files": file_count,
        "chunks": chunk_count,
        "issues": issues,
        "status": "PASSED" if not issues else "FAILED"
    }
    
    return report


if __name__ == "__main__":
    report = validate_ingestion()
    
    # Exit with error code if validation failed
    if report['status'] == 'FAILED':
        exit(1)
