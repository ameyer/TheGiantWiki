#!/usr/bin/env python3

import re
from pathlib import Path

def main():
    broken_links = [
        "Face_to_%2AFace.html",
        "Flaming_Lips_New_Year's_Eve.html",
        "Greetings_from_Iraq.html",
        "N%2AE%2AR%2AD:_Cracked_But_Unbroken.html",
        "NØISE_Little_Lions.html",
        "POP_Wave_(Gold)_Shepard_Fairey_X_Craig_Stecyk_III.html",
        "Print_and_Destroy_Letterpress.html",
        "Psychedelic_Andre_('92_Obey_Giant_Blotter_Variant).html",
        "Smoke_'Em_While_You_Got_'Em.html",
        "This_is_a_Poster_Offset.html",
    ]

    # Get all HTML files
    all_files = {f.name for f in Path('.').glob('*.html')}

    for broken in broken_links:
        print(f"\n=== Looking for: {broken} ===")

        # Try various transformations
        search_terms = [
            broken.replace('%2A', '*'),
            broken.replace('%2A', '').replace('**', '*'),
            broken.replace('ø', 'o'),
            broken.replace('Ø', 'O'),
            broken.split('_')[0] + '_' + broken.split('_')[1] if '_' in broken else broken,
        ]

        # Search for partial matches
        for search in search_terms:
            matches = [f for f in all_files if search[:10].lower() in f.lower()]
            if matches:
                for match in sorted(matches)[:5]:
                    print(f"  Possible: {match}")
                break

if __name__ == '__main__':
    main()
