import os
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("pdfplumber not installed. Installing...")
    os.system("pip install pdfplumber")
    import pdfplumber


def extract_text_with_pdfplumber(pdf_path):
    """Extract text from PDF using pdfplumber (better quality)"""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {str(e)}")
        return None
    return text


def convert_pdfs_advanced(ebook_directory):
    """Convert PDF files using advanced extraction"""
    ebook_path = Path(ebook_directory)

    if not ebook_path.exists():
        print(f"Directory {ebook_directory} does not exist!")
        return

    pdf_files = list(ebook_path.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    print(f"Found {len(pdf_files)} PDF files to convert...")

    for pdf_file in pdf_files:
        print(f"Converting: {pdf_file.name}")

        text_content = extract_text_with_pdfplumber(pdf_file)

        if text_content:
            text_file = pdf_file.with_suffix(".txt")

            try:
                with open(text_file, "w", encoding="utf-8") as f:
                    f.write(text_content)
                print(f"✓ Converted to: {text_file.name}")
            except Exception as e:
                print(f"✗ Error saving {text_file.name}: {str(e)}")
        else:
            print(f"✗ Failed to extract text from {pdf_file.name}")


if __name__ == "__main__":
    ebook_dir = r"D:\Project\thesucesswaynote\ebook"
    convert_pdfs_advanced(ebook_dir)
    print("\nAdvanced conversion completed!")
