from earn_money import earnmoney
import urllib.request
import json

def buyhealth(health,money):
    print("money",money)
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    print('This is health center. You can drink our special cocktail to boost your health. But you can buy only if you have $50 or more money with you')

    if money<50:
        print('You do not sufficient money to buy health. Go and EARN money first!!!')
        earnmoney(money)
    else:
        spend = int(input("How much money do you want to spend to buy health. Here are the prices:\n1.$20 for 50% health\n2.$30 for 75% health\n3.$40 for 100% health\n:"))
        if spend == 20 or spend == 1:
            print(f"Here is your energy cocktail: {result['drinks'][0]['strDrink']}")
            print(f"Please follow following instructions and drink it to boost health: {result['drinks'][0]['strInstructions']}")
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
            print("Enter valid amount!!")




    print(f'Your new health is: {health}%')
    return health