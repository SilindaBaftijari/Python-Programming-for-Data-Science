import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read CSV file
df = pd.read_csv('BigCitiesHealth_CA.csv')

# Collecting the data set 
def collect_data(filename, city, health_metric):
    # Filter data based on city and health metric
    filtered_data = df[(df['geo_label_city'] == city) & (df['metric_item_label'] == health_metric)]
    
    sub_df = filtered_data[['date_label', 'value', 'strata_race_label', 'strata_sex_label']].rename(
        columns={'date_label': 'year', 'value': 'value', 'strata_race_label': 'race', 'strata_sex_label': 'sex'}
    )
    
    sub_df.reset_index(drop=True, inplace=True)

    return sub_df

# Cleaning the data set
def clean_data(df):
    df_list = []
    # Group by the (race, sex) pair
    for pair, pair_dataframe in df.groupby(['race', 'sex']):
        # Check if all values in pair_dataframe are NaNs
        if pair_dataframe['value'].isnull().all():
            continue 
        else:
            # Sort pair_dataframe by year
            pair_dataframe = pair_dataframe.sort_values(by=['year'])
            
            # Apply backward interpolation
            pair_dataframe = pair_dataframe.interpolate(method='linear', limit_direction='backward')
            
            # Apply forward interpolation
            pair_dataframe = pair_dataframe.interpolate(method='linear', limit_direction='forward')

            # Append the modified pair_dataframe to df_list
            df_list.append(pair_dataframe)

    # Concatenate all dataframes in df_list
    output_df = pd.concat(df_list)
    output_df.reset_index(drop=True, inplace=True)

    return output_df

# Plot and main
def exploratory_data_analysis(df, year): 
    filtered_df = df[df["year"] == year]
    
    ax = sns.barplot(x="race", y="value", hue="sex", data=filtered_df)
    
    ax.set_title(f"Drug overdose death across sex and race groups -- {year}")
    
    fig = ax.get_figure()
    
    return fig, ax

df = collect_data('BigCitiesHealth_CA.csv', 'San Jose', 'Drug Overdose Deaths')
clean_df = clean_data(df)
barplot_2015_fig, barplot_2015_ax = exploratory_data_analysis(clean_df, 2015)

plt.show()
