class Card:
    number = "0000 0000 0000 0000"
    validDay = "01/99"
    holder = "unknnow"

    def __init__(self, number, day, holder):
        self.holder = holder
        self.validDay = day
        self.number = number
    
    def pay(self, amount):
        print("с карты", self.number, "списали", amount)
