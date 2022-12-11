from uuid import UUID
from sqlalchemy.orm import Session

from database.models import Permission
from schemas.models import (
    PermissionCreate , 
    PermissionUpdate , 
    PermissionDelete , 
    PermissionStatment
)


def permission_create(db : Session , record : Permission):
    db_record = Permission(
        name=record.name, 
        role= record.roles,
        )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def permission_get_all(db: Session):
    return db.query(Permission).all()

def permission_get_one(db: Session , id : UUID):
    return db.query(Permission).filter_by(id=id).one()

def permission_add_to_role(
    db : Session , 
    record : PermissionUpdate , 
    statment : PermissionStatment
    ):

    # write the add to role function
    pass  

def permission_update(db: Session , record : PermissionUpdate):
    update_query = {
        Permission.name : record.name ,
        Permission.roles : record.roles ,
        }
    db.query(Permission).filter_by(id=record.id).update(update_query)
    db.commit()
    return db.query(Permission).filter_by(id=record.id).one()

def permission_delete(db : Session , id : UUID):
    record = db.query(Permission).filter_by(id = id).all()
    if not record:
        return PermissionDelete(message = "Record does not exists")
    db.query(Permission).filter_by(id = id).delete()
    db.commit()
    return PermissionDelete(message = "Record deleted")
