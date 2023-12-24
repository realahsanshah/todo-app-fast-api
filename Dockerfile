FROM python:3.11.0a1-alpine3.14

# Path: /app
WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn","main:app","--reload"]

