# Finding the file
my_file = open("sanhose_covid_deaths.txt", "r")

# Reading the file
data = my_file.read()

# Splitting 
list_of_lines = data.split("\n")

# Iterating over the list of lines
for line in list_of_lines:
    line_pieces = line.strip().split()

    # Check if data, has "2021", and "Male"
    if len(line_pieces) > 1 and line_pieces[0].isdigit() and int(line_pieces[0]) == 2021 and "Male" in line:
        print(line)

