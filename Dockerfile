# Usando Python 3.10 como base
FROM python:3.10-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar o conteúdo do projeto para o contêiner
COPY . /app/

# Instalar as dependências do projeto
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install psycopg2-binary

# Expor a porta que o Django usará
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
