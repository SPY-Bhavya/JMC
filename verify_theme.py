"""
Theme Verification Script
Verifies that JMC colors and fonts have been applied correctly
"""

import re
from collections import Counter

def verify_theme(filename):
    """Verify JMC theme application"""

    print(f"Verifying JMC theme in: {filename}")
    print("=" * 80)

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # JMC Colors
    jmc_colors = {
        '#05231c': 'JMC Green',
        '#f9f5f0': 'JMC Cream',
        '#d4af37': 'JMC Gold',
        '#e5c567': 'JMC Gold Light',
    }

    # Find all hex colors
    hex_pattern = r'#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b'
    all_hex_colors = ['#' + c.lower() for c in re.findall(hex_pattern, content)]
    color_counts = Counter(all_hex_colors)

    print("\nJMC BRAND COLORS FOUND:")
    print("-" * 80)
    jmc_color_total = 0
    for color, name in jmc_colors.items():
        count = color_counts.get(color.lower(), 0)
        jmc_color_total += count
        status = "[OK]" if count > 0 else "[MISSING]"
        print(f"{status} {name:20} ({color}): {count:4} occurrences")

    print("\n" + "=" * 80)
    print("\nOTHER COLORS FOUND (Top 15):")
    print("-" * 80)

    other_colors = {c: cnt for c, cnt in color_counts.items()
                   if c not in [k.lower() for k in jmc_colors.keys()]}

    for color, count in sorted(other_colors.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"{color:15} - {count:4} times")

    # Check for fonts
    print("\n" + "=" * 80)
    print("FONT VERIFICATION:")
    print("-" * 80)

    playfair_count = len(re.findall(r'Playfair Display', content, re.IGNORECASE))
    lato_count = len(re.findall(r'Lato', content, re.IGNORECASE))

    print(f"{'[OK]' if playfair_count > 0 else '[MISSING]'} Playfair Display: {playfair_count} references")
    print(f"{'[OK]' if lato_count > 0 else '[MISSING]'} Lato: {lato_count} references")

    # Check for Google Fonts link
    if 'fonts.googleapis.com' in content:
        print("[OK] Google Fonts link present")
    else:
        print("[WARNING] Google Fonts link not found")

    # Check for Tailwind config
    if 'tailwind.config' in content:
        print("[OK] Tailwind config found")
    else:
        print("[INFO] Tailwind config not present")

    # Check for CSS variables
    if '--jmc-green' in content or 'var(--jmc-' in content:
        print("[OK] CSS variables for JMC colors found")
    else:
        print("[INFO] CSS variables not present")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY:")
    print("=" * 80)
    print(f"JMC Brand Colors:     {jmc_color_total} total occurrences")
    print(f"Other Colors:         {len(other_colors)} unique colors, {sum(other_colors.values())} occurrences")
    print(f"JMC Fonts:            {'Yes' if playfair_count > 0 and lato_count > 0 else 'No'}")
    print("=" * 80)

    # Save detailed report
    report_filename = f"{filename.replace('.html', '')}_verification_report.txt"
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write("JMC THEME VERIFICATION REPORT\n")
        f.write("=" * 80 + "\n\n")

        f.write("JMC BRAND COLORS:\n")
        f.write("-" * 80 + "\n")
        for color, name in jmc_colors.items():
            count = color_counts.get(color.lower(), 0)
            f.write(f"{name:20} ({color}): {count:4} occurrences\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("OTHER COLORS FOUND:\n")
        f.write("-" * 80 + "\n")
        for color, count in sorted(other_colors.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{color:15} - {count:4} times\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("FONTS:\n")
        f.write("-" * 80 + "\n")
        f.write(f"Playfair Display: {playfair_count} references\n")
        f.write(f"Lato: {lato_count} references\n")

    print(f"\nDetailed report saved to: {report_filename}")

if __name__ == "__main__":
    verify_theme("JMC_Themed_Final.html")
