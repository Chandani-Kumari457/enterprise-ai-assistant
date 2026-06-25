from pypdf import PdfReader

def read_pdf(uploaded_file):

    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    return text