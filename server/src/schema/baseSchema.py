from datetime import date
from pydantic import BaseModel

class MemberBase(BaseModel):
    """
        principal schema 
        inherited after
        it attibute will be default 
        otran hoe par default
    """
    email: str



