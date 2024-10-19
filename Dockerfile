# Usar a imagem oficial do Python
FROM python:3.9

# Definir o diretório de trabalho no container
WORKDIR /code

# Instalar as dependências
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copiar o código do projeto para o container
COPY . /code/

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
