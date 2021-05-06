from product import Product


class OrderItem:
    def __init__(self, product: Product, amount: float):
        self.product = product
        self.amount = amount
        self.order = None

    def __str__(self):
        return "[order=" + str(self.order) + "-product=" + str(self.product.id) + "-amount=" + str(self.amount) + "]"
