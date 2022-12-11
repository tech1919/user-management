import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String , ForeignKey , Integer , JSON , Boolean
from sqlalchemy.dialects.postgresql import UUID

from typing import AsyncGenerator

from database.connection import Base, engine




# class User(SQLAlchemyBaseUserTableUUID, Base):
#     pass



########################
# Users                #
########################

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    name = Column(String(340) , nullable=True)
    email = Column(String(340) , nullable=True)
    hased_password = Column(String(1024) , nullable=True)
    is_active = Column(Boolean , default = True)
    is_superuser  = Column(Boolean , default = False)
    is_verified  = Column(Boolean , default = True)


    # def get_user_permissions(self):
    #     return session.query(PermissionEntities).filter_by(user_id=self.id).first()

########################
# Permissions          #
########################

class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    name = Column(String(50))
    roles = Column(JSON , default = {} , nullable = False)

class PermissionEntities(Base):
    __tablename__ = "permissions_entities"
    id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    permission_id = Column(UUID(as_uuid=True), ForeignKey('permissions.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))

########################
# Groups               #
########################

class Group(Base):

    __tablename__ = 'groups'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)

class GroupUser(Base):
    __tablename__ = "groups_users"

    id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    group_id =  Column(UUID(as_uuid=True), ForeignKey('groups.id'))
    user_ids = Column(UUID(as_uuid=True), ForeignKey('users.id'))


########################
# Events               #
########################

class Event(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    event_src = Column(String)
    name = Column(String(100))
    content = Column(String)

class EventUser(Base):
    __tablename__ = "events_users"

    id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)

    event_id = Column(UUID(as_uuid=True), ForeignKey('events.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))





Base.metadata.create_all(engine)
