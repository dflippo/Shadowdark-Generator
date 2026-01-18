# PDF Reader Skill

This skill enables accurate page-by-page reading of PDF files by extracting text and images.

## Structure

- `SKILL.md` - Main skill documentation and usage instructions
- `scripts/extract_pdf.py` - Python script for PDF extraction
- `PDF_READER_GUIDE.md` - This file

## Quick Start

Extract a PDF to text and image files:

```bash
python scripts/extract_pdf.py "path/to/document.pdf"
```

This creates a subdirectory with the PDF's name containing:

- One `.txt` file per page (extracted text)
- One `.png` file per page (page image)

Files are numbered `page_0000.txt`, `page_0001.txt`, etc., starting from 0 (page 0 = first page/title page).

## Requirements

- Python 3.x
- PyMuPDF (fitz)
- Pillow (PIL)

Install with: `pip install PyMuPDF Pillow`

## Use Cases

- Reading RPG rulebooks and modules with accurate page references
- Extracting text from PDFs for analysis
- Converting scanned PDFs (image-based) for reading via images
- Analyzing documents that combine text and visual elements

## Example

```bash
# Extract Shadowdark RPG rulebook
python scripts/extract_pdf.py "Shadowdark RPG - V4-8.pdf"

# Result: Directory "Shadowdark RPG - V4-8/" with 332 text and 332 image files

# Read specific page
cat "Shadowdark RPG - V4-8/page_0042.txt"

# Search across all pages
grep -r "death saving throw" "Shadowdark RPG - V4-8/"
```

## Best Practices

Following general best practices for agent tool use:

- ✅ Concise documentation with progressive disclosure
- ✅ Utility script handles errors explicitly
- ✅ Clear usage examples and workflows
- ✅ Specific description for skill discovery
- ✅ Dependencies clearly documented
- ✅ Platform-agnostic file paths (forward slashes)
