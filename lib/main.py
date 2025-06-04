from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from models import Customer, Car, Rental

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
    customer_id = int("Enter customer id: ")
    customer = session.query(Customer).filter_by(id=customer_id)
    if customer:
        print(f" Name: {customer.name} Email: {customer.email}, Contact: {customer.contact}")
    else:
        print("Customer not found")
        
def update_customer():
    customer_id = input("\033[31mEnter customer id: \033[0m")
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        name = input("\033[31Enter new customer name: \033[0m")
        email = input("\033[31Enter new customer email: \033[0m")
        contact = input("\033[31Enter new customer contact: \033[0m")
        customer.name = name
        customer.email = email
        customer.contact = contact
        
        session.commit()
        print("\033[35mcustoemr uploaded successfully\033[0m")
    else:
        print("Customer not found")
        
def delete_customer():
    customer_id = input("Enter customer id: ")
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        print("\033[31mCustomer deleted successfully\033[0m")
        
    else:
        print("\033[31mCustomer not found\033[0m")
        
        
# car model
# def create_car():
#     make = input("Enter car make: ")
#     model = input("Enter car model: ")
#     year = int(input("Enter car make year: "))
#     # license_plate = input("Enter license number: ")
#     color = Car(make= make, model = model, make_year = year, license_plate = license_plate)
#     session.add(car)
#     session.commit()
#     print("Car added successfully")

def find_car():
    cars = session.query(Car).all()
    car_dict = {car.make: car for car in cars}

    make = input("Enter the name of the car: ").title()
    if not make:
        print("\033[31mCar name cannot be empty.\033[0m")
        return
    
    if make in car_dict:
        car = car_dict[make]
        print(f"\nCar Id: {car.id}")
        print(f"Car make: {car.make}")
        print(f"Car Model: {car.model}")
        print(f"Make Year: {car.year}")
        print(f"Car Color: {car.color}")
        print(f"Car Mileage: {car.mileage}")
        print(f"Car Price: {car.rental_price}")
        print(f"Availability: {car.available}")
        print("\n")
        print("\033[32mCar Successfully found\033[0m")
    else:
        print("\033[31mCar not found.\033[0m")

    
# def fetch_car():
    # customer_id = input("Enter customer id: ")
    # cars = session.query(Car).all()
    
    # for car in cars:
    #     print(f"Make: {car.make}, Model: {car.model}, MakeYear: {car.make_year}, license_plate{car.license_plate}")

def list_cars():
    # car_id = input("Enter car id: ")
    cars = session.query(Car).all()
    car_list = {car.make for car in cars}
    if car_list:
        print("Cars: \n")
        for make in car_list:
            print(make)
    else:
        print("\033[31mCar not found.\033[0m")
    #     print(f"Make: {car.make} Model: {car.model}, Makeyear: {car.make_year}, license_plate{car.license_plate}")
    # else:
    #     print("Car not found")
        
def update_car():
    car_id = input("\033[Enter car id: \033[0m]")
    car = session.query(Car).filter_by(id=car_id).first()
    if car:
        make = input("Enter new make: ")
        model = input("Enter new model: ")
        make_year = input("Enter new make year: ")
        # license_plate = input("Enter license plate: ")
        car.make = make
        car.model = model
        car.make_year = make_year
        # car.license_plate = license_plate
        
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

# if __name__ == "__main__":
#     create_customer()

    
    
    

        
    
    
