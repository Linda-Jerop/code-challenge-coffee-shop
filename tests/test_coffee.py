import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order


def setup_function():
    Customer._all.clear()
    Coffee._all.clear()
    Order._all.clear()


def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")


def test_orders_customers_and_stats():
    alice = Customer("Alice")
    bob = Customer("Bob")
    mocha = Coffee("Mocha")
    alice.create_order(mocha, 5.0)
    bob.create_order(mocha, 3.0)
    orders = mocha.orders()
    assert len(orders) == 2
    customers = mocha.customers()
    assert set(customers) == {alice, bob}
    assert mocha.num_orders() == 2
    assert pytest.approx(mocha.average_price(), rel=1e-6) == 4.0