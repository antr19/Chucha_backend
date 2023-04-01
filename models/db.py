from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, scoped_session

engine = create_engine("postgresql+psycopg2://svc_database:XLQVRjpM5ktMt9yOkBq2vKqxRFKYgBIj@dpg-cgdkp01mbg54astb1drg-a.oregon-postgres.render.com/main_s2ox")

Base = declarative_base()
session_maker = scoped_session(sessionmaker(bind=engine))
session = Session(bind=engine)

Base.query = session_maker.query_property()
