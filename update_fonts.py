"""
Font Update Script
Updates fonts to Playfair Display and Lato as per JMC theme
"""

import re

def update_fonts(input_file, output_file):
    """Update font families to match JMC theme"""

    print(f"Reading: {input_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # JMC Font scheme
    SERIF_FONT = '"Playfair Display", serif'
    SANS_FONT = '"Lato", sans-serif'

    print("\nUpdating font families...")
    print("=" * 80)

    # Common font replacements
    font_mappings = [
        # Generic sans-serif to Lato
        (r'font-family:\s*sans-serif', f'font-family: {SANS_FONT}'),
        (r'font-family:\s*-apple-system[^;]+;', f'font-family: {SANS_FONT};'),
        (r'font-family:\s*system-ui[^;]+;', f'font-family: {SANS_FONT};'),

        # Generic serif to Playfair Display
        (r'font-family:\s*serif', f'font-family: {SERIF_FONT}'),
        (r'font-family:\s*Georgia[^;]+;', f'font-family: {SERIF_FONT};'),

        # Common web fonts to JMC fonts
        (r'font-family:\s*["\']?Arial["\']?[^;]*;', f'font-family: {SANS_FONT};'),
        (r'font-family:\s*["\']?Helvetica["\']?[^;]*;', f'font-family: {SANS_FONT};'),
        (r'font-family:\s*["\']?Verdana["\']?[^;]*;', f'font-family: {SANS_FONT};'),
        (r'font-family:\s*["\']?Roboto["\']?[^;]*;', f'font-family: {SANS_FONT};'),
        (r'font-family:\s*["\']?Open Sans["\']?[^;]*;', f'font-family: {SANS_FONT};'),
    ]

    replacements_count = 0
    for pattern, replacement in font_mappings:
        matches = len(re.findall(pattern, content, re.IGNORECASE))
        if matches > 0:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            replacements_count += matches
            print(f"Pattern: {pattern[:50]:50} - {matches} replacements")

    # Ensure Google Fonts link is present
    google_fonts_link = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">'

    if 'Playfair Display' not in content:
        if '<head>' in content:
            # Find position after <head> tag
            head_pos = content.find('<head>') + len('<head>')
            content = content[:head_pos] + '\n    ' + google_fonts_link + content[head_pos:]
            print("\n[OK] Added Google Fonts link for Playfair Display and Lato")
        else:
            print("\n[WARNING] Could not find <head> tag to add Google Fonts")

    # Add body font-family if not present
    body_font_rule = f'''
    <style>
        body {{
            font-family: {SANS_FONT};
        }}
        h1, h2, h3, h4, h5, h6 {{
            font-family: {SERIF_FONT};
        }}
    </style>
    '''

    # Only add if body font not already specified
    if 'body {' not in content or 'body{' not in content:
        if '</head>' in content:
            content = content.replace('</head>', body_font_rule + '\n</head>')
            print("[OK] Added default font families for body and headings")

    print("\n" + "=" * 80)
    print(f"Writing to: {output_file}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("=" * 80)
    print(f"[OK] Font updates complete! Made {replacements_count} font replacements")
    print("\nJMC FONT SCHEME:")
    print("=" * 80)
    print(f"Serif (Headings):  {SERIF_FONT}")
    print(f"Sans (Body):       {SANS_FONT}")
    print("=" * 80)

if __name__ == "__main__":
    input_file = "JMC_Themed.html"
    output_file = "JMC_Themed_Final.html"

    update_fonts(input_file, output_file)
