from fastapi import FastAPI
from routes.persona import persona

app = FastAPI()

# Incluyendo el router de persona
app.include_router(persona)

# Mensaje de bienvenida usando logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Bienvenido a mi aplicación")