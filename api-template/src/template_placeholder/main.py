from fastapi import FastAPI

app = FastAPI(title="template-placeholder API", version="0.1.0")

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "template-placeholder"}

@app.get("/health")
def health_check():
    return {"status": "UP"}
