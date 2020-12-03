from noteultra import NoteUltra

class S20Ultra(NoteUltra):
    available_colors = ["cosmic grey", "cosmic black"]

    def view_selection(self):
        print(f"You have purchased a Samsung Galaxy S20 Ultra 5G \
(Storage: {self.storage}) (Color: {self.color}) for ${self.price}")


