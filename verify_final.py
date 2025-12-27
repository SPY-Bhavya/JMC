"""
Final Verification Script
Verifies that images are correctly fixed
"""

import re
import os

def verify_final(filename):
    """Verify final website has correct images"""

    print(f"Verifying: {filename}")
    print("=" * 80)

    if not os.path.exists(filename):
        print(f"ERROR: {filename} not found!")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    print("\n1. Checking Logo Images...")
    print("-" * 80)

    # Count logo_small.png references
    logo_count = len(re.findall(r'logo_small\.png', content))
    print(f"  logo_small.png found: {logo_count} times")

    # Check for data URLs in logo positions
    header_data_urls = len(re.findall(r'header[^>]*>.*?data:image/', content, re.DOTALL))
    if header_data_urls > 0:
        print(f"  [WARNING] Found {header_data_urls} data URLs in header")
    else:
        print(f"  [OK] No data URLs in header")

    print("\n2. Checking JMC Jewellery Images...")
    print("-" * 80)

    # Count JMC images
    jmc_image_patterns = [
        r'Images/JMC_',
        r'Images/IMG_',
    ]

    total_jmc_images = 0
    for pattern in jmc_image_patterns:
        count = len(re.findall(pattern, content))
        total_jmc_images += count

    print(f"  JMC jewellery images used: {total_jmc_images}")

    if total_jmc_images > 0:
        print(f"  [OK] JMC images are being used")
    else:
        print(f"  [WARNING] No JMC images found")

    # List unique JMC images being used
    all_jmc_images = re.findall(r'(Images/[^"\'>\s]+\.(?:jpg|png|JPG|PNG))', content)
    unique_jmc_images = set(all_jmc_images)

    if unique_jmc_images:
        print(f"\n  Unique JMC images in use ({len(unique_jmc_images)}):")
        for img in sorted(unique_jmc_images):
            # Check if file exists
            exists = "[EXISTS]" if os.path.exists(img) else "[MISSING]"
            print(f"    {exists} {img}")

    print("\n3. Checking for Remaining Data URLs...")
    print("-" * 80)

    # Count all data URLs
    all_data_urls = len(re.findall(r'src="data:image/', content))
    print(f"  Total data URLs remaining: {all_data_urls}")

    if all_data_urls > 0:
        # Show first few
        data_url_samples = re.findall(r'src="(data:image/[^"]{50})', content)
        print(f"\n  Sample data URLs found:")
        for i, sample in enumerate(data_url_samples[:3], 1):
            print(f"    {i}. {sample}...")
    else:
        print(f"  [OK] No data URLs found (all replaced)")

    print("\n4. Checking Branding...")
    print("-" * 80)

    # JMC branding
    jmc_count = len(re.findall(r'JMC', content))
    mm_count = len(re.findall(r'Manish Malhotra', content, re.IGNORECASE))

    print(f"  JMC references: {jmc_count}")
    print(f"  Manish Malhotra references: {mm_count}")

    if mm_count == 0:
        print(f"  [OK] No Manish Malhotra references")
    else:
        print(f"  [WARNING] Still has Manish Malhotra references")

    print("\n5. Checking Colors...")
    print("-" * 80)

    jmc_green = len(re.findall(r'#05231c', content, re.IGNORECASE))
    jmc_cream = len(re.findall(r'#f9f5f0', content, re.IGNORECASE))
    jmc_gold = len(re.findall(r'#d4af37', content, re.IGNORECASE))

    print(f"  JMC Green (#05231c): {jmc_green}")
    print(f"  JMC Cream (#f9f5f0): {jmc_cream}")
    print(f"  JMC Gold (#d4af37): {jmc_gold}")

    if jmc_green > 0 and jmc_cream > 0:
        print(f"  [OK] JMC colors applied")

    print("\n6. File Information...")
    print("-" * 80)

    file_size = os.path.getsize(filename) / (1024 * 1024)
    print(f"  File size: {file_size:.2f} MB")

    # Summary
    print("\n" + "=" * 80)
    print("VERIFICATION SUMMARY")
    print("=" * 80)

    issues = []
    successes = []

    if logo_count >= 2:
        successes.append(f"Logo properly set ({logo_count} references)")
    else:
        issues.append("Logo might not be set correctly")

    if total_jmc_images >= 5:
        successes.append(f"JMC jewellery images in use ({total_jmc_images} references)")
    else:
        issues.append(f"Few JMC images found ({total_jmc_images})")

    if mm_count == 0:
        successes.append("No Manish Malhotra references")
    else:
        issues.append(f"Manish Malhotra still present ({mm_count} times)")

    if jmc_green > 0 and jmc_cream > 0:
        successes.append("JMC colors applied")
    else:
        issues.append("JMC colors might not be applied")

    print(f"\nSuccesses: {len(successes)}")
    print(f"Issues: {len(issues)}")

    if issues:
        print("\nISSUES:")
        for issue in issues:
            print(f"  - {issue}")

    if successes:
        print("\nSUCCESSES:")
        for success in successes:
            print(f"  [OK] {success}")

    if len(issues) == 0:
        print("\n" + "=" * 80)
        print("[SUCCESS] Website verification PASSED!")
        print("=" * 80)
    else:
        print("\n" + "=" * 80)
        print("[ATTENTION] Some issues found - review above")
        print("=" * 80)

    print(f"\n[OK] Verification complete for: {filename}")

if __name__ == "__main__":
    verify_final("JMC_Website.html")
