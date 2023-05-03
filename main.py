from fastapi import FastAPI, Depends
import uvicorn
from app.routers import usuario, rol
from app.models.db import Base, engine

def create_tables():
    Base.metadata.create_all(bind = engine) 
create_tables()

app = FastAPI()
app.include_router(usuario.router)
app.include_router(rol.router)

#Corre el sv desde main.py
if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload = True)
    
#Corre desde terminal con uvicorn main:app