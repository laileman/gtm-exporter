from python:3.13-alpine

workdir /app
copy requirements.txt .
run pip install -r requirements.txt

copy . .

entrypoint ["python", "main.py"]