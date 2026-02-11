"""Embeddings generator using OpenAI API."""

import os
from openai import OpenAI
from typing import List, Dict
import time
from pathlib import Path


def load_env():
    """Load environment variables from .env.local"""
    env_path = Path(__file__).parent.parent / ".env.local"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, val = line.strip().split('=', 1)
                    os.environ[key] = val


def generate_embeddings(
    texts: List[str],
    model: str = "text-embedding-3-small",
    batch_size: int = 100
) -> List[List[float]]:
    """
    Generate embeddings for a list of texts using OpenAI API.
    
    Args:
        texts: List of text strings to embed
        model: OpenAI embedding model to use
        batch_size: Number of texts to process per API call
        
    Returns:
        List of embedding vectors
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment")
    
    client = OpenAI(api_key=api_key)
    
    all_embeddings = []
    
    # Process in batches
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        
        try:
            response = client.embeddings.create(
                input=batch,
                model=model
            )
            
            # Extract embeddings from response
            embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(embeddings)
            
            print(f"Processed {len(all_embeddings)}/{len(texts)} texts")
            
            # Rate limiting - small delay between batches
            if i + batch_size < len(texts):
                time.sleep(0.1)
                
        except Exception as e:
            print(f"Error processing batch {i//batch_size + 1}: {e}")
            raise
    
    return all_embeddings


if __name__ == "__main__":
    # Load environment variables
    load_env()
    
    # Test with sample texts
    sample_texts = [
        "This is a test document about automotive service.",
        "Dealer performance metrics include hours per RO and service absorption.",
        "Video MPIs increase customer trust and repair order value."
    ]
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY not set. Add it to .env.local")
        print("Usage: OPENAI_API_KEY=sk-... python embedder.py")
        exit(1)
    
    embeddings = generate_embeddings(sample_texts)
    
    print(f"\nGenerated {len(embeddings)} embeddings")
    print(f"Embedding dimension: {len(embeddings[0])}")
    print(f"First embedding preview: {embeddings[0][:5]}...")
