from model import User, UpdateUser
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
async def cadastro(req: User, res: Response):
    try:
        request = jsonable_encoder(req)
        integrity = test_integrity(request)
        if len(request) == 5 and integrity: 
            results = await controller.cadastro_usuario(request)
            print(results)
            if results['status'] == 0:
                res.status_code = status.HTTP_400_BAD_REQUEST
                return {'ERRO': 'USUARIO JÁ CADASTRADO'}
            elif results:
                return results
            else:
                res.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
                return {'ERRO' : 'BRABO'}
        else:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return {'ERRO': 'Informações faltantes'}
    except Exception as erro:
        print(erro)
        return {'ERRO': erro}

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



def test_integrity(req):
    for value in req:
        if not req[value]:
            return False
    return True