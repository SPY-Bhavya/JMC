"""
JMC Conversion Verification Script
Verifies that all Manish Malhotra content has been replaced with JMC content
"""

import re

def verify_conversion(filename):
    """Verify JMC conversion completeness"""

    print(f"Verifying JMC conversion in: {filename}")
    print("=" * 80)

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []
    warnings = []
    successes = []

    # ============================================================================
    # 1. Check for remaining Manish Malhotra references
    # ============================================================================
    print("\n1. Checking for Remaining Manish Malhotra References...")
    print("-" * 80)

    mm_patterns = [
        'Manish Malhotra',
        'manish malhotra',
        'MANISH MALHOTRA',
        'manishmalhotra',
        'MM White Logo',
    ]

    for pattern in mm_patterns:
        count = len(re.findall(pattern, content, re.IGNORECASE))
        if count > 0:
            issues.append(f"Found '{pattern}': {count} occurrence(s)")
            print(f"  [ISSUE] Found '{pattern}': {count} times")
        else:
            print(f"  [OK] No '{pattern}' found")

    if not issues:
        successes.append("No Manish Malhotra references found")

    # ============================================================================
    # 2. Verify JMC branding is present
    # ============================================================================
    print("\n2. Verifying JMC Branding Presence...")
    print("-" * 80)

    jmc_checks = {
        'JMC': 'JMC brand name',
        'Jewellers Madanlal Chaganlal': 'Full business name',
        'logo_small.png': 'JMC logo',
    }

    for pattern, description in jmc_checks.items():
        count = len(re.findall(pattern, content))
        if count > 0:
            print(f"  [OK] {description}: {count} occurrence(s)")
            successes.append(f"{description} present")
        else:
            issues.append(f"{description} NOT found")
            print(f"  [ISSUE] {description} NOT found")

    # ============================================================================
    # 3. Check Navigation Menu
    # ============================================================================
    print("\n3. Checking Navigation Menu...")
    print("-" * 80)

    jewellery_nav_items = [
        'Bridal Collection',
        'Fine Jewellery',
        'Diamond Necklaces',
        'Gold Rings',
        'Bridal Sets',
    ]

    fashion_nav_items = [
        'Lehengas',
        'Kurta Sets',
        'Sarees',
        'Sherwani Sets',
    ]

    # Check for jewellery items (should be present)
    for item in jewellery_nav_items:
        count = len(re.findall(item, content))
        if count > 0:
            print(f"  [OK] '{item}': {count} occurrence(s)")
            successes.append(f"Nav item '{item}' present")
        else:
            warnings.append(f"Nav item '{item}' not found")
            print(f"  [WARNING] '{item}' not found")

    # Check for fashion items (should NOT be present)
    for item in fashion_nav_items:
        count = len(re.findall(item, content))
        if count > 0:
            issues.append(f"Fashion item '{item}' still present ({count} times)")
            print(f"  [ISSUE] Fashion item '{item}' still present: {count} times")
        else:
            print(f"  [OK] Fashion item '{item}' removed")
            successes.append(f"Fashion item '{item}' removed")

    # ============================================================================
    # 4. Check Color Scheme
    # ============================================================================
    print("\n4. Checking JMC Color Scheme...")
    print("-" * 80)

    jmc_colors = {
        '#05231c': 'JMC Green',
        '#f9f5f0': 'JMC Cream',
        '#d4af37': 'JMC Gold',
    }

    for color, name in jmc_colors.items():
        count = len(re.findall(color, content, re.IGNORECASE))
        if count > 0:
            print(f"  [OK] {name} ({color}): {count} occurrence(s)")
            successes.append(f"{name} color present")
        else:
            warnings.append(f"{name} color not found")
            print(f"  [WARNING] {name} ({color}) not found")

    # ============================================================================
    # 5. Check Meta Tags
    # ============================================================================
    print("\n5. Checking Meta Tags...")
    print("-" * 80)

    # Title tag
    title_match = re.search(r'<title>([^<]+)</title>', content)
    if title_match:
        title = title_match.group(1)
        if 'JMC' in title:
            print(f"  [OK] Title contains JMC: '{title}'")
            successes.append("Title tag contains JMC")
        else:
            issues.append(f"Title doesn't contain JMC: '{title}'")
            print(f"  [ISSUE] Title doesn't contain JMC: '{title}'")
    else:
        issues.append("No title tag found")
        print(f"  [ISSUE] No title tag found")

    # Meta description
    meta_desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content)
    if meta_desc_match:
        desc = meta_desc_match.group(1)
        if 'JMC' in desc or 'Jewellers' in desc:
            print(f"  [OK] Meta description contains JMC")
            successes.append("Meta description contains JMC")
        else:
            warnings.append("Meta description might need JMC branding")
            print(f"  [WARNING] Meta description: '{desc[:100]}...'")
    else:
        warnings.append("No meta description found")
        print(f"  [WARNING] No meta description found")

    # ============================================================================
    # 6. Check Logo References
    # ============================================================================
    print("\n6. Checking Logo References...")
    print("-" * 80)

    logo_count = len(re.findall(r'logo_small\.png', content))
    base64_logo_count = len(re.findall(r'src="data:image/', content))

    if logo_count > 0:
        print(f"  [OK] logo_small.png referenced: {logo_count} time(s)")
        successes.append(f"JMC logo referenced {logo_count} times")
    else:
        issues.append("logo_small.png not found")
        print(f"  [ISSUE] logo_small.png not found")

    if base64_logo_count > 0:
        issues.append(f"Base64 encoded images still present: {base64_logo_count}")
        print(f"  [ISSUE] Base64 encoded images still present: {base64_logo_count}")
    else:
        print(f"  [OK] No base64 encoded logos")
        successes.append("No base64 encoded logos")

    # ============================================================================
    # 7. File Size Check
    # ============================================================================
    print("\n7. File Information...")
    print("-" * 80)

    import os
    file_size = os.path.getsize(filename) / (1024 * 1024)
    print(f"  File size: {file_size:.2f} MB")

    # ============================================================================
    # SUMMARY
    # ============================================================================
    print("\n" + "=" * 80)
    print("VERIFICATION SUMMARY")
    print("=" * 80)

    print(f"\nSuccesses: {len(successes)}")
    print(f"Warnings:  {len(warnings)}")
    print(f"Issues:    {len(issues)}")

    if len(issues) == 0 and len(warnings) == 0:
        print("\n" + "=" * 80)
        print("[SUCCESS] JMC conversion is COMPLETE!")
        print("=" * 80)
        status = "COMPLETE"
    elif len(issues) == 0:
        print("\n" + "=" * 80)
        print("[SUCCESS] JMC conversion is complete with minor warnings")
        print("=" * 80)
        status = "COMPLETE WITH WARNINGS"
    else:
        print("\n" + "=" * 80)
        print("[ATTENTION NEEDED] Some issues need to be resolved")
        print("=" * 80)
        status = "NEEDS ATTENTION"

    if warnings:
        print("\nWARNINGS:")
        print("-" * 80)
        for warning in warnings:
            print(f"  - {warning}")

    if issues:
        print("\nISSUES TO RESOLVE:")
        print("-" * 80)
        for issue in issues:
            print(f"  - {issue}")

    # Save report
    report_file = filename.replace('.html', '_verification_report.txt')
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("JMC CONVERSION VERIFICATION REPORT\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"Status: {status}\n")
        f.write(f"File: {filename}\n")
        f.write(f"Size: {file_size:.2f} MB\n\n")

        f.write(f"Successes: {len(successes)}\n")
        f.write(f"Warnings: {len(warnings)}\n")
        f.write(f"Issues: {len(issues)}\n\n")

        if successes:
            f.write("SUCCESSES:\n")
            f.write("-" * 80 + "\n")
            for success in successes:
                f.write(f"  - {success}\n")
            f.write("\n")

        if warnings:
            f.write("WARNINGS:\n")
            f.write("-" * 80 + "\n")
            for warning in warnings:
                f.write(f"  - {warning}\n")
            f.write("\n")

        if issues:
            f.write("ISSUES:\n")
            f.write("-" * 80 + "\n")
            for issue in issues:
                f.write(f"  - {issue}\n")

    print(f"\nDetailed report saved to: {report_file}")
    print("=" * 80)

if __name__ == "__main__":
    verify_conversion("JMC_Website.html")
