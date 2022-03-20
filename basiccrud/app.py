from fastapi import FastAPI

from basiccrud.database.db import create_db
from basiccrud.routes.user import user_router

app = FastAPI()


@app.on_event('startup')
def startup_event():
    create_db()
    print('Application startup successful!')


@app.on_event('shutdown')
def shutdown_event():
    print('Shutting down api...')


app.include_router(user_router)
