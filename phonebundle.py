from noteultra import NoteUltra
from s20ultra import S20Ultra
from iphone12 import IPhone12

class PhoneBundle:
    def __init__(self, num_phones, budget):
        self.num_phones = num_phones
        self.budget = float(budget)
        self.amount_due = 0

    available_phones = ["note 20 ultra", "s20 ultra", "iphone 12"]
    # phone_classes refer to the class name of each available phone
    phone_classes = ["NoteUltra", "S20Ultra", "IPhone12"]

    def pick_phone(self, phone_name, storage, color):
        for phone in self.available_phones:
            phone_index = self.available_phones.index(phone)
            if phone_name == phone:
                class_name = self.phone_classes[phone_index]
                new_phone = eval(class_name)(storage, color)
                
                price = new_phone.get_current_price()
                self.add_phone_price(price)
           
    def add_phone_price(self, phone_price):
        self.amount_due += phone_price

    def check_budget(self):

        if self.num_phones == 1:
            print("Only one phone purchased, not eligible for discount.")
        elif self.num_phones >= 10:
            amount_saved = self.amount_due * 0.15
            self.amount_due = self.amount_due - amount_saved
            amount_saved = "{:.2f}".format(amount_saved)

            print(f"Maximum discount reached. Taking 15 percent off your original amount! You saved ${amount_saved}!")
        else:
            discount = (self.num_phones * 0.01) + 0.05
            amount_saved = self.amount_due * discount
            self.amount_due = self.amount_due - amount_saved
            amount_saved = "{:.2f}".format(amount_saved)

            print(f"You purchased {self.num_phones} phones for {int(discount * 100)} percent off your order. \
You saved ${amount_saved}!")
        
        difference = self.budget - self.amount_due
        difference = float("{:.2f}".format(difference))

        if difference >= 0:
            print(f"Congrats! You are within your budget with ${difference} to spare.")
        else:
            positive_difference = difference * -1
            positive_difference = "{:.2f}".format(positive_difference)

            print(f"You are ${positive_difference} overbudget.")

