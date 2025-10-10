FROM python:3.12

# Instale dependências do sistema para o Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-11 \
    libayatana-appindicator3-1 \
    libnss3 \
    libxss1 \
    libasound2 \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    xdg-utils

# Baixe o Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome*.deb; apt-get -fy install

# Copie seu projeto
WORKDIR /app
COPY . .

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando de inicialização (altere conforme sua aplicação)
CMD ["python", "main.py"]
