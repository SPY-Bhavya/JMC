"""
Hero Image Update Script
Replaces hero/banner/slideshow images with JMC jewellery photos
"""

import re
import os

def update_hero_images(input_file, output_file):
    """Update hero and banner images with JMC jewellery photos"""

    print(f"Reading: {input_file}")
    print("=" * 80)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # JMC jewellery images available
    jmc_images = [
        'Images/JMC_28april24_89123.jpg',
        'Images/JMC_28april24_89230.jpg',
        'Images/JMC_28april24_89469.jpg',
        'Images/JMC_7aug22_8026.jpg',
        'Images/JMC_7aug22_8205.jpg',
        'Images/JMC_7aug22_8214.jpg',
        'Images/JMC_7aug22_8335.jpg',
        'Images/JMC_7aug22_8403.jpg',
        'Images/JMC_7aug22_8666.jpg',
        'Images/JMC_7aug22_9530.jpg',
        'Images/JMC_Rushali_9sept20_8885.jpg',
        'Images/JMC_Rushali_9sept20_8908.jpg',
        'Images/IMG_2209.JPG',
    ]

    # Verify images exist
    available_images = [img for img in jmc_images if os.path.exists(img)]

    print(f"\nFound {len(available_images)} JMC jewellery images:")
    for img in available_images:
        print(f"  - {img}")

    if not available_images:
        print("\nERROR: No JMC images found!")
        return

    print("\n" + "=" * 80)
    print("UPDATING HERO/BANNER IMAGES")
    print("=" * 80)

    replacements_count = 0
    image_index = 0

    # =========================================================================
    # 1. Find and replace hero slideshow images
    # =========================================================================
    print("\n1. Replacing Hero Slideshow Images...")
    print("-" * 80)

    # Pattern for slideshow/hero sections
    # Look for image tags in hero/slideshow sections
    hero_pattern = r'(<(?:div|section)[^>]*(?:class="[^"]*(?:hero|slideshow|banner|slider)[^"]*")[^>]*>.*?<img[^>]*src=")([^"]+)(".*?</(?:div|section)>)'

    def replace_hero_image(match):
        nonlocal image_index, replacements_count
        before = match.group(1)
        old_src = match.group(2)
        after = match.group(3)

        # Skip if it's already a JMC image or logo
        if 'logo' in old_src.lower() or 'JMC' in old_src or 'Images/' in old_src:
            return match.group(0)

        # Use next JMC image
        new_src = available_images[image_index % len(available_images)]
        image_index += 1
        replacements_count += 1

        print(f"  [{replacements_count}] Replacing hero image -> {new_src}")
        return before + new_src + after

    content = re.sub(hero_pattern, replace_hero_image, content, flags=re.DOTALL | re.IGNORECASE)

    # =========================================================================
    # 2. Replace data URLs in hero sections (if any remain)
    # =========================================================================
    print("\n2. Replacing Data URLs in Hero Sections...")
    print("-" * 80)

    # Find hero sections
    hero_section_patterns = [
        r'<div[^>]*class="[^"]*hero[^"]*"[^>]*>.*?</div>',
        r'<section[^>]*class="[^"]*slideshow[^"]*"[^>]*>.*?</section>',
        r'<div[^>]*class="[^"]*banner[^"]*"[^>]*>.*?</div>',
    ]

    for pattern in hero_section_patterns:
        def replace_data_urls_in_section(match):
            nonlocal image_index, replacements_count
            section = match.group(0)

            # Find data URLs
            data_url_pattern = r'(<img[^>]*src=")data:image/[^"]+(")'

            def replace_data_url(img_match):
                nonlocal image_index, replacements_count
                before = img_match.group(1)
                after = img_match.group(2)

                # Skip logos
                full_tag = img_match.group(0)
                if 'logo' in full_tag.lower():
                    return full_tag

                new_src = available_images[image_index % len(available_images)]
                image_index += 1
                replacements_count += 1

                print(f"  [{replacements_count}] Replacing data URL -> {new_src}")
                return before + new_src + after

            section = re.sub(data_url_pattern, replace_data_url, section)
            return section

        content = re.sub(pattern, replace_data_urls_in_section, content, flags=re.DOTALL)

    # =========================================================================
    # 3. Update specific Shopify CDN URLs if present
    # =========================================================================
    print("\n3. Updating Shopify CDN Images...")
    print("-" * 80)

    shopify_pattern = r'(<img[^>]*src=")https://[^"]*(?:cdn\.shopify\.com|JMC\.in)[^"]*\.(jpg|png|webp)[^"]*(")'

    def replace_shopify_url(match):
        nonlocal image_index, replacements_count
        before = match.group(1)
        ext = match.group(2)
        after = match.group(3)

        # Get full tag to check if it's a logo
        full_match = match.group(0)
        if 'logo' in full_match.lower() or 'header' in full_match.lower():
            return full_match

        new_src = available_images[image_index % len(available_images)]
        image_index += 1
        replacements_count += 1

        print(f"  [{replacements_count}] Replacing Shopify URL -> {new_src}")
        return before + new_src + after

    content = re.sub(shopify_pattern, replace_shopify_url, content, flags=re.IGNORECASE)

    # =========================================================================
    # 4. Update alt text for jewellery images
    # =========================================================================
    print("\n4. Updating Alt Text for Jewellery Images...")
    print("-" * 80)

    # Update alt text that still references fashion
    fashion_alt_patterns = [
        (r'alt="[^"]*(?:lehenga|kurta|saree|fashion|dress|outfit|wear)[^"]*"',
         'alt="JMC Fine Jewellery Collection"', re.IGNORECASE),
    ]

    for pattern, replacement, flags in fashion_alt_patterns:
        matches = len(re.findall(pattern, content, flags))
        if matches > 0:
            content = re.sub(pattern, replacement, content, flags=flags)
            print(f"  Updated {matches} fashion-related alt text(s)")

    # =========================================================================
    # Write output
    # =========================================================================
    print("\n" + "=" * 80)
    print(f"Writing updated content to: {output_file}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # =========================================================================
    # Summary
    # =========================================================================
    print("=" * 80)
    print("\nHERO IMAGE UPDATE SUMMARY:")
    print("=" * 80)
    print(f"Total Hero/Banner Images Replaced: {replacements_count}")
    print(f"JMC Images Used: {len(set(available_images[:image_index]))}")
    print("\nUpdated Sections:")
    print("  [OK] Hero slideshow images")
    print("  [OK] Banner images")
    print("  [OK] Data URL images in hero sections")
    print("  [OK] Shopify CDN images")
    print("  [OK] Alt text updated")
    print("=" * 80)
    print(f"\n[OK] Updated file saved: {output_file}")
    print("\nYour JMC jewellery images are now featured in hero/banner sections!")

if __name__ == "__main__":
    input_file = "JMC_Website_Fixed.html"
    output_file = "JMC_Website_Final.html"

    update_hero_images(input_file, output_file)
