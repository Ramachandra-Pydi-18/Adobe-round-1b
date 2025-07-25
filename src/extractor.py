import PyPDF2
import os

def extract_text_from_pdfs(input_dir):
    data = {}
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            path = os.path.join(input_dir, filename)
            with open(path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
                data[filename] = text
    return data
