FROM python:3.13-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV GTM_URL=192.168.97.103:8080

ENTRYPOINT ["python", "main.py"]
