# Start resources
start_water = 300
start_milk = 200
start_coffee = 100
start_money = 0

class Beverage():
    def __init__(self, name, cost, consumption_water, consumption_milk, consumption_coffee):
        self.name = name
        self.cost = cost
        self.consumption_water = consumption_water
        self.consumption_milk = consumption_milk
        self.consumption_coffee = consumption_coffee


def check_money(beverage):
    print('Please insert coins.')
    quarters = float(input('how many quarters?: '))*0.25
    dimes = float(input('how many dimes?: '))*0.10
    nickles = float(input('how many nickles?: '))*0.05
    pennies = float(input('how many pennies: '))*0.01
    if quarters + dimes + nickles + pennies < beverage.cost:
        print("Sorry that's not enough money. Money refunded.")
    if quarters + dimes + nickles + pennies > beverage.cost:
        refund = (quarters + dimes + nickles + pennies) - beverage.cost
        format_refund = "{:.2f}".format(refund)
        print(f"Here is ${format_refund} in change.")
        print(f"Here is your {beverage.name} ☕️.Enjoy!")
    elif quarters + dimes + nickles + pennies == beverage.cost:
        print(f"Here is your {beverage.name} ☕️.Enjoy!")


def consumption(beverage):
    global start_water
    global start_milk
    global start_coffee
    global start_money
    if beverage == beverage1:
        start_water -= beverage1.consumption_water
        start_milk -= beverage1.consumption_milk
        start_coffee -= beverage1.consumption_coffee
        start_money += beverage1.cost
    if beverage == beverage2:
        start_water -= beverage2.consumption_water
        start_milk -= beverage2.consumption_milk
        start_coffee -= beverage2.consumption_coffee
        start_money += beverage2.cost
    if beverage == beverage3:
        start_water -= beverage3.consumption_water
        start_milk -= beverage3.consumption_milk
        start_coffee -= beverage3.consumption_coffee
        start_money += beverage3.cost


def critical_resources(beverage):
    global start_water
    global start_milk
    global start_coffee
    if beverage.consumption_water > start_water:
        print('Sorry there is not enough water')
    if beverage.consumption_milk > start_milk:
        print('Sorry there is not enough milk')
    if beverage.consumption_coffee > start_coffee:
        print('Sorry there is not enough coffee')

    # else:ca
        # ask_again = input("Sorry, I didn't understand you.\n What would you like? (espresso/latte/cappuccino): " )


def shut_down(ask_user):
    if ask_user == 'off' or ask_user == 'Off':
        exit()


def check_consumption_and_money(beverage):
    if beverage.consumption_milk <= start_milk and beverage.consumption_water <= start_water and beverage.consumption_coffee <= start_coffee:
        consumption(beverage)
        check_money(beverage)
    elif beverage.consumption_milk > start_milk or beverage.consumption_water > start_water or beverage.consumption_coffee > start_coffee:
        critical_resources(beverage)

beverage1 = Beverage('espresso', 1.5, 50, 0, 18)
beverage2 = Beverage('latte', 2.5, 200, 150, 24)
beverage3 = Beverage('cappuccino', 3.0, 250, 150, 24)

while True:
    ask_user = input('What would you like? (espresso/latte/cappuccino): ')
    if ask_user == 'espresso' or ask_user == 'Espresso':
        check_consumption_and_money(beverage1)
    if ask_user == 'latte' or ask_user == 'Latte':
        check_consumption_and_money(beverage2)
    if ask_user == 'cappuccino' or ask_user == 'Cappuccino':
        check_consumption_and_money(beverage3)
    if ask_user == 'report' or ask_user == 'Report':
        print(f'Water: {start_water}ml')
        print(f'Milk: {start_milk}ml')
        print(f'Coffee: {start_coffee}g')
        print(f'Money: ${start_money}')
    shut_down(ask_user)

# TODO 1. Implement low resources function




