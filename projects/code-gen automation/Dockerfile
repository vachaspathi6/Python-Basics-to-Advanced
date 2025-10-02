FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Ensure certs for TLS
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY code_generator.py ./
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Create output directory (secret.txt is mounted at runtime)
RUN mkdir -p /app/output

# Optionally allow passing token at runtime: -e GITHUB_TOKEN=...
ENV GITHUB_TOKEN=""

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

