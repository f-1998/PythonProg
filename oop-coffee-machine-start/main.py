from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


cm = CoffeeMaker()
m = Menu()
mon = MoneyMachine()


shop = True
while shop:
    print(m.get_items())
    inp = input(f"Choice among {m.get_items()}").lower()
    if inp == "off":
        break

    elif inp == "report":
        cm.report()
        print()
        mon.report()
        break

    elif inp == "espresso" or inp == "latte" or inp == "cappuccino":
        drink = m.find_drink(inp)
        if cm.is_resource_sufficient(drink):
            if mon.make_payment(drink.cost):
                cm.make_coffee(drink)

    else:
        print("Enter a valid option")
