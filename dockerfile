
FROM python:3.8.10-slim

WORKDIR /app

COPY . /app

RUN pip install uvicorn
RUN pip install -r requirements.txt

