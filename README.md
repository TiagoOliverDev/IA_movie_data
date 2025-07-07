# 🎬 IA Movie Insights - OpenAI + Python

Projeto simples e objetivo que utiliza **OpenAI API** para buscar informações sobre um filme com base apenas no seu **título**. Ele retorna uma resposta estruturada contendo:

- 📅 Data de lançamento  
- 💵 Bilheteria estimada  
- 📝 Sinopse curta  


---

## 🚀 Funcionalidades

✅ Recebe o nome de um filme  
✅ Consulta a OpenAI (Chat Completions)  
✅ Retorna os dados formatados em JSON  
✅ Possui tratamento de erros e logs  
✅ Estrutura de projeto modular e escalável

---

## 🗂️ Estrutura do Projeto

```bash
IA_movie_data/
├── app/
│ └── main.py                   # Ponto de entrada do projeto
├── core/
│ └── openai_handler.py         # Função que consulta a OpenAI
├── config/
│ └── config.py                 # Configurações e API Key
├── tests/
│ └── test_openai_handler.py    # Testes unitários básicos
├── utils/
│ └── logger.py                 # Logger personalizado
├── .env                        # Armazena OPENAI_API_KEY e OPENAI_MODEL
├── requirements.txt            # Dependências
└── README.md                  
```


## ⚙️ Como Executar o Projeto

### 🔧 Pré-requisitos
- Python 3.11+   
- Conta OpenAI com uma chave de API ativa

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

### 4. Execute o projeto
```bash
python app/main.py
```

### 💡 Exemplo de Uso

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

### 🧪 Testes

```bash

Execute com: pytest

```

### 🧩 Tecnologias Utilizadas

```bash
OpenAI API

Python 3.11

Dotenv

Pytest

Logging
```


### ⚠️ Aviso de Segurança

```bash
A IA pode retornar respostas inconsistentes se o título do filme for ambíguo ou desconhecido.

Este projeto utiliza Chat Completions, mas pode ser adaptado para Assistants API se necessário.
```


## 📚 Licença

Este projeto é open-source e está sob a licença [MIT](LICENSE).

---

## 👨‍💻 Desenvolvido por

**Tiago Oliveira**  
Analista desenvolvedor e Engenheiro de dados em formação

- 💼 [LinkedIn](https://www.linkedin.com/in/tiago-oliveira-49a2a6205/)
- 💻 [GitHub](https://github.com/TiagoOliverDev)