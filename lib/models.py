from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer(), primary_key = True)
    name = Column(String(),)
    email = Column(String())
    contact = Column(Integer())
    
    car_rentals = relationship("Rental", back_populates="customer")
    
class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    color = Column(String)
    mileage = Column(Integer)
    rental_price = Column(Integer)
    available = Column(Boolean)
    
    car_rentals = relationship("Rental", back_populates="car")

    
class Rental(Base):
    __tablename__ = "car_rentals"
    
    id = Column(Integer(), primary_key = True)
    customer_id = Column(Integer(), ForeignKey("customers.id"), unique = True)
    car_id = Column(Integer(), ForeignKey("cars.id"), unique = True)
    price = Column(Integer())
    rental_date = (DateTime)
    return_date = Column(DateTime())
    
    
    customer = relationship("Customer", back_populates= "car_rentals")
    car = relationship("Car", back_populates= "car_rentals")
    