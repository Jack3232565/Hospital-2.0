from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

# Crear un enrutador para las rutas de persona
usuario = APIRouter()

# Lista para almacenar las personas en memoria (solo para demostración)
usuarios = []

# Modelo de datos para una Persona
class ModelUsuarios(BaseModel):
    id: int
    usuario: str
    contrasena: str
    id_persona: Optional[int] = None
    estatus: bool = False
    created_at: datetime = Field(default_factory=datetime.now)


# Modelo de datos para actualizar parcialmente una Persona
class UpdateUsuario(BaseModel):
    usuario: Optional[str] = None
    contrasena: Optional[str] = None
    id_persona: Optional[int] = None
    estatus: Optional[bool] = None


@usuario.get('/')
def bienvenida():
    """
    Ruta de bienvenida.
    """
    return 'Bienvenido al Sistema'


# Ruta para obtener todas las personas
@usuario.get("/usuario", response_model=List[ModelUsuarios])
async def get_usuario(): 
    """
    Obtiene la lista de todas las personas.
    """
    return usuarios


# Ruta para guardar una nuevo usuario
@usuario.post("/usuario")
async def save_usuario(datos_usuario: ModelUsuarios):
    """
    Guarda una nuevo usuario en la lista.
    """
    usuarios.append(datos_usuario)
    return 'Datos Guardados'


# Ruta para actualizar una persona existente
@usuario.put("/usuario/{usuario_id}")
async def update_usuario(usuario_id: int, datos_actualizados: UpdateUsuario):
    """
    Actualiza los datos de una persona existente.
    """
    for idx, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            # Actualiza solo los campos proporcionados en la solicitud
            update_data = datos_actualizados.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(usuarios[idx], key, value)
            return 'Datos Actualizados'
    raise HTTPException(status_code=404, detail="Usuario no encontrado")



# Ruta para eliminar una persona existente
@usuario.delete("/usuario/{usuario_id}")
async def delete_usuario(usuario_id: int):
    """
    Elimina un usuario de la lista.
    """
    for idx, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            del usuarios[idx]
            return 'Datos Eliminados'
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@usuario.get("/usuario/{usuario_id}", response_model=ModelUsuarios)
async def get_persona(usuario_id: int):
    """
    Obtiene el usuario solicitado por su ID.
    """
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrada")


@usuario.post("/usuario/{usuario_id}", response_model=ModelUsuarios)
async def get_usuario(usuario_id: int):
    """
    Obtiene el usuario solicitado por su ID.
    """
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")



