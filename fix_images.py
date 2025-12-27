"""
Image Fix Script
Restores product images and only replaces logo images with JMC logo
"""

import re
import os

def fix_images(broken_file, original_file, output_file):
    """Fix images - restore products, keep only logo as JMC logo"""

    print(f"Reading files...")
    print("=" * 80)

    # Read the broken file (with all images as logos)
    with open(broken_file, 'r', encoding='utf-8') as f:
        broken_content = f.read()

    # Read the original file (with all original images)
    with open(original_file, 'r', encoding='utf-8') as f:
        original_content = f.read()

    print("\nStep 1: Restoring original product images from backup...")
    print("-" * 80)

    # We'll use the original content but keep JMC branding
    # Start with original content
    fixed_content = original_content

    # ========================================================================
    # Apply only the branding changes (not image changes)
    # ========================================================================

    # 1. Brand name replacements
    print("\nApplying JMC branding...")
    brand_replacements = [
        (r'Manish Malhotra', 'JMC - Jewellers Madanlal Chaganlal'),
        (r'MANISH MALHOTRA', 'JMC - JEWELLERS MADANLAL CHAGANLAL'),
        (r'Manish\s*Malhotra', 'JMC'),
    ]

    for pattern, replacement in brand_replacements:
        fixed_content = re.sub(pattern, replacement, fixed_content, flags=re.IGNORECASE)

    # 2. Navigation menu replacements
    print("Updating navigation...")
    nav_replacements = [
        ('High Jewellery', 'Bridal Collection'),
        ('Lehengas', 'Diamond Necklaces'),
        ('Kurta Sets', 'Gold Rings'),
        ('Sarees', 'Bridal Sets'),
        ('Fusion Wear', 'Polki Collection'),
        ('Sherwani Sets', 'Heritage Jewellery'),
        ("Men's Jacket Sets", 'Silver Collection'),
        ('Menswear Jewellery', 'Mens Jewellery'),
        ('Couture', 'Collections'),
        ('In the Spotlight', 'Featured Collections'),
    ]

    for old, new in nav_replacements:
        fixed_content = fixed_content.replace(old, new)

    # 3. Color scheme
    print("Applying JMC colors...")
    color_replacements = {
        '#f6f3f0': '#f9f5f0',  # Cream
        '#000000': '#05231c',  # Green
        '#000': '#05231c',
        '#090a0b': '#05231c',
        '#020202': '#05231c',
        '#202020': '#05231c',
        '#928f85': '#d4af37',  # Gold
    }

    for old_color, new_color in color_replacements.items():
        pattern = re.compile(re.escape(old_color), re.IGNORECASE)
        fixed_content = pattern.sub(new_color, fixed_content)

    # 4. RGBA colors
    rgba_mappings = [
        (r'rgba\(0,\s*0,\s*0,\s*1\)', 'rgba(5, 35, 28, 1)'),
        (r'rgba\(0,\s*0,\s*0,\s*0\.9\)', 'rgba(5, 35, 28, 0.9)'),
        (r'rgba\(14,\s*18,\s*19,\s*1\)', 'rgba(5, 35, 28, 1)'),
        (r'rgba\(30,\s*30,\s*30,\s*1\)', 'rgba(5, 35, 28, 1)'),
    ]

    for old_pattern, new_rgba in rgba_mappings:
        fixed_content = re.sub(old_pattern, new_rgba, fixed_content)

    # 5. Update ONLY header logo images (not all images)
    print("\nReplacing ONLY header/logo images...")
    print("-" * 80)

    # Find logo wrapper sections and replace images within them
    # Match: header__heading-logo-wrapper ... img tag
    logo_pattern = r'(<div[^>]*class="[^"]*header__heading-logo-wrapper[^"]*"[^>]*>.*?<img[^>]*src=")([^"]+)(".*?</div>)'

    def replace_logo_only(match):
        before = match.group(1)
        old_src = match.group(2)
        after = match.group(3)

        # Only replace if it's a data URL or MM logo
        if old_src.startswith('data:') or 'MM' in old_src or 'malhotra' in old_src.lower():
            new_src = 'logo_small.png'
            print(f"  Replacing logo: {old_src[:50]}... -> logo_small.png")
            return before + new_src + after
        else:
            # Keep original
            return match.group(0)

    fixed_content = re.sub(logo_pattern, replace_logo_only, fixed_content, flags=re.DOTALL | re.IGNORECASE)

    # Also update any remaining data:image URLs in header sections specifically
    # But preserve product images
    header_section_pattern = r'(<header[^>]*>.*?</header>)'

    def fix_header_images(match):
        header = match.group(1)
        # Replace data URLs in header only
        header = re.sub(r'(<img[^>]*src=")data:image/[^"]+(")',
                       r'\1logo_small.png\2',
                       header)
        return header

    fixed_content = re.sub(header_section_pattern, fix_header_images, fixed_content, flags=re.DOTALL)

    # 6. Update alt text for logo images only
    print("\nUpdating logo alt text...")
    fixed_content = re.sub(
        r'(<img[^>]*class="[^"]*header__heading-logo[^"]*"[^>]*alt=")[^"]*(")',
        r'\1JMC - Jewellers Madanlal Chaganlal Logo\2',
        fixed_content
    )

    # 7. Meta tags
    print("\nUpdating meta tags...")

    # Title
    title_pattern = r'<title>\s*[^<]*Malhotra[^<]*</title>'
    if re.search(title_pattern, fixed_content, re.IGNORECASE):
        fixed_content = re.sub(title_pattern,
                              '<title>JMC - Jewellers Madanlal Chaganlal | Finest Jewellery</title>',
                              fixed_content, flags=re.IGNORECASE)

    # Add meta description if not exists
    if 'name="description"' not in fixed_content:
        meta_tags = '''<meta name="description" content="JMC - Jewellers Madanlal Chaganlal offers the finest collection of bridal, diamond, gold, and heritage jewellery. Experience timeless elegance and exceptional craftsmanship.">
<meta name="keywords" content="JMC Jewellers, Madanlal Chaganlal, bridal jewellery, diamond jewellery, gold jewellery">
'''
        fixed_content = re.sub(r'(<html[^>]*>)', r'\1\n' + meta_tags, fixed_content, count=1)

    # 8. Schema.org logo
    schema_logo_pattern = r'"logo":"https://[^"]*(?:MM|malhotra)[^"]*\.png[^"]*"'
    fixed_content = re.sub(schema_logo_pattern, '"logo":"https://jmc.in/logo_small.png"',
                          fixed_content, flags=re.IGNORECASE)

    # ========================================================================
    # Write output
    # ========================================================================
    print("\n" + "=" * 80)
    print(f"Writing fixed content to: {output_file}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

    # ========================================================================
    # Summary
    # ========================================================================
    print("=" * 80)
    print("\nIMAGE FIX SUMMARY:")
    print("=" * 80)
    print("[OK] Original product images RESTORED")
    print("[OK] Only header/logo images replaced with logo_small.png")
    print("[OK] JMC branding applied")
    print("[OK] JMC colors applied")
    print("[OK] Navigation updated")
    print("[OK] Meta tags updated")
    print("=" * 80)
    print(f"\n[OK] Fixed file saved: {output_file}")
    print("\nNow product images are preserved, only logos are JMC logo!")

if __name__ == "__main__":
    broken_file = "JMC_Website.html"  # File with all images as logos
    original_file = "Manish_Malhotra_Original.html"  # Original with all images
    output_file = "JMC_Website_Fixed.html"

    if not os.path.exists(original_file):
        print(f"ERROR: {original_file} not found!")
        print("Please ensure the original backup file exists.")
    else:
        fix_images(broken_file, original_file, output_file)
