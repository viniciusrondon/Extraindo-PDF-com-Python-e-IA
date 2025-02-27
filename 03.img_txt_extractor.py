import pytesseract
from pdf2image import convert_from_path

pdf_path = 'pdfs/orçamento_img.pdf'

pages = convert_from_path(
    pdf_path=pdf_path,
)

text_data = ''

for page in pages:
    text = pytesseract.image_to_string(page)
    text_data += text + '\n'

print(text_data)