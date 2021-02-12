import pymongo
from bson.objectid import ObjectId
from datetime import datetime

client = pymongo.MongoClient()
db = client.api_py


def consulta_usuario(valor):
    return valor


def consulta_usuarios():
    print("ehehe")
    return 'Hola que tal'


def cadastro_usuario(novo_usuario: dict):
    try:
        if db.usuario.find({'user': novo_usuario['user']}):
            return 1
        else:
            usuario_cadastrado = db.usuario.insert_one({
                '_id': ObjectId(),
                'user': novo_usuario['user'],
                'passwd': novo_usuario['passwd'],
                'full_name': novo_usuario['full_name'],
                'birthday': novo_usuario['birthday'],
                'forum_nickname': novo_usuario['forum_nickname']
                })
            return {'Cadastrado':'OK',
                    'id_usuario': str(usuario_cadastrado.inserted_id)}        
    except Exception as err:
        print('[{time}]{error}'.format(time=datetime.now(),error=err))
        return {'ERRO': 'Usuário não Cadastrado'}


def update_usuario(id, nova_info: dict):
