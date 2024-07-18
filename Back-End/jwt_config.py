
from jwt import encode , decode

def solicita_token (dato:dict)->str:
    token:str=encode(payload=dato, key='jack323256', algorithm='HS256')
    return token

def valida_token(token:str)->dict:
    dato:dict = decode(token, key = "jack323256", algorithms = ["HS256"])
    return dato

