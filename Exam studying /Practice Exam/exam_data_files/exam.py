#1 Question Random and Modules (20 points: 6+7+7)
#In this task, we will create a python program that simulates tossing twenty-sided dice to determine a winner between 2 players. You can imagine this as a part of a digital game where a player can play a bonus card to increase their chance of winning.
#a. Create a function called dice_roller(sides, bonus) that rolls the dice that takes 2 parameters, the number of sides, and if the team has a bonus. Be sure to place this and the following functions in exam.py.
#b. Create a second function called game_play() for the gameplay that calls the dice_roller function for players with the following:
#monster rolls a 20-sided dice and has a bonus of +10
#team has 3 rolls
#First roll with an 8-sided dice and no bonus card
#Second roll with a 12-sided dice and a bonus card of +5
#Third roll with a dice of 6 and no bonus card
#Inside game_play() create a conditional statement (if ... then) to return the winners with the score and the losers with the score. Remember that monster or the team will win, requiring the if..then statement and 2 different print statements.
#return ('monster wins', monster, 'team loses', team)
#The output in the terminal should look like this: ('monster wins', 25, 'team loses', 11)
#c. From exam_test.py call the game_play() and print the result.

import random

def dice_roller(sides, bonus = 0):

    return random.randint(1, sides)
        
        
def game_play(): 
    monster_score = dice_roller(20,10) 
    
    team_score = dice_roller(8) + dice_roller(12,5) + dice_roller(6)
    
    if monster_score > team_score:
        return ('monster wins', monster_score, 'team loses', team_score)
    else:
        return ('team wins', team_score, 'monster loses', monster_score)


