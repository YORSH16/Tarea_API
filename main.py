from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from enum import Enum
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
        "Iden1": {
            "username": "nick1",
            "name": "Juan"

        },
        "Iden2": {
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


class TaskStatus(str, Enum):
    pendiente = "pendiente"
    en_progreso = "en progreso"
    completada = "completada"


@app.post("/api/v1/tasks/create")
async def create_task(task: str, description: str, message: str):
    return {
        "name_task": task,
        "status": TaskStatus,
        "description": description,
        "message": "Tarea creada",
        "status_code": 201

    }

# %%
