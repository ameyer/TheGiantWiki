#!/usr/bin/env python3

import os
import re
from pathlib import Path

def main():
    # List of specific patterns to replace - only actual quotes, not apostrophes
    patterns_to_fix = [
        ('"The_End"', '%22The_End%22'),
        ('"Bob"', '%22Bob%22'),
        ('"Disorder"', '%22Disorder%22'),
        ('"Chaos"', '%22Chaos%22'),
        ('%22Wasted_Youth', '%22Wasted_Youth'),  # Already encoded
        ('Eyes_Here%22', 'Eyes_Here%22'),  # Already encoded
    ]

    renamed_map = {}

    # Rename files
    for html_file in Path('.').glob('*.html'):
        old_name = html_file.name
        new_name = old_name

        # Apply each pattern
        for old_pattern, new_pattern in patterns_to_fix:
            new_name = new_name.replace(old_pattern, new_pattern)

        if old_name != new_name:
            new_path = html_file.parent / new_name
            print(f"Renaming: {old_name} -> {new_name}")
            html_file.rename(new_path)
            renamed_map[old_name] = new_name

    print(f"\nDone renaming {len(renamed_map)} files!")

    # Fix links in all HTML files
    print("\nFixing links in HTML files...")

    count = 0
    for html_file in Path('.').glob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            new_content = content

            # Apply each pattern to the content
            for old_pattern, new_pattern in patterns_to_fix:
                new_content = new_content.replace(old_pattern, new_pattern)

            # Also update renamed files
            for old_name, new_name in renamed_map.items():
                new_content = new_content.replace(old_name, new_name)

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
