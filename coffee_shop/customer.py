from typing import List, Optional
from .order import Order
from .coffee import Coffee


class Customer:
    _all: List['Customer'] = []

    def __init__(self, name: str):
        self._name = None
        self.name = name
        Customer._all.append(self)

    def __repr__(self) -> str:
        return f"Customer(name={self.name!r})"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters")
        self._name = value

    @classmethod
    def all(cls) -> List['Customer']:
        return cls._all

    def orders(self) -> List[Order]:
        return [o for o in Order.all() if o.customer is self]

    def coffees(self) -> List[Coffee]:
        coffees = [o.coffee for o in self.orders()]
        # return unique preserving order
        seen = set()
        unique = []
        for c in coffees:
            if c not in seen:
                unique.append(c)
                seen.add(c)
        return unique

    def create_order(self, coffee: Coffee, price: float) -> Order:
        if not isinstance(coffee, Coffee):
            raise TypeError("create_order expects a Coffee instance")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee: Coffee) -> Optional['Customer']:
        if not isinstance(coffee, Coffee):
            raise TypeError("most_aficionado expects a Coffee instance")
        totals = {}
        for order in [o for o in Order.all() if o.coffee is coffee]:
            totals.setdefault(order.customer, 0.0)
            totals[order.customer] += order.price
        if not totals:
            return None
        # return customer with max total spent
        return max(totals.items(), key=lambda kv: kv[1])[0]
