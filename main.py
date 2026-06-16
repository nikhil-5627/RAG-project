from src.pdf_loader import load_pdf
from src.chunker import create_chunks
from src.embedder import create_embeddings

pages = load_pdf("data/sample.pdf")

chunks = create_chunks(pages)

chunks = create_embeddings(chunks)

print(chunks[0]["embedding"][:10])
print(len(chunks[0]["embedding"]))