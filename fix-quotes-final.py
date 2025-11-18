#!/usr/bin/env python3

import os
import re
from pathlib import Path

def main():
    # Step 1: Rename files to use %22 instead of quotes
    renamed_map = {}

    for html_file in Path('.').glob('*.html'):
        old_name = html_file.name
        # Replace both %22, ", and ' with %22
        new_name = old_name.replace('"', '%22').replace("'", '%22')

        if old_name != new_name:
            new_path = html_file.parent / new_name
            print(f"Renaming: {old_name} -> {new_name}")
            html_file.rename(new_path)
            renamed_map[old_name] = new_name

    print(f"\nDone renaming {len(renamed_map)} files!")

    # Step 2: Fix all links in HTML files
    print("\nFixing links in HTML files...")

    count = 0
    for html_file in Path('.').glob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Replace filenames that were renamed
            new_content = content
            for old_name, new_name in renamed_map.items():
                new_content = new_content.replace(old_name, new_name)

            # Also fix any remaining " or ' in .html links by replacing with %22
            # This regex finds href/src attributes and fixes quotes within them
            def fix_quotes_in_url(match):
                full_match = match.group(0)
                # Only process if it's pointing to an .html file
                if '.html' not in full_match:
                    return full_match
                # Replace " and ' with %22 in the URL part
                return full_match.replace('"The_End"', '%22The_End%22').replace("'The_End'", '%22The_End%22') \
                               .replace('"Bob"', '%22Bob%22').replace("'Bob'", '%22Bob%22') \
                               .replace('"Disorder"', '%22Disorder%22').replace("'Disorder'", '%22Disorder%22') \
                               .replace('"Chaos"', '%22Chaos%22').replace("'Chaos'", '%22Chaos%22') \
                               .replace('"Wasted_Youth', '%22Wasted_Youth').replace("'Wasted_Youth", '%22Wasted_Youth') \
                               .replace('Eyes_Here"', 'Eyes_Here%22').replace("Eyes_Here'", 'Eyes_Here%22')

            new_content = re.sub(r'href="[^"]*"', fix_quotes_in_url, new_content)
            new_content = re.sub(r'src="[^"]*"', fix_quotes_in_url, new_content)

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
