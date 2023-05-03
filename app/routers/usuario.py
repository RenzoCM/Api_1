
from fastapi import APIRouter
from fastapi import FastAPI, Depends
from app.schemas import Usuario
from app.models.db import get_db
from sqlalchemy.orm import Session
from app.models import models


router = APIRouter(
    prefix= "/usuarios", tags=["Usuarios"]
    
)

usuarios = []

#GetUsuarios
@router.get("/")
def recibirUsuario(db:Session = Depends(get_db)):
    data = db.query(models.Usuario).all()
    return data

#RegistrarUsuarios
@router.post("/")
def crearUsuario(user:Usuario, db:Session = Depends(get_db)):
    usuario = user.dict()
    
    nuevoUsuario = models.Usuario(
        id = usuario[id],
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
    db.refresh()
    return True

#Get Usuario por ID
@router.get("/{id}")
def recibirUsuarioById(id:int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario 

#Borrar Usuario por ID
@router.delete("/{id}")
def eliminarUsuario(id:int):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return usuario
        
#Actualizar Usuario por ID
@router.put("/{id}")
def actualizarUsuario(id:int, usuarioEditar:Usuario):
    for index, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            usuario[index]["nombre"] = usuarioEditar.dict()["nombre"]
            usuario[index]["apellidoPaterno"] = usuarioEditar.dict()["apellidoPaterno"]
            usuario[index]["apellidoMaterno"] = usuarioEditar.dict()["apellidoMaterno"]
            usuario[index]["direccion"] = usuarioEditar.dict()["direccion"]
            usuario[index]["tipoDocumento"] = usuarioEditar.dict()["tipoDocumento"]
            usuario[index]["foto"] = usuarioEditar.dict()["foto"]
            usuario[index]["rol_id"] = usuarioEditar.dict()["rol_id"]
            usuario[index]["contraseña"] = usuarioEditar.dict()["contraseña"]
            usuario[index]["email"] = usuarioEditar.dict()["email"]
            usuario[index]["celular"] = usuarioEditar.dict()["celular"]
            usuario[index]["fechaCreacion"] = usuarioEditar.dict()["fechaCreacion"]
    
            
