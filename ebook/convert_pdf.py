"""
Script chuyển đổi file PDF sang Markdown sử dụng marker-pdf.
Sử dụng: python convert_pdf.py [path_to_pdf] hoặc chạy không có tham số để convert tất cả PDF trong thư mục.
"""

import sys
from pathlib import Path


def convert_single_pdf(pdf_path: Path, output_dir: Path = None):
    """Chuyển đổi một file PDF sang Markdown."""
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered

    if output_dir is None:
        output_dir = pdf_path.parent

    print(f"Đang chuyển đổi: {pdf_path.name}...")

    # Tạo converter
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )

    # Chuyển đổi
    rendered = converter(str(pdf_path))

    # Lấy text và images
    text, _, images = text_from_rendered(rendered)

    # Lưu file markdown
    md_filename = pdf_path.stem + ".md"
    md_path = output_dir / md_filename

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✓ Đã lưu: {md_path}")

    # Lưu images nếu có
    if images:
        images_dir = output_dir / (pdf_path.stem + "_images")
        images_dir.mkdir(exist_ok=True)
        for img_name, img_data in images.items():
            img_path = images_dir / img_name
            with open(img_path, "wb") as f:
                f.write(img_data)
        print(f"✓ Đã lưu {len(images)} hình ảnh vào: {images_dir}")

    return md_path


def convert_all_pdfs(directory: Path):
    """Chuyển đổi tất cả file PDF trong thư mục."""
    pdf_files = list(directory.glob("*.pdf"))

    if not pdf_files:
        print("Không tìm thấy file PDF nào trong thư mục.")
        return

    print(f"Tìm thấy {len(pdf_files)} file PDF.")
    print("-" * 50)

    for pdf_file in pdf_files:
        try:
            convert_single_pdf(pdf_file)
        except Exception as e:
            print(f"✗ Lỗi khi chuyển đổi {pdf_file.name}: {e}")

    print("-" * 50)
    print("Hoàn thành!")


def main():
    if len(sys.argv) > 1:
        # Chuyển đổi file được chỉ định
        pdf_path = Path(sys.argv[1])
        if not pdf_path.exists():
            print(f"Không tìm thấy file: {pdf_path}")
            sys.exit(1)
        if pdf_path.suffix.lower() != ".pdf":
            print(f"File phải có định dạng .pdf: {pdf_path}")
            sys.exit(1)
        convert_single_pdf(pdf_path)
    else:
        # Chuyển đổi tất cả PDF trong thư mục hiện tại
        current_dir = Path(__file__).parent
        convert_all_pdfs(current_dir)


if __name__ == "__main__":
    main()
