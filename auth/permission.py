from typing import Dict, Optional, List
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN



class Permission:
    def __init__(self , resource , action) -> None:
        self.resource = resource
        self.action = action

    def __call__(self , group_name : str):
        pass