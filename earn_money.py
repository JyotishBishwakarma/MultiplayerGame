import random
from termcolor import colored,cprint 

def earnmoney(money):
    earn_more ='y'
    while earn_more == 'y':
        random_num = random.randint(1,3)

        cprint("This is guessing game. Guess the correct number between 1 to 3!!! If you guess right you will earn money!!","blue")
        user_num = int(input("Enter your number: "))
        if (random_num == user_num):
            cprint('Congrats!!! You guessed correct. You will get $50 as cash prize!!!','green')
            money += 50

        else:
            cprint('Thats a wrong guess!! No money for that!!!','red')

        cprint(f'Your new total money is ${money}','green')
        earn_more = input('Do you want to try again and earn more cash? (y/n): ')

    return money


