class Pub:
    
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.stock = [self.drinks]

    def add_money(self, drink):
        self.till += drink.price

    def is_of_age(self, customer):
        # Return true if customer age >= 18
        return customer.age >= 18

    def refuse_service(self, customer):
        return customer.drunk_level > 5

    def stock_value(self, all_drinks):
        # Calculate the price * stock level
        total = 0
        for drink in all_drinks:
            value = drink.price * drink.stock_level
            total += value
        return total