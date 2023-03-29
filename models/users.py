from models.db import *


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)

    __table_args__ = (
        UniqueConstraint('username'),
        UniqueConstraint('email'),
    )


Base.metadata.create_all(engine)
