# Coffee Shop - Object Relationships

Simple Python domain model for a Coffee Shop with three main entities: `Customer`, `Coffee`, and `Order`.

Features:
- Validations for names and prices.
- Relationship methods: customers -> orders -> coffees and vice-versa.
- Aggregate methods: `num_orders`, `average_price`, and `most_aficionado`.

Run tests:

1. (Optional) create virtual environment and install pytest
```
pip install -r requirements.txt
```
2. Run pytest
```
pytest
```

Files:
- `coffee_shop/customer.py`
- `coffee_shop/coffee.py`
- `coffee_shop/order.py`
- `coffee_shop/debug.py` - small demo
- `tests/` - pytest test suite
