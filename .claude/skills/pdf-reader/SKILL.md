---
name: PDF Reading
description: Extract text and images from PDF files for accurate page-by-page analysis. Use when working with PDF documents, game rulebooks, modules, or any PDF that needs text extraction or visual analysis. Creates one text file and one image per page in a subdirectory.
---

# PDF Reading

Extract text and images from PDF files to enable accurate page-by-page reading and analysis. This skill converts PDFs into structured text and image files, making content accessible to LLMs while preserving page numbers and visual elements.

## When to Use This Skill

- Reading PDF game rulebooks, modules, or supplements
- Extracting text from PDF documents for analysis
- Converting scanned PDFs (images embedded in PDFs) for reading
- Needing accurate page number references from PDFs
- Analyzing both text and visual elements (maps, tables, diagrams) in PDFs

## Quick Start

Extract a PDF:
```bash
python scripts/extract_pdf.py "path/to/document.pdf"
```

This creates a subdirectory named after the PDF (without .pdf extension) containing:
- `page_0000.txt`, `page_0001.txt`, ... (text content)
- `page_0000.png`, `page_0001.png`, ... (page images)

## Output Structure

For a PDF named `Shadowdark RPG - V4-8.pdf`, the output structure is:

```
Shadowdark RPG - V4-8/
├── page_0000.txt
├── page_0000.png
├── page_0001.txt
├── page_0001.png
├── page_0002.txt
├── page_0002.png
└── ...
```

**Page numbering**: Files use 4-digit zero-padded numbers (0000, 0001, etc.) starting from 0 for proper sorting. The first page in the PDF = `page_0000.txt` and `page_0000.png` (typically the title page).

## Usage Patterns

### Extract to default location
```bash
python scripts/extract_pdf.py "document.pdf"
```
Creates `document/` subdirectory next to the PDF.

### Extract to custom directory
```bash
python scripts/extract_pdf.py "document.pdf" --output-dir "extracted_content"
```

### Reading extracted content
After extraction, read specific pages:
- Text: `cat "Shadowdark RPG - V4-8/page_0015.txt"`
- Image: View or analyze `page_0015.png` using vision capabilities

## Benefits

**Accurate page references**: File names directly correspond to PDF page numbers, making it easy to cite sources (page 0 is the first page/title page, page 23 → `page_0023.txt`)

**Dual format**: Text files for fast reading and searching; images for visual elements (maps, tables, artwork, complex layouts)

**Scanned PDF support**: Even image-based PDFs (scanned books) can be analyzed via the extracted PNG images

**Token efficiency**: Read only the pages you need rather than loading entire PDFs

## Dependencies

Required Python packages:
- PyMuPDF (fitz) - PDF processing
- Pillow (PIL) - Image handling

Install with:
```bash
pip install PyMuPDF Pillow
```

Both packages are available in the standard Python ecosystem and work across platforms.

## Script Behavior

### Command Line Options

```bash
python scripts/extract_pdf.py <pdf_file> [--output-dir <directory>]
```

**Arguments**:
- `<pdf_file>` (required) - Path to the PDF file to extract
- `--output-dir` (optional) - Custom output directory; defaults to subdirectory named after the PDF

### Extraction Details

**Image quality**: 2x zoom (~144 DPI) in PNG format for clear text and diagrams

**File naming**: 4-digit zero-padded numbers starting from 0 (page_0000.txt = first page)

**Output**: Creates paired files for each page (`.txt` for text, `.png` for image)

**Error handling**: Validates inputs, creates directories, fails explicitly with clear messages

**Progress**: Shows real-time progress for each page during extraction

## Efficient Navigation Strategy

**Find the table of contents and index first** to navigate books efficiently:

1. **Extract the PDF** (one-time setup)
2. **Locate navigation pages**:
   - Table of Contents: Usually pages 0-5 (title page, copyright, ToC)
   - Index: Usually last few pages of the book
3. **Read these key pages** to understand the book's structure
4. **Use page references** from ToC/index to jump directly to relevant content

### Finding Table of Contents

```bash
# Check first 10 pages for table of contents
cat "Shadowdark RPG - V4-8/page_0000.txt"  # Title page
cat "Shadowdark RPG - V4-8/page_0001.txt"  # Often copyright/credits
cat "Shadowdark RPG - V4-8/page_0002.txt"  # ToC often starts here
cat "Shadowdark RPG - V4-8/page_0003.txt"
```

### Finding the Index

```bash
# Check last few pages for index
ls "Shadowdark RPG - V4-8/page_*.txt" | Select-Object -Last 5

# Read the last page
cat "Shadowdark RPG - V4-8/page_0331.txt"  # Adjust based on total pages
```

### Using ToC/Index for Navigation

Once you've found the ToC or index:

1. **Search within the navigation pages** for your topic
2. **Note the page numbers** listed
3. **Jump directly to those pages** (remember to use 4-digit format)

Example: ToC says "Character Creation - page 12"
```bash
cat "Shadowdark RPG - V4-8/page_0012.txt"
```

**Pro tip**: The page numbers in the ToC/index refer to the book's printed page numbers, which typically match the file numbers (page_0012.txt = page 12 in the book). However, if the book has a preface or introduction with Roman numerals, you may need to add an offset.

## Example Workflow

1. **Extract PDF**:
   ```bash
   python scripts/extract_pdf.py "Shadowdark RPG - V4-8.pdf"
   ```

2. **Read table of contents** (find structure):
   ```bash
   cat "Shadowdark RPG - V4-8/page_0002.txt"
   cat "Shadowdark RPG - V4-8/page_0003.txt"
   ```

3. **Search for content** (when you don't know the page):
   ```bash
   grep -r "death saving throw" "Shadowdark RPG - V4-8/"
   ```

4. **Read specific page** (when you know where to look):
   ```bash
   cat "Shadowdark RPG - V4-8/page_0042.txt"
   ```

5. **Analyze visual elements**: Review `page_0042.png` to see tables, stat blocks, or illustrations that accompany the text.

## Troubleshooting

**"Missing required package" error**: Install dependencies with `pip install PyMuPDF Pillow`

**"PDF file not found" error**: Check the file path. Use quotes around paths with spaces.

**"File is not a PDF" error**: Ensure the file has a .pdf extension and is a valid PDF.

**Empty or garbled text files**: Some PDFs are purely images (scanned). Use the PNG image files for these pages instead.

## Best Practices

- **Start with navigation pages**: Read the table of contents and index first to understand structure
- **Extract PDFs once** and reference the extracted files multiple times
- **Use ToC/index for direct access**: Jump to specific pages when you know what you're looking for
- **Use grep for discovery**: Search across all pages when exploring unfamiliar topics
- **Use text files** for searching and quick reading
- **Use image files** for maps, tables, complex layouts, and visual verification
- **Keep extracted directories organized** by source document name
- **Cite page numbers** directly from filenames (page_0000.txt = page 0/title page, page_0023.txt = page 23)
- **Remember page 0**: The first page is page_0000.txt (often the title or cover page)