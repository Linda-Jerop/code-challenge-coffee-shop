import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order


def setup_function():
    Customer._all.clear()
    Coffee._all.clear()
    Order._all.clear()


def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("a" * 16)


def test_create_order_and_coffees_orders():
    c = Customer("Sam")
    coffee = Coffee("Espresso")
    o = c.create_order(coffee, 3.5)
    assert isinstance(o, Order)
    assert o.customer is c
    assert o.coffee is coffee
    assert c.orders() == [o]
    assert c.coffees() == [coffee]


def test_most_aficionado():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")
    alice.create_order(latte, 4.0)
    alice.create_order(latte, 4.5)
    bob.create_order(latte, 10.0)
    # bob spent more
    assert Customer.most_aficionado(latte) is bob