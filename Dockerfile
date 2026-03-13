FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN apt-get update \
    && apt-get install -y awscli \
    && pip install -r requirements.txt \
    && apt-get clean

CMD ["python", "app.py"]