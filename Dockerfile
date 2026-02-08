FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

EXPOSE 8000

ENTRYPOINT ["python", "-m", "adr_viewer"]
CMD ["--serve"]
