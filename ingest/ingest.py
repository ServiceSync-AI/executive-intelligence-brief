"""
Main ingestion script - parses documents, chunks text, generates embeddings
"""
import os
import argparse
from dotenv import load_dotenv

def main():
    parser = argparse.ArgumentParser(description='Ingest documents into knowledge base')
    parser.add_argument('--file', required=True, help='Path to document file')
    parser.add_argument('--dry-run', action='store_true', help='Test without writing to database')
    parser.add_argument('--force', action='store_true', help='Reprocess even if already processed')
    
    args = parser.parse_args()
    
    load_dotenv('.env.local')
    
    print(f"Ingesting: {args.file}")
    print("Status: Placeholder - implementation coming next")
    
    # TODO: Implement full ingestion pipeline
    # 1. Parse file (PDF/DOCX/Image)
    # 2. Chunk text
    # 3. Generate embeddings
    # 4. Store in Supabase

if __name__ == '__main__':
    main()
