"""
Color Analyzer Script
Extracts all colors used in the HTML/CSS
"""

import re
from collections import Counter

def analyze_colors(input_file):
    """Analyze and extract all colors from HTML/CSS"""

    print(f"Analyzing colors in: {input_file}\n")

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Patterns to find colors
    hex_pattern = r'#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b'
    rgb_pattern = r'rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)'
    rgba_pattern = r'rgba\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*[\d.]+\s*\)'

    # Find all colors
    hex_colors = re.findall(hex_pattern, content)
    rgb_colors = re.findall(rgb_pattern, content)
    rgba_colors = re.findall(rgba_pattern, content)

    # Count occurrences
    hex_counter = Counter(['#' + color.lower() for color in hex_colors])
    rgb_counter = Counter(rgb_colors)
    rgba_counter = Counter(rgba_colors)

    print("=" * 80)
    print("HEX COLORS FOUND (Top 20)")
    print("=" * 80)
    for color, count in hex_counter.most_common(20):
        print(f"{color:20} - Used {count:4} times")

    print("\n" + "=" * 80)
    print("RGB COLORS FOUND (Top 10)")
    print("=" * 80)
    for color, count in rgb_counter.most_common(10):
        print(f"{color:40} - Used {count:4} times")

    print("\n" + "=" * 80)
    print("RGBA COLORS FOUND (Top 10)")
    print("=" * 80)
    for color, count in rgba_counter.most_common(10):
        print(f"{color:50} - Used {count:4} times")

    # Look for color names and CSS variables
    color_name_pattern = r'color:\s*([a-z]+)\s*[;}]'
    bg_color_pattern = r'background-color:\s*([a-z]+)\s*[;}]'

    color_names = re.findall(color_name_pattern, content, re.IGNORECASE)
    bg_names = re.findall(bg_color_pattern, content, re.IGNORECASE)

    if color_names:
        print("\n" + "=" * 80)
        print("NAMED COLORS (Top 10)")
        print("=" * 80)
        name_counter = Counter(color_names)
        for name, count in name_counter.most_common(10):
            print(f"{name:20} - Used {count:4} times")

    # Save to file
    with open('color_analysis.txt', 'w', encoding='utf-8') as f:
        f.write("Color Analysis Report\n")
        f.write("=" * 80 + "\n\n")

        f.write("HEX COLORS (Top 30)\n")
        f.write("-" * 80 + "\n")
        for color, count in hex_counter.most_common(30):
            f.write(f"{color:20} - Used {count:4} times\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("RGB COLORS\n")
        f.write("-" * 80 + "\n")
        for color, count in rgb_counter.most_common(20):
            f.write(f"{color:40} - Used {count:4} times\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("RGBA COLORS\n")
        f.write("-" * 80 + "\n")
        for color, count in rgba_counter.most_common(20):
            f.write(f"{color:50} - Used {count:4} times\n")

    print(f"\n{'=' * 80}")
    print("Detailed analysis saved to: color_analysis.txt")

    return hex_counter, rgb_counter, rgba_counter

if __name__ == "__main__":
    analyze_colors("Manish_Malhotra_Formatted.html")
