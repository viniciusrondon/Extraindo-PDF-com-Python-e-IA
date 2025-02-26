Extraindo dados de PDFs com Python e IA

 ---
 Tags: #fleeting 
 Description: Assistindo a live do Pycode BR
 Theme:
## ID: 20250225220023
---

# <font color="#d7e3bc">Descrição breve: </font>

Em 1990,  [Jown Warnock]((https://en.wikipedia.org/wiki/John_Warnock) começou a trabalhar em um projeto interno na Adobe. Com o objetivo de não apenas criar um formato de arquivo que tivesse a mesma aparência na tela como quando impresso, Warnock queria projetar um formato que permitisse aos usuários de computador compartilhar documentos com outras pessoas de maneira confiável e fácil, independentemente do sistema operacional que estivessem usando. Surgiu então o PDF(Portable Document Format).

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



