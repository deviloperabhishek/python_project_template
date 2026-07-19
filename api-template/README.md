# API Service: template-placeholder

A production-ready FastAPI application boilerplate.

## 🚀 Getting Started

### 1. Local Development (Standard Python)
First, make sure you have initialized a virtual environment and installed the dependencies:
```bash
# Create and activate environment
python3 -m venv .venv
source .venv/bin/activate

# Install development & production dependencies
pip install -e ".[dev]"
```

To run the live reload server locally, execute the following command:
```bash
uvicorn template_placeholder.main:app --reload --port 8000
```
* Once started, open your browser and navigate to the interactive docs at: http://127.0.0

### 2. Running inside Container (Docker Production Setup)
To build and run your workspace code inside an isolated container layout:
```bash
# Build the container image
docker build -t template-placeholder .

# Spin up the application container
docker run -p 8000:8000 template-placeholder
```

