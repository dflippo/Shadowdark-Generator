# Campaigns Directory — Campaign Management Guide

This directory holds your campaign-specific materials: session notes, maps, NPC writeups, handouts, and campaign reference documents.

## Current Structure (River of Night Campaign)

```
campaigns/
├── CAMPAIGN_MANAGEMENT_GUIDE.md (this file)
└── River of Night/
  ├── CAMPAIGN.md              # Main campaign bible and reference
  ├── CAMPAIGN_NOTES.md        # Running notes, todos, scratchpad
  ├── Session 01 - The House on Mivvin's Rest.md
  ├── Session 02 - The Proving Ground.md
  ├── Session 03 - Teeth in the Night.md
  ├── Session 04 - The Serpent's Eye.md
  ├── Session 05 - The Burden of Beasts.md
  ├── Session 06 - The Albion Dominion.md
  ├── Session 07 - The Jungle Strikes Back.md
  ├── tracker              # Initiative/state tracking
  ├── maps/
  │   └── MAPS_README.md
  └── npcs/                # NPC documentation by faction
      ├── README.md
      ├── mivvins-rest/    # Patron and allies
      ├── albion-dominion/ # Military NPCs
      ├── basilisk-cult/   # Antagonists
      ├── jungle-spirits/  # Supernatural entities
      └── servants/        # Minor characters
```

**Quick Links:**

- [CAMPAIGN.md](River%20of%20Night/CAMPAIGN.md) - Main campaign reference
- [CAMPAIGN_NOTES.md](River%20of%20Night/CAMPAIGN_NOTES.md) - Working notes
- [Session 01](River%20of%20Night/Session%2001%20-%20The%20House%20on%20Mivvin's%20Rest.md) | [Session 02](River%20of%20Night/Session%2002%20-%20The%20Proving%20Ground.md) | [Session 03](River%20of%20Night/Session%2003%20-%20Teeth%20in%20the%20Night.md) | [Session 04](River%20of%20Night/Session%2004%20-%20The%20Serpent's%20Eye.md)
- [Session 05](River%20of%20Night/Session%2005%20-%20The%20Burden%20of%20Beasts.md) | [Session 06](River%20of%20Night/Session%2006%20-%20The%20Albion%20Dominion.md) | [Session 07](River%20of%20Night/Session%2007%20-%20The%20Jungle%20Strikes%20Back.md)
- [NPCs Directory](River%20of%20Night/npcs/NPC_DIRECTORY.md)
- [Party Roster](River%20of%20Night/party/PARTY_ROSTER.md)
- [Maps](River%20of%20Night/maps/MAPS_README.md)

## What to Store Here

- **Session Notes**: Detailed session logs with atmosphere, encounters, and outcomes
- **Campaign Documents**: CAMPAIGN.md (main reference), CAMPAIGN_NOTES.md (working notes)
- **Maps**: PNG/SVG/PDF maps used at the table (in maps/ subfolder)
- **NPC Files**: Detailed NPC documentation organized by faction/group (in npcs/ subfolder)
- **Tracking Files**: Initiative order, campaign state, party inventory

## What NOT to Commit

- **Commercial PDFs**: Do NOT commit purchased core rules, adventures, or manuals
- Use `shadowdark-library/` for local copies kept off the repo
- Ensure `.gitignore` prevents accidentally committing copyrighted PDFs
- Large binary files (use `shadowdark-library/` for extracted content instead) `shadowdark-library/` folder for local copies you keep off the repo, and ensure your `.gitignore` prevents accidentally committing copyrighted PDFs.

## Linking to Library Resources

### Shadowdark Library References

From campaign documents, use relative paths to reference library content:

**Core Rules:**

```markdown
[Core Rules Guide](../../shadowdark-library/core-rules/CORE_RULES_GUIDE.md) [Monsters & Tables](../../shadowdark-library/monsters/MONSTERS_AND_TABLES.md)
```

- [Core Rules Guide](../shadowdark-library/core-rules/CORE_RULES_GUIDE.md)
- [Monsters & Tables](../shadowdark-library/monsters/MONSTERS_AND_TABLES.md)
- [Monsters Guide](../shadowdark-library/monsters/MONSTERS_GUIDE.md)

  **Monster Stat Blocks:**

  ```markdown
  [Goblin](../../shadowdark-library/monsters/manual-monsters/goblin.md) [Basilisk](../../shadowdark-library/monsters/manual-monsters/basilisk.md)
  ```

- Example: [Goblin](../shadowdark-library/monsters/manual-monsters/goblin.md) | [Basilisk](../shadowdark-library/monsters/manual-monsters/basilisk.md) | [Treant](../shadowdark-library/monsters/manual-monsters/treant.md)

  **Adventures:**

  ```markdown
  [River of Night Adventure](../../shadowdark-library/adventures/ADVENTURES_GUIDE.md)
  ```

- [Adventures Guide](../shadowdark-library/adventures/ADVENTURES_GUIDE.md)
- [Other Resources](../shadowdark-library/other/OTHER_RESOURCES_GUIDE.md)

### Session Cross-References

Link between session files using wiki-style links (for Logseq compatibility):

```markdown
[[Session 01 - The House on Mivvin's Rest]] [[Session 02 - The Proving Ground]]
```

Or use relative paths:

```markdown
[Session 01](Session%2001%20-%20The%20House%20on%20Mivvin's%20Rest.md)
```

### NPC References

Link to NPC files from sessions or campaign documents:

**Wiki-style (recommended for Logseq):**

```markdown
[[Lady Lara Croft Johnson]] [[Colonel Percival Huzzard]]
```

**Relative paths:**

```markdown
[Lady Johnson](npcs/mivvins-rest/lady-lara-croft-johnson.md) [Colonel Huzzard](npcs/albion-dominion/colonel-percival-huzzard.md)
```

- Examples: [Lady Lara Croft Johnson](River%20of%20Night/npcs/mivvins-rest/lady-lara-croft-johnson.md) | [Allan Quatermain](River%20of%20Night/npcs/mivvins-rest/allan-quatermain.md)
- Military: [Colonel Huzzard](River%20of%20Night/npcs/albion-dominion/colonel-percival-huzzard.md) | [Captain Blackwood](River%20of%20Night/npcs/albion-dominion/captain-blackwood.md)

## NPC Organization

The `npcs/` folder organizes NPCs by faction/group for easy reference during gameplay:

- **mivvins-rest/**: Patron (Lady Johnson), allies (Quatermain), workers
- **albion-dominion/**: Military characters (Colonel Huzzard, officers)
- **basilisk-cult/**: Antagonists and cult members
- **jungle-spirits/**: Supernatural entities (Maied, Alistair's ghost)
- **servants/**: Minor characters and witnesses

  Each NPC file includes:

- Tags for Logseq (#npc, #faction-name, #status)
- Role, location, current status
- Physical description and personality
- Key relationships (with wiki-links to other NPCs)
- Notable events by session
- Combat stats (where applicable)
- Roleplay quotes
- GM notes

  See [npcs/NPC_DIRECTORY.md](River%20of%20Night/npcs/NPC_DIRECTORY.md) for the full NPC directory and relationship map.

## Logseq Integration

This workspace is optimized for Logseq, an open-source knowledge management tool:

**Setup:**

1. Open Logseq
2. Click "Open existing graph"
3. Select the `campaigns/River of Night/` folder

**Features:**

- **Wiki-links**: Use `[[double brackets]]` to link between files
- **Tags**: Use `#tags` for categorization and filtering
- **Graph View**: Visualize relationships between sessions, NPCs, and monsters
- **Backlinks**: See all references to a character or location automatically

  **Recommended Tags:**

- `#session` - Session notes
- `#npc` - Character files
- `#location` - Places and areas
- `#river-of-night` - Campaign identifier
- `#active` / `#deceased` / `#imprisoned` - NPC status

## Path Navigation Tips

- `..` steps up one directory from the current folder
- `../..` steps up two directories (e.g., from session to repo root)
- Adjust paths based on file nesting depth
- Use `%20` for spaces in file paths when using relative links
- Most editors and Logseq will open relative links when previewing Markdown

## Git Best Practices

- **Commit session notes** after each game session
- **Track NPC changes** when status updates occur
- **Version campaign documents** regularly (CAMPAIGN.md, CAMPAIGN_NOTES.md)
- Keep repository lightweight: only track markdown, small images, and tracking files
- Store large PDFs in `shadowdark-library/` (which is gitignored)
- Use the `*_GUIDE.md` files in `shadowdark-library/` to document where to obtain commercial content legallywn [[Session 01 - The House on Mivvin's Rest]] [[Session 02 - The Proving Ground]]

  ````

  Or use relative paths:
  ```markdown
  [Session 01](Session%2001%20-%20The%20House%20on%20Mivvin's%20Rest.md)
  ````

  ### NPC References

  Link to NPC files from sessions or campaign documents:

  **Wiki-style (recommended for Logseq):**

  ```markdown
  [[Lady Lara Croft Johnson]] [[Colonel Percival Huzzard]]
  ```

  **Relative paths:**

  ```markdown
  [Lady Johnson](npcs/mivvins-rest/lady-lara-croft-johnson.md) [Colonel Huzzard](npcs/albion-dominion/colonel-percival-huzzard.md)
  ```

- Examples: [Lady Lara Croft Johnson](River%20of%20Night/npcs/mivvins-rest/lady-lara-croft-johnson.md) | [Allan Quatermain](River%20of%20Night/npcs/mivvins-rest/allan-quatermain.md)
- Military: [Colonel Huzzard](River%20of%20Night/npcs/albion-dominion/colonel-percival-huzzard.md) | [Captain Blackwood](River%20of%20Night/npcs/albion-dominion/captain-blackwood.md)

  Notes about relative links

- `..` steps up one directory from the campaign folder to the repo root. Adjust the path if your file is nested deeper.
- If you move files, update the links accordingly. Most editors will open relative links when previewing Markdown.

  Preserving folders in Git

- Keep this repository lightweight: we track only the `INSTRUCTIONS.md` files inside `shadowdark-library`.
- If you need to make library content available to collaborators, consider storing it outside the repo or in a private storage location and adding a short `INSTRUCTIONS.md` pointing to where team members can obtain legal copies.
