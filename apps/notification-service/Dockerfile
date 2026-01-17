# -----------------------------
# Stage 1: Builder
# -----------------------------
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies (optional but recommended)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (layer caching)
COPY requirements.txt .

# Install dependencies to user site-packages
RUN pip install --upgrade pip \
    && pip install --user --no-cache-dir -r requirements.txt


# -----------------------------
# Stage 2: Runtime
# -----------------------------
FROM python:3.12-slim

WORKDIR /code

# Install curl ONLY in runtime (for healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*
    
# Copy only installed dependencies from builder
COPY --from=builder /root/.local /root/.local

# Make sure installed binaries are on PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy application source code
COPY ./app /code/app

# Expose application port
EXPOSE 8003

# Run FastAPI using CLI (same behavior as original)
CMD ["fastapi", "run", "app/main.py", "--port", "8003"]
