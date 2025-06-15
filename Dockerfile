FROM mcr.microsoft.com/playwright/python:v1.40.0 as base

# Quantum crypto layer
FROM python:3.10 as builder
RUN apt-get update && apt-get install -y build-essential libssl-dev && \
    pip install pqcrypto==0.3.1

FROM base
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY . .
RUN pip install -r requirements.txt && \
    playwright install chromium && \
    playwright install-deps && \
    apt-get update 
CMD ["python", "-u", "src/main.py"]
