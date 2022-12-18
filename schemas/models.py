from typing import Optional , List
from uuid import UUID

from pydantic import BaseModel
from datetime import datetime

class HealthResponse(BaseModel):
    status: str
  
class UserCreate(BaseModel):
    name : str
    email : str
    hased_password : str
    is_active : bool
    is_superuser : bool
    is_verified : bool

class UserCheck(BaseModel):

    id : str
    is_active: bool
    is_superuser: bool
    is_verified: bool

class UserUpdate(BaseModel):
    
    id : str
    name : str
    email : str
    hased_password : str
    is_active : bool
    is_superuser : bool
    is_verified : bool
    creation_date : datetime
    modify_date : datetime

class UserDelete(BaseModel):
    message : str

class Permission(BaseModel):
    statments : List[str]

class RoleCreate(BaseModel):

    name : str
    permissions : dict

class RoleDelete(BaseModel):
    message : str

class RoleUpdate(BaseModel):

    id : str
    name : str
    permissions : dict

class GroupCreate(BaseModel):

    name: str

class GroupUpdate(BaseModel):

    id : str
    name : str

class GroupDelete(BaseModel):
    message : str

class GroupUserCreate(BaseModel):
    group_id : UUID
    user_ids : List[UUID]

class GroupUserUpdate(BaseModel):
    pass

class GroupUserdelete(BaseModel):
    message : str

class EventCreate(BaseModel):
    pass

class EventUpdate(BaseModel):
    pass

class EventDelete(BaseModel):
    message : str

