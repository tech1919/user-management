import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String , ForeignKey , Integer , JSON , Boolean , DateTime
from sqlalchemy.dialects.postgresql import UUID

from typing import AsyncGenerator
from datetime import datetime
from database.connection import Base, engine
from auth.models import *


# class Event(Base):

#     __tablename__ = "events"

#     id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
#     event_src = Column(String , nullable = True)
#     name = Column(String(100) , nullable=False)
#     content = Column(JSON , nullable=False)
#     creation_date = Column(DateTime , default = datetime.now())
#     modify_date = Column(DateTime , default = datetime.now())

# class EventUser(Base):

#     __tablename__ = "events_users"

#     id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
#     event_id = Column(UUID(as_uuid=True), ForeignKey('events.id'))
#     user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
