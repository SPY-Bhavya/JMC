"""
JMC Content Conversion Script
Replaces all Manish Malhotra branding with JMC content
"""

import re

def convert_to_jmc(input_file, output_file):
    """Convert Manish Malhotra content to JMC"""

    print(f"Reading: {input_file}")
    print("=" * 80)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_length = len(content)
    replacements_log = []

    # ============================================================================
    # 1. BRAND NAME REPLACEMENTS
    # ============================================================================
    print("\n1. Replacing Brand Names...")
    print("-" * 80)

    brand_replacements = [
        # Full brand name
        (r'Manish Malhotra', 'JMC - Jewellers Madanlal Chaganlal'),
        (r'MANISH MALHOTRA', 'JMC - JEWELLERS MADANLAL CHAGANLAL'),
        (r'manish malhotra', 'JMC - Jewellers Madanlal Chaganlal'),

        # Short form in titles/headers
        (r'Manish\s*Malhotra', 'JMC'),

        # Meta/SEO variations
        (r'manishmalhotra', 'jmc-jewellers'),
    ]

    for pattern, replacement in brand_replacements:
        matches = len(re.findall(pattern, content, re.IGNORECASE))
        if matches > 0:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            replacements_log.append((pattern, replacement, matches))
            print(f"  '{pattern}' -> '{replacement}' ({matches} times)")

    # ============================================================================
    # 2. NAVIGATION MENU REPLACEMENTS
    # ============================================================================
    print("\n2. Updating Navigation Menus...")
    print("-" * 80)

    nav_replacements = [
        # Main categories - Fashion to Jewellery
        (r'High Jewellery', 'Bridal Collection'),
        (r'Fine Jewellery', 'Fine Jewellery'),  # Keep this

        # Fashion categories to Jewellery categories
        (r'Lehengas', 'Diamond Necklaces'),
        (r'Kurta Sets', 'Gold Rings'),
        (r'Sarees', 'Bridal Sets'),
        (r'Fusion Wear', 'Polki Collection'),
        (r'Sherwani Sets', 'Heritage Jewellery'),
        (r"Men's Kurta Sets", 'Gemstone Rings'),
        (r"Men's Jacket Sets", 'Silver Collection'),

        # Menu items
        (r'Menswear Jewellery', 'Mens Jewellery'),
        (r'Menswear', 'Mens Collection'),

        # Couture -> Collections
        (r'Couture', 'Collections'),

        # In the Spotlight -> Featured
        (r'In the Spotlight', 'Featured Collections'),
    ]

    for pattern, replacement in nav_replacements:
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, replacement, content)
            replacements_log.append((pattern, replacement, matches))
            print(f"  '{pattern}' -> '{replacement}' ({matches} times)")

    # ============================================================================
    # 3. PRODUCT CATEGORIES
    # ============================================================================
    print("\n3. Updating Product Categories...")
    print("-" * 80)

    category_replacements = [
        # Specific items
        (r'Earrings', 'Earrings'),  # Keep
        (r'Rings', 'Rings'),  # Keep
        (r'Bangles & Bracelets', 'Bangles & Bracelets'),  # Keep
        (r'Necklaces', 'Necklaces & Sets'),

        # Add jewellery-specific terms
        (r'View All', 'View All Jewellery'),
    ]

    for pattern, replacement in category_replacements:
        matches = len(re.findall(pattern, content))
        if matches > 0 and pattern != replacement:
            content = re.sub(pattern, replacement, content)
            replacements_log.append((pattern, replacement, matches))
            print(f"  '{pattern}' -> '{replacement}' ({matches} times)")

    # ============================================================================
    # 4. SEARCH & POPULAR TERMS
    # ============================================================================
    print("\n4. Updating Search Terms...")
    print("-" * 80)

    search_replacements = [
        (r'Popular search:', 'Popular Searches:'),
        (r'Popular-ssearch-text', 'Popular-search-text'),
    ]

    for pattern, replacement in search_replacements:
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, replacement, content)
            replacements_log.append((pattern, replacement, matches))
            print(f"  '{pattern}' -> '{replacement}' ({matches} times)")

    # ============================================================================
    # 5. HERO SECTION & BANNERS
    # ============================================================================
    print("\n5. Updating Hero Section Content...")
    print("-" * 80)

    hero_replacements = [
        # Met Gala reference -> JMC Event
        (r'COCO JONES, MET GALA 2025', 'EXQUISITE CRAFTSMANSHIP'),
        (r'MET GALA', 'HERITAGE COLLECTION'),

        # Fashion terms -> Jewellery terms
        (r'HIGH JEWELLERY', 'FINE JEWELLERY'),
        (r'STATEMENT NECKLACES', 'SIGNATURE NECKLACES'),

        # Generic celebrity references
        (r'Featuring over 30 carats of tanzanites', 'Featuring exquisite diamonds and precious gems'),
        (r'alongside diamonds and a graceful', 'crafted with timeless elegance and a graceful'),
        (r'cascade of pearl', 'touch of heritage'),
    ]

    for pattern, replacement in hero_replacements:
        matches = len(re.findall(pattern, content, re.IGNORECASE))
        if matches > 0:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            replacements_log.append((pattern, replacement, matches))
            print(f"  '{pattern}' -> '{replacement}' ({matches} times)")

    # ============================================================================
    # 6. META TAGS & SEO
    # ============================================================================
    print("\n6. Updating Meta Tags & SEO...")
    print("-" * 80)

    # Title tag
    title_pattern = r'<title>\s*Manish Malhotra\s*</title>'
    if re.search(title_pattern, content, re.IGNORECASE):
        content = re.sub(title_pattern,
                        '<title>JMC - Jewellers Madanlal Chaganlal | Finest Jewellery Since Generations</title>',
                        content, flags=re.IGNORECASE)
        print(f"  Updated <title> tag")
        replacements_log.append(('Title tag', 'JMC title', 1))

    # Meta description
    meta_desc_pattern = r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']*["\']'
    new_meta_desc = '<meta name="description" content="JMC - Jewellers Madanlal Chaganlal offers the finest collection of bridal, diamond, gold, and heritage jewellery. Experience timeless elegance and exceptional craftsmanship."'
    if re.search(meta_desc_pattern, content):
        content = re.sub(meta_desc_pattern, new_meta_desc, content)
        print(f"  Updated meta description")
        replacements_log.append(('Meta description', 'JMC description', 1))
    else:
        # Add if not exists
        if '<head>' in content:
            content = content.replace('<head>', f'<head>\n    {new_meta_desc}>')
            print(f"  Added meta description")
            replacements_log.append(('Meta description', 'Added JMC description', 1))

    # ============================================================================
    # 7. LOGO REFERENCES
    # ============================================================================
    print("\n7. Updating Logo References...")
    print("-" * 80)

    # Find and replace logo image sources
    logo_patterns = [
        # SVG or image tags with Manish Malhotra logo
        (r'<img[^>]*manish[^>]*>', '<img src="logo_small.png" alt="JMC Logo" class="logo">'),

        # Update any existing logo_small.png references to ensure proper alt text
        (r'alt=["\'][^"\']*logo[^"\']*["\']', 'alt="JMC - Jewellers Madanlal Chaganlal Logo"'),
    ]

    for pattern, replacement in logo_patterns:
        matches = len(re.findall(pattern, content, re.IGNORECASE))
        if matches > 0:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            print(f"  Updated logo references ({matches} times)")
            replacements_log.append(('Logo', replacement, matches))

    # ============================================================================
    # 8. SOCIAL MEDIA & LINKS
    # ============================================================================
    print("\n8. Updating Social Media References...")
    print("-" * 80)

    # Update social media link placeholders
    social_replacements = [
        (r'Instagram', 'Instagram'),  # Keep but note for manual update
        (r'Facebook', 'Facebook'),    # Keep but note for manual update
        (r'YouTube', 'YouTube'),      # Keep but note for manual update
        (r'Pinterest', 'Pinterest'),  # Keep but note for manual update
    ]

    print(f"  [INFO] Social media links preserved - update URLs manually")

    # ============================================================================
    # 9. CART & COMMERCE
    # ============================================================================
    print("\n9. Updating Shopping Cart Text...")
    print("-" * 80)

    cart_replacements = [
        (r'Main cart', 'Shopping Cart'),
        (r'Your cart is empty', 'Your cart is empty'),  # Keep
        (r'Continue shopping', 'Continue Shopping'),
        (r'Log into check out faster', 'Login for faster checkout'),
    ]

    for pattern, replacement in cart_replacements:
        matches = len(re.findall(pattern, content))
        if matches > 0 and pattern != replacement:
            content = re.sub(pattern, replacement, content)
            replacements_log.append((pattern, replacement, matches))
            print(f"  '{pattern}' -> '{replacement}' ({matches} times)")

    # ============================================================================
    # 10. THEME CLASSES & IDs
    # ============================================================================
    print("\n10. Updating CSS Classes & IDs...")
    print("-" * 80)

    # Update Shopify section IDs if present
    content = re.sub(r'shopify-section-[^"\'>\s]+', 'jmc-section', content)
    print(f"  Updated Shopify section classes to JMC")

    # ============================================================================
    # WRITE OUTPUT
    # ============================================================================
    print("\n" + "=" * 80)
    print(f"Writing converted content to: {output_file}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    new_length = len(content)

    # ============================================================================
    # SUMMARY
    # ============================================================================
    print("=" * 80)
    print("\nCONVERSION SUMMARY:")
    print("=" * 80)

    total_replacements = sum(count for _, _, count in replacements_log)
    print(f"Total Replacements: {total_replacements}")
    print(f"Original Length: {original_length:,} characters")
    print(f"New Length: {new_length:,} characters")
    print(f"Difference: {new_length - original_length:+,} characters")

    print("\n" + "=" * 80)
    print("KEY CHANGES:")
    print("=" * 80)
    print("[OK] Brand name: Manish Malhotra -> JMC")
    print("[OK] Navigation: Fashion categories -> Jewellery categories")
    print("[OK] Search terms: Updated to jewellery-focused")
    print("[OK] Meta tags: Updated with JMC information")
    print("[OK] Logo references: Updated to logo_small.png")
    print("[OK] Hero content: Updated to jewellery theme")

    print("\n" + "=" * 80)
    print("[INFO] MANUAL UPDATES NEEDED:")
    print("=" * 80)
    print("- Update social media URLs to JMC accounts")
    print("- Replace fashion product images with jewellery images")
    print("- Update detailed product descriptions")
    print("- Add JMC store address and contact info")
    print("- Update footer with JMC policies")
    print("=" * 80)

    # Save detailed log
    log_file = output_file.replace('.html', '_conversion_log.txt')
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write("JMC CONVERSION LOG\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total Replacements: {total_replacements}\n\n")

        f.write("DETAILED REPLACEMENTS:\n")
        f.write("-" * 80 + "\n")
        for pattern, replacement, count in replacements_log:
            f.write(f"{pattern:40} -> {replacement:40} ({count} times)\n")

    print(f"\nDetailed log saved to: {log_file}")
    print(f"\n[OK] Conversion complete! Output: {output_file}")

if __name__ == "__main__":
    input_file = "Manish_Malhotra_Formatted.html"
    output_file = "JMC_Website.html"

    convert_to_jmc(input_file, output_file)
