from fastapi import FastAPI , Depends , Security , HTTPException , status
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from fastapi.staticfiles import StaticFiles
import subprocess
import platform
from pydantic import create_model


from auth.routes.user_handlers import router as user_router
from auth.auth import jwks
from auth.JWTBearer import JWTBearer
from auth.router import auth_router
from auth.schemas.models import HealthResponse
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

app.include_router(router = auth_router , prefix="/auth")

# @app.get("/", response_model=HealthResponse)
# async def health():
#     return HealthResponse(status="Ok")


@app.get('/test')
async def run_test():
    subprocess.run(['pytest'])



# http://localhost:8000/static/index.html
app.mount("/static", StaticFiles(directory="static" , html=True), name="basic_client")