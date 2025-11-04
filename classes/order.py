from classes.customer import Customer

class Order:

    def __init__(self, customer, order_number):
        self.customer = customer
        self.order_number = order_number
        self.items = []
        self.status = "pending"
        self.total_price = 0

    def add_item(self, menu_item):
        self.items.append(menu_item)
        self.total_price += menu_item.price

    def remove_item(self, menu_item):
        self.items.remove(menu_item)
        self.total_price -= menu_item.price

    def get_total(self):
        return self.total_price

    def set_status(self, new_status):
        self.status = new_status

    def display_order(self):
        print(f"the customer: {self.customer}, order number: {self.order_number}, items: {self.items}, status: {self.status}, total price: {self.total_price}")

    def is_complete(self):
        if self.status == "delivered":
            return True