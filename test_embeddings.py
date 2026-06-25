from utils.text_splitter import split_text
from utils.embeddings import create_embeddings

sample_text = """
Employee leave policy allows 20 leaves annually.
""" * 50

chunks = split_text(sample_text)

embeddings = create_embeddings(chunks)

print("Chunks:", len(chunks))

print("Embeddings Shape:")

print(embeddings.shape)