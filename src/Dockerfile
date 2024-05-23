FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y libfbclient2

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "./main.py"]