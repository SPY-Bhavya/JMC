"""
JMC Color Theme Application Script
Replaces Manish Malhotra colors with JMC brand colors
"""

import re

def apply_jmc_colors(input_file, output_file):
    """Apply JMC color scheme to the HTML file"""

    print(f"Reading: {input_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # JMC Color Scheme
    JMC_COLORS = {
        'green': '#05231c',      # Dark green (primary)
        'cream': '#f9f5f0',      # Cream background
        'gold': '#d4af37',       # Gold accent
        'gold_light': '#e5c567', # Light gold
    }

    # Manish Malhotra colors to JMC mapping
    COLOR_MAPPINGS = {
        # Main background (beige/cream) -> JMC Cream
        '#f6f3f0': JMC_COLORS['cream'],
        '#F6F3F0': JMC_COLORS['cream'],

        # Black/dark colors -> JMC Green (for headers, text)
        '#000000': JMC_COLORS['green'],
        '#000': JMC_COLORS['green'],
        '#090a0b': JMC_COLORS['green'],
        '#020202': JMC_COLORS['green'],
        '#202020': JMC_COLORS['green'],

        # Medium grays -> Keep some as-is for contrast, or lighten
        '#6b6b6b': '#4a4a4a',
        '#cec7c0': '#d4cdc6',

        # Accent colors (will be mapped to gold)
        '#928f85': JMC_COLORS['gold'],

        # White stays white
        '#ffffff': '#ffffff',
        '#fff': '#fff',

        # Other specific colors
        '#555': '#333333',
        '#222': JMC_COLORS['green'],
    }

    print("\nApplying color replacements...")
    print("=" * 80)

    replacements_made = {}

    # Replace hex colors
    for old_color, new_color in COLOR_MAPPINGS.items():
        # Case-insensitive replacement
        pattern = re.compile(re.escape(old_color), re.IGNORECASE)
        matches = len(pattern.findall(content))
        if matches > 0:
            content = pattern.sub(new_color, content)
            replacements_made[old_color] = {'new': new_color, 'count': matches}
            print(f"{old_color:15} -> {new_color:15} ({matches:4} replacements)")

    # Replace RGBA black/dark colors with JMC green equivalent
    rgba_mappings = [
        (r'rgba\(0,\s*0,\s*0,\s*1\)', f'rgba(5, 35, 28, 1)'),  # jmc-green with full opacity
        (r'rgba\(0,\s*0,\s*0,\s*0\.9\)', f'rgba(5, 35, 28, 0.9)'),
        (r'rgba\(14,\s*18,\s*19,\s*1\)', f'rgba(5, 35, 28, 1)'),
        (r'rgba\(30,\s*30,\s*30,\s*1\)', f'rgba(5, 35, 28, 1)'),
    ]

    print("\n" + "=" * 80)
    print("RGBA Color Replacements:")
    print("=" * 80)

    for old_pattern, new_rgba in rgba_mappings:
        matches = len(re.findall(old_pattern, content))
        if matches > 0:
            content = re.sub(old_pattern, new_rgba, content)
            print(f"{old_pattern[:40]:40} -> {new_rgba:30} ({matches} replacements)")

    # Add JMC color variables if there's a style section
    print("\n" + "=" * 80)
    print("Adding JMC CSS Variables...")
    print("=" * 80)

    # Look for existing <style> tag or <head>
    jmc_css_vars = """
    <style>
        :root {
            --jmc-green: #05231c;
            --jmc-cream: #f9f5f0;
            --jmc-gold: #d4af37;
            --jmc-gold-light: #e5c567;
        }

        /* Override any remaining dark backgrounds */
        body {
            background-color: var(--jmc-cream) !important;
        }
    </style>
    """

    # Insert CSS variables before closing </head>
    if '</head>' in content:
        content = content.replace('</head>', jmc_css_vars + '\n</head>')
        print("[OK] Added JMC CSS variables to <head>")

    # Update Tailwind config if present
    tailwind_config = '''
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              "jmc-green": "#05231c",
              "jmc-cream": "#f9f5f0",
              "jmc-gold": "#d4af37",
              "jmc-gold-light": "#e5c567",
            },
            fontFamily: {
              serif: ['"Playfair Display"', "serif"],
              sans: ['"Lato"', "sans-serif"],
            },
          },
        },
      };
    </script>
    '''

    # Add Google Fonts for Playfair Display and Lato
    google_fonts = '''
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
    '''

    if '<head>' in content and 'Playfair Display' not in content:
        content = content.replace('<head>', '<head>\n' + google_fonts)
        print("[OK] Added Google Fonts (Playfair Display & Lato)")

    if 'tailwind' in content.lower() and 'tailwind.config' not in content:
        # Add Tailwind config before first <script> or in <head>
        if '<script' in content:
            content = content.replace('<script', tailwind_config + '\n    <script', 1)
            print("[OK] Added Tailwind config with JMC colors")

    # Write output
    print("\n" + "=" * 80)
    print(f"Writing to: {output_file}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # Calculate changes
    total_replacements = sum(info['count'] for info in replacements_made.values())

    print("=" * 80)
    print(f"[OK] Complete! Made {total_replacements} color replacements")
    print(f"[OK] Output saved to: {output_file}")

    # Summary
    print("\n" + "=" * 80)
    print("JMC COLOR SCHEME APPLIED:")
    print("=" * 80)
    print(f"JMC Green (Primary):     {JMC_COLORS['green']}")
    print(f"JMC Cream (Background):  {JMC_COLORS['cream']}")
    print(f"JMC Gold (Accent):       {JMC_COLORS['gold']}")
    print(f"JMC Gold Light:          {JMC_COLORS['gold_light']}")
    print("=" * 80)

if __name__ == "__main__":
    input_file = "Manish_Malhotra_Formatted.html"
    output_file = "JMC_Themed.html"

    apply_jmc_colors(input_file, output_file)
