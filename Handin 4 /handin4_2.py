import csv

def read_csv_to_list(file_path):
    list_of_rows = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Skip lines that don't have the expected number of columns
            if len(row) < 5:
                continue
            # Skip lines that start with '%'
            if row[0].startswith('%'):
                continue

            value, year, race, gender = row[1], row[2], row[3], row[4]
            list_of_rows.append(['Drug Overdose Deaths', value, year, race, gender])
    return list_of_rows


def calculate_deaths(total):
    sum_fatal_rates = sum(total)
    result = round(sum_fatal_rates * 900000 / 100000)
    return result

def get_data(year, gender, race, data): 
    fatal_list = []
    year = str(year)
    
    for line in data:
        if line[2] == year and line[3].lower() == race.lower() and line[4].lower() == gender.lower():
            fatal_list.append(float(line[1]))
    return fatal_list


def get_started():
    list_of_rows = read_csv_to_list('san_jose_drug.csv')
    arguments = [(2017, "Male", "White"), (2017, "Male", "Black"), (2019, "Male", "White"), (2019, "Male", "Black")]

    for year, gender, race in arguments:
        fatal_rate_total = get_data(year, gender, race, list_of_rows)
        number_of_deaths = calculate_deaths(fatal_rate_total) 
        print(f"The deaths in {year} per thousand of {race} {gender}s were {number_of_deaths}")

get_started()
