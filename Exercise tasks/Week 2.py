#Exercise  
# Create three variables. One called firstname with your first name, 
# one called lastname with your last name and one called age with your age. 
# Merge them into one string, which should look like:"


firstname = "silinda" 
lastname = "baftijari" 
age = 21

print("Name:" + firstname+ " "+ lastname + "\nAge: " + str(age) )


# Nov 27 Exercise Problems
#Create a folder named myfolder. Under the folder, create a text file called hello.txt, and write 5 lines 
# of text. A single word on each line is enough. Create a new program called file_test.py. In this 
# program, use the open function to read the hello.txt file. Read its content into a list of strings. Print 
# the last two lines to screen



#Lab exercise: in a computer program, when a variable has more than one words, you cannot leave
#spaces between the different words when creating it. So there are different ways available to combine
#them in different programming languages
# 
# Write a program that converts snake case string to kebab, pascal and camel cases. The snake case
# string should be assigned to variable snake_case_str and the converted strings should be saved at 
# kebab_case_str, pascal_case_str and camel_case_str, respectively.


snake_case_str = 'number_of_donuts' 

kebab_case_str = 'number-of-donuts'
pascal_case_str = 'NumberOfDonuts' # Challenging
camel_case_str = 'numberOfDonuts' # Challenging

# kebab conversion
kebab_case_str = snake_case_str.replace('_','-')
# pascal conversion
pascal_case_str = snake_case_str.replace('_',' ').title().replace(' ','')
# camel conversion
camel_case_str = pascal_case_str[0].lower() + pascal_case_str[1:]

print(kebab_case_str, pascal_case_str, camel_case_str)


#Nov 29 Exercise Problems 

#1. I want to calculate the average of 4 and 6. What's wrong with the following expression:
#4+6 / 2 

x = (4+6)/2 
print(x) 

x = 4
x += 1
x //= 2
x **= 2
x %= 5
print(x)


#Lab exercise: Chinese Zodiac Year
#Chinese zodiac years are represented by 12 animals. Each Chinese lunar year in the repeating zodiac
#cycle of 12 years is represented by a zodiac animal.
#The order of animals in a zodic cycle: Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig.
#The corresponding years for each zodiac:

#Task: reformatting your birth date and calculating your Chinese Zodiac sign

birth_date = input('Please type in your birth date:')

birth_date_dmy = birth_date.split('/')
year = int(birth_date_dmy[2])
month = int(birth_date_dmy[1])
day = int(birth_date_dmy[0])

zodiacs = ['Rat', 'Ox', 'Tiger', 'Rabbit',
'Dragon', 'Snake', 'Horse','Goat',
'Monkey', 'Rooster', 'Dog', 'Pig']

zodiac = zodiacs[(year - 1996) % 12]

month_abbrevs = ['Jan','Feb','Mar','Apr',
'May','Jun', 'Jul','Aug',
'Sep','Oct', 'Nov','Dec']

month_abbrev = month_abbrevs[month-1]

print(f'You were born on {day} {month_abbrev} {year}. Your chinese zodiac sign is: {zodiac}')

