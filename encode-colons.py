#!/usr/bin/env python3

import os
import re
from pathlib import Path

def fix_colon_in_links(filepath):
    """Encode colons in href links"""

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Replace : with %3A in href and src attributes
    # Match href="something:something.html"
    def encode_colon(match):
        prefix = match.group(1)  # href=" or src="
        target = match.group(2)  # the URL
        suffix = match.group(3)  # "

        # Skip external URLs
        if target.startswith(('http://', 'https://', '#', 'mailto:')):
            return match.group(0)

        # Skip if it's a resource path
        if target.startswith(('images/', 'skins/')):
            return match.group(0)

        # Encode colons
        encoded_target = target.replace(':', '%3A')
        return f'{prefix}{encoded_target}{suffix}'

    content = re.sub(r'(href=")(.*?)(")', encode_colon, content)
    content = re.sub(r'(src=")(.*?)(")', encode_colon, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    html_files = list(Path('.').glob('*.html'))
    total = len(html_files)

    print(f"Encoding colons in {total} HTML files...")

    for i, html_file in enumerate(html_files, 1):
        try:
            fix_colon_in_links(html_file)

            if i % 100 == 0:
                print(f"Processed {i} / {total} files...")
        except Exception as e:
            print(f"Error processing {html_file}: {e}")

    print(f"Done! Processed {total} files.")

if __name__ == '__main__':
    main()
