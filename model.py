from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    user: str
    passwd: str
    full_name: str
    birthday: datetime
    forum_nickname: str
    class Config:
        schema_extra = {
            "example" : {
                'user' : 'rafa',
                'passwd' : 'rafa123',
                'full_name' : 'Rafael Barbosa',
                'birthday' : datetime.now(),
                'forum_nickname' : 'rafinhabrabo'
            }
        }


class UpdateUser(BaseModel):
    user: Optional[str] = None
    passwd: Optional[str] = None
    full_name: Optional[str] = None
    birthday: Optional[datetime] = None
    forum_nickname: Optional[str] = None
    class Config:
        schema_extra = {
            "example" : {
                'user' : 'rafa',
                'passwd' : 'rafa123',
                'full_name' : 'Rafael Barbosa',
                'birthday' : datetime.now(),
                'forum_nickname' : 'rafinhabrabo'
            }
        }