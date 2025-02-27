import pdfplumber
import numpy as np

pdf_path = 'pdfs/orçamento.pdf'

table_row = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                print(row)
                table_row.append(row)

table_row
np.shape(table_row)