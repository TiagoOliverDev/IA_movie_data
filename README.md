# 🎬 IA Movie Insights - OpenAI + Python

Projeto simples e objetivo que utiliza a **OpenAI API** para buscar informações sobre um filme com base apenas no seu **título**. Ele retorna uma resposta estruturada contendo:

- 📅 Data de lançamento  
- 💵 Bilheteria estimada  
- 📝 Sinopse curta  

Além disso, o projeto **armazena as consultas válidas em um banco SQLite** para evitar chamadas repetidas à API, otimizando **custos** e melhorando a **performance**.

---

## 🚀 Funcionalidades

✅ Recebe o nome de um filme  
✅ Consulta a OpenAI (Chat Completions) com Function Calling  
✅ Valida a resposta com Pydantic  
✅ Salva histórico das consultas em SQLite  
✅ Consulta o histórico antes de chamar a OpenAI  
✅ Retorna os dados formatados em JSON  
✅ Possui tratamento de erros e logs detalhados  
✅ Estrutura modular e escalável  
✅ Interface de linha de comando com Typer  
✅ API Web com FastAPI  
✅ Totalmente testado com Pytest  

---

## 🗂️ Estrutura do Projeto

```bash
IA_movie_data/
├── app/
│   └── api/
│       └── routes.py             # Rotas da API
│   └── main.py                   # Ponto de entrada do FastAPI
├── cli.py                        # CLI com Typer
├── core/
│   └── openai_handler.py         # Integração com OpenAI + lógica de cache
├── config/
│   └── config.py                 # Carrega variáveis de ambiente
├── storage/
│   └── db_handler.py             # Interação com banco SQLite
├── schemas/
│   └── movie_info.py             # Schema principal de resposta
│   └── request.py                # Schema da requisição da API
│   └── response.py               # Schema da resposta da API
├── tests/
│   ├── test_openai_handler.py    # Testes da função principal
│   ├── test_db_handler.py        # Testes do banco
│   └── test_api.py               # Testes do endpoint da API
├── utils/
│   └── logger.py                 # Logger estruturado e colorido
├── .env                          # Chave da OpenAI + modelo
├── Dockerfile                    # Imagem Docker
├── docker-compose.yml            # Orquestração Docker
├── requirements.txt              # Dependências
└── README.md              

## ⚙️ Como Executar o Projeto

### 🔧 Pré-requisitos
- Python 3.11+   
- Conta OpenAI com uma chave de API ativa
- Docker (opcional, para executar em container)

### 1. Clone o repositório

```bash
git clone https://github.com/TiagoOliverDev/IA_movie_data.git
cd IA_movie_data
```

### 2. Crie arquivo .env e insira sua api key OpenAi

```bash
OPENAI_API_KEY=sk-sua-chave-aqui
OPENAI_MODEL=gpt-3.5-turbo
```

### 3. Instale as dependências

```bash
python -m venv env
source env/bin/activate  # ou env\Scripts\activate no Windows
pip install -r requirements.txt
```

### 🎯 Formas de Uso


### ✅ CLI (Linha de Comando com Typer)

```bash
python cli.py "Titanic"
```

### 🌐 API Web com FastAPI

```bash
python -m app.main  

Acesse a documentação interativa: http://localhost:8000/docs
```

### 🐳 Executando com Docker

```bash
docker-compose up --build

Acesse a documentação interativa: http://localhost:8000/docs
```


### 🧪 Testes Automatizados

Execute todos os testes com:

```bash
pytest
```


### 💻 Exemplo via Código Python

```bash

from core.openai_handler import get_movie_insights

resultado = get_movie_insights("Interestelar")
print(resultado)

```

### Retorno esperado

```bash

{
  "data_lancamento": "07 de novembro de 2014",
  "bilheteria": "$677 milhões",
  "sinopse": "Um grupo de astronautas viaja por um buraco de minhoca em busca de um novo lar para a humanidade."
}

```


### 🧩 Tecnologias Utilizadas

```bash

🧠 OpenAI API

🐍 Python 3.11

⚡ FastAPI

🧰 Typer

🗃️ SQLite

🔍 Pydantic

🧪 Pytest

🧾 Logging estruturado

📦 Docker

📁 dotenv

```


### ⚠️ Aviso de Segurança

```bash
A IA pode retornar informações imprecisas, incompletas ou inconsistentes, especialmente se o título for ambíguo ou desconhecido.
Este projeto usa Chat Completions com Function Calling, mas pode ser adaptado para a Assistants API.
```


## 📚 Licença

Este projeto é open-source e está sob a licença [MIT](LICENSE).

---

## 👨‍💻 Desenvolvido por

**Tiago Oliveira**  
Analista desenvolvedor e Engenheiro de dados em formação

- 💼 [LinkedIn](https://www.linkedin.com/in/tiago-oliveira-49a2a6205/)
- 💻 [GitHub](https://github.com/TiagoOliverDev)