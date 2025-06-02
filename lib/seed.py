from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Car, Base  

car_inventory = [
    {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "color": "White",
        "mileage": 25000,
        "rental_price": 3500,
        "available": True
    },
    {
        "make": "Honda",
        "model": "Civic",
        "year": 2019,
        "color": "Silver",
        "mileage": 30000,
        "rental_price": 3200,
        "available": True
    },
    {
        "make": "Nissan",
        "model": "X-Trail",
        "year": 2021,
        "color": "Black",
        "mileage": 18000,
        "rental_price": 5000,
        "available": True
    },
    {
        "make": "Mazda",
        "model": "CX-5",
        "year": 2022,
        "color": "Red",
        "mileage": 12000,
        "rental_price": 5400,
        "available": True
    },
    {
        "make": "BMW",
        "model": "3 Series",
        "year": 2020,
        "color": "Blue",
        "mileage": 22000,
        "rental_price": 8000,
        "available": True
    },
    {
        "make": "Mercedes-Benz",
        "model": "C-Class",
        "year": 2021,
        "color": "Gray",
        "mileage": 20000,
        "rental_price": 8500,
        "available": False
    },
    {
        "make": "Volkswagen",
        "model": "Golf",
        "year": 2018,
        "color": "Green",
        "mileage": 40000,
        "rental_price": 2800,
        "available": True
    },
    {
        "make": "Subaru",
        "model": "Forester",
        "year": 2023,
        "color": "White",
        "mileage": 8000,
        "rental_price": 6000,
        "available": True
    },
    {
        "make": "Ford",
        "model": "Escape",
        "year": 2019,
        "color": "Black",
        "mileage": 35000,
        "rental_price": 4000,
        "available": False
    },
    {
        "make": "Hyundai",
        "model": "Tucson",
        "year": 2020,
        "color": "Silver",
        "mileage": 27000,
        "rental_price": 3900,
        "available": True
    }
    # Add more if needed...
]

engine = create_engine('sqlite:///lib/wheel_base.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

# Delete all existing cars if more than 10
car_count = session.query(Car).count()
if car_count > 10:
    session.query(Car).delete()
    session.commit()

# Populate cars
for data in car_inventory:
    car = Car(
        make=data["make"],
        model=data["model"],
        year=data["year"],
        color=data["color"],
        mileage=data["mileage"],
        rental_price=data["rental_price"],
        available=data["available"]
    )
    session.add(car)

session.commit()
# print("Cars populated successfully.")
