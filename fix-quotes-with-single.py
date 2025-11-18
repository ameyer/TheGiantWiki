#!/usr/bin/env python3

import os
import re
from pathlib import Path

def main():
    # Rename files: replace %22 and " with single quote '
    renamed_map = {}

    # Specific patterns for files with quotation marks (not apostrophes)
    patterns = [
        ('%22The_End%22', "'The_End'"),
        ('%22Bob%22', "'Bob'"),
        ('%22Disorder%22', "'Disorder'"),
        ('%22Chaos%22', "'Chaos'"),
        ('%22Wasted_Youth', "'Wasted_Youth"),
        ('Eyes_Here%22', "Eyes_Here'"),
    ]

    for html_file in Path('.').glob('*.html'):
        old_name = html_file.name
        new_name = old_name

        # Apply specific patterns
        for old_pattern, new_pattern in patterns:
            new_name = new_name.replace(old_pattern, new_pattern)

        if old_name != new_name:
            new_path = html_file.parent / new_name
            print(f"Renaming: {old_name} -> {new_name}")
            html_file.rename(new_path)
            renamed_map[old_name] = new_name

    print(f"\nDone renaming {len(renamed_map)} files!")

    # Fix links in all HTML files using regex
    print("\nFixing links in HTML files...")

    count = 0
    for html_file in Path('.').glob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            def fix_href(match):
                prefix = match.group(1)  # 'href="' or 'src="'
                url = match.group(2)      # the URL value
                suffix = match.group(3)   # '"'

                # Apply patterns to the URL
                new_url = url
                for old_pattern, new_pattern in patterns:
                    new_url = new_url.replace(old_pattern, new_pattern)

                return f'{prefix}{new_url}{suffix}'

            # Use regex to only replace within href/src attribute values
            new_content = re.sub(r'(href=")(.*?)(")', fix_href, content)
            new_content = re.sub(r'(src=")(.*?)(")', fix_href, new_content)

            if content != new_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                if count % 100 == 0:
                    print(f"Processed {count} files...")
        except Exception as e:
            print(f"Error: {html_file}: {e}")

    print(f"Done! Fixed links in {count} files.")

if __name__ == '__main__':
    main()
