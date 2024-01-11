import csv

def read_csv_to_list_of_dicts(file_path):
    data_list = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 5:
                continue
            if row[0].startswith('%') or not row[0].strip():
                continue
            try:
                processed_row = {
                    'year': int(row[2]),  # Year
                    'value': float(row[1]),  # Value
                    'race': row[3],  # Race
                    'gender': row[4]  # Gender
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


drug_deaths = read_csv_to_list_of_dicts('san_jose_drug.csv')
drug_deaths_per_gender_and_race = group_by_gender_race(drug_deaths)
drug_deaths_sum_over_5_years = sum_over_years(drug_deaths_per_gender_and_race)


print(f"The deaths of Black Male between 2017-2020 is {drug_deaths_sum_over_5_years[('Male', 'Black')]}")
print(f"The deaths of White Male between 2017-2020 is {drug_deaths_sum_over_5_years[('Male', 'White')]}")
print(f"The deaths of Hispanic Male between 2017-2020 is {drug_deaths_sum_over_5_years[('Male', 'Hispanic')]}")
print(f"The deaths of Asian/PI Male between 2017-2020 is {drug_deaths_sum_over_5_years[('Male', 'Asian/PI')]}")
