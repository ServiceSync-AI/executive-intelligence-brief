"""
Commitment normalization - maps dealer takeaways to canonical themes
"""
import argparse
from dotenv import load_dotenv

def main():
    parser = argparse.ArgumentParser(description='Extract and normalize dealer commitments')
    parser.add_argument('--images', required=True, help='Path to handwritten takeaways image')
    parser.add_argument('--review', action='store_true', help='Enable manual review of ambiguous mappings')
    
    args = parser.parse_args()
    
    load_dotenv('.env.local')
    
    print(f"Processing: {args.images}")
    print("Status: Placeholder - implementation coming next")
    
    # TODO: Implement commitment extraction
    # 1. OCR handwritten notes
    # 2. Parse dealer codes and statements
    # 3. Map to 6 canonical themes
    # 4. Manual QA if --review flag
    # 5. Store in commitments table

if __name__ == '__main__':
    main()
