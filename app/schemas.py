from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Usuario(BaseModel):
    id:int
    nombre = str
    apellidoPaterno = str
    apellidoMaterno = str
    direccion = str
    tipoDocumento = str
    foto = str
    rol_id = int
    contraseña = str
    email = str
    celular = int
    direccion: Optional[str]
    fechaCreacion: datetime = datetime.now().strftime("%d/%m/%Y")
    

class Rol(BaseModel):
    id:int
    nombre:str
