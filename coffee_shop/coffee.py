from typing import List, Optional
from .order import Order


class Coffee:
    _all: List['Coffee'] = []  # Class variable to track all Coffee instances

    def __init__(self, name: str):
        self._name = None
        self.name = name  # Use setter to validate name
        Coffee._all.append(self)

    def __repr__(self) -> str:
        return f"Coffee(name={self.name!r})"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        if len(value) < 3:  # Minimum length of 3 characters
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = value

    @classmethod
    def all(cls) -> List['Coffee']:
        return cls._all

    def orders(self) -> List[Order]:
        return [o for o in Order.all() if o.coffee is self]

    def customers(self) -> List['Customer']:  # Returns unique customers who ordered this coffee
        customers = [o.customer for o in self.orders()]
        seen = set()  # Track customers we've seen to maintain uniqueness
        unique = []
        for c in customers:
            if c not in seen:
                unique.append(c)
                seen.add(c)
        return unique

    def num_orders(self) -> int:
        return len(self.orders())

    def average_price(self) -> Optional[float]:
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(o.price for o in orders) / len(orders)  # Sum all prices and divide by count
