from model import User
from fastapi import FastAPI, Response, status
from fastapi.encoders import jsonable_encoder
import controller

app = FastAPI()

@app.get("/")
def root(res: Response):    
    return {'Message': 'Hello World!'}

@app.get("/consulta/{valor}")
def consulta(valor, res: Response):
    try:
        if valor == 'all':
            resultado = controller.consulta_usuarios()
        else:
            resultado = controller.consulta_usuario(valor)
        if resultado:
            return {'data': [resultado]}
        else:
            res.status_code = status.HTTP_404_NOT_FOUND
            return {'Message': 'Nenhum usuario encontrado'}
    except:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'erro': 'Não sei qual erro mas erro'} 

@app.post("/cadastro")
def cadastro(req: User, res: Response):
    try:
        request = jsonable_encoder(req)
        if ('user' and 'passwd' and 'full_name' and 'birthday' and 'forum_nickname' in request):
            return {'Message': 'Cu'}
        else:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return {'ERRO': 'Informações faltantes'}
    except:
        return {'ERRO': 'Não sei qual'}

@app.put("/update/{id}")
def update_usuario(id, req: UpdateUser, res: Response):
    try:
        if len(id) == 24:
            request = jsonable_encoder(req)
            updated_content = controller.update_usuario(id, request)
            if updated_content:
                res.status_code = status.HTTP_204_NO_CONTENT
                return {'Message': 'Usuario modificado'}
        else:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return {'Message': 'ID não enviado'}
    except:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'ERRO': 'não sei qual'}

    