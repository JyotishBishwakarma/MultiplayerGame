import random

def earnmoney(money):
    earn_more ='y'
    while earn_more == 'y':
        random_num = random.randint(1,3)

        print("This is guessing game. Guess the correct number between 1 to 3!!! If you guess right you will earn money!!")
        user_num = int(input("Enter your number: "))
        if (random_num == user_num):
            print('Congrats!!! You guessed correct. You will get $50 as cash prize!!!')
            money += 50

        else:
            print('Thats a wrong guess!! No money for that!!!')

        print(f'Your new total money is ${money}')
        earn_more = input('Do you want to try again and earn more cash? (y/n): ')

    return money


