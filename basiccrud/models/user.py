from pydantic import BaseModel, root_validator


class UserSchema(BaseModel):
    login: str
    password: str
    nickname: str

class ModifyUserSchema(BaseModel):
    login: str | None
    password: str | None
    nickname: str | None

    @root_validator
    def any_of(cls, v):
        if not any(v.values()):
            raise ValueError('no field inserted')
        return v 
