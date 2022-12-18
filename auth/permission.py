from typing import Dict, Optional, List
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN
from fastapi import Depends , HTTPException



# auth handel
from auth.JWTBearer import JWTBearer
from auth.auth import jwks
from database.connection import get_db
from sqlalchemy.orm import Session

auth = JWTBearer(jwks)


from database.models import RolesEntities , Role



class PermissionCheck:
    """
    This class will act as a dependency for every route
    with a given statment, the __call__ function will query
    in the roles_entities table to find all the roles related to the group
    then the method will check if the required statment is in one of those
    roles to grant permission for the user to use this route
    """
    def __init__(self , statments : List[str] ) -> None:

        # convert the statments list to a dictionary with
        # the list element as key and the values all False
        self.required_statments = self.list_to_dict(statments)

    def list_to_dict(self , list_of_strings):
        new_dictionary = {}
        for item in list_of_strings:
            new_dictionary[item] = False
        return new_dictionary

    def get_role_statments(self, role_id : str , db : Session):
        role_record = db.query(Role).filter_by(id = role_id).one()
        try:
            return role_record.permissions["statments"]
        except KeyError:
            return []

    def find_group_roles(self , group_name : str , db : Session):

        group_roles = db.query(RolesEntities).filter_by(cognito_group_name = group_name)
        return list(group_roles)

    def validate_required_statments(self):
        
        """
            This method checks if all the values in the 
            self.required_statments dictionary are True
            if only in is False, The permission in denied
        """

        for k in list(self.required_statments.keys()):
            if not self.required_statments[k]:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail=f"Permission denied : User must have {k} permission"
                )

        return True

    def __call__(self , jwt_creds : dict = Depends(auth) , db : Session = Depends(get_db)):

        
        if not dict(jwt_creds.claims)["cognito:groups"]:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Not related to any group"
            )
        else:
            cognito_groups = dict(jwt_creds.claims)["cognito:groups"]
            try:
                for group in cognito_groups:
                    groups_roles_records = self.find_group_roles(group , db=db)
            except:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="Could not query in the database"
                )

            
            for g_r in groups_roles_records:
                cur_statments_list = self.get_role_statments(g_r.role_id , db=db)
                for s in cur_statments_list:
                    if s in self.required_statments:
                        self.required_statments[s] = True
                
            
            
            self.validate_required_statments()


            # consider return some useful data
            return True
                

