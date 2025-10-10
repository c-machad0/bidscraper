# Use imagem oficial do Selenium com Chrome e ChromeDriver já instalados e configurados
FROM selenium/standalone-chrome:latest

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia todo o código do seu projeto para o container
COPY . .

# Instala dependências Python necessárias do seu projeto
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o seu scraper
CMD ["python", "main.py"]