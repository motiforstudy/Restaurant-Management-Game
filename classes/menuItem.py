class MenuItem:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.available = True

    def get_info(self):
        return f"name: {self.name}, price: {self.price}, category: {self.category}"

    def set_available(self, status):
        self.available = status

    def is_available(self):
        if self.available:
            return True
        else:
            return False