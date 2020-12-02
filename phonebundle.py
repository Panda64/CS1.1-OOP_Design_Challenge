from noteultra import NoteUltra

class PhoneBundle:
    def __init__(self, num_phones, budget):
        self.num_phones = num_phones
        self.budget = float(budget)
        self.amount_due = 0

    def pick_phone(self, phone, storage, color):
        pass
        
           

    def check_budget(self):

        if self.num_phones == 1:
            print("Only one phone purchased, not eligible for discount.")
        elif self.num_phones >= 10:
            amount_saved = self.amount_due * 0.15
            self.amount_due = self.amount_due - amount_saved

            print(f"Maximum discount reached. Taking 15 percent off your original amount! You saved ${amount_saved}!")
        else:
            discount = (self.num_phones * 0.01) + 0.05
            amount_saved = self.amount_due * discount
            self.amount_due = self.amount_due - amount_saved

            print(f"You purchased {self.num_phones} phones for {discount * 10} percent off your order. You saved ${amount_saved}!")
        
        difference = self.budget - self.amount_due

        if difference >= 0:
            print(f"Congrats! You are within your budget with ${difference} to spare.")
        else:
            positive_difference = difference * -1

            print(f"You are ${positive_difference} overbudget.")