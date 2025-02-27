 Extraindo dados de PDFs com Python e IA
 
 ---
 Tags: #fleeting 
 Description: Assistindo a live do Pycode BR
 Theme:
## ID: 20250225220023
---

# <font color="#d7e3bc">Descrição breve: </font>

Em 1990,  [Jown Warnock](https://en.wikipedia.org/wiki/John_Warnock) começou a trabalhar em um projeto interno na Adobe. Com o objetivo de não apenas criar um formato de arquivo que tivesse a mesma aparência na tela como quando impresso, Warnock queria projetar um formato que permitisse aos usuários de computador compartilhar documentos com outras pessoas de maneira confiável e fácil, independentemente do sistema operacional que estivessem usando. Surgiu então o PDF(Portable Document Format).

Um arquivo PDF é um tipo de arquivo digital que pode conter texto, imagens, gráficos, tabelas, hiperlinks, assinaturas digitais, entre outros.

**Estrutura do PDF:**

- Os arquivos PDF são baseados na tecnologia [PostScript](https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf), que é uma linguagem de marcação usada para construir páginas.
- Os arquivos PDF podem conter dicionários, referências de objetos indiretos e streams.
- Os arquivos PDF podem ser otimizados para diferentes finalizações, como tela, web ou impressão.

O PDF usa uma linguagem chamada **PostScript**, como base, mais especificamente um versão chamada **PDF Syntax**, que é uma linguagem de descrição de página. Essa linguagem define como os textos, gráficos, imagens e outros elementos são posicionados e renderizados no documento.

O PostScript foi criado pela Adobe nos anos 80 como uma linguagem de marcação para impressão. Ele descreve documentos como um conjunto de instruções para impressoras e monitores. O PDF evoluiu a partir do PostScript, tornando-se um formato mais otimizado e independente para visualização em qualquer dispositivo.

Enquanto o PostScript é uma linguagem completa de programação com loops e condições, o PDF é mais uma estrutura de dados baseada em objetos e referencias, sem capacidade de execução de código dinâmico.

## Exemplo do código de um PDF


```
%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj

2 0 obj
<< /Type /Pages /Count 1 /Kids [3 0 R] >>
endobj

3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 300] /Contents 4 0 R >>
endobj

4 0 obj
<< /Length 44 >>
stream
BT
/F1 12 Tf
50 250 Td
(Hello, PDF!) Tj
ET
endstream
endobj

xref
0 5
0000000000 65535 f
0000000009 00000 n
0000000047 00000 n
0000000093 00000 n
0000000147 00000 n

trailer
<< /Size 5 /Root 1 0 R >>
startxref
200
%%EOF

```

- `%PDF-1.4` → Define a versão do PDF.
- `1 0 obj ... endobj` → Define o **catálogo**, que aponta para as páginas.
- `2 0 obj ... endobj` → Define a estrutura das páginas.
- `3 0 obj ... endobj` → Define a página e sua área de desenho (`MediaBox`).
- `4 0 obj ... endobj` → Contém o **conteúdo da página**, que é um texto `"Hello, PDF!"`.
    - `BT ... ET` → Inicia (`BT`) e finaliza (`ET`) o bloco de texto.
    - `/F1 12 Tf` → Define uma fonte fictícia (`F1`) com tamanho `12`.
    - `50 250 Td` → Move o cursor de escrita para a posição `(50,250)`.
    - `(Hello, PDF!) Tj` → Escreve o texto `"Hello, PDF!"`.
- `xref` → Índice dos objetos dentro do arquivo.
- `trailer` → Define o tamanho do documento e aponta para o **objeto raiz**.

**Curiosidade**: Quando um PDF contém uma mídia/imagem, o binário ou o base64 da mídia em questão é inserido no código do PDF.

# <font color="#76923c">Extrator de texto simples</font>

Utilizaremos a biblioteca [pdfplumber](https://github.com/jsvine/pdfplumber)

```
pip install pdfplumber
```

```
import pdfplumber

pdf_path = 'pdfs/orçamento.pdf'

text = ''
with pdfplumber.open(path_pdf) as pdf:
	for page in pdf.pages:
		text += page.extract_text()

print(text)
```

1. É necessário estudar a documentação do pdfplumber para entender os objetos.
2. `with pdfplumber.open(path_pdf) as pdf: `
	1. com a biblioteca pdfplumber `open` o pdf passado pelo caminho atribuído a variável `pdf_path` em uma instancia local chamada `pdf`
3. o `for` é necessário para ler todas as paginas do pdf
	1. `pdf.pages` o `pages` é uma classe da biblioteca pdfplumber
	2. `text += page.extract_text()` o texto será extraído e adicionado `+=` a variável `text` anteriormente declarada.

# <font color="#76923c">Extração de tabelas</font>


```
pip install pdfplumber
```


```
import pdfplumber

pdf_path = 'pdfs/orcamento.pdf'

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
```

O interessante é que a extração retorna uma lista. 
O `table_row` desta maneira conterá um conjunto de listas 
`np.shape(table_row)` retornará (15, 4)

# <font color="#76923c">Extraindo texto de PDF com imagem(scan)</font>


```
pip install pdf2image pytesseract
```

```
import pytesseract
from pdf2image import convert_from_path

pdf_path = 'pdfs/orcamento_img.pdf'

pages = convert_from_path(
	pdf_path = pdf_path,
)

text_data = ''
for page in pages:
	text = pytesseract.image_to_string(page)
	text_data += text + '\n'

print(text_data)

```


Para extrair texto quando se trata de uma imagem com conteúdo textual é necessário passar por um processo de [[Optical Character Recognition (OCR) ]].


# <font color="#92cddc">Extração de texto + RegEx para extrair dados</font>


```
pip install pdfplumber
```

```
import pdfplumber
import re

pdf_path = 'pdfs/orçamento.pdf'

text = ''
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()

name_regex = r"Nome:\s*(\w+\s\w+)"
name = re.search(name_regex, text)

address_regex = r"Endereco:\s*([\w\s,\.]+[\d]+(?:\s?-\s?[A-Za-z\s]+(?:,\s?[A-Za-z\s]+)*\s?-\s?[A-Za-z]{2,})?)"
address = re.search(address_regex, text)

date_regex = r"Data:\s*(\d{2}/\d{2}/\d{4})"
date = re.search(date_regex, text)

total_regex = r"TOTAL\s*R\$\s*([\d.,]+)"
total = re.search(total_regex, text)

if name:
    print("Nome:", name.group(1))
else:
    print("Nome não encontrado")

if address:
    print("Endereço:", address.group(1))
else:
    print("Endereço não encontrado")

if date:
    print("Data:", date.group(1))
else:
    print("Data não encontrada")

if total:
    print("Valor Total:", total.group(1))
else:
    print("Valor Total não encontrado")
```

[RegEx](https://en.wikipedia.org/wiki/Regular_expression) são expressões regulares, sendo basicamente uma linguagem, que possui sintaxe própria utilizada para localizar trechos dentro de um texto padrão. [Um site excelente para produzir regex.](https://regex101.com/)

Dado a extração do texto proveniente de um PDF o próximo passo seria encontrar um conteúdo ou algum trecho especifico, para isso foi utilizado regex para selecionar essa informação e armazenar em algum banco de dados ou json.

No python existem um biblioteca nativa chamada `re` que serve para rodar expressões regulares.

O grande problema enfrentado quando se coloca esse procedimento em produção esta no fato de que constante mente os documentos sofrem alterações nas suas formatações pelos usuários e empresas. 
O passo a seguir resolve o problema que é ter que ficar constantemente alterando o regex constantemente utilizando IA para esse trabalho extenuante. 

# <font color="#ff0000">Extração de texto + IA para extrair dados</font>

Neste exemplo iremos extrair o texto de um PDF e envia-lo para uma IA que ira devolver o dado estruturado.


```
pip install pdfplumber python-dotenv langchain langchain_openai 

# .env 
OPENAI_API_KEY='API KEY'
```

### OBS:

- `temperature` o parâmetro que controla a precisão das respostas, = 0 significa que retornará respostas o mais assertivas possível.

- `template` é o que será inserido no prompt que será passado para IA.

- Snake_case significa separar do dados por _ como é comum em python.

- `chain = prompt | llm | JsonOutputParser()` essa sintaxe separada por OR( | ) tem um significado especifico dentro do framework da LangChain, onde neste caso entende como conectores, como um pipeline que foi construído. 
- Neste caso ele ira utilizar o prompt, depois enviara o prompt para a llm e por fim essa resposta será parseada em Json.

# <font color="#ff0000">Extração de texto (scan) + IA para extrair dado 2</font>


```
pip install pdf2image pytesseract python-dotenv langchain langchain_openai 

# .env 
OPENAI_API_KEY='API KEY'
```

```
import pytesseract

import os
from dotenv import load_dotenv

  

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from pdf2image import convert_from_path


load_dotenv(dotenv_path=".env")
openai_api_key = os.getenv("OPENAI_API_KEY")


pdf_path = 'pdfs/orçamento_img.pdf'


pages = convert_from_path(
    pdf_path=pdf_path,
)


text_data = ''
for page in pages:
    text = pytesseract.image_to_string(page)
    text_data += text + '\n'


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
```



# <font color="#ffff00">Extração de texto + IA para extrair dados genéricos</font>

Neste exemplo foi dado um template genérico para que a própria IA identificasse os dados que poderiam ser relevantes sem que fosse especificado explicitamente.

```
pip install pdfplumber python-dotenv langchain langchain_openai 

# .env 
OPENAI_API_KEY='API KEY'
```


```
import pdfplumber
import os
from dotenv import load_dotenv


from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
  

load_dotenv(dotenv_path=".env")
openai_api_key = os.getenv("OPENAI_API_KEY")


pdf_path = 'pdfs/boleto.pdf'

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
Extraia e retorne as informações mais relevantes do texto fornecido:

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
```

O resultado foi satisfatório.

# <font color="#ffff00">Extração de texto (Scan) + IA para extrair dados genéricos</font>


```
pip install pdf2image pytesseract python-dotenv langchain langchain_openai 

# .env 
OPENAI_API_KEY='API KEY'
```

```
import pytesseract
import os
from dotenv import load_dotenv


from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from pdf2image import convert_from_path


load_dotenv(dotenv_path=".env")
openai_api_key = os.getenv("OPENAI_API_KEY")


pdf_path = 'pdfs/orçamento_img.pdf'

pages = convert_from_path(
    pdf_path=pdf_path,
)


text_data = ''

for page in pages:
    text = pytesseract.image_to_string(page)
    text_data += text + '\n'


llm = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0,
    openai_api_key=openai_api_key
)

  

template = """
Extraia e retorne as informações mais relevantes do texto fornecido:

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
```

# <font color="#e36c09">Extrair texto + IA local com Ollama e modelo DeepSeek 32b para extrair dados</font>

Após baixar o [Ollama](https://ollama.com/download) basta utilizar o código abaixo para rodar localmente sua IA:

```
ollama run deepseek-r1:32b
```


```
pip install pdfplumber langchain langchain_ollama
```


```
import pdfplumber


from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama.llms import OllamaLLM


pdf_path = 'pdfs/boleto.pdf' 


text = ''
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()
        

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
```






---
## Contexto
- **Situação**: Iniciando o mestrado no ITA, primeiro semestre, me interessei no tema IA e criação de agents e por isso decidi assistir conteúdos relacionados a aplicações com IA.
- **Fonte**: 

## Próximos Passos
- **Ação 1**: 
- **Ação 2**: 

## Referências
- [Live 036](https://www.youtube.com/watch?v=YPuKikID98g) - Link da live
- [Meu git](lhttps://github.com/viniciusrondon/Extraindo-PDF-com-Python-e-IA/tree/master) - github
- [Um site excelente para produzir regex.](https://regex101.com/) - RegEx
- [ferramenta para Json 01](https://jsonformatter.curiousconcept.com/#)
- [ferramenta para json 02](https://jsoncrack.com/editor)
- [ferramenta para json 03](https://todiagram.com/editor?utm_source=jsoncrack&utm_medium=upgrade_modal)
- [Ollama](https://ollama.com/download)




