from sqlalchemy import Column, Integer, String, Boolean, DateTime
from config.db import Base
from sqlalchemy.orm import relationship

class tbb_usuarios(Base):
    __tablename__ = 'tbb_usuarios'
    
    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer)
    Nombre_Usuario = Column(String(255))
    Correo_Electronico = Column(String(255))
    Contrasena = Column(String(255))
    Numero_Telefonico_Movil = Column(String(255))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    roles = relationship("UsuarioRoles", back_populates="usuario")