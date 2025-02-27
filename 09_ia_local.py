import pdfplumber

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama.llms import OllamaLLM


pdf_path = 'pdfs/boleto.pdf' # 'pdfs/despesas_sapiranga_2025.pdf' 'pdfs/orçamento.pdf'

text = ''
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()
        # break # pegar apenas página 1

llm = OllamaLLM(
    model='deepseek-r1:32',
    temperature=0,
)

template = """
Extraia e retorne as informações mais relevantes do texto fornecido:

Retorne os dados no formato JSON com nomes dos campos em snake_case.
{text}
"""

prompt = PromptTemplate(
    input_variables=['text'],
    template=template,
)

chain = prompt | llm | JsonOutputParser()

response = chain.invoke({'text': text})

print(response)