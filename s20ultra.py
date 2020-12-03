from noteultra import NoteUltra

class S20Ultra(NoteUltra):

    def validate_choices(self):
        super().validate_choices()
        
        color1 = "cosmic grey"
        color2 = "cosmic black"

        if self.color != color1 and self.color != color2:
            self.color = "Invalid"
            self.price = 0
            print("Error. Invalid color entered. You will not be charged for this phone. Try again.")

        


