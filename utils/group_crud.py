from uuid import UUID
from sqlalchemy.orm import Session
from database.models import Group
from schemas.models import GroupCreate , GroupUpdate , GroupDelete


def group_create(db : Session , record : Group):
    db_record = Group(
        name=record.name,
        )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def groups_get_all(db: Session):
    return db.query(Group).all()

def group_get_one(db: Session , id : UUID):
    return db.query(Group).filter_by(id=id).one()

def group_update(db: Session , record : GroupUpdate):
    update_query = {
        Group.name : record.name,
        }
    db.query(Group).filter_by(id=record.id).update(update_query)
    db.commit()
    return db.query(Group).filter_by(id=record.id).one()

def group_delete(db : Session , id : UUID):
    record = db.query(Group).filter_by(id = id).all()
    if not record:
        return GroupDelete(message = "Record does not exists")
    db.query(Group).filter_by(id = id).delete()
    db.commit()
    return GroupDelete(message = "Record deleted")
