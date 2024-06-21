from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional 

persona = APIRouter()
personas = []

class ModelPersona(BaseModel):
    id: int
    nombre: str
    primer_apellido: str
    segundo_apellido: Optional[str] = None
    edad: int
    fecha_nacimiento: datetime
    curp: str
    sangre: str
    created_at: datetime = Field(default_factory=datetime.now)
    estatus: bool = False

@persona.get('/')
def bienvenida():
    return 'Bienvenido al Sistema'

@persona.get("/persona")
async def get_personas():
    return personas

@persona.post("/persona")
async def save_personas(datos_persona: ModelPersona):
    personas.append(datos_persona)
    return 'Datos Guardados'

@persona.put("/persona/{persona_id}")
async def update_persona(persona_id: int, datos_actualizados: ModelPersona):
    for idx, persona in enumerate(personas):
        if persona.id == persona_id:
            personas[idx] = datos_actualizados
            return 'Datos Actualizados'
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@persona.delete("/persona/{persona_id}")
async def delete_persona(persona_id: int):
    for idx, persona in enumerate(personas):
        if persona.id == persona_id:
            del personas[idx]
            return 'Datos Eliminados'
    raise HTTPException(status_code=404, detail="Persona no encontrada")