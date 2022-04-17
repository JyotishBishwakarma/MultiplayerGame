import urllib.request 
import json 
from clear_screen import clear
import random 
import sys
from login import login,signup
import os
from termcolor import colored,cprint
from earn_money import earnmoney
from health import buyhealth
from weather import weather



#import login #turned it off for testing
#import os


login()
stones_to_be_collected = ["space", "mind", "soul","reality","time","power","ego"]
data = open("current_player.json","r")
current_player = json.loads(data.read())
health = current_player['health']
money = current_player['money'] 
items = current_player['items']

url = "https://raw.githubusercontent.com/JyotishBishwakarma/MultiplayerGame/main/data.json"
request = urllib.request.urlopen(url)
response = json.loads(request.read())

room = 0


#global health,money,items,room
while True:
  clear()
  cprint(f"You have {health}% health, ${money}, and these items: {items}\n", "green")
  print(f"You are located in {response[room]['name']}.")
  weather()
  print(response[room]["story"])

  for stone in stones_to_be_collected:
    if stone == response[room]["item"] and stone not in items:
      print(f'Bravo!! You found {response[room]["item"]} stone!! Collect this!!')
      items.append(response[room]["item"])
      cprint(f'Now you have {items} stones.','red')


  if len(items) == 7:
    cprint("Congrats!!! You collected all stones. Mission completed", "green")
    cprint("Thanks for playing!", "red")
    break


  if money <= 10:
    cprint('\nYour money is very low, so you cannot go to rooms to search infinity stones! GO AND EARN MONEY FIRST\n','red')
    money = earnmoney(money)

  if health <=25:
    cprint("\nYour health is very low! Go and be strong and come back!!","red")
    health = buyhealth(health,money)


  print(response[room]["nav"])

  try:
    choice = int(input("\nPlease make a selection: "))
  except ValueError:
    print('Invalid choice!!!')
    continue

  if choice == 1:
    room = response[room]["c1"] - 1

    money -= 5
    health -= 5
  elif choice == 2:
    room = response[room]["c2"] -1
    money -= 5
    health -= 5
  elif choice ==3:
    room = response[room]["c3"] -1
    money -= 5
    health -= 5
  else:
    print("Please make a valid choice")




  #open the file of the user playing now (current player)
  data = open("current_player.json","r")
  new = json.loads(data.read())

  new["progress"] = room
  new["health"] = health
  new["items"] = items
  new["money"] = money

  #dump the current player info
  with open("current_player.json", "w") as file:
    json.dump(new, file)

  #{"username": "sid", "password": "sid", "progress": 18, "health": 100, "items": [], "money": 0, "start_time": 1649363555.04086, "last_login": 1649363555.040861}

  path ="players"
  with open(os.path.join(path, new['username'] + ".json"), "w") as infile:
    json.dump(new, infile)




