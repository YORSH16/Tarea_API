from fastapi import FastAPI

import uuid

app = FastAPI(
    title="APIs en clase de Mlops 5",
    version="0.0.1"
)

@app.post("/api/v1/users/")
async def create_user(username: str, mail: str, password: str):
    return {
        "username": username,
        "mail": mail,
        "password": password,
        "message": "El usuario se creo correctamente",
        "status_code": 201
    }



















#%%
