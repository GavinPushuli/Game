# -*- coding: utf-8 -*-
"""
updated on Fri Jun 12 09:57:27 2020

@author: Gavin T Pushuli
"""

import random
import time

min = 1
max = 6
# These are my Global Variables

roll_again = True

while roll_again:
    print("Rolling Dice")
    time.sleep(random.randint(1, 3))    #Wait 3 Seconds for the dice to roll
    result = random.randint(min, max)
    print(result)
    roll_again = False
    GoAgain = input("Roll Again :(y or n)? :").lower()             #option to choose whether you want to play the game
    while GoAgain not in ["y", "n"]:GoAgain = input("BAD MOVE, Try Again : ").lower()
    if GoAgain == "y":          #after declaring you want to play the game, choose y or n . Any other character is invalid
        roll_again = True
    elif GoAgain == "n":
        roll_again = False
    print("FANTASTIC...!!!")