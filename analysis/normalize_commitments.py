"""Extract dealer commitments from Take A Way's notes."""

import os
import sys
from pathlib import Path
from supabase import create_client
from openai import OpenAI
import json


def load_env():
    """Load environment variables"""
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
    return create_client(url, key)


def get_takeaways_content(supabase):
    """Get Take A Way's file content"""
    print("📥 Retrieving Take A Way's notes...")
    
    result = supabase.table('raw_files').select('*').ilike('file_name', '%Take A Way%').limit(1).execute()
    
    if not result.data:
        print("❌ Take A Way's file not found")
        return None
    
    content = result.data[0]['content']
    print(f"   ✓ Retrieved {len(content)} chars")
    return content


def extract_commitments_with_llm(content):
    """Use LLM to extract commitments from messy OCR text"""
    print(f"\n🤖 Extracting commitments with LLM...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    
    prompt = f"""This is OCR text from handwritten dealer commitment notes from a NADA meeting.

Extract dealer commitments and map them to these themes:
1. AI Phone & Scheduling
2. Video MPI
3. Postponed Service Follow-up
4. Reconditioning Speed
5. Daily Accountability
6. Tech Retention

For each commitment provide:
- dealer_code: (e.g., "D01", "D02" - assign sequentially)
- theme: (one of the 6 themes above)
- statement: (clean, readable commitment statement)

Format as JSON array. Extract as many commitments as you can identify.

OCR Text:
{content}

Return only the JSON array."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    commitments_json = response.choices[0].message.content.strip()
    
    # Remove markdown if present
    if commitments_json.startswith("```"):
        commitments_json = commitments_json.split("```")[1]
        if commitments_json.startswith("json"):
            commitments_json = commitments_json[4:]
    
    commitments = json.loads(commitments_json)
    
    print(f"   ✓ Extracted {len(commitments)} commitments")
    return commitments


def store_commitments(supabase, commitments):
    """Store commitments in database"""
    print(f"\n💾 Storing commitments...")
    
    records = []
    for c in commitments:
        records.append({
            'dealer_code': c['dealer_code'],
            'theme': c['theme'],
            'statement': c['statement'],
            'evidence': {'source': 'Take A Way\'s.pdf'}
        })
    
    result = supabase.table("commitments").insert(records).execute()
    
    print(f"   ✓ Stored {len(result.data)} commitments")
    return result.data


def main():
    print("\n🚀 Starting Commitment Extraction\n")
    print("=" * 60)
    
    load_env()
    supabase = get_supabase_client()
    print("✓ Connected to Supabase")
    
    # Get content
    content = get_takeaways_content(supabase)
    if not content:
        return
    
    # Extract commitments
    commitments = extract_commitments_with_llm(content)
    
    # Store commitments
    stored = store_commitments(supabase, commitments)
    
    # Summary
    print("\n" + "=" * 60)
    print(f"\n✅ Commitment Extraction Complete!")
    print(f"\n📊 Results:")
    print(f"   Commitments extracted: {len(stored)}")
    
    # Group by theme
    by_theme = {}
    for c in commitments:
        theme = c['theme']
        by_theme[theme] = by_theme.get(theme, 0) + 1
    
    print(f"\n📋 By Theme:")
    for theme, count in sorted(by_theme.items(), key=lambda x: -x[1]):
        print(f"   {theme}: {count}")
    
    print(f"\n📝 Sample Commitments:")
    for c in commitments[:5]:
        print(f"   {c['dealer_code']} - {c['theme']}")
        print(f"      {c['statement']}")
        print()


if __name__ == "__main__":
    main()
