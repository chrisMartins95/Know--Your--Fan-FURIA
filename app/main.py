from fastapi import FastAPI

app = FastAPI(title="FURIA Tech Challenge – Know Your Fan")

@app.get("/health")
def health():
    return {"status": "ok"}
