"""
Knowledge index builder - LLM-driven topic extraction
"""
import argparse
from dotenv import load_dotenv

def main():
    parser = argparse.ArgumentParser(description='Build knowledge index from chunks')
    parser.add_argument('--sample', type=int, default=200, help='Number of chunks to sample')
    parser.add_argument('--output', help='Save output to file')
    
    args = parser.parse_args()
    
    load_dotenv('.env.local')
    
    print(f"Building knowledge index with {args.sample} sample chunks")
    print("Status: Placeholder - implementation coming next")
    
    # TODO: Implement knowledge extraction
    # 1. Query representative chunks from Supabase
    # 2. Use LLM to extract canonical topics
    # 3. Map evidence to source files
    # 4. Store in knowledge_topics table

if __name__ == '__main__':
    main()
