from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.tbb_usuarios, config.db, schemas.tbb_usuarios, models.tbb_usuarios
from typing import List

tbb_usuarios_router = APIRouter()

models.tbb_usuarios.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@tbb_usuarios_router.get("/tbb_usuarios/", response_model=List[schemas.tbb_usuarios.tbb_usuario], tags=["Tbb_Usuarios"])
def read_tbb_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_tbb_usuarios = crud.tbb_usuarios.get_all_tbb_usuarios(db=db, skip=skip, limit=limit)
    return db_tbb_usuarios

@tbb_usuarios_router.get("/tbb_usuarios/{id}", response_model=schemas.tbb_usuarios.tbb_usuario, tags=["Tbb_Usuarios"])
def read_tbb_usuario(id: int, db: Session = Depends(get_db)):
    db_tbb_usuario = crud.tbb_usuarios.get_tbb_usuario(db=db, id=id)
    if db_tbb_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_tbb_usuario

@tbb_usuarios_router.post("/tbb_usuarios/", response_model=schemas.tbb_usuarios.tbb_usuario, tags=["Tbb_Usuarios"])
def create_tbb_usuario(tbb_usuario: schemas.tbb_usuarios.tbb_usuarioCreate, db: Session = Depends(get_db)):
    db_tbb_usuario = crud.tbb_usuarios.get_tbb_usuario_by_name(db, nombre=tbb_usuario.Nombre_Usuario)
    if db_tbb_usuario:
        raise HTTPException(status_code=400, detail="Usuario existente, intenta nuevamente")
    return crud.tbb_usuarios.create_tbb_usuario(db=db, tbb_usuario=tbb_usuario)

@tbb_usuarios_router.put("/tbb_usuarios/{id}", response_model=schemas.tbb_usuarios.tbb_usuario, tags=["Tbb_Usuarios"])
def update_tbb_usuario(id: int, tbb_usuario: schemas.tbb_usuarios.tbb_usuarioUpdate, db: Session = Depends(get_db)):
    db_tbb_usuario = crud.tbb_usuarios.update_tbb_usuario(db=db, id=id, tbb_usuario=tbb_usuario)
    if db_tbb_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_tbb_usuario

@tbb_usuarios_router.delete("/tbb_usuarios/{id}", response_model=schemas.tbb_usuarios.tbb_usuario, tags=["Tbb_Usuarios"])
def delete_tbb_usuario(id: int, db: Session = Depends(get_db)):
    db_tbb_usuario = crud.tbb_usuarios.delete_tbb_usuario(db=db, id=id)
    if db_tbb_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_tbb_usuario
