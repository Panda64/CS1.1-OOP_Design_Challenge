from noteultra import NoteUltra

class IPhone12(NoteUltra):
    storage_options = ["64gb", "128gb", "256gb"]
    storage_prices = [799, 849, 949]
    available_colors = ["white", "black", "blue", "green", "(product)red"]

    def view_selection(self):
        print(f"You have purchased an iPhone 12 \
(Storage: {self.storage}) (Color: {self.color}) for ${self.price}")