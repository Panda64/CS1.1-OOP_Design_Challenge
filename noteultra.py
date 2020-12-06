
class NoteUltra:
    def __init__ (self, storage, color):
        self.storage = storage
        self.color = color
        self.price = float(0)
        self.validate_choices()

    storage_options = ["128gb", "512gb"]
    storage_prices = [1299.99, 1399.99]
    available_colors = ["mystic bronze", "mystic black", "mystic white"]

    # This method makes sure that the options that were passed are valid available options of the phone
    def validate_choices(self):

        for option in self.storage_options:
            storage_index = self.storage_options.index(option)
            if self.storage == option:
                self.price = self.storage_prices[storage_index]
        
        if self.storage not in self.storage_options:
            self.storage = "Invalid"
            print("Error. Invalid storage size entered. You will not be charged for this phone. Try again.")

        if self.color not in self.available_colors:
            self.color = "Invalid"
            self.price = 0
            print("Error. Invalid color entered. You will not be charged for this phone. Try again.")

        if self.storage in self.storage_options and self.color in self.available_colors:
            self.view_selection()

    def get_current_price(self):
        return self.price

    def view_selection(self):
        print(f"You have purchased a Samsung Galaxy Note 20 Ultra 5G \
(Storage: {self.storage}) (Color: {self.color}) for ${self.price}")


    