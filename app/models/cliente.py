# app/routers/clientes.py

from fastapi import APIRouter
from app.models.cliente import Cliente

router = APIRouter(prefix="/clientes", tags=["Clientes"])

# Datos simulados (puedes conectar a base de datos después)
clientes_db = []

@router.get("/")
def listar_clientes():
    return clientes_db

@router.post("/")
def crear_cliente(cliente: Cliente):
    clientes_db.append(cliente)
    return {"mensaje": "Cliente creado", "cliente": cliente}
