from fastapi import FastAPI
from routes.persona import persona
from routes.usuarios import usuario


app = FastAPI()

# Incluyendo el router de persona dentro del ruta http://127.0.0.1:8000/docs
# Registrar los routers
app.include_router(persona, tags=["Personas"])
app.include_router(usuario, tags=["Usuarios"])

# Mensaje de bienvenida usando logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Bienvenido a mi aplicación")

