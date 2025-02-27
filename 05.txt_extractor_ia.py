import pdfplumber
import os
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

load_dotenv(dotenv_path=".env")
openai_api_key = os.getenv("OPENAI_API_KEY")

pdf_path = 'pdfs/orçamento.pdf'

text = ''

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()

llm = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0,
    openai_api_key=openai_api_key
)

template = """
Extraia e retorne os seguintes dados do texto fornecido:
- Nome
- Endereço
- Serviços
    - Unidade
    - Descrição
    - Valor unitário
    - Valor total do serviço
- Valor total

Retorne os dados no formato JSON com nomes dos campos em snake_case.
{text}
"""
prompt = PromptTemplate(
    input_variables=['text'],
    template=template
)

chain = prompt | llm | JsonOutputParser()

response = chain.invoke({'text': text})

print(response)
