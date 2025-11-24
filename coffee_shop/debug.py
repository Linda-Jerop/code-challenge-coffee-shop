"""Simple interactive debug/demo for the coffee_shop models."""
from .customer import Customer
from .coffee import Coffee


def demo():
    # reset any previous state if demo re-run in same process
    Customer._all.clear()
    Coffee._all.clear()
    from .order import Order
    Order._all.clear()

    alice = Customer("Alice")
    bob = Customer("Bob")

    latte = Coffee("Latte")
    mocha = Coffee("Mocha")

    alice.create_order(latte, 4.5)
    alice.create_order(mocha, 5.0)
    bob.create_order(latte, 3.5)
    bob.create_order(latte, 6.0)

    print("Customers:", Customer.all())
    print("Coffees:", Coffee.all())
    print("Latte orders:", latte.orders())
    print("Latte customers:", latte.customers())
    print("Latte num orders:", latte.num_orders())
    print("Latte avg price:", latte.average_price())
    print("Most aficionado for Latte:", Customer.most_aficionado(latte))


if __name__ == "__main__":
    demo()
