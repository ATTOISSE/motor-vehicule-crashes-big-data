FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt


RUN pip install --no-cache-dir -r requirements.txt

COPY utils/insert_data.py /app/

COPY data /app/data

CMD ["python", "/app/insert_data.py"]