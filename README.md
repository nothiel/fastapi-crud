# Basic CRUD

Simple CRUD operations using [FastAPI](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/) :)

## 💻 Pre-requisites

Before starting, be sure you have:
* Python 3.10+
* PostgreSQL

**or**


* Docker
* Docker-compose


## ☕ Using Basic CRUD:

There's two ways of using it:

**1: docker-compose**
```
$ git clone https://github.com/nothiel/fastapi-crud.git && cd fastapi-crud
$ docker-compose up
```
**2: python**
```
# make sure you have postgresql installed
$ git clone https://github.com/nothiel/fastapi-crud.git && cd fastapi-crud
$ pip install -r requirements.txt
# optional: run pip install -r requirements.dev.txt to add developer tools like isort and etc..
$ uvicorn entrypoint:app --reload
```

## 📔 API Documentation

All API documentation can be found at /docs endpoint :) have fun!

[⬆ Back to top](#basic-crud)<br>