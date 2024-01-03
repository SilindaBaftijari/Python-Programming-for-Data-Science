import csv
import re

def read_csv_to_list_of_dicts(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        pattern = re.compile(r'Drug Overdose Deaths (\d+\.\d+) (\d{4}) (\w+) Male')
        for line in file:
            if line.startswith('%') or not line.strip():
                continue
            match = pattern.search(line)
            if match:
                value, year, race = match.groups()
                try:
                    processed_row = {
                        'year': int(year),  # Year
                        'value': float(value),  # Value
                        'race': race,  # Race
                        'gender': 'Male'  # Gender
                    }
                    data_list.append(processed_row)
                except (IndexError, ValueError):
                    continue
    return data_list

def group_by_gender_race(data):
    grouped_data = {}
    for item in data:
        gender_race_key = (item['gender'], item['race'])
        if gender_race_key not in grouped_data:
            grouped_data[gender_race_key] = []
        grouped_data[gender_race_key].append(item)
    return grouped_data

def sum_over_years(grouped_data):
    sum_data = {}
    for key, values in grouped_data.items():
        total = sum([float(item['value']) for item in values])
        sum_data[key] = round(total, 2)
    return sum_data

drug_deaths = read_csv_to_list_of_dicts('Handin 5/san_jose_drug.csv')
drug_deaths_per_gender_and_race = group_by_gender_race(drug_deaths)
drug_deaths_sum_over_5_years = sum_over_years(drug_deaths_per_gender_and_race)

print(f"The deaths of Black Males between 2017-2020 is {drug_deaths_sum_over_5_years[('Male', 'Black')]}")
print(f"The deaths of White Males between 2017-2020 is {drug_deaths_sum_over_5_years[('Male', 'White')]}")
print(f"The deaths of Hispanic Males between 2017-2020 is {drug_deaths_sum_over_5_years[('Male', 'Hispanic')]}")
print(f"The deaths of Asian/PI Males between 2017-2020 is {drug_deaths_sum_over_5_years[('Male', 'Asian/PI')]}")