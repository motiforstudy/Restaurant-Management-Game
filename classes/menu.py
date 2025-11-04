class Menu:

    def __init__(self):
        self.list_of_items = []

    def add_item(self, menu_item):
        self.list_of_items.append (menu_item)

    def remove_item(self, item_name):
        for item in self.list_of_items:
            if item.name == item_name:
                self.list_of_items.remove(item)

    def get_item_by_name(self, name):
        for item in self.list_of_items:
            if item.name == name:
                return item
            else:
                return "the itrm isn't in the menu"

    def get_item_by_category(self, category):
        list_of_spaecific_category = []
        for item in self.list_of_items:
            if item.category == category:
                list_of_spaecific_category.append(item)
        return list_of_spaecific_category

    def display_menu(self):
        for item in self.list_of_items:
            print(item.get_info())

    def get_total_items(self):
        return len(self.list_of_items)