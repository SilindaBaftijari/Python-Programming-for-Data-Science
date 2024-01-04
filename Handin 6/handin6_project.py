import csv

def read_csv_data(file_path):
    data_list = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if not row or row.startswith('%'): 
                continue
            try:
                processed_row = {
                    'year': int(row['year']),  # Year
                    'value': float(row['value']),  # Value 
                    'race': row['race'],  # Race
                    'gender': row['gender']  # Gender
                }
                data_list.append(processed_row)
            except (ValueError, KeyError):  
                continue
    return data_list

def line_plot_race_over_years(data, race, plot=True):
    