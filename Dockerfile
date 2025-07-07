# Imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Expõe a porta padrão do Streamlit (caso esteja usando Streamlit como front)
EXPOSE 8501

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
