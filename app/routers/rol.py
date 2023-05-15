
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends
from fastapi import HTTPException
from app.schemas import Rol
from app.models.db import get_db
from sqlalchemy.orm import Session
from app.models import models


gestionarRoles = APIRouter(
    prefix= "/roles", tags=["Roles"]
    
)

#*Listar Roles
@gestionarRoles.get("/listar", response_model=list[Rol])
def listar_roles(db: Session = Depends(get_db)) -> list:
    roles = db.query(models.Roles).all()
    return [rol.__dict__ for rol in roles]

#*Obtener Rol por id
@gestionarRoles.get("/{id}", response_model=Rol)
def obtener_rol(id: int, db: Session = Depends(get_db)):
    rol = db.query(models.Roles).filter(models.Roles.id == id).first()
    if rol is None:
        raise HTTPException(status_code=404, detail = "Rol no encontrado")
    return rol.__dict__

@gestionarRoles.post("/crear", response_model=Rol)
def crear_rol(rol: Rol, db: Session = Depends(get_db)):
    rol_db = db.query( models.Roles).filter( models.Roles.id == rol.id).first()
    if rol_db is not None:
        raise HTTPException(status_code=500 , detail={"message": "Rol Existente"})
    rol_db =  models.Roles(id =rol.id, nombre = rol.nombre)
    db.add(rol_db)
    db.commit()
    db.refresh(rol_db)
    return rol_db.__dict__

@gestionarRoles.put("/actualizar/{id}", response_model=Rol)
def actualizar_rol(id: int, rol: Rol, db: Session = Depends(get_db)):
    rol_db = db.query( models.Roles).filter( models.Roles.id == id).first()
    if rol_db is None:
        raise HTTPException(status_code=404, detail={"message": "Rol no encontrado"})
    rol_db.nombre = rol.nombre
    db.commit()
    db.refresh(rol_db)
    return rol_db.__dict__

            
 