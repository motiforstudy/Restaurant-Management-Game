class Staff:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.energy = 100

    def work(self):
        self.energy -= 10
        print(f"the energy level decrease by 10, and now is: {self.energy}")

    def rest(self):
        self.energy += 20
        if self.energy > 100:
            self.energy = 100

    def is_tired(self):
        if self.energy < 30:
            return True

    def get_info(self):
        return f"the name: {self.name}, the role: {self.role}, the salary: {self.salary}, the energy level: {self.energy}"