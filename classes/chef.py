from classes.staff import Staff

class Chef(Staff):

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.name = name
        self.salary = salary
        self.specialty = "italian"

    def work(self):
        self.energy -= 15
        print(f"the energy level decrease by 15, and now is: {self.energy}")

    def cook_order(self, order):
        self.order.status = "cooking"
        self.order.status = "ready"
        self.work()