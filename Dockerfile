FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    potrace \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000

CMD ["python", "app.py"]
