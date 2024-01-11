# Import pandas and use pd.read_csv() to read in the data
import pandas as pd

#Collecting the Data set 
def collect_data(filename, city, health_metric):
    df = pd.read_csv('Handin 7/BigCitiesHealth_CA.csv')
    filtered_data = df[(df['geo_label_city'] == city) & (df['metric_item_label'] == health_metric)]
    
    sub_df = filtered_data[['date_label', 'value_column', 'race_column', 'sex_column']].rename(
        columns={'date_label': 'year', 'value_column': 'value', 'race_column': 'race', 'sex_column': 'sex'}
    )
    
    sub_df.reset_index(drop=True, inplace=True)

    return sub_df

