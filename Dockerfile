FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt


RUN pip install --no-cache-dir -r requirements.txt




CMD ["python", "utils/insert_data.py"]
