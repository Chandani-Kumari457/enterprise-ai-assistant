from utils.text_splitter import split_text
from utils.embeddings import create_embeddings
from utils.faiss_db import create_faiss_index

sample_text = """
Employee leave policy allows 20 leaves annually.
""" * 50

chunks = split_text(sample_text)

embeddings = create_embeddings(chunks)

index = create_faiss_index(embeddings)

print("Total Vectors Stored:")

print(index.ntotal)

def search_faiss(index, query_embedding):

    distances, indices = index.search(
        query_embedding.astype("float32"),
        k=3
    )

    return indices