import csv
from matplotlib import pyplot as plt

def read_csv_data(file_path):
    data_list = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as csvfile:
        # Skip initial comment lines
        while True:
            position = csvfile.tell()
            if not csvfile.readline().startswith('%'):
                csvfile.seek(position)
                break

        # read the CSV data
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            try:
                processed_row = {
                    'year': int(row['date_label']),  # Year
                    'value': float(row['value']),  # Value
                    'race': row['strata_race_label'],  # Race
                    'gender': row['strata_sex_label']  # Gender
                }
                data_list.append(processed_row)
            except (ValueError, KeyError):
                continue

    return data_list

def line_plot_race_over_years(data, race, plot=True):
    years = []
    values = []

    for entry in data:
        if entry['race'] == race:
            years.append(entry['year'])
            values.append(entry['value'])

    if plot:
        fig, ax = plt.subplots()
        ax.plot(years, values, marker='o', label=f'Death rate for {race}')
        unique_sorted_years = sorted(set(years))
        ax.set_xticks(unique_sorted_years)
        ax.set_xticklabels(unique_sorted_years)
        ax.set_title(f'Death rate over years -- {race}')
        ax.legend()
        plt.show()
        plt.savefig('line_plot_{}.png'.format(race))
        return fig, ax
    else:
        return years, values

    
def bar_plot_year_across_races(data, year, plot=True):
    races = []
    values = []

    for entry in data:
        if entry['year'] == year:
            races.append(entry['race'])
            values.append(entry['value'])

    if plot:
        fig, ax = plt.subplots()
        ax.bar(races, values)
        unique_sorted_races = sorted(set(races))
        ax.set_xticks(range(len(unique_sorted_races)))
        ax.set_xticklabels(unique_sorted_races, rotation=45)
        ax.set_title(f'Death rate across races -- {year}')
        plt.show()
        plt.savefig('bar_plot_{}.png'.format(year))
        return fig, ax
    else:
        return races, values


# Load data from CSV file
drug_deaths_data = read_csv_data('san_jose_drug.csv')

# Line plot for Black race group over the years
line_plot_fig, line_plot_ax = line_plot_race_over_years(drug_deaths_data, 'Black', plot=True)

# Bar plot for the year 2017
bar_plot_fig, bar_plot_ax = bar_plot_year_across_races(drug_deaths_data, 2017, plot=True)

# Combined line plots for different race groups
fig, ax = plt.subplots()
all_races, _ = bar_plot_year_across_races(drug_deaths_data, 2017, plot=False)

for race in all_races[:4]: 
    years, values = line_plot_race_over_years(drug_deaths_data, race, plot=False)
    ax.plot(years, values, marker='o', label=race)

ax.set_title('Death rate over years -- all races')
ax.legend()
plt.show()

plt.savefig('combined_line_plot.png')  # Save the combined plot

line_plots_fig, line_plots_ax = fig, ax
