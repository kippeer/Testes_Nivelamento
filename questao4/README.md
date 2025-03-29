# Sistema de Busca de Operadoras de Saúde

Este projeto implementa um sistema completo de busca de operadoras de saúde, consistindo em uma interface web em Vue.js e um servidor Python/Flask. O sistema permite buscar informações detalhadas sobre operadoras de saúde usando diversos critérios de pesquisa.

## Funcionalidades

- Busca inteligente por múltiplos campos:
  - Razão Social
  - Nome Fantasia
  - Cidade
  - Bairro
  - Endereço
  - Representante
- Interface responsiva e amigável
- Exibição detalhada das informações das operadoras
- Debounce na busca para melhor performance
- Feedback visual durante o carregamento

## Estrutura do Projeto

```
.
├── src/
│   └── App.vue           # Interface web em Vue.js
├── server.py             # Servidor Flask com API de busca
├── requirements.txt      # Dependências Python
├── package.json         # Dependências Node.js
└── postman_collection.json  # Coleção Postman para testes
```

## Requisitos

### Backend (Python)
- Python 3.8+
- Flask 2.3.3
- Flask-CORS 4.0.0
- pandas 2.1.1
- fuzzywuzzy 0.18.0
- python-Levenshtein 0.21.1

### Frontend (Node.js)
- Node.js 14+
- Vue.js 3.3.4
- Vite 5.0.0
- Tailwind CSS 3.3.5
- Axios 1.6.2

## Instalação

1. Clone o repositório:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

3. Instale as dependências Node.js:
```bash
npm install
```

## Configuração

1. Certifique-se de que o arquivo CSV `Relatorio_cadop.csv` está presente na raiz do projeto
2. O arquivo deve conter todos os campos necessários conforme a estrutura da tabela `operadoras_ativas`

## Executando o Projeto

1. Inicie o servidor Python:
```bash
python server.py
```

2. Em outro terminal, inicie o frontend:
```bash
npm run dev
```

3. Acesse a aplicação em `http://localhost:5173`

## API Endpoints

### GET /api/search
- **Descrição**: Busca operadoras de saúde
- **Parâmetros**:
  - `q` (query string): Termo de busca
- **Retorno**: Lista de operadoras que correspondem à busca (máximo 10 resultados)
- **Exemplo**: `http://localhost:5000/api/search?q=unimed`

## Estrutura de Dados

Cada operadora contém os seguintes campos:
- `nome_operadora`
- `cnpj`
- `razao_social`
- `nome_fantasia`
- `modalidade`
- `logradouro`
- `numero`
- `complemento`
- `bairro`
- `cidade`
- `uf`
- `cep`
- `ddd`
- `telefone`
- `fax`
- `endereco_eletronico`
- `representante`
- `cargo_representante`
- `regiao_de_comercializacao`
- `data_registro_ans`

## Testes

A coleção Postman inclui testes para diversos cenários:
- Busca por nome da operadora
- Busca por endereço
- Busca por representante
- Busca com query vazia
- Busca com correspondência parcial

## Características Técnicas

### Frontend
- Interface responsiva com Tailwind CSS
- Componentes Vue.js 3 com Composition API
- Debounce nas buscas (300ms)
- Tratamento de estados de loading e erro
- Layout em grid para informações detalhadas

### Backend
- API RESTful com Flask
- CORS habilitado para desenvolvimento
- Busca fuzzy para melhor correspondência
- Ordenação por relevância
- Limite de 10 resultados por busca
- Threshold de relevância de 60%

## Segurança
- Sanitização de inputs
- Proteção contra SQL injection (usando pandas)
- Headers CORS apropriados
- Validação de parâmetros de busca