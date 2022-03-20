from fastapi import APIRouter
from starlette.responses import JSONResponse

from basiccrud.controller.user import create, delete, read, update
from basiccrud.models.user import ModifyUserSchema, UserSchema

user_router = APIRouter()


@user_router.post('/user')
def create_user(user: UserSchema):
    if create(user.dict()):
        return JSONResponse({'Message': 'User created'}, 201)


@user_router.get('/users')
def get_all_users():
    return read()


@user_router.get('/user/{id}')
def get_one_user(id: int):
    return read(id)


@user_router.put('/user/{id}')
def modify_user(id: int, sets: ModifyUserSchema):
    return update(id, sets.dict(exclude_unset=True))


@user_router.delete('/user/{id}')
def delete_user(id: int):
    if delete(id):
        return JSONResponse({'Message': 'User deleted'}, 200)
