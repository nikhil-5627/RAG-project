from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embeddings(chunks):

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding

    return chunks