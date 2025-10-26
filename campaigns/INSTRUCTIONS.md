# Campaigns directory — what to put here and how to link to the library

This directory holds your campaign-specific materials: session notes, maps, NPC writeups, handouts, and campaign reference documents.

Recommended structure (example):

- campaigns/
	- River of Night/
		- INSTRUCTIONS.md        # Campaign-specific notes and pointers
		- CAMPAIGN_NOTES.md
		- CAMPAIGN_REFERENCE.md
		- maps/
		- Session 01 - The House on Mivvin's Rest.md
		- Session 02 - The Proving Ground.md

What to store here
- Session transcripts and session planning notes
- Maps (PNG/SVG) used at the table
- NPC & encounter notes specific to this campaign
- Player handouts (non-copyrighted or homebrew content)

What NOT to commit
- Do NOT commit copies of purchased commercial PDFs (core rules, adventures, manuals).
	Use the `shadowdark-library/` folder for local copies you keep off the repo, and ensure your `.gitignore`
	prevents accidentally committing copyrighted PDFs.

Linking to official/manual files in `shadowdark-library`
- To reference a file you keep in `shadowdark-library` from a campaign document, use a relative Markdown link.
	Example (from `campaigns/River of Night/CAMPAIGN_REFERENCE.md`):

	[Shadowdark Core Rules — Monsters](../shadowdark-library/core-rules/INSTRUCTIONS.md)

	If you want to link directly to an individual file inside the library (for example a monster stat block), use:

	[Goblin stat block](../shadowdark-library/monsters/manual-monsters/goblin.md)

Notes about relative links
- `..` steps up one directory from the campaign folder to the repo root. Adjust the path if your file is nested deeper.
- If you move files, update the links accordingly. Most editors will open relative links when previewing Markdown.

Preserving folders in Git
- Keep this repository lightweight: we track only the `INSTRUCTIONS.md` files inside `shadowdark-library`.
- If you need to make library content available to collaborators, consider storing it outside the repo or in a private storage location and adding a short `INSTRUCTIONS.md` pointing to where team members can obtain legal copies.

