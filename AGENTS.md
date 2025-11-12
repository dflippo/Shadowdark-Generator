# Agent Rules

This workspace includes specialized skills to assist with Shadowdark RPG game mastering and document management.


### 1. Shadowdark Module Generator

**Location**: `.claude/skills/shadowdark-module-generator/`

**Purpose**: Create detailed Shadowdark RPG sessions with atmospheric descriptions, combat encounters, NPC interactions, and proper stat blocks.

**Use When**:
- Writing RPG adventures and game master notes
- Creating session content for Shadowdark games
- Need proper monster stat blocks and encounter design
- Generating atmospheric grim-dark descriptions
- Working with Shadowdark campaign content

**Key Features**:
- Grim-dark atmospheric writing style
- Proper Shadowdark stat block formatting
- Monster abilities and special powers
- Compass-based navigation descriptions
- Campaign continuity tracking
- Map extraction from Shadowdark PDFs

**Campaign Equipment Rule**:
Shadowdark in this workspace uses classic fantasy tech (steel, alchemy, occasional clockwork). Firearms/guns do not exist; references to pistols or rifles should be reinterpreted as crossbows or other medieval equivalents.

**Reference**: Campaign-specific content in `campaign_docs/CAMPAIGN.md` (if exists)

**Documentation**: [.claude/skills/shadowdark-module-generator/SKILL.md](.claude/skills/shadowdark-module-generator/SKILL.md)

---

### 2. PDF Reading

**Location**: `.claude/skills/pdf-reader/`

**Purpose**: Extract text and images from PDF files for accurate page-by-page analysis.

**Use When**:
- Working with PDF documents (rulebooks, modules, supplements)
- Need text extraction or visual analysis from PDFs
- Require accurate page number references
- Analyzing both text and visual elements (maps, tables, diagrams)
- Converting scanned PDFs for reading

**Key Features**:
- Extracts one text file and one image per page
- 4-digit zero-padded page numbering starting from 0 (page_0000.txt = first page)
- Supports large documents (up to 9,999 pages)
- Efficient navigation using table of contents and indexes
- PNG images at 144 DPI for quality and reasonable file sizes

**Output Structure**:
```
Document Name/
├── page_0000.txt (text content)
├── page_0000.png (page image)
├── page_0001.txt
├── page_0001.png
└── ...
```

**Quick Start**:
```bash
python .claude/skills/pdf-reader/scripts/extract_pdf.py "document.pdf"
```

**Documentation**: [.claude/skills/pdf-reader/SKILL.md](.claude/skills/pdf-reader/SKILL.md)

---

## Using Skills

Skills are automatically available to the agent when working in this workspace. The agent will activate the appropriate skill based on your request.

### Tips for Effective Use

1. **Be specific about your task**: Mention PDFs, Shadowdark adventures, or specific game content to trigger the right skill
2. **Reference extracted content**: Once PDFs are extracted, reference specific pages (e.g., "see page_0042.txt")
3. **Leverage navigation**: Use table of contents and indexes from extracted PDFs for efficient access
4. **Campaign continuity**: Update campaign_docs/CAMPAIGN.md for ongoing Shadowdark campaigns

## Skill Development

Skills follow general best practices for agent tool use:
- Concise documentation assuming agent intelligence
- Progressive disclosure (main docs in SKILL.md, details in separate files)
- Utility scripts handle errors explicitly
- Platform-agnostic paths (forward slashes)
- Dependencies clearly documented

## Adding New Skills

To add a new skill to this workspace:

1. Create directory: `.claude/skills/skill-name/`
2. Add `SKILL.md` with YAML frontmatter (name, description)
3. Include scripts in `scripts/` subdirectory if needed
4. Add reference to this AGENTS.md file
5. Test with all agent models you plan to use

---

### 3. Anthropic General Skills

**Location**: `.claude/skills/skills-main/`

**Purpose**: A collection of general-purpose skills from Anthropic to demonstrate a range of capabilities.

**Use When**:
- You need additional capabilites that the skills provide

**Key Features**:
- A wide variety of creative, technical, and enterprise skills.
- Document creation and editing for formats like `.docx`, `.pdf`, `.pptx`, and `.xlsx`.

**Documentation**: [.claude/skills/skills-main/README.md](.claude/skills/skills-main/README.md)

**Available Skills**:
-- **algorithmic-art**: Generative p5.js art (flow fields, particles, seeded randomness)
-- **canvas-design**: Visual philosophy design exports (PNG/PDF)
-- **slack-gif-creator**: Size-optimized animated GIF & emoji creation
-- **artifacts-builder**: React + Tailwind + shadcn/ui artifact construction
-- **mcp-server**: High-quality Model Context Protocol server design guidance
-- **webapp-testing**: Playwright automation for local web app testing
-- **brand-guidelines**: Anthropic brand color & typography application
-- **internal-comms**: Structured status reports, newsletters, FAQs
-- **theme-factory**: Preset/custom theme generation & application
-- **skill-creator**: Instructions for crafting new workspace skills
-- **template-skill**: Minimal starter scaffold for a new skill
-- **docx**: Word doc creation/editing (tracked changes, comments)
-- **pdf**: Extraction, merge/split, table & form handling
-- **pptx**: Slide generation/editing (layouts, charts, theming)
-- **xlsx**: Spreadsheet formulas, analysis, visualization

---

## Unified Skill Catalog (All Skills)

Shadowdark & Core Tools:
- Shadowdark Module Generator – Session notes, NPCs, traps, stat blocks, map extraction. [SKILL](.claude/skills/shadowdark-module-generator/SKILL.md)
- PDF Reading – Per-page text/image extraction for reference. [SKILL](.claude/skills/pdf-reader/SKILL.md)

Generative & Visual:
- Algorithmic Art – Generative p5.js art. [SKILL](.claude/skills/skills-main/algorithmic-art/SKILL.md)
- Canvas Design – Visual design compositions. [SKILL](.claude/skills/skills-main/canvas-design/SKILL.md)
- Slack GIF Creator – Optimized GIF/emoji output. [SKILL](.claude/skills/skills-main/slack-gif-creator/SKILL.md)
- Artifacts Builder – Complex HTML artifacts (React/Tailwind/shadcn/ui). [SKILL](.claude/skills/skills-main/artifacts-builder/SKILL.md)
- Theme Factory – Apply/generate themes. [SKILL](.claude/skills/skills-main/theme-factory/SKILL.md)
- Brand Guidelines – Anthropic brand tokens. [SKILL](.claude/skills/skills-main/brand-guidelines/SKILL.md)

Productivity & Communication:
- Internal Comms – Reports, newsletters, FAQs. [SKILL](.claude/skills/skills-main/internal-comms/SKILL.md)
- Skill Creator – Build new skills. [SKILL](.claude/skills/skills-main/skill-creator/SKILL.md)
- Template Skill – Starter scaffold. [SKILL](.claude/skills/skills-main/template-skill/SKILL.md)

Testing & Integration:
- Webapp Testing – Playwright harness. [SKILL](.claude/skills/skills-main/webapp-testing/SKILL.md)
- MCP Builder – MCP server design. [SKILL](.claude/skills/skills-main/mcp-builder/SKILL.md)

Document & Data:
- DOCX – Word docs w/ tracked changes. [SKILL](.claude/skills/skills-main/document-skills/docx/SKILL.md)
- PDF – Extraction, forms, manipulation. [SKILL](.claude/skills/skills-main/document-skills/pdf/SKILL.md)
- PPTX – Slide automation/editing. [SKILL](.claude/skills/skills-main/document-skills/pptx/SKILL.md)
- XLSX – Formulas, analysis, viz. [SKILL](.claude/skills/skills-main/document-skills/xlsx/SKILL.md)

Quick Tips:
1. Reference pages directly after PDF extraction (e.g., page_0042.txt).
2. Keep `<campaingn>/CAMPAIGN_NOTES.md` and `<campaingn>/CAMPAIGN.md` updated for session continuity.
3. Use Module Generator for encounter scaffolding; PDF Reader for rules.
4. Document skills produce polished player handouts.

**Last Updated (Catalog Move)**: October 23, 2025
