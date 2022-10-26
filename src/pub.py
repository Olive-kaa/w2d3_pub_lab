class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink = []
    
    def increase_till(self, amount):
        self.till += amount

    def check_age(self, num):
        # if num >= 18:
        #     return "What would you like?"
        # else:
        #     return "Sorry, too young"
        if num >= 18:
            return "What would you like?"
        else:
            return "Sorry, too young"
        
