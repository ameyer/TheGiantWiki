#!/usr/bin/env python3

import os
import re
from pathlib import Path

def add_dot_slash(filepath):
    """Add ./ to relative links"""

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    def fix_link(match):
        prefix = match.group(1)  # href=" or src="
        target = match.group(2)  # the URL
        suffix = match.group(3)  # "

        # Skip if already has ./ or ../
        if target.startswith(('./', '../')):
            return match.group(0)

        # Skip external URLs, anchors
        if target.startswith(('http://', 'https://', '#', 'mailto:', '/')):
            return match.group(0)

        # Skip empty
        if not target:
            return match.group(0)

        # Add ./
        return f'{prefix}./{target}{suffix}'

    content = re.sub(r'(href=")(.*?)(")', fix_link, content)
    content = re.sub(r'(src=")(.*?)(")', fix_link, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    html_files = list(Path('.').glob('*.html'))
    total = len(html_files)

    print(f"Adding ./ to links in {total} HTML files...")

    for i, html_file in enumerate(html_files, 1):
        try:
            add_dot_slash(html_file)

            if i % 100 == 0:
                print(f"Processed {i} / {total} files...")
        except Exception as e:
            print(f"Error processing {html_file}: {e}")

    print(f"Done! Processed {total} files.")

if __name__ == '__main__':
    main()
