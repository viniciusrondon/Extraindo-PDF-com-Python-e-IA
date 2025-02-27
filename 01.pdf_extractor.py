import pdfplumber

pdf_path = 'pdfs/orçamento.pdf'

text = ''

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()

print(text)

pdf_path_2 = 'pdfs/boleto.pdf'

text_2 = ''

with pdfplumber.open(pdf_path_2) as pdf:
    for page in pdf.pages:
        text_2 += page.extract_text()

print(text_2)
