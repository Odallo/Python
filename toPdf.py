import fitz
from docx import Document
def pdf_to_word(pdf_path, word_path):
    pdf_document = fitz.open(pdf_path)
    doc = Document()
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        text = page.get_text()
        doc.add_paragraph(text)
    doc.save(word_path)