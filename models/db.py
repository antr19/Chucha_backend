from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine("postgresql+psycopg2://svc_database:XLQVRjpM5ktMt9yOkBq2vKqxRFKYgBIj@dpg-cgdkp01mbg54astb1drg-a.oregon-postgres.render.com/main_s2ox")

Base = declarative_base()
session_maker = sessionmaker(bind=engine)
session = Session(bind=engine)
