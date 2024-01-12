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


