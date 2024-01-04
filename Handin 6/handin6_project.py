import csv
import numpy as np
from matplotlib import pyplot as plt

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
    years = []
    values = []

    # Data Extraction
    for entry in data:
        if entry['race'] == race:
            years.append(entry['year'])
            values.append(entry['value'])

    if plot:
        # Create figure and axis
        fig, ax = plt.subplots()

        # Plot the data
        ax.plot(years, values, marker='o', label=f'Death rate for {race}')

        # Set x ticks
        ax.set_xticks(years)

        # Set title
        ax.set_title(f'Death rate over years -- {race}')

        # Add legend
        ax.legend()

        # Show the plot
        plt.show()

        return fig, ax
    else:
        return years, values