from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

@user.get('/users')
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post('/users')
def create_user(user:User):
    new_user = {"name":user.name,"email":user.email,"password":user.password}
    conn.execute(users.insert().values(new_user))
    return 'agregado'

@user.get('/users/{id}')
def get_user(id:str):
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.delete('/users/{id}')
def delete_user(id:str):
    conn.execute(users.delete().where(users.c.id == id))
    return 'eliminado datos de cliente con id = {id}'

@user.put('/users/{id}')
def update_user(id:str, user:User):
    conn.execute(users.update().values(name = user.name, 
        email = user.email, password = user.password).where(users.c.id == id))
    return 'actualizando datos de cliente con id = {id}'
