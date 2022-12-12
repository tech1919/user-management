from uuid import UUID
from sqlalchemy.orm import Session

from database.models import Role
from schemas.models import (
    RoleCreate , 
    RoleUpdate , 
    RoleDelete ,
    Permission,
)


def has_permission(role : RoleUpdate , resource : str , action : str) -> bool:
    """
        This function check if a given role has a permission
        return True is it has and False if not
    """
    for s in role.permissions["statments"]:
        if s["resource"] == resource:
            for a in s["actions"]:
                if action == a:
                    return True
    
    return False

def role_create(db : Session , record : Role):
    db_record = Role(
        name=record.name, 
        permissions= record.permissions,
        )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def role_get_all(db: Session):
    return db.query(Role).all()

def role_get_one(db: Session , id : UUID):
    return db.query(Role).filter_by(id=id).one()

def role_add_a_permission(
    db : Session , 
    record : RoleUpdate , 
    permission : Permission,
    ):

    db_record = db.query(Role).filter_by(id = record.id).first()
    new_permission = {
            "resource" : permission.resource, # one string with the name of the resource
            "actions" : permission.actions, # a list of strings
            }
    try:
        db_record.permissions["statments"].append(new_permission)
    except:
        db_record.permissions["statments"] = [new_permission]
    finally:
        return role_update(db=db , record=db_record)

def role_remove_a_permission(
    db : Session , 
    record : RoleUpdate , 
    permission : Permission,
    ):

    db_record = db.query(Role).filter_by(id = record.id).first()


    permission_to_remove = {
            "resource" : permission.resource, # one string with the name of the resource
            "actions" : permission.actions, # a list of strings
            }

    # for all the statments in this permission 
    for i , s in enumerate(db_record.permissions["statments"]):
        # if matching resource found for this role
        if s["resource"] == permission_to_remove["resource"]:
            # search matching action to remove
            for action in permission_to_remove["actions"]:
                
                
                try:
                    # try to remove this action
                    db_record.permissions["statments"][i]["actions"].remove(action)
                    # check if now the statment is empty, if it is remove it too
                    if len(db_record.permissions["statments"][i]["actions"]) == 0:
                        db_record.permissions["statments"].pop(i)
                except:
                    pass
  

    return role_update(db=db , record=db_record)

def role_update(db: Session , record : RoleUpdate):
    update_query = {
        Role.name : record.name ,
        Role.permissions : record.permissions ,
        }
    db.query(Role).filter_by(id=record.id).update(update_query)
    db.commit()
    return db.query(Role).filter_by(id=record.id).one()

def role_delete(db : Session , id : UUID):
    record = db.query(Role).filter_by(id = id).all()
    if not record:
        return RoleDelete(message = "Record does not exists")
    db.query(Role).filter_by(id = id).delete()
    db.commit()
    return RoleDelete(message = "Record deleted")
