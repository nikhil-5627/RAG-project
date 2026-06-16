from pypdf import PdfReader


def load_pdf(pdf_path: str):
    """
    Load PDF and extract text page by page.
    """

    reader = PdfReader(pdf_path)

    pages = []

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()

        pages.append(
            {
                "page_number": page_num + 1,
                "text": text
            }
        )

    return pages