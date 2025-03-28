# Questao 1 ....................
# Download e Compactação de PDFs - ANS

Este projeto tem como objetivo baixar arquivos PDF de uma página da ANS (Agência Nacional de Saúde Suplementar) e compactá-los em um arquivo ZIP. Ele utiliza o BeautifulSoup para fazer o parsing da página HTML e encontrar os links dos arquivos PDF, e o `requests` para realizar o download dos arquivos.

## Funcionalidades

- Baixa arquivos PDF contendo os anexos "Anexo I" e "Anexo II" da página da ANS.
- Compacta os arquivos PDF em um arquivo ZIP.
- Realiza o download e a compactação na mesma pasta onde o script é executado.
- Utiliza logs para mostrar o andamento do processo.

## Dependências

Este projeto usa as seguintes bibliotecas:

- `requests`: para fazer requisições HTTP e baixar os arquivos PDF.
- `beautifulsoup4`: para fazer o parsing da página HTML e extrair os links para os arquivos PDF.
- `zipfile`: para criar o arquivo ZIP contendo os arquivos PDF baixados.


## Instale as denpendências com pip

 pip install requests beautifulsoup4 lxml

## iniciando o programa no seu terminal

``python questao1.py ``









# QUESTAO 2 ...........................
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




## QUESTAO 3 

# Importação de Dados para MySQL e Consultas de Operadoras

Este projeto tem como objetivo importar dados de arquivos CSV para um banco de dados MySQL e realizar consultas sobre as operadoras de saúde com base nos dados importados.

## Pré-requisitos

- Python 3.x
- MySQL Server instalado
- Biblioteca Python `mysql-connector-python`
- Acesso a arquivos CSV com os dados a serem importados para o banco de dados

## Instalação



Se você ainda não tiver a biblioteca mysql-connector-python instalada, use o seguinte comando:

``bash``

pip install mysql-connector-python
Configuração do MySQL:

#Antes de rodar o programa, certifique-se de ter o MySQL instalado e rodando na sua máquina.

#Crie um banco de dados MySQL com o nome desejado (por exemplo, seu_banco).

## Altere as configurações de conexão no código, caso necessário. O código usa as seguintes credenciais por padrão:

Host: localhost

Usuário: root

Senha: senha

Banco de dados: seu_banco

Estrutura dos arquivos CSV:

Coloque seus arquivos CSV na pasta especificada no código. O caminho padrão está definido como C:\Users\fabio\OneDrive\Área de Trabalho\Testes_Nivelamento.

O programa irá buscar arquivos que começam com 1T2023, 2T2023, 3T2023, 4T2023, 1T2024, 2T2024, 3T2024, 4T2024.

##Como Usar
Execute o programa Python:

Após ter feito as configurações necessárias, você pode rodar o programa executando o seguinte comando no terminal ou prompt de comando:


python questao3.py
## O que o programa faz:

Criação das tabelas no banco de dados: O programa irá criar as tabelas demonstrativos_contabeis e operadoras_ativas no banco de dados MySQL se elas ainda não existirem.

Importação dos dados CSV: O programa irá importar os dados dos arquivos CSV para a tabela demonstrativos_contabeis.

Consultas de Operadoras:

Consultará as 10 operadoras com mais despesas no último trimestre.

Consultará as 10 operadoras com mais despesas no último ano.

Exibição dos resultados: As informações das consultas serão impressas no terminal.



## O programa exibirá informações sobre a criação das tabelas, a importação dos dados e as consultas realizadas, como por exemplo:


Tabela criada com sucesso!
Dados do arquivo 1T2023.csv importados com sucesso!
Dados do arquivo 2T2023.csv importados com sucesso!
Top 10 Operadoras no Último Trimestre:
Operadora A: 1,000,000.00 de despesas
Operadora B: 850,000.00 de despesas
...

Top 10 Operadoras no Último Ano:
Operadora A: 5,000,000.00 de despesas
Operadora C: 4,500,000.00 de despesas
...
Fechamento da conexão:

Após a execução das consultas, o programa irá fechar a conexão com o banco de dados.

Considerações Finais
Certifique-se de que os arquivos CSV estão no formato correto e com as informações necessárias para o correto funcionamento do programa.

A base de dados do MySQL deve estar configurada corretamente, com as permissões de acesso adequadas.

#####################################################

## QUESTAO 4

