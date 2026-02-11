"""PDF parser for extracting text from PDF documents."""

import pdfplumber
from pathlib import Path
from typing import Dict, List


def parse_pdf(file_path: str) -> Dict[str, any]:
    """
    Extract text from a PDF file.
    
    Args:
        file_path: Path to the PDF file
        
    Returns:
        Dict with extracted text and metadata
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")
    
    pages = []
    
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if text:
                pages.append({
                    "page_number": i,
                    "text": text.strip()
                })
    
    # Combine all pages
    full_text = "\n\n".join([p["text"] for p in pages])
    
    return {
        "file_name": path.name,
        "file_type": "pdf",
        "num_pages": len(pages),
        "text": full_text,
        "pages": pages
    }


if __name__ == "__main__":
    # Test with a sample file
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python pdf_parser.py <path_to_pdf>")
        sys.exit(1)
    
    result = parse_pdf(sys.argv[1])
    print(f"Parsed: {result['file_name']}")
    print(f"Pages: {result['num_pages']}")
    print(f"Text length: {len(result['text'])} characters")
    print(f"\nFirst 500 chars:\n{result['text'][:500]}")
