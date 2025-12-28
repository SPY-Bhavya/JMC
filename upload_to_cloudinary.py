import os
import requests
import json
import sys

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Cloudinary configuration
CLOUD_NAME = "dzgd0daeb"
UPLOAD_PRESET = "ml_default"  # You can create a custom upload preset in Cloudinary settings
FOLDER_NAME = "JMC"

# Get all images
images_dir = "images"
image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

print(f"Found {len(image_files)} images to upload to Cloudinary")
print(f"Cloud name: {CLOUD_NAME}")
print(f"Folder: {FOLDER_NAME}\n")

uploaded_urls = {}

for image_file in image_files:
    image_path = os.path.join(images_dir, image_file)

    print(f"Uploading {image_file}...", end=" ")

    try:
        # Cloudinary upload URL
        url = f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/image/upload"

        # Upload file
        with open(image_path, 'rb') as file:
            files = {'file': file}
            data = {
                'upload_preset': UPLOAD_PRESET,
                'folder': FOLDER_NAME,
                'public_id': os.path.splitext(image_file)[0]  # Use filename without extension as public_id
            }

            response = requests.post(url, files=files, data=data)

            if response.status_code == 200:
                result = response.json()
                uploaded_urls[image_file] = result['secure_url']
                print(f"✓ SUCCESS")
                print(f"  URL: {result['secure_url']}")
            else:
                print(f"✗ FAILED - Status code: {response.status_code}")
                print(f"  Error: {response.text}")

    except Exception as e:
        print(f"✗ ERROR - {str(e)}")

print(f"\n{'='*60}")
print(f"Upload Summary: {len(uploaded_urls)}/{len(image_files)} images uploaded successfully")
print(f"{'='*60}\n")

# Save URLs to file for reference
with open('cloudinary_urls.json', 'w') as f:
    json.dump(uploaded_urls, f, indent=2)

print("URLs saved to cloudinary_urls.json")
print("\nCloudinary URLs:")
for filename, url in uploaded_urls.items():
    print(f"{filename}: {url}")
