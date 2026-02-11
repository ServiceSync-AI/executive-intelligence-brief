"""Text chunking utility for splitting documents into manageable pieces."""

import tiktoken
from typing import List, Dict


def chunk_text(
    text: str,
    chunk_size: int = 800,
    overlap: int = 200,
    model: str = "text-embedding-3-small"
) -> List[Dict[str, any]]:
    """
    Split text into chunks with overlap, respecting token limits.
    
    Args:
        text: Text to chunk
        chunk_size: Maximum tokens per chunk (default: 800)
        overlap: Token overlap between chunks (default: 200)
        model: Model name for tokenization
        
    Returns:
        List of chunk dicts with text and metadata
    """
    # Get tokenizer for the model
    encoding = tiktoken.encoding_for_model(model)
    
    # Tokenize the full text
    tokens = encoding.encode(text)
    
    chunks = []
    start = 0
    chunk_num = 0
    
    while start < len(tokens):
        # Get chunk tokens
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        
        # Decode back to text
        chunk_text = encoding.decode(chunk_tokens)
        
        chunks.append({
            "chunk_id": chunk_num,
            "text": chunk_text,
            "start_token": start,
            "end_token": min(end, len(tokens)),
            "num_tokens": len(chunk_tokens)
        })
        
        chunk_num += 1
        
        # Move start forward, accounting for overlap
        start = end - overlap
        
        # Break if we've processed all tokens
        if end >= len(tokens):
            break
    
    return chunks


if __name__ == "__main__":
    # Test with sample text
    sample_text = """
    This is a test document for chunking. It contains multiple sentences and paragraphs.
    
    The chunking algorithm will split this text into smaller pieces while maintaining overlap
    between chunks to preserve context. This is important for semantic search and embeddings.
    
    Each chunk will have metadata including token counts and position information.
    """ * 50  # Repeat to make it longer
    
    chunks = chunk_text(sample_text, chunk_size=200, overlap=50)
    
    print(f"Original text: {len(sample_text)} characters")
    print(f"Created {len(chunks)} chunks")
    print(f"\nFirst chunk:")
    print(f"  Tokens: {chunks[0]['num_tokens']}")
    print(f"  Text preview: {chunks[0]['text'][:200]}...")
    print(f"\nLast chunk:")
    print(f"  Tokens: {chunks[-1]['num_tokens']}")
    print(f"  Text preview: {chunks[-1]['text'][:200]}...")
