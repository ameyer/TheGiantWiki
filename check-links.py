#!/usr/bin/env python3

import re
from pathlib import Path

def main():
    # Read the Category:Prints.html file
    with open('Category:Prints.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Extract all href links that point to local HTML files
    # Pattern: href="./filename.html"
    links = re.findall(r'href="\./(.*?\.html)"', content)

    # Get all actual HTML files in the directory
    actual_files = {f.name for f in Path('.').glob('*.html')}

    # Check which links are broken
    broken_links = []
    working_links = []

    for link in links:
        if link not in actual_files:
            broken_links.append(link)
        else:
            working_links.append(link)

    print(f"Total links checked: {len(links)}")
    print(f"Working links: {len(working_links)}")
    print(f"Broken links: {len(broken_links)}")

    if broken_links:
        print("\n=== BROKEN LINKS ===")
        # Group by reason
        for link in sorted(set(broken_links)):
            print(f"  {link}")

if __name__ == '__main__':
    main()
