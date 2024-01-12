#Problem Sets

#Create a python filed called coffee_count.py remember to save it in a directory that you 
# will use for the course. Initialize a varaible called coffee_cups = 0 , set the value to 0 as
# shown. Now we will create a for loop with a range() of 4 use coffee_count as iteration value in the loop.

# Make 2 print() statements to output to terminal with the variables coffee_count and coffee_cups . 
# Finally make a print() statement that prints out this Today, drank 5 cups of coffee today. in the terminal

#Coffee Count down 
coffee_cups =0

for coffee_count in range(1,5):
    coffee_cups=coffee_cups+1
print(coffee_count)
print('Today i drank', coffee_count, 'cups of coffee')

#Your mission is to tinker with this code
#1. Change the integer in coffee_cups to 1 for instance
#2. Change the range() function to range(0,8) , what happens = you get 7 cups instead of 4
#3. Make an error like this print("Today, I drank " + coffee_cups + " cups of coffee") = typeerror, 

#Coffee Count down 
coffee_cups =1

for coffee_count in range(0,8):
    coffee_cups=coffee_cups+1
print(coffee_count)

#Exercise: Pet Happiness
#1. Initialize two variables, one an integer and the other a string. The integer is named dog_needs and the
#starting value to 0 . The string is name dog_mode, and set the value to "happy"
#2. Create a for loop with a range(1,5) and increase the dog_needs variable by 1
#3. Make a print statement that outputs My dog was outside 4 times today, and is happy in the terminal.
#4. Remember the need for the : in the for loop and to indent the code block.
#5. You can copy the "Coffee Countdown to start".
#6. On Wednesday we work with CodeGrade assingment tool.

dog_needs=0
dog_mode = "happy"

for dog_walks in range(1,5):
    dog_needs = dog_needs + 1
print("My dog was outside " +str(dog_needs) + " times today, and is " + dog_mode)


donut_box = "closed"
coffee_cup = "open"
off_work = True

if donut_box == "open" or coffee_cup == "open":
    print("Kicking back like Homer")
else:
    print("Working hard like Lisa")


# donuts
donut_box = "closed"
coffee_cup = "open"
work_status = False
if donut_box == "open" or coffee_cup == "open":
    if work_status:
        print("Kicking back like Homer at work")
    else:
        print("TV and sofa")
else:
    print("Working hard like Lisa")

#Your Task: Make a bigger holiday tree 
#Explain to your peer what it does and how you would expand it 6 rows to make a tall tree. 

for i in range(3):
    print(' ' * (2 - i) + '*' * (2 * i + 1))

# What happens with the `range(3)? At what number does it start = loop iterates 3 times, creating 3 layers of the tree. 
# What does ' ' * (2 - i) do = creates the necessary spaces on the left to center the stars. 
# What happens with '*' * (2 * i + 1) = creates the stars in the tree. The number of stars increases with each layer to form the tree shape
# What happens as the loop progresses = the tree forms 

#Your task now is to increase the range() to 7 iterations and add a trunk to the bottom of the tree. 

for i in range(7):
    print(' ' * (6 - i) + '*' * (2 * i + 1))
print(" "*5+"**")




#Human needs with a run-time error
dog_needs = 0
human_mode = "happy"
dog_accident = 1

for dog_walks in range(1, 5):
    dog_needs = dog_needs + 1
    
dog_needs = dog_needs/dog_accident

print("My dog was outside " + str(dog_needs) + " times today, and the owner is " + human_mode)

dog_accident = input("enter YES if the dog had an accident ")

if dog_accident == "YES": 
    human_mode = "sad"
    print("My dog was outside " + str(dog_needs) + " times today, and the owner is " +
human_mode)
else :
    print("My dog was outside " + str(dog_needs) + " times today, and the owner is " + human_mode )
