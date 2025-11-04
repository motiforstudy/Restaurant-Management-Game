from classes.staff import Staff
from classes.order import Order

class Waiter(Staff):

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.name = name
        self.salary = salary
        self.tips = 0

    def take_order(self, customer, menu):
        order = Order(customer, 1)
        create_order = input("please make your order: ")
        return create_order

    def serve_order(self, order):
        