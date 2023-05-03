from app.models.db import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.schema import ForeignKey


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key = True)
    nombre = Column(String(255))
    apellidoPaterno = Column(String(30))
    apellidoMaterno = Column(String(30))
    direccion = Column(String(50))
    tipoDocumento = Column(String(30))
    fechaCreacion = Column(DateTime, default = datetime.now().strftime("%d/%m/%Y"), onupdate = datetime.now().strftime("%d/%m/%Y"))
    foto = Column(String(255))
    rol_id = Column(Integer, ForeignKey("Roles.id", ondelete = "CASCADE"))
    contraseña = Column(String(30))
    email = Column(String(50))
    celular = Column(Integer)
    
class Roles(Base):
    __tablename__ = "Roles"
    id = Column(Integer, primary_key = True, autoincrement = True)
    nombre = Column(String(30))
    
