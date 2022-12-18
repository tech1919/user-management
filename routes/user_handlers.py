from fastapi import APIRouter, Depends , Security
router = APIRouter(tags=["auth"])

# auth handel
from auth.JWTBearer import JWTBearer
from auth.auth import jwks
from auth.permission import PermissionCheck


auth = JWTBearer(jwks)



users_read_permission_check = PermissionCheck(statments=["events:read" , "events:write" , "aoi:read"])


@router.get("/secure", 
description="this route is an example for a secure route",
dependencies=[Depends(users_read_permission_check)],)
async def secure():
    
    return "You have access"


@router.get("/not_secure",
description="this route is an example for a non secure route",

)
async def not_secure(

):
    return True

