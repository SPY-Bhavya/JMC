"""
Logo Update Script
Replaces embedded/base64 logo with JMC logo_small.png
"""

import re

def update_logo(input_file, output_file):
    """Replace logo references with JMC logo"""

    print(f"Reading: {input_file}")
    print("=" * 80)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements_count = 0

    # ============================================================================
    # 1. Replace base64/data URL logos with logo_small.png
    # ============================================================================
    print("\n1. Replacing Logo Images...")
    print("-" * 80)

    # Pattern to match img tags with base64 or data URLs
    base64_logo_pattern = r'<img\s+([^>]*\s+)?src="data:image/[^"]+"\s*([^>]*)>'

    def logo_replacement(match):
        # Extract any existing attributes
        attrs_before = match.group(1) if match.group(1) else ""
        attrs_after = match.group(2) if match.group(2) else ""

        # Create new img tag with logo_small.png
        new_img = f'<img {attrs_before}src="logo_small.png" alt="JMC - Jewellers Madanlal Chaganlal Logo" class="header__heading-logo motion-reduce" loading="eager" {attrs_after}>'

        # Clean up any duplicate attributes
        new_img = re.sub(r'\s+', ' ', new_img)
        new_img = re.sub(r'\s+>', '>', new_img)

        return new_img

    # Count and replace
    base64_logos = len(re.findall(base64_logo_pattern, content))
    if base64_logos > 0:
        content = re.sub(base64_logo_pattern, logo_replacement, content)
        print(f"  Replaced {base64_logos} base64 logo(s) with logo_small.png")
        replacements_count += base64_logos

    # ============================================================================
    # 2. Update alt text for all logo images
    # ============================================================================
    print("\n2. Updating Logo Alt Text...")
    print("-" * 80)

    # Update alt attributes to JMC
    alt_patterns = [
        (r'alt="[^"]*Manish Malhotra[^"]*"', 'alt="JMC - Jewellers Madanlal Chaganlal Logo"'),
        (r'alt="[^"]*logo[^"]*"', 'alt="JMC - Jewellers Madanlal Chaganlal Logo"', re.IGNORECASE),
    ]

    for pattern, replacement, *flags in alt_patterns:
        flag = flags[0] if flags else 0
        matches = len(re.findall(pattern, content, flag))
        if matches > 0:
            content = re.sub(pattern, replacement, content, flags=flag)
            print(f"  Updated {matches} alt text(s)")
            replacements_count += matches

    # ============================================================================
    # 3. Update Schema.org/JSON-LD logo references
    # ============================================================================
    print("\n3. Updating Schema.org Logo...")
    print("-" * 80)

    # Update JSON-LD schema logo
    schema_logo_pattern = r'"logo":"https://[^"]*(?:New-MM-White-Logo|manish|malhotra)[^"]*\.png[^"]*"'
    schema_logo_replacement = '"logo":"https://jmc.in/logo_small.png"'

    schema_matches = len(re.findall(schema_logo_pattern, content, re.IGNORECASE))
    if schema_matches > 0:
        content = re.sub(schema_logo_pattern, schema_logo_replacement, content, flags=re.IGNORECASE)
        print(f"  Updated {schema_matches} schema logo reference(s)")
        replacements_count += schema_matches

    # ============================================================================
    # 4. Update Favicon if present
    # ============================================================================
    print("\n4. Checking Favicon...")
    print("-" * 80)

    favicon_pattern = r'<link[^>]*rel="(?:icon|shortcut icon)"[^>]*>'
    if re.search(favicon_pattern, content, re.IGNORECASE):
        # Update favicon to JMC
        content = re.sub(r'(<link[^>]*rel="(?:icon|shortcut icon)"[^>]*href=")[^"]+(")',
                        r'\1logo_small.png\2',
                        content, flags=re.IGNORECASE)
        print(f"  Updated favicon reference")
        replacements_count += 1
    else:
        # Add favicon if not present
        favicon_tag = '    <link rel="icon" type="image/png" href="logo_small.png">\n'
        if '<head>' in content:
            content = content.replace('<head>', '<head>\n' + favicon_tag)
            print(f"  Added favicon link")
            replacements_count += 1

    # ============================================================================
    # 5. Update og:image and social media images
    # ============================================================================
    print("\n5. Updating Open Graph Images...")
    print("-" * 80)

    og_patterns = [
        (r'<meta\s+property="og:image"\s+content="[^"]*"', '<meta property="og:image" content="https://jmc.in/logo_small.png"'),
        (r'<meta\s+name="twitter:image"\s+content="[^"]*"', '<meta name="twitter:image" content="https://jmc.in/logo_small.png"'),
    ]

    for pattern, replacement in og_patterns:
        matches = len(re.findall(pattern, content, re.IGNORECASE))
        if matches > 0:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            print(f"  Updated social media image ({matches} occurrence(s))")
            replacements_count += matches

    # ============================================================================
    # WRITE OUTPUT
    # ============================================================================
    print("\n" + "=" * 80)
    print(f"Writing updated content to: {output_file}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # ============================================================================
    # SUMMARY
    # ============================================================================
    print("=" * 80)
    print("\nLOGO UPDATE SUMMARY:")
    print("=" * 80)
    print(f"Total Updates: {replacements_count}")
    print("\n" + "=" * 80)
    print("CHANGES MADE:")
    print("=" * 80)
    print("[OK] Base64 logos replaced with logo_small.png")
    print("[OK] Alt text updated to JMC branding")
    print("[OK] Schema.org logo updated")
    print("[OK] Favicon updated/added")
    print("=" * 80)
    print(f"\n[OK] Logo update complete! Output: {output_file}")

if __name__ == "__main__":
    input_file = "JMC_Website.html"
    output_file = "JMC_Website.html"  # Update same file

    update_logo(input_file, output_file)
