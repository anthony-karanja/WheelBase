#  WheelBase

**WheelBase** is a Command-Line Interface (CLI) Python application for managing car rentals. Built with **SQLAlchemy**, it allows users to interact with a car rental system that supports car listings, availability tracking, and rental pricing.

---

##  Project Structure

wheelbase/
├── cli.py # CLI interface logic
├── main.py # Entry point and app execution
├── models.py
├── seed.py
├── wheel_base.db 
├── migrations/ # Alembic migrations
├── env.py # Alembic environment setup
├── README.md # Project description
├── LICENSE # License information
├── Pipfile + Pipfile.lock # Dependencies and package management



---

##  Features

- Add, view, or update car listings
- Filter cars based on availability
- Track rental prices, mileage, color, and year
- SQLite database backend
- Database seeding with sample car data
- Alembic migrations for schema changes

---

##  Getting Started

### Prerequisites

- Python 3.12+
- [Pipenv](https://pipenv.pypa.io/en/latest/)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/anthony-karanja/WheelBase
cd wheelbase
Install dependencies:


pipenv install
pipenv shell
Run migrations (optional):


alembic upgrade head
Seed the database:


python seed.py
Run the CLI app:


python main.py
🗂️ Sample Data Format (from seed.py)
python

{
  "make": "Toyota",
  "model": "Corolla",
  "year": 2020,
  "color": "White",
  "mileage": 25000,
  "rental_price": 3500,
  "available": True
}
🛠 Technologies Used
Python 3.12

SQLAlchemy

SQLite

Alembic (for migrations)

Pipenv (for dependency management)