from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

engine = create_engine('sqlite:///lib/wheel_base.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session =Session

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer(), primary_key = True)
    name = Column(String(),)
    email = Column(String())
    contact = Column(Integer())