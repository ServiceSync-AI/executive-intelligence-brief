"""Image parser with OCR for extracting text from images."""

import pytesseract
from PIL import Image
from pathlib import Path
from typing import Dict


def parse_image(file_path: str) -> Dict[str, any]:
    """
    Extract text from an image using OCR.
    
    Args:
        file_path: Path to the image file
        
    Returns:
        Dict with extracted text and metadata
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Image file not found: {file_path}")
    
    # Open image
    image = Image.open(file_path)
    
    # Extract text using Tesseract OCR
    text = pytesseract.image_to_string(image)
    
    # Get image info
    width, height = image.size
    
    return {
        "file_name": path.name,
        "file_type": "image",
        "format": image.format,
        "width": width,
        "height": height,
        "text": text.strip()
    }


if __name__ == "__main__":
    # Test with a sample file
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python image_parser.py <path_to_image>")
        sys.exit(1)
    
    result = parse_image(sys.argv[1])
    print(f"Parsed: {result['file_name']}")
    print(f"Format: {result['format']}")
    print(f"Size: {result['width']}x{result['height']}")
    print(f"Text length: {len(result['text'])} characters")
    print(f"\nExtracted text:\n{result['text']}")
