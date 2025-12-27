"""
HTML Formatter Script
Cleans and formats the Manish Malhotra HTML file with proper indentation
"""

from bs4 import BeautifulSoup
import os

def format_html_file(input_file, output_file):
    """Format HTML file with proper indentation"""

    print(f"Reading file: {input_file}")
    print(f"File size: {os.path.getsize(input_file) / (1024*1024):.2f} MB")

    # Read the HTML file
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("Parsing HTML...")
    # Parse with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    print("Formatting with proper indentation...")
    # Format with indentation
    formatted_html = soup.prettify()

    # Write to output file
    print(f"Writing to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_html)

    output_size = os.path.getsize(output_file) / (1024*1024)
    print(f"Done! Output file size: {output_size:.2f} MB")
    print(f"\nFormatted file saved as: {output_file}")

if __name__ == "__main__":
    input_file = "Manish_Malhotra_Original.html"
    output_file = "Manish_Malhotra_Formatted.html"

    try:
        format_html_file(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
