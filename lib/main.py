from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from models import Customer, Car, Rental

from cli import main

engine = create_engine('sqlite:///lib/wheel_base.db')

Session = sessionmaker(bind = engine)
session = Session()

# Customermodel
def create_customer():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    contact = int(input("Enter your contact: "))
    
    customer = Customer(name= name, email = email, contact = contact)
    session.add(customer)
    session.commit()
    print("Customer added successfully")
    
def fetch_customers():
    # customer_id = input("Enter customer id: ")
    customers = session.query(Customer).all()
    for customer in customers:
        print(f"Name: {customer.name}, Email: {customer.email}, Contact: {customer.contact}")

def list_customer():
    customer_id = input("Enter customer id: ")
    customer = session.query(Customer).get(customer_id)
    if customer:
        print(f"Name: {customer.name} Email: {customer.email}, Contact: {customer.contact}")
    else:
        print("Customer not found")
        
def update_customer():
    customer_id = input("Enter custoner id: ")
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        name = input("Enter new customer name: ")
        email = input("Enter new customer email: ")
        contact = input("Enter new customer contact: ")
        customer.name = name
        customer.email = email
        customer.contact = contact
        
        session.commit()
        print("custoemr uploaded successfully")
    else:
        print("Customer not found")
        
def delete_customer():
    customer_id = input("Enter customer id: ")
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        print("Customer deleted successfully")
        
    else:
        print("Customer not found")
        
        
# car model
def create_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    make_year = int(input("Enter car make year: "))
    license_plate = input("Enter license number: ")
    car = Car(make= make, model = model, make_year = make_year, license_plate = license_plate)
    session.add(car)
    session.commit()
    print("Car added successfully")
    
def fetch_car():
    # customer_id = input("Enter customer id: ")
    cars = session.query(Car).all()
    for car in cars:
        print(f"Make: {car.make}, Model: {car.model}, MakeYear: {car.make_year}, license_plate{car.license_plate}")

def list_cars():
    car_id = input("Enter car id: ")
    car = session.query(Car).filter_by(id=car_id).first()
    if car:
        print(f"Make: {car.make} Model: {car.model}, Makeyear: {car.make_year}, license_plate{car.license_plate}")
    else:
        print("Car not found")
        
def update_car():
    car_id = input("Enter car id: ")
    car = session.query(Car).filter_by(id=car_id).first()
    if car:
        make = input("Enter new make: ")
        model = input("Enter new model: ")
        make_year = input("Enter new make year: ")
        license_plate = input("Enter license plate: ")
        car.make = make
        car.model = model
        car.make_year = make_year
        car.license_plate = license_plate
        
        session.commit()
        print("Car uploaded successfully")
    else:
        print("Car not found")
        
def delete_car():
    car_id = input("Enter car id: ")
    car = session.query(Car).get(car_id)
    if car:
        session.delete(car)
        session.commit()
        print("Car deleted successfully")
        
    else:
        print("Car not found")
        
# rental model
def create_car_rental():
    car_id = input("Enter car id: ")
    customer_id= input("Enter customer Id:")
    price = int(input("Enter Amount:"))
    hire_date = input("Enter hire date(YYYY/MM/DD) or none :")
    date_return = input("Enter return date(YYYY/MM/DD) or none :")
    rental_date = datetime.strptime(hire_date, "%Y/%m/%d") if hire_date else None
    return_date= datetime.strptime(date_return, "%Y/%m/%d") if date_return else None
    
    car = session.query(Car).filter_by(id= car_id).first()
    customer = session.query(Customer).filter_by(id= customer_id).first()
    if car and customer:
        car_rental = Rental(car_id= car_id,customer_id=customer_id, price=price, rental_date= rental_date, return_date= return_date)
        session.add(car_rental)
        session.commit()
        print("Car hired")
    else:
        print("Car or customer not found")
        
def fetch_car_rentals():
    car_rentals = session.query(Rental).all()
    for car_rental in car_rentals: 
        print(f"Price: {car_rental.price}, car: {car_rental.car.make}, Customer: {car_rental.customer.name} Hire-date: {car_rental.rental_date}, Return: {car_rental.return_date}")
        
def list_car_rental():
    car_rental_id = input("Enter rental id:") 
    car_rental = session.query(Rental).filter_by(id=car_rental_id).first()
    if car_rental:
        print(f"Price: {car_rental.price}, car: {car_rental.car.make}, Customer: {car_rental.customer.name} Hire-date: {car_rental.rental_date}, Return: {car_rental.return_date}")
    else:
        print("Car not hired!")
        
def update_car_rental():
    car_rental_id = input("Enter car rental id:") 
    car_rental = session.query(Rental).filter_by(id=car_rental_id).first()
    if car_rental:
        car_id = input("Enter new car rental id: ")
        customer_id= input("Enter customer  Id:")
        price = int(input("Enter new amount:"))
        hire_date = input("Enter hire date(YYYY-MM-DD) or none :")
        return_date = input("Enter return date(YYYY-MM-DD) or none :")
        date_hire = datetime.strptime(hire_date, "%Y/%m/%d") if hire_date else None
        date_return = datetime.strptime(return_date, "%Y/%m/%d") if return_date else None
        car_rental.car_id= car_id
        car_rental.customer_id = customer_id
        car_rental.price = price
        car_rental.date_hire=date_hire
        car_rental.date_return = date_return
        session.commit()
        print("Car rented updated successfully!")
    else:
        print("Car not found!")
        
        
def delete_car_rental():
    car_rental_id = input("Enter rental id")
    car_rental = session.query(Rental).get(car_rental_id)
    if car_rental:
        session.delete(car_rental)
        session.commit()
        print("Car hired deleted succesfully")
    else:
        print("Car not hired!")

if __name__ == "__main__":
    update_car_rental()
    delete_customer()

    
    
    

        
    
    
