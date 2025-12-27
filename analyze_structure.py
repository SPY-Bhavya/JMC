"""
HTML Structure Analyzer
Extracts the main structure and sections from the HTML file
"""

from bs4 import BeautifulSoup

def analyze_html_structure(input_file):
    """Analyze HTML structure and extract main sections"""

    print(f"Analyzing: {input_file}\n")

    # Read the HTML file
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    print("=" * 80)
    print("DOCUMENT STRUCTURE")
    print("=" * 80)

    # Get title
    title = soup.find('title')
    if title:
        print(f"\nTitle: {title.text}")

    # Analyze main sections
    print("\n" + "=" * 80)
    print("MAIN SECTIONS")
    print("=" * 80)

    # Find all major sections (header, nav, main, section, footer, etc.)
    sections = soup.find_all(['header', 'nav', 'main', 'section', 'footer', 'div'],
                            class_=True, limit=50)

    for i, section in enumerate(sections, 1):
        tag_name = section.name
        classes = ' '.join(section.get('class', []))
        id_attr = section.get('id', '')

        # Get text preview (first 100 chars)
        text_preview = section.get_text(strip=True)[:100]

        print(f"\n{i}. <{tag_name}>")
        if id_attr:
            print(f"   ID: {id_attr}")
        if classes:
            print(f"   Classes: {classes}")
        if text_preview:
            print(f"   Content: {text_preview}...")

    # Count images
    images = soup.find_all('img')
    print(f"\n" + "=" * 80)
    print(f"Total Images: {len(images)}")

    # Count links
    links = soup.find_all('a')
    print(f"Total Links: {len(links)}")

    # Find navigation items
    print("\n" + "=" * 80)
    print("NAVIGATION STRUCTURE")
    print("=" * 80)

    nav_items = soup.find_all(['nav', 'ul', 'menu'])
    for nav in nav_items[:5]:  # First 5 nav elements
        nav_text = nav.get_text(strip=True)[:200]
        print(f"\n{nav.name}: {nav_text}")

    # Save structure to file
    with open('structure_analysis.txt', 'w', encoding='utf-8') as f:
        f.write(f"HTML Structure Analysis\n")
        f.write(f"{'=' * 80}\n\n")
        f.write(f"Title: {title.text if title else 'N/A'}\n\n")
        f.write(f"Total Images: {len(images)}\n")
        f.write(f"Total Links: {len(links)}\n\n")

        f.write(f"Main Sections:\n")
        f.write(f"{'-' * 80}\n")

        for i, section in enumerate(sections, 1):
            tag_name = section.name
            classes = ' '.join(section.get('class', []))
            id_attr = section.get('id', '')
            text_preview = section.get_text(strip=True)[:150]

            f.write(f"\n{i}. <{tag_name}>\n")
            if id_attr:
                f.write(f"   ID: {id_attr}\n")
            if classes:
                f.write(f"   Classes: {classes}\n")
            if text_preview:
                f.write(f"   Content: {text_preview}...\n")

    print(f"\n" + "=" * 80)
    print("Analysis saved to: structure_analysis.txt")

if __name__ == "__main__":
    analyze_html_structure("Manish_Malhotra_Formatted.html")
