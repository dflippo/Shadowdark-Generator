#!/usr/bin/env python3
"""
Auto-formatter for markdown files to remove hard text wrapping.
Preserves intentional formatting like lists, code blocks, headers, etc.
"""

import re
from pathlib import Path
from typing import List


def should_preserve_line(line: str) -> bool:
    """Check if a line should be preserved as-is (headers, lists, code, etc.)"""
    stripped = line.lstrip()
    
    # Preserve empty lines
    if not stripped:
        return True
    
    # Preserve headers
    if stripped.startswith('#'):
        return True
    
    # Preserve list items (-, *, +, numbered)
    if re.match(r'^[-*+]\s', stripped) or re.match(r'^\d+\.\s', stripped):
        return True
    
    # Preserve blockquotes
    if stripped.startswith('>'):
        return True
    
    # Preserve horizontal rules
    if re.match(r'^[-*_]{3,}$', stripped):
        return True
    
    # Preserve tables
    if '|' in line:
        return True
    
    # Preserve YAML-style metadata (key:: value)
    if '::' in line and not line.startswith(' '):
        return True
    
    # Preserve tags
    if stripped.startswith('#') and ' ' not in stripped:
        return True
    
    # Preserve bold/section markers at start of line
    if stripped.startswith('**') and stripped.endswith('**'):
        return True
    
    return False


def unwrap_markdown(content: str) -> str:
    """Unwrap hard-wrapped paragraphs in markdown content."""
    lines = content.split('\n')
    result = []
    i = 0
    in_code_block = False
    
    while i < len(lines):
        line = lines[i]
        
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            i += 1
            continue
        
        # Preserve everything in code blocks
        if in_code_block:
            result.append(line)
            i += 1
            continue
        
        # Preserve special lines
        if should_preserve_line(line):
            result.append(line)
            i += 1
            continue
        
        # Start of a paragraph - collect continuation lines
        paragraph_lines = [line]
        i += 1
        
        while i < len(lines):
            next_line = lines[i]
            
            # Stop at empty line
            if not next_line.strip():
                break
            
            # Stop at special formatting
            if should_preserve_line(next_line):
                break
            
            # Check if this looks like a continuation (doesn't start with special chars)
            # and has reasonable indentation continuity
            if not next_line.strip().startswith(('**', '-', '*', '+', '>', '#', '|')):
                # Check indentation - continuations often have extra indent
                curr_indent = len(line) - len(line.lstrip())
                next_indent = len(next_line) - len(next_line.lstrip())
                
                # If significantly more indented, it might be a continuation
                # or if same level and looks like prose
                if next_indent <= curr_indent + 2:
                    paragraph_lines.append(next_line.strip())
                    i += 1
                else:
                    break
            else:
                break
        
        # Join paragraph lines with spaces
        if len(paragraph_lines) > 1:
            # Preserve original indentation of first line
            indent = len(paragraph_lines[0]) - len(paragraph_lines[0].lstrip())
            joined = ' '.join(line.strip() for line in paragraph_lines)
            result.append(' ' * indent + joined)
        else:
            result.append(paragraph_lines[0])
    
    return '\n'.join(result)


def format_markdown_file(file_path: Path, dry_run: bool = False) -> bool:
    """Format a single markdown file. Returns True if changes were made."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        formatted_content = unwrap_markdown(original_content)
        
        if original_content != formatted_content:
            if not dry_run:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(formatted_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Format markdown files to remove hard text wrapping'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show which files would be changed without modifying them'
    )
    parser.add_argument(
        '--path',
        type=str,
        default='.',
        help='Root path to search for markdown files (default: current directory)'
    )
    parser.add_argument(
        '--exclude',
        type=str,
        nargs='*',
        default=['node_modules', '.git', 'logseq/bak'],
        help='Directories to exclude from search'
    )
    
    args = parser.parse_args()
    
    root_path = Path(args.path)
    exclude_patterns = args.exclude
    
    # Find all markdown files
    md_files = []
    for md_file in root_path.rglob('*.md'):
        # Check if file is in excluded directory
        if any(excluded in md_file.parts for excluded in exclude_patterns):
            continue
        md_files.append(md_file)
    
    print(f"Found {len(md_files)} markdown files")
    
    if args.dry_run:
        print("\n=== DRY RUN MODE - No files will be modified ===\n")
    
    changed_files = []
    for md_file in md_files:
        if format_markdown_file(md_file, dry_run=args.dry_run):
            changed_files.append(md_file)
            status = "[WOULD CHANGE]" if args.dry_run else "[CHANGED]"
            print(f"{status} {md_file}")
    
    print(f"\n{len(changed_files)} file(s) {'would be' if args.dry_run else 'were'} modified")
    
    if args.dry_run and changed_files:
        print("\nRun without --dry-run to apply changes")


if __name__ == '__main__':
    main()
