# DevOps Lab 1: Arithmetic API with Docker & CI/CD Pipeline

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![Docker](https://img.shields.io/badge/docker-20.10+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)

A complete DevOps implementation featuring a Python Flask API for arithmetic operations with Docker containerization, automated monitoring, and CI/CD pipeline.
**Author**: LAMGHARI Noureddine  
**Course**: DevSecOps  
**Date**: 07 October 2025

## 🚀 Features

### Arithmetic API Operations
- **Addition** (`POST /add`)
- **Subtraction** (`POST /subtract`)
- **Multiplication** (`POST /multiply`)
- **Division** (`POST /divide`)
- **Health Check** (`GET /health`)

### DevOps Pipeline
- 🐳 **Docker containerization** with multi-stage builds
- 📊 **Automated monitoring** for local file changes
- 🔄 **Git repository monitoring** for new commits
- 🚀 **Automatic rebuild and deployment**
- 🐙 **Docker Hub integration** (manual push)
- 📝 **Comprehensive logging**

## 📁 Project Structure

```
├── app.py              # Flask API with arithmetic operations
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── deploy.sh          # Monitoring and deployment script
├── .dockerignore      # Docker ignore file
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 🛠️ Prerequisites

- Python 3.9+
- Docker 20.10+
- Git
- curl (for testing)

## 🏃‍♂️ Quick Start

### 1. Clone the repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Build and run with Docker
```bash
# Build the image
docker build -t arithmetic-api .

# Run the container
docker run -d --name arithmetic-api-container -p 5000:5000 arithmetic-api
```

### 3. Test the API
```bash
# Test addition
curl -X POST http://localhost:5000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'

# Test health endpoint
curl http://localhost:5000/health
```

## 🤖 Automated Deployment

The `deploy.sh` script provides automated monitoring and deployment:

```bash
# Make script executable
chmod +x deploy.sh

# Start monitoring (automatically rebuilds on changes)
./deploy.sh monitor

# Manual operations
./deploy.sh build      # Build Docker image
./deploy.sh deploy     # Deploy container
./deploy.sh git-test   # Test git monitoring functionality
./deploy.sh stop       # Stop container
```

## 📋 API Documentation

### Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| POST | `/add` | Add two numbers | `{"a": number, "b": number}` |
| POST | `/subtract` | Subtract two numbers | `{"a": number, "b": number}` |
| POST | `/multiply` | Multiply two numbers | `{"a": number, "b": number}` |
| POST | `/divide` | Divide two numbers | `{"a": number, "b": number}` |
| GET | `/health` | Health check | - |

### Example Requests

```bash
# Addition
curl -X POST http://localhost:5000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 15, "b": 25}'

# Response: {"operation": "add", "result": 40, "inputs": {"a": 15, "b": 25}}

# Division
curl -X POST http://localhost:5000/divide \
  -H "Content-Type: application/json" \
  -d '{"a": 20, "b": 4}'

# Response: {"operation": "divide", "result": 5.0, "inputs": {"a": 20, "b": 4}}
```

## 🐳 Docker Hub Integration

### Manual Push to Docker Hub:
```bash
# Login to Docker Hub
docker login

# Tag your image
docker tag arithmetic-api YOUR_DOCKERHUB_USERNAME/arithmetic-api:latest

# Push to Docker Hub
docker push YOUR_DOCKERHUB_USERNAME/arithmetic-api:latest
```

### Example with username 'dr1li':
```bash
docker login
docker tag arithmetic-api dr1li/arithmetic-api:latest
docker push dr1li/arithmetic-api:latest
```

## 🔧 Development

### Running locally without Docker:
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 📊 Monitoring Features

The deployment script monitors:
- ✅ Local file changes (`.py`, `.txt`, `Dockerfile`)
- ✅ Git repository changes (new commits)
- ✅ Automatic rebuild triggers
- ✅ Container lifecycle management
- ✅ Timestamped logging

## 🧪 Testing

### Manual Testing:
```bash
# Test all operations
curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"a": 5, "b": 3}'
curl -X POST http://localhost:5000/subtract -H "Content-Type: application/json" -d '{"a": 5, "b": 3}'
curl -X POST http://localhost:5000/multiply -H "Content-Type: application/json" -d '{"a": 5, "b": 3}'
curl -X POST http://localhost:5000/divide -H "Content-Type: application/json" -d '{"a": 6, "b": 2}'
```

### Error Handling:
```bash
# Division by zero
curl -X POST http://localhost:5000/divide -H "Content-Type: application/json" -d '{"a": 5, "b": 0}'
# Response: {"error": "Division by zero not allowed"}

# Missing parameters
curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"a": 5}'
# Response: {"error": "Missing parameters a and b"}
```

## 📝 Lab Requirements Fulfilled

- ✅ **Python API** with arithmetic operations (add, subtract, multiply, divide)
- ✅ **Shell script** for monitoring and automated deployment
- ✅ **Docker containerization** with automatic rebuilds
- ✅ **Git repository** with version control
- ✅ **Git monitoring** for new commits and auto-deployment
- ✅ **Docker Hub integration** with image pushing

## 🚀 Deployment Instructions for Teachers

1. **Clone the repository**
2. **Ensure Docker is installed**
3. **Run the monitoring script**: `./deploy.sh monitor`
4. **Test the API** using the provided curl commands
5. **Verify auto-rebuild** by modifying any file and watching the logs

## 📞 Support

If you encounter any issues:
1. Check Docker is running: `docker --version`
2. Verify port 5000 is available: `lsof -i :5000`
3. Check container logs: `docker logs arithmetic-api-container`
4. Review deployment logs from `./deploy.sh monitor`

---
