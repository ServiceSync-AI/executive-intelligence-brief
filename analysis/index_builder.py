"""Topic extraction using LLM to identify canonical knowledge from chunks."""

import os
import sys
from pathlib import Path
from supabase import create_client
from openai import OpenAI
import json


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
    return create_client(url, key)


def sample_chunks(supabase, limit=200):
    """Sample chunks from database for topic extraction"""
    print(f"📥 Sampling {limit} chunks from database...")
    
    result = supabase.table("chunks").select("id, content, file_id").limit(limit).execute()
    
    print(f"   ✓ Retrieved {len(result.data)} chunks")
    return result.data


def extract_topics_with_llm(chunks):
    """Use LLM to extract canonical topics from chunks"""
    print(f"\n🤖 Extracting topics with LLM...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    
    # Combine chunk content
    combined_text = "\n\n---\n\n".join([c['content'][:500] for c in chunks[:50]])
    
    prompt = f"""Analyze these excerpts from automotive dealership service manager meeting notes.

Extract 10-15 canonical topics that represent what the industry knows and discusses.

For each topic provide:
1. Topic name (concise, 3-5 words)
2. Definition (1-2 sentences)
3. Status (e.g., "Widely discussed", "Emerging practice", "Known challenge")

Format as JSON array:
[
  {{
    "topic": "Video MPI Implementation",
    "definition": "Using video multi-point inspections to increase customer trust and repair order value",
    "status": "Widely discussed, variable adoption"
  }}
]

Meeting excerpts:
{combined_text}

Return only the JSON array, no other text."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    topics_json = response.choices[0].message.content.strip()
    
    # Remove markdown code blocks if present
    if topics_json.startswith("```"):
        topics_json = topics_json.split("```")[1]
        if topics_json.startswith("json"):
            topics_json = topics_json[4:]
    
    topics = json.loads(topics_json)
    
    print(f"   ✓ Extracted {len(topics)} topics")
    return topics


def find_evidence_for_topics(supabase, topics, chunks):
    """Find supporting evidence chunks for each topic"""
    print(f"\n🔍 Finding evidence for topics...")
    
    for topic in topics:
        # Simple keyword matching for now
        topic_name = topic['topic'].lower()
        keywords = topic_name.split()
        
        evidence_chunks = []
        for chunk in chunks:
            content_lower = chunk['content'].lower()
            if any(kw in content_lower for kw in keywords):
                evidence_chunks.append(chunk['id'])
        
        topic['evidence'] = {
            'chunk_ids': evidence_chunks[:10],  # Limit to 10
            'count': len(evidence_chunks)
        }
        topic['confidence'] = min(len(evidence_chunks) / 10, 1.0)
    
    print(f"   ✓ Mapped evidence for all topics")
    return topics


def store_topics(supabase, topics):
    """Store topics in knowledge_topics table"""
    print(f"\n💾 Storing topics in database...")
    
    records = []
    for topic in topics:
        records.append({
            'topic': topic['topic'],
            'definition': topic['definition'],
            'status': topic['status'],
            'evidence': topic['evidence'],
            'confidence': topic['confidence']
        })
    
    result = supabase.table("knowledge_topics").insert(records).execute()
    
    print(f"   ✓ Stored {len(result.data)} topics")
    return result.data


def main():
    print("\n🚀 Starting Topic Extraction\n")
    print("=" * 60)
    
    # Load environment
    load_env()
    
    # Connect to Supabase
    supabase = get_supabase_client()
    print("✓ Connected to Supabase")
    
    # Sample chunks
    chunks = sample_chunks(supabase, limit=200)
    
    # Extract topics with LLM
    topics = extract_topics_with_llm(chunks)
    
    # Find evidence
    topics = find_evidence_for_topics(supabase, topics, chunks)
    
    # Store topics
    stored_topics = store_topics(supabase, topics)
    
    # Summary
    print("\n" + "=" * 60)
    print(f"\n✅ Topic Extraction Complete!")
    print(f"\n📊 Results:")
    print(f"   Topics extracted: {len(stored_topics)}")
    print(f"   Avg confidence: {sum(t['confidence'] for t in topics) / len(topics):.2f}")
    print(f"\n📋 Topics:")
    for i, topic in enumerate(topics, 1):
        print(f"   {i}. {topic['topic']}")
        print(f"      {topic['definition']}")
        print(f"      Evidence: {topic['evidence']['count']} chunks")
        print()


if __name__ == "__main__":
    main()
