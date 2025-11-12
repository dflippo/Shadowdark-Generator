#!/usr/bin/env python3
"""
PDF Extraction Script - Extracts text and images from PDFs, one file per page.

Usage: python extract_pdf.py <pdf_file> [--output-dir <directory>]
Requirements: PyMuPDF, Pillow
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
    from PIL import Image
except ImportError as e:
    print(f"ERROR: Missing required package: {e}")
    print("Install dependencies with: pip install PyMuPDF Pillow")
    sys.exit(1)


def extract_pdf(pdf_path, output_dir=None):
    """
    Extract text and images from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Optional output directory. If not provided, creates 
                   subdirectory next to the PDF with the same name (without .pdf)
    
    Returns:
        Path to the output directory containing extracted files
    """
    pdf_path = Path(pdf_path).resolve()
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    if not pdf_path.suffix.lower() == '.pdf':
        raise ValueError(f"File is not a PDF: {pdf_path}")
    
    # Determine output directory
    if output_dir is None:
        # Create subdirectory with same name as PDF (without .pdf extension)
        output_dir = pdf_path.parent / pdf_path.stem
    else:
        output_dir = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Processing PDF: {pdf_path.name}")
    print(f"Output directory: {output_dir}")
    print()
    
    # Open the PDF
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        raise RuntimeError(f"Failed to open PDF: {e}")
    
    total_pages = len(doc)
    print(f"Total pages: {total_pages}")
    print()
    
    # Process each page
    for page_num in range(total_pages):
        page = doc[page_num]
        page_number = page_num  # 0-indexed for filenames
        
        print(f"Processing page {page_number}/{total_pages - 1}...", end=" ")
        
        # Extract text
        text = page.get_text()
        text_filename = output_dir / f"page_{page_number:04d}.txt"
        
        with open(text_filename, 'w', encoding='utf-8') as f:
            f.write(text)
        
        # Extract page as image
        # Use a reasonable DPI for image quality (150 DPI is good for reading)
        zoom = 2.0  # Zoom factor (2.0 = 144 DPI, good balance of quality/size)
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        
        # Convert to PIL Image for better format support
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Save as PNG (lossless, good for text/diagrams)
        image_filename = output_dir / f"page_{page_number:04d}.png"
        img.save(image_filename, "PNG")
        
        print("✓")
    
    doc.close()
    
    print()
    print(f"Extraction complete!")
    print(f"Text files: {total_pages}")
    print(f"Image files: {total_pages}")
    print(f"Location: {output_dir}")
    
    return output_dir


def main():
    parser = argparse.ArgumentParser(
        description="Extract text and images from PDF files, one per page."
    )
    parser.add_argument(
        "pdf_file",
        help="Path to the PDF file to extract"
    )
    parser.add_argument(
        "--output-dir",
        help="Output directory for extracted files (default: subdirectory named after PDF)"
    )
    
    args = parser.parse_args()
    
    try:
        extract_pdf(args.pdf_file, args.output_dir)
        return 0
    except Exception as e:
        print(f"\nERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
