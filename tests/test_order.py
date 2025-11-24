import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order


def setup_function():
    Customer._all.clear()
    Coffee._all.clear()
    Order._all.clear()


def test_order_validation():
    c = Customer("C")
    cf = Coffee("Latte")
    with pytest.raises(TypeError):
        Order("not a customer", cf, 3)
    with pytest.raises(TypeError):
        Order(c, "not a coffee", 3)
    with pytest.raises(TypeError):
        Order(c, cf, "3")
    with pytest.raises(ValueError):
        Order(c, cf, 0.5)
    with pytest.raises(ValueError):
        Order(c, cf, 11)


def test_order_properties_and_all():
    c = Customer("Zoe")
    cf = Coffee("Americano")
    o = Order(c, cf, 4.25)
    assert o.customer is c
    assert o.coffee is cf
    assert o.price == pytest.approx(4.25)
    assert Order.all() == [o]