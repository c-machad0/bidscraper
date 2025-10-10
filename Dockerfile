FROM selenium/standalone-chrome:latest

WORKDIR /app

COPY . .

USER root
RUN pip install --no-cache-dir -r requirements.txt

USER seluser

CMD ["python", "main.py"]
