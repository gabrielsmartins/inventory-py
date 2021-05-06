class Product:
    def __init__(self, id: int, description: str, amount: float):
        self.id = id
        self.description = description
        self.amount = amount

    def __str__(self):
        return "[id=" + str(self.id) + "-description=" + self.description + "-amount=" + str(self.amount) + "]"
