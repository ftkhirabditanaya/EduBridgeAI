import os
import pdfplumber
from docx import Document


def extract_text(file_path):
    """
    Extract text from PDF, DOCX or TXT resumes.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf(file_path)

    elif extension == ".docx":
        return extract_docx(file_path)

    elif extension == ".txt":
        return extract_txt(file_path)

    else:
        raise ValueError(
            "Unsupported file format. Use PDF, DOCX or TXT."
        )


def extract_pdf(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_docx(file_path):

    doc = Document(file_path)

    paragraphs = []

    for para in doc.paragraphs:
        paragraphs.append(para.text)

    return "\n".join(paragraphs)


def extract_txt(file_path):

    with open(file_path, "r", encoding="utf-8") as file:

        return file.read()