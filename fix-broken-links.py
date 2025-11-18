#!/usr/bin/env python3

import re
from pathlib import Path

def main():
    # Mapping of broken links to correct files
    fixes = {
        'Face_to_%2AFace.html': 'Face_to_*Face.html',
        "Flaming_Lips_New_Year's_Eve.html": "Dalek_and_Shepard_Fairey_-_Flaming_Lips_New_Year's_Eve.html",
        'Greetings_from_Iraq.html': 'Greetings_From_Iraq.html',
        'N%2AE%2AR%2AD:_Cracked_But_Unbroken.html': 'N*E*R*D:_Cracked_But_Unbroken.html',
        'POP_Wave_(Gold)_Shepard_Fairey_X_Craig_Stecyk_III.html': 'POP_WAVE_(Gold)_Shepard_Fairey_X_Craig_Stecyk_III.html',
        'Print_and_Destroy_Letterpress.html': 'Print_And_Destroy_Letterpress.html',
        'This_is_a_Poster_Offset.html': 'This_Is_a_Poster_Offset.html',
    }

    # Read Category:Prints.html
    with open('Category:Prints.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply fixes
    changes_made = 0
    for broken, correct in fixes.items():
        if broken in content:
            content = content.replace(broken, correct)
            changes_made += 1
            print(f"Fixed: {broken} → {correct}")

    # Write back
    if changes_made > 0:
        with open('Category:Prints.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\nFixed {changes_made} broken links in Category:Prints.html")
    else:
        print("No changes needed")

if __name__ == '__main__':
    main()
