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
}

def run_coffee_machine():
    run_machine = True
    def print_report():
        print(resources)
    while run_machine:
        coffee_choice = input("What would you like? Please select 'espresso' 'latte' or 'cappuccino'. ").lower()
        if coffee_choice == 'report':
            print_report()
        elif coffee_choice == 'espresso':
            
