from datetime import date

from order_item import OrderItem
from product import Product
from order import Order

p = Product(1, 'Smartphone', 500)

print("New Product: " + str(p))

item = OrderItem(p, 1)

order = Order(1, str(date.today()))
order.add_item(item)

print("Item added: " + str(item))

print("New Order: " + str(order))

