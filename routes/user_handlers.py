from fastapi import APIRouter, Depends

router = APIRouter(tags=["auth"])

# auth handel
from auth.JWTBearer import JWTBearer
from auth.auth import get_current_user
from auth.auth import jwks
auth = JWTBearer(jwks)


@router.get("/secure", 
description="this route is an example for a secure route",
dependencies=[Depends(auth)],)
async def secure() -> bool:
    
    return auth.jwt_creds


@router.get("/not_secure",
description="this route is an example for a non secure route",
)
async def not_secure() -> bool:
    return True


@router.get("/test")
async def test(username: str = Depends(get_current_user)):
    return {"username": username}