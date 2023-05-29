from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()
run_machine = True

while run_machine:
    choices = menu.get_items()
    order = input("​What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        run_machine = False
    elif order == "report":
        coffeeMachine.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(order)
        if coffeeMachine.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMachine.make_coffee(drink)
