from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    login: str
    password: str
    nickname: str

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    @classmethod
    def create_from(cls,user_dict):
        with Session(engine) as session:
            session.add(cls(**user_dict))
            session.commit()
            return True

    @classmethod
    def get_all(cls):
        with Session(engine) as session:
            return session.exec(select(cls)).all()


    @classmethod
    def get_by_id(cls, id):
        with Session(engine) as session:
            return session.exec(select(cls).where(cls.id == id)).first()

    @classmethod
    def update_by_id(cls, id, set):
        user = cls.get_by_id(id)
        with Session(engine) as session:
            for k,v in set.items():
                user[k] = v
            session.add(user)
            session.commit()
            session.refresh(user)
        return user

    @classmethod
    def delete_by_id(cls, id):
        user = cls.get_by_id(id)
        with Session(engine) as session:
            session.delete(user)
            session.commit()
        return True
        



engine = create_engine('postgresql://postgres:postgres@db:5432/postgres')

def create_db():
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)


