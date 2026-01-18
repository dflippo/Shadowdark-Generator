# Agent Skills

This workspace includes specialized agent skills to assist with Shadowdark RPG
game mastering and document management.

## Project Layout

This section outlines the structure of the project files to help you navigate
and understand where resources are located.

- **.agent/**: Contains the agent skills, configuration files, and workflows that
  power the agent's capabilities in this workspace.
- **campaigns/**: The directory where all campaign-specific notes, session logs,
  and tracking documents are stored.
  - **CAMPAIGN_MANAGEMENT_GUIDE.md**: Instructions for managing campaigns.
  - **River of Night/** (Example Campaign Folder):
    - **CAMPAIGN.md**: The main campaign bible and reference document.
    - **CAMPAIGN_NOTES.md**: Running notes, todos, and scratchpad for the
      campaign.
    - **Session 01 - The House on Mivvin's Rest.md**: Session log.
    - **Session 02 - The Proving Ground.md**: Session log.
    - **Session 03 - Teeth in the Night.md**: Session log.
    - **tracker**: File for tracking initiative or other states.
    - **maps/**: Directory for campaign maps.
- **shadowdark-library/**: A centralized library for Shadowdark RPG resources.
  - **adventures/**: Pre-written adventures and modules.
    - **Cursed Scroll 4 - River of Night V1-2 (horizontal pages).pdf**:
      Adventure PDF.
    - **ADVENTURES_GUIDE.md**: Usage instructions.
  - **core-rules/**: Core rulebooks and supplements.
    - **Shadowdark RPG - V4-8.pdf**: The core rulebook PDF.
    - **CORE_RULES_GUIDE.md**: Usage instructions.
  - **monsters/**: Monster statistics and lore.
    - **MONSTERS_AND_TABLES.md**: Comprehensive markdown of monster stats and
      tables.
    - **MONSTERS_GUIDE.md**: Usage instructions.
  - **other/**: Miscellaneous resources.
    - **OTHER_RESOURCES_GUIDE.md**: Usage instructions.
- **AGENT.md**: The primary documentation file for the agent, listing available
  skills and how to use them.
- **AGENTS.md**: Additional documentation regarding agent rules and skills.
- **refresh_anthropic_skills.sh**: A shell script used to update and refresh the
  Anthropic skills definition.
- **LICENSE**: The license file for the project.
- **README.md**: The project's readme file.

## Available Skills

## Skill Index (Direct SKILL.md Links)

Below is a consolidated index of every skill's primary `SKILL.md` with a concise
usage description:

- Shadowdark Module Generator – Create detailed Shadowdark RPG session notes
  (atmosphere, NPC dialog, traps, puzzles, stat blocks, map extraction).
  [Link](.agent/skills/shadowdark-module-generator/SKILL.md)
- PDF Reading – Extract per-page text & images from PDFs for precise referencing
  and visual analysis. [Link](.agent/skills/pdf-reader/SKILL.md)
- Algorithmic Art – Generate original p5.js-based algorithmic art using seeded
  randomness, flow fields, particles.
  [Link](.agent/skills/skills-main/algorithmic-art/SKILL.md)
- Artifacts Builder – Build complex multi-component HTML artifacts (React,
  Tailwind, shadcn/ui) with bundling.
  [Link](.agent/skills/skills-main/artifacts-builder/SKILL.md)
- Brand Guidelines – Apply Anthropic brand colors and typography to artifacts
  for consistent styling.
  [Link](.agent/skills/skills-main/brand-guidelines/SKILL.md)
- Canvas Design – Formulate and visually express design philosophies into
  PNG/PDF art pieces. [Link](.agent/skills/skills-main/canvas-design/SKILL.md)
- Internal Comms – Produce structured internal communications (3P updates,
  newsletters, FAQs, reports).
  [Link](.agent/skills/skills-main/internal-comms/SKILL.md)
- MCP Builder – Guide for designing high-quality MCP servers integrating
  external APIs/workflows.
  [Link](.agent/skills/skills-main/mcp-builder/SKILL.md)
- Skill Creator – Instructions for crafting effective new skills with metadata,
  workflows, resources.
  [Link](.agent/skills/skills-main/skill-creator/SKILL.md)
- Slack GIF Creator – Toolkit for optimized Slack GIF/emoji creation with
  validators & animation primitives.
  [Link](.agent/skills/skills-main/slack-gif-creator/SKILL.md)
- Template Skill – Minimal starter template for creating a new skill (add proper
  description before use).
  [Link](.agent/skills/skills-main/template-skill/SKILL.md)
- Theme Factory – Apply one of 10 preset or custom-generated color/font themes
  to artifacts. [Link](.agent/skills/skills-main/theme-factory/SKILL.md)
- Webapp Testing – Playwright-based toolkit for testing local web apps (server
  lifecycle, UI verification).
  [Link](.agent/skills/skills-main/webapp-testing/SKILL.md)
- DOCX (Document Skill) – Create/edit/analyze Word docs with tracked changes,
  comments, formatting.
  [Link](.agent/skills/skills-main/document-skills/docx/SKILL.md)
- PDF (Document Skill) – Programmatic PDF processing (text/table extraction,
  merge/split, forms).
  [Link](.agent/skills/skills-main/document-skills/pdf/SKILL.md)
- PPTX (Document Skill) – Presentation creation/editing (layouts, notes, XML
  unpacking, theming).
  [Link](.agent/skills/skills-main/document-skills/pptx/SKILL.md)
- XLSX (Document Skill) – Spreadsheet creation/editing with formulas,
  formatting, analysis & visualization.
  [Link](.agent/skills/skills-main/document-skills/xlsx/SKILL.md)

---

### 1. Shadowdark Module Generator

**Location**: `.agent/skills/shadowdark-module-generator/`

**Purpose**: Create detailed Shadowdark RPG sessions with atmospheric
descriptions, combat encounters, NPC interactions, and proper stat blocks.

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

**Reference**: Campaign-specific content in `campaign_docs/CAMPAIGN.md` (if
exists)

**Documentation**:
[.agent/skills/shadowdark-module-generator/SKILL.md](.agent/skills/shadowdark-module-generator/SKILL.md)

---

### 2. PDF Reading

**Location**: `.agent/skills/pdf-reader/`

**Purpose**: Extract text and images from PDF files for accurate page-by-page
analysis.

**Use When**:

- Working with PDF documents (rulebooks, modules, supplements)
- Need text extraction or visual analysis from PDFs
- Require accurate page number references
- Analyzing both text and visual elements (maps, tables, diagrams)
- Converting scanned PDFs for reading

**Key Features**:

- Extracts one text file and one image per page
- 4-digit zero-padded page numbering starting from 0 (page_0000.txt = first
  page)
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

**Documentation**:
[.claude/skills/pdf-reader/SKILL.md](.claude/skills/pdf-reader/SKILL.md)

---

## Using Skills

Skills are automatically available to the agent when working in this workspace.
The agent will activate the appropriate skill based on your request.

### Tips for Effective Use

1. **Be specific about your task**: Mention PDFs, Shadowdark adventures, or
   specific game content to trigger the right skill
2. **Reference extracted content**: Once PDFs are extracted, reference specific
   pages (e.g., "see page_0042.txt")
3. **Leverage navigation**: Use table of contents and indexes from extracted
   PDFs for efficient access
4. **Campaign continuity**: Update campaign_docs/CAMPAIGN.md for ongoing
   Shadowdark campaigns

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

**Workspace**: Shadowdark RPG Campaign Management  
**Last Updated**: October 19, 2025

---

### 3. Anthropic General Skills

**Location**: `.claude/skills/skills-main/`

**Purpose**: A collection of general-purpose skills from Anthropic to
demonstrate a range of capabilities.

**Use When**:

- You need additional capabilites that the skills provide

**Key Features**:

- A wide variety of creative, technical, and enterprise skills.
- Document creation and editing for formats like `.docx`, `.pdf`, `.pptx`, and
  `.xlsx`.

**Documentation**:
[.claude/skills/skills-main/README.md](.claude/skills/skills-main/README.md)

**Available Skills**:

- **algorithmic-art**: Create generative art using p5.js with seeded randomness,
  flow fields, and particle systems
- **canvas-design**: Design beautiful visual art in .png and .pdf formats using
  design philosophies
- **slack-gif-creator**: Create animated GIFs optimized for Slack's size
  constraints
- **artifacts-builder**: Build complex HTML artifacts using React, Tailwind CSS,
  and shadcn/ui components
- **mcp-server**: Guide for creating high-quality MCP servers to integrate
  external APIs and services
- **webapp-testing**: Test local web applications using Playwright for UI
  verification and debugging
- **brand-guidelines**: Apply Anthropic's official brand colors and typography
  to artifacts
- **internal-comms**: Write internal communications like status reports,
  newsletters, and FAQs
- **theme-factory**: Style artifacts with 10 pre-set professional themes or
  generate custom themes on-the-fly
- **skill-creator**: Guide for creating effective skills that extend Claude's
  capabilities
- **template-skill**: A basic template to use as a starting point for new skills
- **docx**: Create, edit, and analyze Word documents with support for tracked
  changes, comments, formatting preservation, and text extraction
- **pdf**: Comprehensive PDF manipulation toolkit for extracting text and
  tables, creating new PDFs, merging/splitting documents, and handling forms
- **pptx**: Create, edit, and analyze PowerPoint presentations with support for
  layouts, templates, charts, and automated slide generation
- **xlsx**: Create, edit, and analyze Excel spreadsheets with support for
  formulas, formatting, data analysis, and visualization
