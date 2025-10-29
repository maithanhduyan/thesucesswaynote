import os
import sys
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print("PyPDF2 not installed. Installing...")
    os.system("pip install PyPDF2")
    import PyPDF2


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyPDF2"""
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {str(e)}")
        return None
    return text


def convert_pdfs_to_text(ebook_directory):
    """Convert all PDF files in the directory to text files"""
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

        # Extract text
        text_content = extract_text_from_pdf(pdf_file)

        if text_content:
            # Create output text file
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
    convert_pdfs_to_text(ebook_dir)
    print("\nConversion completed!")
