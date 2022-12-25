from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum) :
    male = "male"
    female = "female"

class Role(str, Enum) :
    admin = "admin"
    user = "user"

class User(BaseModel) :
    id: Optional[UUID] = uuid4()
    firstName: str
    lastName: str
    middleName: Optional[str]
    gender: Gender
    roles: List[Role]

class UserUpdateRequest(BaseModel) :
    firstName: Optional[str]
    lastName: Optional[str]
    middleName: Optional[str]
    roles: Optional[List[Role]]