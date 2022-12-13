from fastapi import FastAPI , Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from fastapi.staticfiles import StaticFiles

from routes import (
    users,
    groups,
    roles,
)
from schemas.models import HealthResponse


# auth
from auth.user_handlers import router as user_router
from auth.auth import jwks
from auth.JWTBearer import JWTBearer
auth = JWTBearer(jwks)


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
app.include_router(user_router, prefix="/auth", dependencies=[Depends(auth)])


@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")



@app.get("/secure", dependencies=[Depends(auth)])
async def secure() -> bool:
    return True


@app.get("/not_secure")
async def not_secure() -> bool:
    return True

# http://localhost:8000/static/index.html
app.mount("/static", StaticFiles(directory="static" , html=True), name="basic_client")




