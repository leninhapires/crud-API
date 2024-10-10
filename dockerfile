
FROM python:3.12-alpine


RUN adduser -D fastapi

WORKDIR /api

COPY requirements.txt requirements.txt

RUN apk add --no-cache gcc musl-dev postgresql-dev netcat-openbsd bash

RUN pip install --no-cache-dir -r requirements.txt


COPY . .


USER fastapi

HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1


CMD ["./wait-for-it.sh", "db", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
