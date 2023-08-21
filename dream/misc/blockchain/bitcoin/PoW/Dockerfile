# Dockerfile

FROM python:3.9

WORKDIR /app

COPY challenge.py .
COPY flag.txt .

RUN pip install Flask

CMD ["python", "challenge.py"]
