#!/usr/bin/env python3

import os
import re
from pathlib import Path

def fix_quotes_in_links(filepath):
    """Replace quotes in href/src URLs only, not in HTML delimiters"""

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    def fix_link(match):
        prefix = match.group(1)  # href=" or src="
        target = match.group(2)  # the URL
        suffix = match.group(3)  # "

        # Replace both %22 and literal " with ' in the URL
        fixed_target = target.replace('%22', "'").replace('"', "'")

        return f'{prefix}{fixed_target}{suffix}'

    # Fix href and src attributes
    content = re.sub(r'(href=")(.*?)(")', fix_link, content)
    content = re.sub(r'(src=")(.*?)(")', fix_link, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Rename files: replace %22 and " with single quote
    renamed_map = {}

    for html_file in Path('.').glob('*.html'):
        old_name = html_file.name
        # Replace both %22 and actual " with single quote
        new_name = old_name.replace('%22', "'").replace('"', "'")

        if old_name != new_name:
            new_path = html_file.parent / new_name
            print(f"Renaming: {old_name} -> {new_name}")
            html_file.rename(new_path)
            renamed_map[old_name] = new_name

    print(f"\nDone renaming {len(renamed_map)} files!")

    # Now fix links in all HTML files
    print("\nFixing links in HTML files...")

    count = 0
    for html_file in Path('.').glob('*.html'):
        try:
            fix_quotes_in_links(html_file)
            count += 1
            if count % 100 == 0:
                print(f"Processed {count} files...")
        except Exception as e:
            print(f"Error: {html_file}: {e}")

    print(f"Done! Fixed links in {count} files.")

if __name__ == '__main__':
    main()
