FROM python:3.11-slim

EXPOSE 8085

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT python server.py
