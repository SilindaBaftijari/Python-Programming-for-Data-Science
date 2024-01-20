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


#2 Question List of List / For Loops (25 points: 5+10+10)
#In this task, we need to transpose (switch the rows and the columns if thinking about a table) the dia_list (See below or get here). The transposition of a list of lists (matrix) is a new list of lists (matrix) where the rows of the original become the columns, and the columns become the rows.
#Once you have transposed the matrix, we create a new matrix with the PatientNumber, BMI, and Outcome. However, we also need to change the 1 and 0 integers to strings positive and negative.
#a. Start with creating and copying the dia_list in the exam.py (see below)
#b. In exam.py create a function called transpose_list() that uses a for loop (comprehension not allowed) to transpose items and the subitems from a "9x19" matrix to a "19x9" matrix.
#Name the new list transposed_new
#Remember to make a nested loop for the items and subitems. Use the following names:
#Create a for loop inside another for loop
#For the first loop, the item is the variable.
#For the second loop, use for subitem in...
#From exam_test.py, print out the third, fourth, and fifth items of the transposed_new list.
#c. Create a second function in  exam.py for get_patients() that takes the transposed_new list and extracts PatientNumber, BMI, and Outcome.
#Name this new list age_bmi
#Create the loop with for rows in... for the extraction
#Use a conditional statement that tests if Outcome is an integer of 1 and 0 and converts to positive and negative with 1 being positive.
#d. From exam_test.py call get_patients() and print the result.

import numpy as np

dia_list=[
['PatientNumber',14568,22368,30168,37968,45768,53568,61368,69168,76968,84768,92568,50368,18168,15968,33768,41315,39368,14168,54968],
['Glucose',148,85,183,89,137,116,78,115,197,125,110,168,139,189,166,100,118,107,103],
['BloodPressure',72,66,64,66,40,74,50,0,70,96,92,74,80,60,72,0,84,74,30],
['SkinThickness',35,29,0,23,35,0,32,0,45,0,0,0,0,23,19,0,47,0,38],
['Insulin',0,0,0,94,168,0,88,0,543,0,0,0,0,846,175,0,230,0,83],
['BMI',33.6,26.6,23.3,28.1,43.1,25.6,31,35.3,30.5,0,37.6,38,27.1,30.1,25.8,30,45.8,29.6,43.3],
['DiabetesPedigreeFunction',0.627,0.351,0.672,0.167,2.288,0.201,0.248,0.134,0.158,0.232,0.191,0.537,1.441,0.398,0.587,0.484,0.551,0.254,0.183],
['Age',50,31,32,21,33,30,26,29,53,54,30,34,57,59,51,32,31,31,33],
['Outcome',1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0]]


# b. transpose_list function
def transpose_list(matrix):
    transposed_new = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed_new.append(transposed_row)
    return transposed_new

# c. get_patients function
def get_patients(transposed_matrix):
    age_bmi = []
    for row in transposed_matrix:
        if row[0] in ['PatientNumber', 'BMI', 'Outcome']:
            # Modify Outcome to positive/negative
            if row[0] == 'Outcome':
                row = ['positive' if x == 1 else 'negative' if x == 0 else x for x in row]
            age_bmi.append(row)
    return age_bmi