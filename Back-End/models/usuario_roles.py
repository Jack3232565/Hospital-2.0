# from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime, PrimaryKeyConstraint
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from config.db import Base

# from models.tbb_usuarios import tbb_usuarios  # Importa el modelo Usuario
# from models.roles import Roles  # Importa el modelo Rol

# class UsuarioRoles(Base):
#     __tablename__ = 'tbd_usuarios_roles'

#     Usuario_ID = Column(Integer, ForeignKey('tbb_usuarios.ID'), primary_key=True)
#     Rol_ID = Column(Integer, ForeignKey('tbc_roles.id'), primary_key=True)
#     Estatus = Column(Boolean, nullable=False, default=True)
#     Fecha_Registro = Column(DateTime, nullable=False, default=datetime.utcnow)
#     Fecha_Actualizacion = Column(DateTime, default=None, onupdate=datetime.utcnow)

#     usuario = relationship("Usuario", back_populates="roles")
#     rol = relationship("Rol", back_populates="usuarios")

#     __table_args__ = (
#         PrimaryKeyConstraint('Usuario_ID', 'Rol_ID', name='usuario_roles_pk'),
#     )