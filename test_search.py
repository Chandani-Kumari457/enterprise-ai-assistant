import numpy as np

from utils.text_splitter import split_text
from utils.embeddings import create_embeddings
from utils.faiss_db import (
    create_faiss_index,
    search_faiss
)

text = """
Employee leave policy allows 20 leaves annually.

Medical leave is limited to 10 days.

Work from home is allowed twice a week.

Projects must be completed before deadlines.
"""

chunks = split_text(text)

embeddings = create_embeddings(chunks)

index = create_faiss_index(embeddings)

question = "What is the leave policy?"

query_embedding = create_embeddings(
    [question]
)

indices = search_faiss(
    index,
    np.array(query_embedding)
)

print(indices)

print("\nRelevant Chunk:\n")

print(
    chunks[
        indices[0][0]
    ]
)