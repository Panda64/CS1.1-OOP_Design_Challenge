
class NoteUltra:
    def __init__ (self, storage, color):
        self.storage = storage
        self.color = color
        self.price = float(0)
        self.validate_choices()
        self.view_selection()

    def validate_choices(self):
        storage1 = "128gb"
        storage2 = "512gb"

        color1 = "mystic bronze"
        color2 = "mystic black"
        color3 = "mystic white"

        low_storage_price = 1299.99
        high_storage_price = 1399.99

        if self.storage == storage1:
            self.price = low_storage_price
        elif self.storage == storage2:
            self.price = high_storage_price
        else:
            self.storage = "Invalid"
            print("Error. Invalid storage size entered. You will not be charged for this phone. Try again.")

        if self.color != color1 and self.color != color2 and self.color != color3:
            self.color = "Invalid"
            self.price = 0
            print("Error. Invalid color entered. You will not be charged for this phone. Try again.")

        return self.price

    def view_selection(self):
        print(f"You have purchased a Samsung Galaxy Note 20 Ultra 5G \
(Storage: {self.storage}) (Color: {self.color}) for ${self.price}")


    