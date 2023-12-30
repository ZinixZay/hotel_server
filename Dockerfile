FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT gunicorn --bind 0.0.0.0:8000 hotel_server.wsgi