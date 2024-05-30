MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 20,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



is_on=True
profit=0
def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry!there is no enough {item}")
            return False
    return True
def money_cal():
    print("please insert coins:")
    total=int(input("enter number of 5 rupee coins "))*5
    total+=int(input("enter number of 2 rupee coins "))*2
    total+=int(input("enter number of 1 rupee coins "))*1
    return total


def transaction_successful(money_received,drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your {change} rupees change")
        global profit
        profit += drink_cost
        return True
    else:
        print("oops not enough money")
        return False

def order(coffee_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your {coffee_name}🍵.Enjoy!")

while is_on:
    choice=input("what would you like to order? (espresso/latte/cappuccino) ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water:{resources['water']} ml")
        print(f"Milk:{resources['milk']} ml")
        print(f"Coffee:{resources['coffee']} g")
        print(f"Money:{profit} rupees")
    else:
        drink=MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment=money_cal()
            if transaction_successful(payment,drink["cost"]):
                order(choice,drink["ingredients"])

