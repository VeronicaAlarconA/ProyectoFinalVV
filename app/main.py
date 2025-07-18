# app/main.py

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.routers import clientes

app = FastAPI(title="Sistema de Gestión - Taller DevOps")

# Middleware Prometheus
Instrumentator().instrument(app).expose(app)

# Incluir rutas
app.include_router(clientes.router)
