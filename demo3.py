from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudiante(BaseModel):
    nombre: str
    edad: int

@app.get("/")
def inicio():
    return {"mensaje": "La API está funcionando"}

@app.post("/saludar")
def saludar(estudiante: Estudiante):
    return {"mensaje": f"Hola {estudiante.nombre}, tienes {estudiante.edad} años"}