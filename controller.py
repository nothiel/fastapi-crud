import motor.motor_asyncio
from bson.objectid import ObjectId
from datetime import datetime

mongo_info = 'mongodb+srv://userToken:randompassword@apinodecluster.stepb.mongodb.net/api_py?retryWrites=true&w=majority'
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_info)
db = client.api_py
user_collection = db.get_collection("usuario")


def consulta_usuario(valor):
    return valor


def consulta_usuarios():
    print("ehehe")
    return 'Hola que tal'


async def cadastro_usuario(novo_usuario: dict):
    try:
        user = await user_collection.find_one({'user': str(novo_usuario['user'])})
        if user:
            return {'status': 0}
        else:
            usuario_cadastrado = await user_collection.insert_one({
                '_id': ObjectId(),
                'user': str(novo_usuario['user']),
                'passwd': str(novo_usuario['passwd']),
                'full_name': str(novo_usuario['full_name']),
                'birthday': novo_usuario['birthday'],
                'forum_nickname': str(novo_usuario['forum_nickname'])
                })
            return {'Cadastrado':'OK', 'id_usuario': str(usuario_cadastrado.inserted_id), 'status': 1 }         
    except Exception as err:
        print('[{time}]{error}'.format(time=datetime.now(),error=err))
        return {'ERRO': 'Usuário não Cadastrado'}


def update_usuario(id, nova_info: dict):
    return