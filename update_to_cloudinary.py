import json
import re
import sys

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load Cloudinary URL mapping
with open('cloudinary_urls_mapping.json', 'r') as f:
    cloudinary_mapping = json.load(f)

# Read the HTML file
with open('JMC Final.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

print("Replacing local image paths with Cloudinary URLs...\n")

replacements_made = 0

# Replace img src attributes
for filename, cloudinary_url in cloudinary_mapping.items():
    # Replace in img tags
    old_path = f'images/{filename}'

    # Count occurrences
    count = html_content.count(old_path)

    if count > 0:
        html_content = html_content.replace(old_path, cloudinary_url)
        replacements_made += count
        print(f"✓ Replaced '{old_path}' with Cloudinary URL ({count} occurrences)")

# Replace CSS background-image URLs
for filename, cloudinary_url in cloudinary_mapping.items():
    # Pattern for CSS background-image
    old_pattern = f"url\\('images/{filename}'\\)"
    new_pattern = f"url('{cloudinary_url}')"

    matches = re.findall(old_pattern, html_content)
    if matches:
        html_content = re.sub(old_pattern, new_pattern, html_content)
        replacements_made += len(matches)
        print(f"✓ Replaced CSS background for '{filename}' ({len(matches)} occurrences)")

# Save the updated HTML
with open('JMC Final.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\n{'='*60}")
print(f"✓ SUCCESS: Made {replacements_made} replacements")
print(f"✓ File updated: JMC Final.html")
print(f"{'='*60}\n")
print("All images now load from Cloudinary CDN!")
