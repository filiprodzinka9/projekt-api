import os
import socket
from fastapi import FastAPI
import redis

app = FastAPI(title="ATinS Microservice Demo")

# Bezpieczne połączenie z Redisem (nie wywali aplikacji, jeśli Redisa nie ma)
try:
    r = redis.Redis(host='cache', port=6379, decode_responses=True, socket_timeout=1)
except Exception:
    r = None

@app.get("/")
def get_info():
    return {
        "komunikat": "Wersja bazowa",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "production"),
        "version": "1.1.0"
    }

@app.get("/hits")
def read_hits():
    if r:
        try:
            count = r.incr('hits')
            return {"hits": count, "hostname": socket.gethostname()}
        except Exception:
            pass
    return {"hits": "Redis niedostępny", "hostname": socket.gethostname()}

@app.get("/healthz")
def healthcheck():
    return {"status": "healthy"}