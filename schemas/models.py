from typing import Optional , List
from uuid import UUID

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str

        
class UserCreate(BaseModel):
    name : str
    email : str
    hased_password : str
    is_active : bool
    is_superuser : bool
    is_verified : bool

    # def create(self):
    #     session.add(User(
    #         name = self.name,
    #         # email = self.email,
    #         # hased_password = self.hased_password,
    #         is_active = self.is_active,
    #         is_superuser = self.is_superuser,
    #         is_verified = self.is_verified,
    #     ))
    #     session.commit()

    #     return self
    
class UserCheck(BaseModel):

    id : str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    
    # def has_permission(self):
        
    #     """Check out whether a user has a permission or not."""

    #     # if the permission does not exist or was not given to the user
    #     pass

class UserUpdate(BaseModel):
    
    id : str
    name : str
    email : str
    hased_password : str
    is_active : bool
    is_superuser : bool
    is_verified : bool

    # def update(self):

    #     return

class UserDelete(BaseModel):
    pass

class RoleStatement(BaseModel):
    resource : str
    actions : List[str] 

class PermissionCreate(BaseModel):

    name : str
    roles : dict

    # def create(self):
    #     exists_permission = session.query(Permission).filter_by(name = self.name).first()
    #     if exists_permission == None:
    #         session.add(Permission(
    #             name = self.name,
    #         ))
    #         session.commit()
    #         return self
    #     else:
    #         return False

class PermissionUpdate(BaseModel):

    id : str
    name : str
    roles : dict

    # def add_role(self , new_role):

    #     permission_to_update = session.query(Permission).filter_by(id = self.id)
    #     if permission_to_update == None:
    #         return
    #     else:
    #         permission_to_update.roles[new_role.resource] = new_role.actions
    #         session.commit()
            


class GroupCreate(BaseModel):

    name: str

    
    # def create(self):
    #     exists_permission = session.query(Group).filter_by(name = self.name).first()
    #     if exists_permission == None:
    #         session.add(Group(
    #             name = self.name,
    #         ))
    #         session.commit()
    #         return self
    #     else:
    #         return False

class GroupUpdate(BaseModel):

    id : str
    name : str

    # def update(self):

    #     return




class EventCreate(BaseModel):
    pass

class EventUpdate(BaseModel):
    pass

class EventDelete(BaseModel):
    pass


