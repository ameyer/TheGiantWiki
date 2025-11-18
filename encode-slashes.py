#!/usr/bin/env python3

import os
import re
from pathlib import Path

def encode_slashes_in_links(filepath):
    """Encode / as %2F in href/src links to match filenames"""

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    def fix_link(match):
        prefix = match.group(1)  # href=" or src="
        target = match.group(2)  # the URL
        suffix = match.group(3)  # "

        # Skip if doesn't start with ./
        if not target.startswith('./'):
            return match.group(0)

        # Skip external URLs, anchors
        if target.startswith(('http://', 'https://', '#', 'mailto:')):
            return match.group(0)

        # Skip resource paths (images, skins)
        if target.startswith('./images/') or target.startswith('./skins/'):
            return match.group(0)

        # Encode slashes after the ./
        # ./Black_Sabbath_(Red/Black).html -> ./Black_Sabbath_(Red%2FBlack).html
        rest_of_path = target[2:]  # Everything after ./
        encoded_rest = rest_of_path.replace('/', '%2F')
        encoded_target = './' + encoded_rest

        return f'{prefix}{encoded_target}{suffix}'

    content = re.sub(r'(href=")(.*?)(")', fix_link, content)
    content = re.sub(r'(src=")(.*?)(")', fix_link, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    html_files = list(Path('.').glob('*.html'))
    total = len(html_files)

    print(f"Encoding slashes in {total} HTML files...")

    for i, html_file in enumerate(html_files, 1):
        try:
            encode_slashes_in_links(html_file)

            if i % 100 == 0:
                print(f"Processed {i} / {total} files...")
        except Exception as e:
            print(f"Error processing {html_file}: {e}")

    print(f"Done! Processed {total} files.")

if __name__ == '__main__':
    main()
