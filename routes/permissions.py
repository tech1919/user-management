from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db
from schemas.models import (
    PermissionDelete,
    PermissionCreate,
    PermissionStatment,
    PermissionUpdate,
)

from utils.permission_crud import (
    permission_add_to_role,
    permission_create,
    permission_get_all,
    permission_get_one,
    permission_update,
    permission_delete
)

router = APIRouter(tags=["permissions"])



@router.post("/create" , status_code=status.HTTP_201_CREATED) # response_model=UserCreate
def create_permission(
    record : PermissionCreate,
    db: Session = Depends(get_db),
):
  
    return permission_create(db=db , record=record)

@router.get("/list/all" , status_code=status.HTTP_200_OK , ) # response_model=List[UserCreate]
def get_all_permission(
    db: Session = Depends(get_db),
):
    return permission_get_all(db=db)

@router.get("/get/{id}", status_code=status.HTTP_200_OK, ) # response_model=UserCreate
def get_one_permission(id, db: Session = Depends(get_db)):
    return permission_get_one(db=db, id=id)

@router.put("/update" , status_code=status.HTTP_200_OK , ) # response_model=UserCreate
def update_permission(
    record : PermissionUpdate,
    db: Session = Depends(get_db),    
):
    return permission_update(db=db , record=record)

@router.delete(
    "/delete/{id}" , 
    status_code=status.HTTP_200_OK , 
    response_model=PermissionDelete
)
def delete_permission(
    id,
    db : Session = Depends(get_db),
):
    return permission_delete(db=db , id=id)

