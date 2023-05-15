
from fastapi import APIRouter, HTTPException
from fastapi import FastAPI, Depends
from app.schemas import Usuario
from app.models.db import get_db
from sqlalchemy.orm import Session
from app.models import models
from datetime import datetime


gestionarUsuarios = APIRouter(
    prefix= "/usuarios", tags=["Usuarios"]
    
)


#GetUsuarios
@gestionarUsuarios.get("/listar", response_model=list[Usuario])
def listar_usuarios(db:Session = Depends(get_db)) -> list:
    usuarios = db.query(models.Usuario).all()
    return [usuario.__dict__ for usuario in usuarios]

#RegistrarUsuarios
@gestionarUsuarios.post("/crear")
def crear_usuario(user:Usuario, db:Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == user.id).first()
    if usuario is not None:
        raise HTTPException(status_code = 500, detail = {"message": "Usuario Existente"})
    usuario = user.dict()
    nuevoUsuario = models.Usuario(
        id = usuario["id"],
        nombre = usuario["nombre"],
        apellidoPaterno = usuario["apellidoPaterno"],
        apellidoMaterno = usuario["apellidoMaterno"],
        direccion = usuario["direccion"],
        tipoDocumento = usuario["tipoDocumento"],
        foto = usuario["foto"],
        rol_id = usuario["rol_id"],
        contraseña = usuario["contraseña"],
        email = usuario["email"],
        celular = usuario["celular"],
        fechaCreacion = usuario["fechaCreacion"],
    )
    db.add(nuevoUsuario)
    db.commit()
    db.refresh(nuevoUsuario)
    return nuevoUsuario.__dict__

#Get Usuario por ID
@gestionarUsuarios.get("/{id}")
def recibir_usuario(id:int, db:Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if usuario is None:
        raise HTTPException(status_code=404,detail ={"message": "Usuario no existe"})
    return usuario.__dict__
#Borrar Usuario por ID
@gestionarUsuarios.delete("/borrar/{id}")
def eliminarUsuario(id:int, db:Session = Depends(get_db)):
    
    usuario = db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail= {"message": "Usuario no existe"})
    usuario.delete()
    return usuario.__dict__
        
#Actualizar Usuario por ID
@gestionarUsuarios.put("/actualizar/{id}")
def actualizarUsuario(id:int, usuarioEditar:Usuario, db:Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if usuario is None:
        raise HTTPException(status_code=404,detail ={"message": "Usuario no existe"})
    usuario.nombre = usuarioEditar.dict()["nombre"]
    usuario.apellidoPaterno = usuarioEditar.dict()["apellidoPaterno"]
    usuario.apellidoMaterno = usuarioEditar.dict()["apellidoMaterno"]
    usuario.direccion = usuarioEditar.dict()["direccion"]
    usuario.tipoDocumento = usuarioEditar.dict()["tipoDocumento"]
    usuario.foto = usuarioEditar.dict()["foto"]
    usuario.rol_id = usuarioEditar.dict()["rol_id"]
    usuario.contraseña = usuarioEditar.dict()["contraseña"]
    usuario.email = usuarioEditar.dict()["email"]
    usuario.celular = usuarioEditar.dict()["celular"]
    usuario.fechaCreacion = usuarioEditar.dict()["fechaCreacion"]
    return usuario.__dict__
    
            
