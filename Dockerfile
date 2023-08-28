FROM python:3.11

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y tesseract-ocr wget

ENV PATH="/usr/bin/tesseract:${PATH}"

WORKDIR /app

COPY . .

RUN python3 -m pip install poetry

RUN python3 -m poetry config virtualenvs.create false

RUN python3 -m poetry install --no-root

CMD ["python", "main.py"]

