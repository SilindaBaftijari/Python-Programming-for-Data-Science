def read_file(file_path):
    list_of_lists = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            list_of_lists.append(data)
    return list_of_lists

def get_data(list_of_lines, year, gender, race):
    fatal_list = []
    for line in list_of_lines:
        if (
            line[0] == year
            and line[1].lower() == gender.lower()
            and line[2].lower() == race.lower()
        ):
            fatal_list.append(float(line[3]))
    return fatal_list

def covid_fatal(values):
    return sum(values)

# Specify the relative path to your data file
file_path = 'sanhose_covid_deaths.txt'

# Create a list variable called fatalities
fatalities = []

# Call the read_file() function
list_of_lines = read_file(file_path)

# Use get_data() to filter the data
fatalities.extend(get_data(list_of_lines, '2020', 'male', 'white'))
fatalities.extend(get_data(list_of_lines, '2020', 'male', 'hispanic'))
fatalities.extend(get_data(list_of_lines, '2021', 'male', 'white'))
fatalities.extend(get_data(list_of_lines, '2021', 'male', 'hispanic'))

# Call covid_fatal() to calculate the sum of fatalities
total_fatalities = covid_fatal(fatalities)

# Print the list of fatalities and total fatalities
print(f"List of fatalities: {fatalities}")
print(f"Total fatalities: {total_fatalities}")
