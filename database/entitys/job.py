from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///../dados.db')
Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    empresa = Column(String)
    link = Column(String, nullable=True)

Base.metadata.create_all(engine)