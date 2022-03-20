from basiccrud.database.db import Users


def create(user: dict):
    new_user = Users.create_from(user)
    return new_user


def read(id=None):
    if id:
        return Users.get_by_id(id)

    user = Users.get_all()
    return [usr for usr in user]


def update(id, sets):
    return Users.update_by_id(id, sets)


def delete(id):
    return Users.delete_by_id(id)
