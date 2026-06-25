from utils.text_splitter import split_text

sample_text = """
This is a test document.
""" * 200

chunks = split_text(sample_text)

print("Number of Chunks:", len(chunks))

print("\nFirst Chunk:\n")

print(chunks[0])