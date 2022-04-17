from earn_money import earnmoney
import urllib.request
import json
from termcolor import colored,cprint 

def buyhealth(health,money):
    print("money",money)
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    cprint('This is health center. You can drink our special cocktail to boost your health. But you can buy only if you have $50 or more money with you','green')

    if money<50:
        cprint('You do not sufficient money to buy health. Go and EARN money first!!!','red')
        earnmoney(money)
    else:
        spend = int(input("How much money do you want to spend to buy health. Here are the prices:\n1.$20 for 50% health\n2.$30 for 75% health\n3.$40 for 100% health\n:"))
        if spend == 20 or spend == 1:
            cprint(f"Here is your energy cocktail: {result['drinks'][0]['strDrink']}","green")
            cprint(f"Please follow following instructions and drink it to boost health: {result['drinks'][0]['strInstructions']}","green")
            health = 50
            money -= 20
        elif spend == 30 or spend == 2:
            print(f"Here is your energy cocktail: {result['drinks'][0]['strDrink']}")
            print(f"Please follow following instructions and drink it to boost health: {result['drinks'][0]['strInstructions']}")
            health = 75
            money -= 30
        elif spend == 40 or spend ==3:
            print(f"Here is your energy cocktail: {result['drinks'][0]['strDrink']}")
            print(f"Please follow following instructions and drink it to boost health: {result['drinks'][0]['strInstructions']}")
            health = 100
            money -= 40
        else:
            cprint("Enter valid amount!!","red")




    print(f'Your new health is: {health}%','green')
    return health