"""DOCX parser for extracting text from Word documents."""

from docx import Document
from pathlib import Path
from typing import Dict


def parse_docx(file_path: str) -> Dict[str, any]:
    """
    Extract text from a DOCX file.
    
    Args:
        file_path: Path to the DOCX file
        
    Returns:
        Dict with extracted text and metadata
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"DOCX file not found: {file_path}")
    
    doc = Document(file_path)
    
    # Extract paragraphs
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    
    # Extract tables
    tables = []
    for table in doc.tables:
        table_data = []
        for row in table.rows:
            row_data = [cell.text.strip() for cell in row.cells]
            table_data.append(row_data)
        tables.append(table_data)
    
    # Combine all text
    full_text = "\n\n".join(paragraphs)
    
    return {
        "file_name": path.name,
        "file_type": "docx",
        "num_paragraphs": len(paragraphs),
        "num_tables": len(tables),
        "text": full_text,
        "paragraphs": paragraphs,
        "tables": tables
    }


if __name__ == "__main__":
    # Test with a sample file
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python docx_parser.py <path_to_docx>")
        sys.exit(1)
    
    result = parse_docx(sys.argv[1])
    print(f"Parsed: {result['file_name']}")
    print(f"Paragraphs: {result['num_paragraphs']}")
    print(f"Tables: {result['num_tables']}")
    print(f"Text length: {len(result['text'])} characters")
    print(f"\nFirst 500 chars:\n{result['text'][:500]}")
