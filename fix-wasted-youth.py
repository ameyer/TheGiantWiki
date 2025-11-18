#!/usr/bin/env python3

from pathlib import Path

def main():
    broken_pattern = '"Wasted_Youth_/_Your_Eyes_Here"_(CAC_Malaga_Edition).html'
    correct_pattern = "'Wasted_Youth_-_Your_Eyes_Here'_(CAC_Malaga_Edition).html"

    files_fixed = 0
    for html_file in Path('.').glob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            if broken_pattern in content:
                new_content = content.replace(broken_pattern, correct_pattern)
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_fixed += 1
                print(f"Fixed: {html_file.name}")
        except Exception as e:
            print(f"Error: {html_file}: {e}")

    print(f"\nFixed {files_fixed} files")

if __name__ == '__main__':
    main()
