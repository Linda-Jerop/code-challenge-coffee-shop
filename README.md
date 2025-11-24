# Coffee Shop - Object Relationships

A Python domain model demonstrating Object-Oriented Programming with `Customer`, `Coffee`, and `Order` classes implementing a many-to-many relationship.

## Overview

This project models a coffee shop where:
- A `Customer` can place many `Orders`
- A `Coffee` can have many `Orders`
- An `Order` belongs to one `Customer` and one `Coffee`

## Features

- Input validation (customer names: 1-15 chars, coffee names: 3+ chars, prices: $1-$10)
- Bidirectional object relationships
- Aggregate methods: `num_orders()`, `average_price()`, `most_aficionado()`
- Exception handling for invalid inputs
- Comprehensive test suite

## Project Structure

```
coffee_shop/
├── coffee_shop/
│   ├── __init__.py
│   ├── customer.py       # Customer class
│   ├── coffee.py         # Coffee class
│   ├── order.py          # Order class
│   └── debug.py          # Demo script
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
├── README.md
├── requirements.txt
└── Pipfile
```

## Setup

**Using pipenv:**
```bash
pipenv install
pipenv shell
pipenv install pytest
```

**Using pip:**
```bash
pip install -r requirements.txt
```

**Verify installation:**
```bash
python3 -c "from coffee_shop.customer import Customer; print('Success!')"
```

## Usage

```python
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

# Create instances
alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")

# Create orders
alice.create_order(latte, 4.5)
bob.create_order(latte, 6.0)

# Query relationships
print(alice.orders())           # List of Alice's orders
print(alice.coffees())          # Unique coffees Alice ordered
print(latte.customers())        # [Alice, Bob]
print(latte.num_orders())       # 2
print(latte.average_price())    # 5.25

# Find top spender
top = Customer.most_aficionado(latte)  # Returns Bob
```

**Run demo:**
```bash
python3 -m coffee_shop.debug
```

## Class Documentation

### Customer
- **Property:** `name` (str, 1-15 characters)
- **Methods:**
  - `orders()` → List[Order]
  - `coffees()` → List[Coffee] (unique)
  - `create_order(coffee, price)` → Order
  - `most_aficionado(coffee)` → Customer | None (class method)

### Coffee
- **Property:** `name` (str, 3+ characters)
- **Methods:**
  - `orders()` → List[Order]
  - `customers()` → List[Customer] (unique)
  - `num_orders()` → int
  - `average_price()` → float

### Order
- **Properties (read-only):**
  - `customer` → Customer
  - `coffee` → Coffee
  - `price` → float ($1.00-$10.00)

## Testing

```bash
# Run all tests
pytest

# Verbose output
pytest -v

# Specific test file
pytest tests/test_customer.py
```

**Test coverage includes:**
- Input validation (types, lengths, ranges)
- Relationship methods (orders, coffees, customers)
- Aggregate calculations (num_orders, average_price, most_aficionado)
- Edge cases (empty lists, None returns)

## Learning Objectives

- Object-Oriented Programming (classes, properties, methods)
- Object relationships (one-to-many, many-to-many)
- Data validation and exception handling
- Property decorators and encapsulation
- Class variables and class methods
- Test-driven development with pytest

## Requirements

- Python 3.7+
- pytest

## FAQ

**Q: Why use `_all` class variables?**  
A: Track all instances to enable relationship queries across objects.

**Q: Why `@property` decorators?**  
A: Make attributes read-only after initialization to maintain data integrity.

**Q: Why lazy imports in `order.py`?**  
A: Avoid circular import issues between interdependent modules.

## Author

Linda Jerop

## Sources
Mostly from Canvas

## License

Educational project for learning purposes.
