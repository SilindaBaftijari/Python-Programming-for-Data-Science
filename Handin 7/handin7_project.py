# Import pandas and use pd.read_csv() to read in the data
import pandas as pd
import numpy as np
df = pd.read_csv('Handin 7/BigCitiesHealth_CA.csv')


#Collecting the Data set 
def collect_data(filename, city, health_metric):
    filtered_data = df[(df['geo_label_city'] == city) & (df['metric_item_label'] == health_metric)]
    
    sub_df = filtered_data[['date_label', 'value_column', 'race_column', 'sex_column']].rename(
        columns={'date_label': 'year', 'value_column': 'value', 'race_column': 'race', 'sex_column': 'sex'}
    )
    
    sub_df.reset_index(drop=True, inplace=True)

    return sub_df

def clean_data():
    df_list = []
    # Group by the (race, sex) pair
    for pair, pair_dataframe in df.groupby('sex_column','race_column'):
        # check if all values in pair_dataframe are nans
        if pair_dataframe['sex_column','race_column'].isnull():
            continue 
        else:
    # sort pair_dataframe by year
            df.interpolate(method ='linear', limit_direction ='backward', limit = 1)
            df.interpolate(method ='linear', limit_direction ='forward', limit = 1)  
            df_list.append(pair_dataframe)