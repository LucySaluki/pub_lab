class Customer:

    def __init__(self, name, wallet, age, drunk_level):
        self.name = name
        self.wallet = wallet
        self.drinks = []
        self.age = age
        self.drunk_level = drunk_level

    def buy_drink(self, drink_name):
        # Reduce money in customer wallet by drink price
        if self.wallet >= drink_name.price:
            self.wallet -= drink_name.price

    def increase_drunk_level(self, drink):
        # Increase drunk_level by drink alcohol level
        self.drunk_level += drink.alcohol_level

    def reduce_drunk_level(self, food):
        # Reduce customer drunk_level by food rejuv_level
        self.drunk_level -= food.rejuv_level
