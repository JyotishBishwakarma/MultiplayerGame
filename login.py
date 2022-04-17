import json
import os
import random
import time

path = 'players' #player data in this folder
if not os.path.exists(path):
  os.makedirs(path)

def login():
  question = input("Do you have an account y/n ")
  if question.lower() == 'n':
    signup()
  elif question.lower() == 'y':
    print("Please Enter you account information:\n")
    username = input("Username: ")
    password = input("Password: ")

    try:
      with open(os.path.join(path,username + ".json"), "r") as game:
        info = json.load(game)
      if info["username"] == username and info["password"] == password:
        print("Welcome to your game account", username.title() + "!\n")
        

        #saves current file
        with open("current_player.json","w") as file:
          json.dump(info, file)
          
      else:
        print("Incorrect username or password")
        forgetpwd = input("Did you forget password and want to reset?(y/n)")
        if forgetpwd.lower() == 'y':
          forgetpassword()
        else:
          login()

    except FileNotFoundError:
      print("We cannot find that account\nPlease try again")
      login()
      
    
  else:
    print("invalid choice")
    login()


def signup():
  print("Welcome to the game! Sign up for an account!")
  username = input("Please select a username ")
  password = input("Please choose a password ")
  security_question1 = "What is your favorite animal: "
  security_answer1 = input(security_question1)

  data = {}
  data["username"] = username
  data["password"] = password
  data["security_question1"] = security_question1
  data["security_answer1"] = security_answer1
  data["progress"] = 0
  data["health"] = 100
  data["items"] = []
  data["credit"] = 0
  data["start_time"] = time.time()
  data["last_login"] = time.time()
  data["money"]=0

  with open(os.path.join(path, username + ".json"),"w") as infile:
    data = json.dump(data,infile)

  print('Thanks for signing up, now you can login')

  login()
  
  
def forgetpassword():
  user = input("Enter your username: ")

  try:
    with open(os.path.join(path, user + ".json"), "r") as g:
      x = json.load(g)

    sa_user = input(x["security_question1"])

    if x["security_answer1"] == sa_user:
      #print(f'Your password is: {x["password"]}')
      new_password = input("Enter new password")
      confirm_password = input("Confirm password")
      reset(user,new_password, confirm_password)

    else:
      print('Wrong answer!!! Back to login')
      login()


  except FileNotFoundError:
    print("We cannot find that account\nPlease try again")
    login()

def reset(user, newpassword, confirmpassword):
  if newpassword == confirmpassword:
    with open(os.path.join(path, user + ".json"), "r") as game:
      x = json.load(game)
    x["password"] = newpassword

    with open(os.path.join(path, user + ".json"), "w") as game:
      json.dump(x,game)

    print('Password changed successfully. Please login now!!')
    login()
  else:
    print('Mismatch between new password and confirm password! Please try again')
    forgetpassword()





