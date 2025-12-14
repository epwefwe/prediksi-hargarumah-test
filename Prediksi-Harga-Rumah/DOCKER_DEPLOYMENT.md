# 🐳 Docker & Container Deployment Guide

## Prerequisites
- Docker installed (https://docs.docker.com/get-docker/)
- Docker Compose installed (comes with Docker Desktop)

## Quick Start with Docker

### 1. Build Docker Image

```bash
docker build -t prediksi-harga-rumah .
```

### 2. Run Container

```bash
docker run -p 8501:8501 prediksi-harga-rumah
```

Access at: `http://localhost:8501`

### Stop Container

```bash
# Get container ID
docker ps

# Stop container
docker stop <container_id>
```

---

## Using Docker Compose (Recommended)

### 1. Start Application

```bash
docker-compose up
```

Or in background:
```bash
docker-compose up -d
```

### 2. View Logs

```bash
docker-compose logs -f
```

### 3. Stop Application

```bash
docker-compose down
```

### 4. Rebuild Image

```bash
docker-compose up --build
```

---

## Docker Commands Reference

### Image Management

```bash
# List images
docker images

# Remove image
docker rmi prediksi-harga-rumah

# Tag image
docker tag prediksi-harga-rumah myrepo/prediksi:v1.0
```

### Container Management

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# View container logs
docker logs <container_id>

# Execute command in container
docker exec <container_id> ls -la

# Remove container
docker rm <container_id>
```

### Network Management

```bash
# List networks
docker network ls

# Inspect network
docker network inspect prediksi-network
```

---

## Docker Hub Deployment

### 1. Create Docker Hub Account
Visit https://hub.docker.com

### 2. Login to Docker Hub

```bash
docker login
```

### 3. Tag Image

```bash
docker tag prediksi-harga-rumah <username>/prediksi-harga-rumah:latest
```

### 4. Push Image

```bash
docker push <username>/prediksi-harga-rumah:latest
```

### 5. Pull and Run from Docker Hub

```bash
docker run -p 8501:8501 <username>/prediksi-harga-rumah:latest
```

---

## Deploy to Cloud Platforms

### Google Cloud Run

```bash
# Build image
docker build -t gcr.io/<project-id>/prediksi-harga-rumah .

# Push to Google Container Registry
docker push gcr.io/<project-id>/prediksi-harga-rumah

# Deploy to Cloud Run
gcloud run deploy prediksi-harga-rumah \
  --image gcr.io/<project-id>/prediksi-harga-rumah \
  --port 8501 \
  --memory 1Gi \
  --region us-central1 \
  --allow-unauthenticated
```

### AWS ECR

```bash
# Create ECR repository
aws ecr create-repository --repository-name prediksi-harga-rumah

# Login to ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag prediksi-harga-rumah:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/prediksi-harga-rumah:latest

# Push image
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/prediksi-harga-rumah:latest
```

### Azure Container Registry

```bash
# Create ACR
az acr create --resource-group myResourceGroup \
  --name myreg --sku Basic

# Login to ACR
az acr login --name myreg

# Tag image
docker tag prediksi-harga-rumah myreg.azurecr.io/prediksi-harga-rumah:latest

# Push image
docker push myreg.azurecr.io/prediksi-harga-rumah:latest
```

---

## Environment Variables in Docker

### Using .env file

Create `.env` file:
```
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
LOG_LEVEL=error
```

In docker-compose.yml:
```yaml
services:
  streamlit:
    env_file: .env
```

### In docker-compose.yml

```yaml
services:
  streamlit:
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### Via command line

```bash
docker run -e STREAMLIT_SERVER_PORT=8501 \
  -p 8501:8501 prediksi-harga-rumah
```

---

## Volume Mounting

### Using Docker

```bash
# Mount local directory
docker run -v /path/to/data:/app/data \
  -p 8501:8501 prediksi-harga-rumah

# Read-only mount
docker run -v /path/to/models:/app/models:ro \
  -p 8501:8501 prediksi-harga-rumah
```

### Using Docker Compose

```yaml
volumes:
  - ./src:/app/src        # Read-write
  - ./models:/app/models:ro  # Read-only
  - data_volume:/app/data    # Named volume
```

---

## Troubleshooting

### Container exits immediately

```bash
# Check logs
docker logs <container_id>

# Run in interactive mode
docker run -it prediksi-harga-rumah /bin/bash
```

### Port already in use

```bash
# Use different port
docker run -p 8080:8501 prediksi-harga-rumah
```

### Out of memory

Increase memory in docker-compose.yml:
```yaml
services:
  streamlit:
    deploy:
      resources:
        limits:
          memory: 2G
```

### Module not found

Verify requirements.txt is in root and Dockerfile copies it correctly:
```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
```

---

## Best Practices

✅ **DO:**
- Use multi-stage builds for smaller images
- Cache dependencies separately from app code
- Use .dockerignore to exclude unnecessary files
- Use health checks
- Run as non-root user
- Use environment variables for configuration

❌ **DON'T:**
- Use `latest` tag in production
- Run as root user
- Mount entire filesystem
- Ignore security vulnerabilities
- Use hardcoded credentials

---

## Performance Optimization

### Multi-stage Build

```dockerfile
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["streamlit", "run", "src/streamlit.py"]
```

### Resource Limits

```bash
docker run --memory=512m --cpus=1 prediksi-harga-rumah
```

---

## Monitoring & Logging

### View Real-time Logs

```bash
docker-compose logs -f streamlit
```

### Save Logs to File

```bash
docker-compose logs > app.log
```

### Container Stats

```bash
docker stats <container_id>
```

---

## Security

### Build with Security Scan

```bash
docker build --label security=scan .
```

### Run in Read-only Mode

```bash
docker run --read-only \
  --tmpfs /tmp \
  --tmpfs /var/tmp \
  prediksi-harga-rumah
```

### Run as Non-root

```dockerfile
RUN useradd -m appuser
USER appuser
```

---

For more information:
- [Docker Documentation](https://docs.docker.com)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Best Practices](https://docs.docker.com/develop/dev-best-practices/)
