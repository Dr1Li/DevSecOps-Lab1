#!/bin/bash

echo "🚀 Setting up DevOps Lab 1 Environment"
echo "======================================"

# Check prerequisites
command -v docker >/dev/null 2>&1 || { echo "❌ Docker not found. Please install Docker first."; exit 1; }
command -v git >/dev/null 2>&1 || { echo "❌ Git not found. Please install Git first."; exit 1; }
command -v curl >/dev/null 2>&1 || { echo "❌ curl not found. Please install curl first."; exit 1; }

echo "✅ Prerequisites check passed"

# Make deploy script executable
chmod +x deploy.sh
echo "✅ Made deploy.sh executable"

# Build and test
echo "🔨 Building Docker image..."
docker build -t arithmetic-api .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully"
else
    echo "❌ Failed to build Docker image"
    exit 1
fi

# Quick test
echo "🧪 Running quick test..."
docker run -d --name temp-test-container -p 5001:5000 arithmetic-api
sleep 5

if curl -s http://localhost:5001/health > /dev/null; then
    echo "✅ API is responding correctly"
else
    echo "❌ API test failed"
fi

docker stop temp-test-container >/dev/null 2>&1
docker rm temp-test-container >/dev/null 2>&1

echo ""
echo "🎉 Setup complete! You can now:"
echo "  • Run './deploy.sh monitor' to start monitoring"
echo "  • Test API at http://localhost:5000 after deployment"
echo "  • Push to GitHub for teacher evaluation"
echo ""
