from models.db import *
from flask_jwt_extended import create_access_token
from datetime import timedelta
from passlib.hash import bcrypt


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    __table_args__ = (
        UniqueConstraint('login'),
        UniqueConstraint('email'),
    )

    def __init__(self, **kwargs):
        self.login = kwargs.get('login')
        self.email = kwargs.get('email')
        self.password = bcrypt.hash(kwargs.get('password'))

    def get_token(self, expire_date=24):
        expire_delta = timedelta(expire_date)
        token = create_access_token(
            identity=self.id, expires_delta=expire_delta
        )
        return token

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email).one()
        if not bcrypt.verify(password, user.password):
            raise Exception("Invalid password")
        return user


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
