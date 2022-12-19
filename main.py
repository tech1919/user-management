from fastapi import FastAPI , Depends , Security , HTTPException , status
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from fastapi.staticfiles import StaticFiles
import subprocess
import platform
from pydantic import create_model


from routes import (
    users,
    groups,
    roles,
)
from schemas.models import HealthResponse


# auth
from routes.user_handlers import router as user_router
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
app.include_router(router=user_router, prefix="/auth") # , dependencies=[Depends(auth)]


@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")


@app.get('/test')
async def run_test():
    subprocess.run(['pytest'])



# http://localhost:8000/static/index.html
app.mount("/static", StaticFiles(directory="static" , html=True), name="basic_client")




