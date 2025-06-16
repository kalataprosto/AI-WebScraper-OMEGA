FROM mcr.microsoft.com/playwright/python:v1.40.0 AS base


FROM python:3.10-slim AS builder
RUN apt update && \
    apt install -y --no-install-recommends\
    build-essential \
    libssl-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir pqcrypto==0.3.1


FROM base
WORKDIR /app


COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    playwright install chromium && \
    playwright install-deps

COPY . .

CMD ["python", "-u", "src/main.py"]