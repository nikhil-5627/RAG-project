from src.pdf_loader import load_pdf
from src.chunker import create_chunks

pages = load_pdf("data/sample.pdf")

chunks = create_chunks(
    pages,
    chunk_size=500,
    overlap=50
)

print(f"Total Chunks: {len(chunks)}")

for chunk in chunks[:5]:
    print("\n================")
    print(f"Chunk ID: {chunk['chunk_id']}")
    print(f"Page: {chunk['page_number']}")
    print(chunk["text"])