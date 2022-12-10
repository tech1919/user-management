from fastapi import FastAPI
from db import *
from uuid import uuid4
app = FastAPI(title="User Management API")



@app.get("/")
async def home():
    return {"message": "User management API is up. Go to /docs"}


########################
# Users                #
########################


@app.get("/users/{user_id}" , tags=["users"])
async def get_user(
    user_id : str = None,
):

    if user_id == None:
        # finding all
        return session.query(User).all()
    else:
        # searching for one
        return [session.query(User).get(user_id)]

@app.get("/users/get-permissions/{user_id}" , tags=["users"])
async def get_permission(
    user_id: str,
): 
   
    # check for user permission and return it
    
    user = session.query(User).filter_by(id = user_id).first()
    return user.get_user_permissions()

@app.post("/users/create-user/" , tags=["users"])
async def sign_new_user(
    user : UserCreate,
):
    return user.create()


# @app.get("/users/check-permission/" , tags=["users"])
# async def check_permission(
#     user: UserCheck,
#     permission_desc : str,): 
   
#     # check for user permission and return it
    
#     return user.has_permission(permission_desc)

@app.put("/users/update-user/" , tags=["users"])
async def update_user(
    user : UserUpdate,
):
    return user.update()


########################
# Permissions          #
########################

@app.get("/permissions/{permission_id}" , 
tags=["permissions"] , 
description="returns a list of permissions * if no id given - returns list of all the permissions* if id was given - return a list with one permission")
async def get_permissions(
    id : str = None,
): 

    if id == None:
        # finding all 
        return session.query(Permission).all()
    else:
        # searching for one 
        return [session.query(Permission).get(id)]

@app.post("/permissions/create-permission/" ,tags=["permissions"])
async def create_new_permission(
    permission : PermissionCreate,
): 
   
    return permission.create()

@app.put("/permissions/update-permission/add-role" ,tags=["permissions"])
async def update_permission(
    permission : PermissionUpdate,
    new_role : RoleStatement,
): 
   
    return permission.add_role(new_role)


########################
# Groups               #
########################

@app.get("/groups/" ,
tags=["groups"])
async def get_group(
    id: str = None
):
    
    if id == None:
        # finding all
        return session.query(Group).all()
    else:
        # searching for one
        return [session.query(Group).get(id)]

@app.post("/groups/create-group/" ,
tags=["groups"])
async def create_new_group(
    group : GroupCreate,
): 
   
    return group.create()   

@app.put("/groups/update-group/" ,
tags=["groups"])
async def update_group(
    group : GroupUpdate,
):

    return group.update()