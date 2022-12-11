from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
# from routes improt posts
from routes import users
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



@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")


