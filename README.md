# Shadowdark-Generator

The Shadowdark Generator is a toolkit designed to assist Dungeon Masters in creating immersive Shadowdark RPG sessions. It combines AI agent skills with structured campaign management to generate atmospheric descriptions, combat encounters, NPC interactions, and proper stat blocks.

## Key Features

### 1. Shadowdark Module Generator

- **Atmospheric Writing**: Generates grim-dark descriptions suitable for the Shadowdark setting.
- **Stat Blocks**: Provides accurate monster stat blocks with special abilities.
- **Encounter Design**: Creates detailed encounters with traps, puzzles, and multiple solution paths.
- **Navigation**: Uses precise compass directions for dungeon crawling.

### 2. PDF Reading & Extraction

- **Text & Image Extraction**: Converts PDF pages into text and image files for easy reference.
- **Page-by-Page Analysis**: Allows the agent to reference specific rules or module pages.
- **Script**: Includes `extract_pdf.py` for processing PDF documents.

### 3. Campaign Management

- **Structured Organization**: Dedicated folders for campaigns, session notes, and maps.
- **Continuity Tracking**: Maintains consistency across sessions using campaign bibles (`CAMPAIGN.md`).

## Project Structure

- **`.claude/`**: Contains agent skills and scripts.
  - `skills/shadowdark-module-generator/`: Core logic for session generation.
  - `skills/pdf-reader/`: Tools for PDF extraction.
- **`campaigns/`**: Stores your campaign data.
  - `River of Night/`: Example campaign folder.
- **`shadowdark-library/`**: Central repository for rules, adventures, and monster stats.
  - `core-rules/`: Rulebooks.
  - `adventures/`: Modules.
  - `monsters/`: Monster lists.

## Available Scripts

### PDF Extraction

To extract text and images from a PDF for use with the agent:

```bash
python .claude/skills/pdf-reader/scripts/extract_pdf.py "path/to/document.pdf"
```

## Usage

1.  **Setup**: Ensure your PDFs are in `shadowdark-library/`.
2.  **Campaign**: Create a folder in `campaigns/` for your game.
3.  **Generate**: Ask the agent to "Help me plan the next session for [Campaign Name]" or "Create a random encounter for level 3 characters."
4.  **Reference**: The agent will automatically use the skills to read rules and generate content.

## Credits

- **Shadowdark RPG**: Created by Kelsey Dionne.
- **Design Inspiration**: Based on "How To Write a D&D Adventure" by The Arcane Library.
