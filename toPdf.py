from pdf2docx import Converter
pdf_path = input("Enter the pdf path: ")
word_path = input("Enter the word path: ")
def pdf_to_word(pdf_path, word_path):
    cv = Converter(pdf_path)
    cv.convert(word_path, start=0, end=None)
    cv.close()
    print("Conversion successful")
pdf_to_word("sample.pdf", "sample.docx")