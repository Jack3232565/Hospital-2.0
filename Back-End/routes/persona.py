from fastapi import APIRouter

persona = APIRouter()
@persona.get("/persona")

def helloworld():
    return