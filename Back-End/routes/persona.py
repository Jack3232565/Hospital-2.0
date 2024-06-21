from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

# Crear un enrutador para las rutas de persona
persona = APIRouter()

# Lista para almacenar las personas en memoria (solo para demostración)
personas = []

# Modelo de datos para una Persona
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

# Modelo de datos para actualizar parcialmente una Persona
class UpdatePersona(BaseModel):
    nombre: Optional[str] = None
    primer_apellido: Optional[str] = None
    segundo_apellido: Optional[str] = None
    edad: Optional[int] = None
    fecha_nacimiento: Optional[datetime] = None
    curp: Optional[str] = None
    sangre: Optional[str] = None
    estatus: Optional[bool] = None

# Ruta de bienvenida
@persona.get('/')
def bienvenida():
    """
    Ruta de bienvenida.
    """
    return 'Bienvenido al Sistema'

# Ruta para obtener todas las personas
@persona.get("/persona", response_model=List[ModelPersona])
async def get_personas():
    """
    Obtiene la lista de todas las personas.
    """
    return personas


# Ruta para guardar una nueva persona
@persona.post("/persona")
async def save_personas(datos_persona: ModelPersona):
    """
    Guarda una nueva persona en la lista.
    """
    personas.append(datos_persona)
    return 'Datos Guardados'


# Ruta para actualizar una persona existente
@persona.put("/persona/{persona_id}")
async def update_persona(persona_id: int, datos_actualizados: UpdatePersona):
    """
    Actualiza los datos de una persona existente.
    """
    for idx, persona in enumerate(personas):
        if persona.id == persona_id:
            # Actualiza solo los campos proporcionados en la solicitud
            update_data = datos_actualizados.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(personas[idx], key, value)
            return 'Datos Actualizados'
    raise HTTPException(status_code=404, detail="Persona no encontrada")


# Ruta para eliminar una persona existente
@persona.delete("/persona/{persona_id}")
async def delete_persona(persona_id: int):
    """
    Elimina una persona de la lista.
    """
    for idx, persona in enumerate(personas):
        if persona.id == persona_id:
            del personas[idx]
            return 'Datos Eliminados'
    raise HTTPException(status_code=404, detail="Persona no encontrada")




@persona.get("/persona/{persona_id}", response_model=ModelPersona)
async def get_persona(persona_id: int):
    """
    Obtiene la persona solicitada por su ID.
    """
    for persona in personas:
        if persona.id == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")


@persona.post("/persona/{persona_id}", response_model=ModelPersona)
async def get_persona(persona_id: int):
    """
    Obtiene la persona solicitada por su ID.
    """
    for persona in personas:
        if persona.id == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")



