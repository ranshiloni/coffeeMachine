MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


should_continue = True


def turn_off():
    print("Ok, Bye")
    global should_continue
    should_continue = False


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}mg")
    print(f"Money: £{resources['money']}")


def inventory_check(coffee):
    """ returns true if there's enough resources for the coffee"""
    for ingredient in MENU[coffee]['ingredients']:
        enough_resources = True
        # Iterate on each resource found in the drink and make sure it is not insufficient
        if resources[ingredient] - MENU[coffee]['ingredients'][ingredient] < 0:
            print(f'Sorry, not enough {ingredient}')
            enough_resources = False
        return enough_resources


def get_them_coins(coffee):
    count = 0.0
    change = 0.0
    count += 0.25 * int(input("How Many Quarters? 🪙"))
    count += 0.10 * int(input("How Many Dimes? 🪙"))
    count += 0.01 * int(input("How Many penny? 🪙"))
    print(count)

    if count == MENU[coffee]['cost']:
        resources['money'] += MENU[coffee]['cost']
        return True
    elif count > MENU[coffee]['cost']:
        resources['money'] += MENU[coffee]['cost']
        change = str(round(count - MENU[coffee]['cost'], 2))
        print(f"You've inserted too much money, here's {change} change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def deduct_resources(coffee):
    for ingredient in MENU[coffee]['ingredients']:
        resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]


while should_continue:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'latte' or user_choice == 'cappuccino' or user_choice == 'espresso':
        if inventory_check(user_choice):
            if get_them_coins(user_choice):
                deduct_resources(user_choice)
                print(f"Here's your {user_choice}, Enjoy! ☕️")
    if user_choice == 'report':
        report()
    if user_choice == 'off':
        turn_off()



