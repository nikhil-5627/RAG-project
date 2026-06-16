from src.pdf_loader import load_pdf

pdf_path = "data/sample.pdf"

pages = load_pdf(pdf_path)

for page in pages:
    print(f"\n--- Page {page['page_number']} ---")
    print(page["text"][:500])