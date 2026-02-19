FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    potrace \
    imagemagick \
    ghostscript \
    && rm -rf /var/lib/apt/lists/*

# Fix ImageMagick PDF / policy issues (important)
RUN sed -i 's/rights="none" pattern="PDF"/rights="read|write" pattern="PDF"/' /etc/ImageMagick-6/policy.xml || true

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["python", "app.py"]
