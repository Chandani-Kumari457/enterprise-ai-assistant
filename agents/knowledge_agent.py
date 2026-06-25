from config.gemini_config import model

def knowledge_agent(question, pdf_text):

    prompt = f"""
    Answer the question ONLY using the PDF content.

    PDF Content:
    {pdf_text}

    Question:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text