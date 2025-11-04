class Customer:

    def __init__(self, name):
        self.name = name
        self.satisfaction = 50

    def increase_satisfaction(self, amount):
        if 101 > amount > 0:
            temp_satisfaction = self.satisfaction + amount
            if temp_satisfaction > 100:
                print("the score should be between 0 to 100")
            else:
                self.satisfaction += amount
        else:
            print ("please enter a number between 0 to 100")

    def decrease_satisfaction(self, amount):
        if 101 > amount > 0:
            temp_satisfaction = self.satisfaction - amount
            if temp_satisfaction < 0:
                print("the score should be between 0 to 100")
            else:
                self.satisfaction -= amount
        else:
            print ("please enter a number between 0 to 100")

    def is_happy(self):
        if self.satisfaction > 70:
            return True

    def get_info(self):
        return f"the customer name: {self.name}, his satisfaction = {self.satisfaction}"