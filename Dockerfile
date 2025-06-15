# Stage 1: Base with Playwright
FROM mcr.microsoft.com/playwright/python:v1.40.0 AS base

# Stage 2: Quantum crypto builder
FROM python:3.10-slim AS builder
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir pqcrypto==0.3.1

# Final stage
FROM base
WORKDIR /app

# Copy quantum crypto libraries
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    playwright install chromium && \
    playwright install-deps && \
    rm -rf /var/lib/apt/lists/*

CMD ["python", "-u", "src/main.py"]
