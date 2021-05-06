from order_status import OrderStatus
from order_item import OrderItem


class Order:
    def __init__(self, id: int, created_at: str):
        self.id = id
        self.created_at = created_at
        self.status = OrderStatus.NEW
        self.items = []

    def add_item(self, item: OrderItem):
        item.order = self
        self.items.append(item)
        return len(self.items)

    def __str__(self):
        return "[id=" + str(self.id) + "-created_at=" + self.created_at + "-status=" + str(self.status) + "-items_size=" + str(len(self.items)) + "] "
