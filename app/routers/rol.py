
from fastapi import APIRouter
from fastapi import FastAPI, Depends
from app.schemas import Rol
from app.models.db import get_db
from sqlalchemy.orm import Session
from app.models import models


router = APIRouter(
    prefix= "/roles", tags=["Roles"]
    
)

roles = []

#GetRoles
@router.get("/")
def getRoles(db:Session = Depends(get_db)):
    data = db.query(models.Roles).all()
    return data

#RegistrarRoles
@router.post("/")
def crearRol(Rol:Rol, db:Session = Depends(get_db)):
    rol = Rol.dict()
    
    nuevoRol = models.Roles(
        id = rol["id"],
        nombre = rol["nombre"],
        
    )
    db.add(nuevoRol)
    db.commit()
    db.refresh()
    return True

#Get Rol  por ID
@router.get("/{id}")
def recibirRolById(id:int):
    for rol in roles:
        if rol["id"] == id:
            return rol 

#Borrar Rol por ID
@router.delete("/{id}")
def eliminarRol(id:int):
    for rol in roles:
        if rol["id"] == id:
            roles.remove(rol)
            return rol
        
#Actualizar Rol por ID
@router.put("/{id}")
def actualizarRol(id:int, rolAEditar:Rol):
    for index, rol in enumerate(roles):
        if rol["id"] == id:
            rol[index]["nombre"] = rolAEditar.dict()["nombre"]
            
            
 