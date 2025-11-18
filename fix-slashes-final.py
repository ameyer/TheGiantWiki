#!/usr/bin/env python3

import os
from pathlib import Path

def main():
    # Rename files: replace %2F with -
    for html_file in Path('.').glob('*%2F*.html'):
        new_name = html_file.name.replace('%2F', '-')
        new_path = html_file.parent / new_name
        print(f"Renaming: {html_file.name} -> {new_name}")
        html_file.rename(new_path)

    print("Done renaming files!")

    # Now fix links in all HTML files
    print("\nFixing links in HTML files...")

    count = 0
    for html_file in Path('.').glob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Replace %2F with - in links
            new_content = content.replace('%2F', '-')

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
