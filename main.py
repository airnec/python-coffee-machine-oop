from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: Create objects
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

is_on = True

# TODO: Check resources sufficient?
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")

    if choice == "off":
        is_on = False
    elif choice == "report":
        # TODO: Print reports
        money_machine.report()
        coffe_maker.report()
    else:
        drink = menu.find_drink(choice)
        # TODO: Process coins
        # TODO: Check transaction successful?
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)

