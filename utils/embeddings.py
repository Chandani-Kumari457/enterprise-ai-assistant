from sentence_transformers import SentenceTransformer

print("Loading Model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    device="cpu"
)

print("Model Loaded")


def create_embeddings(chunks):

    embeddings = model.encode(chunks)

    return embeddings