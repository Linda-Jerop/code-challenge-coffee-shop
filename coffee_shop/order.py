from typing import List


class Order:
    _all: List['Order'] = []

    def __init__(self, customer, coffee, price: float):
        # import types lazily to avoid circular import issues in type checking
        from .customer import Customer
        from .coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("Order customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Order coffee must be a Coffee instance")
        if not isinstance(price, (int, float)):
            raise TypeError("Order price must be a number")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("Order price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order._all.append(self)

    def __repr__(self) -> str:
        return f"Order(customer={self.customer!r}, coffee={self.coffee!r}, price={self.price})"

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self) -> float:
        return self._price

    @classmethod
    def all(cls) -> List['Order']:
        return cls._all
