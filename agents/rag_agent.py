import numpy as np
from utils.education_parser import extract_education

from config.gemini_config import model

from utils.text_splitter import split_text
from utils.embeddings import create_embeddings
from utils.faiss_db import (
    create_faiss_index,
    search_faiss
)

def rag_agent(question, document_text):
    education_data = extract_education(document_text)

    print("EDUCATION DATA:")
    print(education_data)

    chunks = split_text(document_text)

    embeddings = create_embeddings(chunks)

    index = create_faiss_index(embeddings)

    query_embedding = create_embeddings(
        [question]
    )

    indices = search_faiss(
        index,
        np.array(query_embedding)
    )

    context = ""

    for idx in indices[0]:

        if idx != -1:

            context += chunks[idx] + "\n"

    context = context[:15000]
    print("\n========== CONTEXT ==========\n")
    print(context)
    print("\n=============================\n")
    print("CONTEXT:")
    print(context)

    prompt = f"""
You are an intelligent document assistant.

Answer questions ONLY using the information
present in the document context.

Rules:

- Understand the meaning of the question.
- Different phrasings may ask the same thing.
- Answer clearly and directly.
- If the answer exists in the document,
  provide it.
- If the answer is not available,
  say:
  "The information is not available in the document."

- If the question refers to:
  person,
  candidate,
  student,
  applicant,
  resume owner,
  resume holder,
  he,
  she,

  - If the user asks:
  "Whose resume is this?"
  "Who is this candidate?"
  "What is the name of the person?"
  "Who owns this resume?"

  Then find and return the candidate's full name from the document.

  identify the person from the document.

Document Context:
{context}

Question:
{question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text


def summarize_document(pdf_text):

    prompt = f"""
Summarize the following document clearly.

Include:
- Main purpose
- Important details
- Skills, projects, education (if resume)
- Key takeaways

Document:

{pdf_text}
"""

    response = model.generate_content(
        prompt
    )

    return response.text