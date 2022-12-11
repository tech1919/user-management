from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile

from routes import (
    users,
    groups,
    roles,
)
from schemas.models import HealthResponse

app = FastAPI(
    title = "User Management API"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=users.router , prefix="/users")
app.include_router(router=groups.router , prefix="/groups")
app.include_router(router=roles.router , prefix="/roles")



@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")


