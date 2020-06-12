# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:03:21 2020

@author: Thamsanqa
"""
import os
import sys
#This is a random module that will allow us to pick any side of the dice randomly
import random
#Welcoming the user 
print("Welcome to the ROLLING DICE SIMULATOR, enjoy the program")
diceRoll = random.randint(1, 6)
print(diceRoll)
limit = 0

def close_restart(self, csvfile):
    choice = input("Do you want to restart the program?")
    
    if choice == "YES" or choice == "NO" :
        print("Restarting now")
        os.execl(sys.executable, sys.executable, *sys.argv)
        
    else:
        print("Thank you for playing the game")
    
#While loop to keep on rolling the dice until no condition is met or until you have reached the limit
while limit <= 4:
    #This ask the input from the user
    ask = input("Do you want to roll again?Yes/No ").upper()#The .upper method will convert all the lowercase characters and returns the original string
    limit = limit + 1
    #This if statement checks the condition, if the user type yes it will print the random number
    if ask == "YES":
        print(random.randint(1, 6))
        #This elif statement is simple there if the condition is no/false it will stop printinf the number
    elif ask == "NO":
        print("Thank You.")
        #If the user types NO the game will break/stop
        break
    else:
        print("Thank You.")
        break
else:
    #This will print if the user has reached the limit of playing
    print("You have reached your limit please try again.")
