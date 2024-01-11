import csv
import matplotlib.pyplot as plt

def read_csv_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)  
        for row in csv_reader:
            if len(row) > 4 and not row[0].startswith('%'):
                data_dict = {
                    'year': int(row[2]),
                    'gender': row[4],
                    'race': row[3],
                    'value': float(row[1])
                }
                data.append(data_dict)
    return data


def line_plot_race_over_years(data, race, plot=True):
    years, values = [], []
    for row in data:
        if row['race'] == race:
            years.append(row['year'])
            values.append(row['value'])

    if plot:
        fig, ax = plt.subplots()
        ax.plot(years, values)
        ax.set_xticks(sorted(set(years)))
        ax.set_title(f'Death rate over years -- {race}')
        plt.legend([race])
        plt.show()
        return fig, ax
    else:
        return years, values

def bar_plot_year_across_races(data, year, plot=True):
    races, values = [], []
    for row in data:
        if row['year'] == year:
            races.append(row['race'])
            values.append(row['value'])

    if plot:
        fig, ax = plt.subplots()
        ax.bar(races, values)
        ax.set_title(f'Death rate across races -- {year}')
        plt.show()
        return fig, ax
    else:
        return races, values


drug_deaths_data = read_csv_data('san_jose_drug.csv')
line_plot_fig, line_plot_ax = line_plot_race_over_years(drug_deaths_data, 'Black')
bar_plot_fig, bar_plot_ax = bar_plot_year_across_races(drug_deaths_data, 2017)

# Combined plot for all races
line_plots_fig, line_plots_ax = plt.subplots()

races, _ = bar_plot_year_across_races(drug_deaths_data, 2017, plot=False)

for race in races:
    years, values = line_plot_race_over_years(drug_deaths_data, race, plot=False)
    line_plots_ax.plot(years, values, label=race) 

line_plots_ax.set_xticks(sorted(set(years)))
line_plots_ax.set_title('Death rate over years -- all races')
line_plots_ax.legend() 
plt.show()
