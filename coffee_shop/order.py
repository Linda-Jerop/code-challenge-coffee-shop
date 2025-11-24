from typing import List


class Order:
    _all: List['Order'] = []  # Class variable to track all Order instances

    def __init__(self, customer, coffee, price: float):
        from .customer import Customer  # Import here to avoid circular dependency
        from .coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("Order customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Order coffee must be a Coffee instance")
        if not isinstance(price, (int, float)):
            raise TypeError("Order price must be a number")
        if not (1.0 <= float(price) <= 10.0):  # Price must be between $1.00 and $10.00
            raise ValueError("Order price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order._all.append(self)  # Add this order to the class-level list

    def __repr__(self) -> str:
        return f"Order(customer={self.customer!r}, coffee={self.coffee!r}, price={self.price})"

    @property  # Makes customer read-only
    def customer(self):
        return self._customer

    @property  # Makes coffee read-only
    def coffee(self):
        return self._coffee

    @property  # Makes price read-only
    def price(self) -> float:
        return self._price

    @classmethod
    def all(cls) -> List['Order']:
        return cls._all
