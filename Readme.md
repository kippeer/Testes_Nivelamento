# Projeto de Extração, Transformação e Compactação de Dados

Este projeto visa extrair dados de uma tabela contida em um PDF, transformar as informações de acordo com um mapeamento específico, salvar esses dados em um arquivo CSV e, por fim, compactá-los em um arquivo ZIP. O código foi implementado em Python.

## Funcionalidade

1. **Extração de Dados**: A partir de um arquivo PDF, o projeto extrai os dados de uma tabela e os armazena em formato de lista.
2. **Transformação de Dados**: As colunas `OD` e `AMB` são transformadas de acordo com um mapeamento pré-definido:
    - `OD`: "S" para "Segmentação Obrigatória" e "N" para "Segmentação Não Obrigatória".
    - `AMB`: "S" para "Procedimento Ambulatorial" e "N" para "Procedimento Não Ambulatorial".
3. **Salvar em CSV**: Os dados transformados são salvos em um arquivo CSV.
4. **Compactação em ZIP**: O arquivo CSV é compactado em um arquivo ZIP para facilitar o armazenamento ou envio.

## Como Usar

### Pré-requisitos

Para rodar este projeto, você precisará do Python instalado em sua máquina. O código também utiliza as bibliotecas `csv`, `zipfile`, e `pdfplumber`.

1. Instale o `pdfplumber` para extrair dados de PDFs:

```bash
pip install pdfplumber