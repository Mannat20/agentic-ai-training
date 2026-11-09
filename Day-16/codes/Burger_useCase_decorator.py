class Burger:
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def show(self):
        print(f'{self.name} | {self.price}')

# Decorator Design pattern
class MealDecorator:
    
    def __init__(self,burger):
        self.burger = burger
        self.burger.price += 100
        
    def show(self):
        self.burger.show()
        print('Burger Upgraded to Meal with Fries and Coke')
        
burger1 = Burger(name='McVeggie',price=150)
burger1.show()

meal = MealDecorator(burger=burger1)
meal.show()