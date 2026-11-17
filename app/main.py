from fastapi import FastAPI

app = FastAPI(title="Laboratorium 3 - Hot Reload")

@app.get("/")
def home():
    return {"komunikat": "Wersja bazowa"}

@app.get("/healthz")
def healthcheck():
    return {"status": "healthy"}