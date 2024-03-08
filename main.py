from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

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

@app.get("/api/v1/{user_id}")
async def get_user(user_id: str):
    users = {
        "Iden1":{
            "username": "nick1",
            "name": "Juan"

        },
        "Iden2":{
            "username": "nick2",
            "name": "Felipe"
        }
    }


    if user_id in users:

        user = users[user_id]
        return JSONResponse(
         content=user,
         status_code=status.HTTP_404_NOT_FOUND
         )

    else:
        return JSONResponse(
            content="no existe el usuario "
        )




#%%
