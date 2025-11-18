#!/usr/bin/env python3

import re
from pathlib import Path

def main():
    # Links to remove - pages that don't exist
    links_to_remove = [
        'Category_talk:Prints.html',
        'Template:Print-Preload.html',
        'Template:Print-preload.html',
        'NØISE_Little_Lions.html',
        "Psychedelic_Andre_('92_Obey_Giant_Blotter_Variant).html",
        "Smoke_'Em_While_You_Got_'Em.html",
    ]

    files_modified = 0
    total_removals = 0

    for html_file in Path('.').glob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            original_content = content
            removals_in_file = 0

            for link in links_to_remove:
                # Match the entire list item containing this link
                # Pattern: <li><a href="./LINK">...</a></li>
                pattern = rf'<li><a href="\./{ re.escape(link) }"[^>]*>.*?</a></li>\s*'
                matches = re.findall(pattern, content)
                if matches:
                    content = re.sub(pattern, '', content)
                    removals_in_file += len(matches)

            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_modified += 1
                total_removals += removals_in_file
                print(f"Modified {html_file.name}: removed {removals_in_file} broken links")

        except Exception as e:
            print(f"Error processing {html_file}: {e}")

    print(f"\nTotal: Modified {files_modified} files, removed {total_removals} broken links")

if __name__ == '__main__':
    main()
