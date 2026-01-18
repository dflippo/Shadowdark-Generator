---
trigger: always_on
glob: "**/*.md"
description: Rules for Shadowdark content generation
---

# Shadowdark Agent Rules

These rules govern how the agent should interact with the Shadowdark RPG
project.

## 1. Session Generation Protocol

- **ALWAYS** use the `shadowdark-module-generator` skill methodology when
  creating or expanding session notes.
- **NEVER** produce generic "AI" fantasy descriptions. Use the "grim-dark" tone:
  dangerous, visceral, and specific.
- **ALWAYS** reference the specific campaign context (`CAMPAIGN.md`) before
  writing.

## 2. Formatting & Mechanics

- **Stat Blocks:** Must strictly follow Shadowdark syntax (`AC`, `HP`, `ATK`,
  `MV`, `AL`, `LV`).
- **Navigation:** All movement descriptions must use absolute compass directions
  (North, South, East, West), never relative "left/right".
- **Read-Aloud Text:** Must be in blockquotes `>`.

## 3. Workflow Adherence

- If asked to "plan a session" or "write the next part", **ALWAYS** check for
  and trigger the defined workflow
  `.agent/workflows/generate-detailed-session.md`.

## 4. Setting Constraints

- **No Firearms/Gunpowder:** Black powder weapons do not exist. Use bows,
  crossbows (including heavy arbalests), and siege weapons instead.
