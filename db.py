# import os
# from typing import AsyncGenerator , List , Any
# from fastapi import Depends
# from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.dialects.postgresql import UUID
# import uuid
# from sqlalchemy import create_engine
# from sqlalchemy.orm import relationship
# from sqlalchemy import Column, Integer, String , DateTime , JSON , ForeignKey , Boolean , Float
# from pydantic import BaseModel
# from datetime import datetime

# connection to the database

# DATABASE_URL = os.environ.get('DATABASE_URL')
# Base: DeclarativeMeta = declarative_base()

# engine = create_engine(DATABASE_URL , echo=True)

# Session = sessionmaker(bind=engine)
# session = Session()

########################
# Users                #
########################

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
#     name = Column(String(340) , nullable=True)
#     email = Column(String(340) , nullable=True)
#     hased_password = Column(String(1024) , nullable=True)
#     is_active = Column(Boolean , default = True)
#     is_superuser  = Column(Boolean , default = False)
#     is_verified  = Column(Boolean , default = True)


#     def get_user_permissions(self):
#         return session.query(PermissionEntities).filter_by(user_id=self.id).first()
        
# class UserCreate(BaseModel):
#     name : str
#     # email : str
#     # hased_password : str
#     is_active : bool
#     is_superuser : bool
#     is_verified : bool

#     def create(self):
#         session.add(User(
#             name = self.name,
#             # email = self.email,
#             # hased_password = self.hased_password,
#             is_active = self.is_active,
#             is_superuser = self.is_superuser,
#             is_verified = self.is_verified,
#         ))
#         session.commit()

#         return self
    
# class UserCheck(BaseModel):

#     id : str
#     is_active: bool
#     is_superuser: bool
#     is_verified: bool

    
#     def has_permission(self):
        
#         """Check out whether a user has a permission or not."""

#         # if the permission does not exist or was not given to the user
#         pass

# class UserUpdate(BaseModel):
    
#     id : str
#     name : str
#     email : str
#     hased_password : str
#     is_active : bool
#     is_superuser : bool
#     is_verified : bool

#     def update(self):

#         return

########################
# Permissions          #
########################

# class Permission(Base):
#     __tablename__ = 'permissions'

#     id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
#     name = Column(String(50))
#     roles = Column(JSON , default = {} , nullable = False)

# class PermissionEntities(Base):
#     __tablename__ = "permissions_entities"
#     id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
#     permission_id = Column(UUID(as_uuid=True), ForeignKey('permissions.id'))
#     user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))

# class RoleStatement(BaseModel):
#     resource : str
#     actions : List[str] 

# class PermissionCreate(BaseModel):

#     name : str
#     roles : dict

#     def create(self):
#         exists_permission = session.query(Permission).filter_by(name = self.name).first()
#         if exists_permission == None:
#             session.add(Permission(
#                 name = self.name,
#             ))
#             session.commit()
#             return self
#         else:
#             return False

# class PermissionUpdate(BaseModel):

#     id : str
#     name : str
#     roles : dict

#     def add_role(self , new_role):

#         permission_to_update = session.query(Permission).filter_by(id = self.id)
#         if permission_to_update == None:
#             return
#         else:
#             permission_to_update.roles[new_role.resource] = new_role.actions
#             session.commit()
            

########################
# Groups               #
########################

# class Group(Base):

#     __tablename__ = 'groups'

#     id = Column(UUID(as_uuid=True), primary_key=True)
#     name = Column(String)

# class GroupUser(Base):
#     __tablename__ = "groups_users"

#     id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
#     group_id =  Column(UUID(as_uuid=True), ForeignKey('groups.id'))
#     user_ids = Column(UUID(as_uuid=True), ForeignKey('users.id'))

# class GroupCreate(BaseModel):

#     name: str

    
#     def create(self):
#         exists_permission = session.query(Group).filter_by(name = self.name).first()
#         if exists_permission == None:
#             session.add(Group(
#                 name = self.name,
#             ))
#             session.commit()
#             return self
#         else:
#             return False

# class GroupUpdate(BaseModel):

#     id : str
#     name : str

#     def update(self):

#         return

########################
# Events               #
########################

# class Event(Base):
#     __tablename__ = "events"

#     id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
#     event_src = Column(String)
#     name = Column(String(100))
#     content = Column(String)

# class EventUser(Base):
#     __tablename__ = "events_users"

#     id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)

#     event_id = Column(UUID(as_uuid=True), ForeignKey('events.id'))
#     user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))

# class EventCreate(BaseModel):
#     pass

# class EventUpdate(BaseModel):
#     pass

# class EventDelete(BaseModel):
#     pass


# # create all tables if not exists
# Base.metadata.create_all(engine)