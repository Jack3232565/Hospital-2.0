from fastapi import FastAPI
from routes.persona import persona
from routes.usuarios import usuario
from routes.users import user
from routes.persons import person
import logging

# Importa database.py para que se ejecuten las funciones de creación de tablas
from models.database import create_tables  # Importa create_tables aquí
create_tables()  # Asegúrate de que las tablas se crean al iniciar la aplicación

app = FastAPI()

# Registrar los routers
app.include_router(persona, tags=["Personas"])
app.include_router(usuario, tags=["Usuarios"])
app.include_router(user)
app.include_router(person)

# Mensaje de bienvenida usando logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Bienvenido a mi aplicación")
