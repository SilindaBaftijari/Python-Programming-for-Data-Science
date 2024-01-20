#1 Question Random and Modules (20 points: 6+7+7)
#In this task, we will create a python program that simulates tossing twenty-sided dice to determine a winner between 2 players. You can imagine this as a part of a digital game where a player can play a bonus card to increase their chance of winning.
#a. Create a function called dice_roller(sides, bonus) that rolls the dice that takes 2 parameters, the number of sides, and if the team has a bonus. Be sure to place this and the following functions in exam.py.
#b. Create a second function called game_play() for the gameplay that calls the dice_roller function for players with the following:
#monster rolls a 20-sided dice and has a bonus of +10
#team has 3 rolls
#First roll with an 8-sided dice and no bonus card
#Second roll with a 12-sided dice and a bonus card of +5
#Third roll with a dice of 6 and no bonus card
#Inside game_play() create a conditional statement (if ... then) to return the winners with the score and the losers with the score. Remember that monster or the team will win, requiring the if..then statement and 2 different print statements.
#return ('monster wins', monster, 'team loses', team)
#The output in the terminal should look like this: ('monster wins', 25, 'team loses', 11)
#c. From exam_test.py call the game_play() and print the result.
import random

def dice_roller(sides, bonus = 0):

    return random.randint(1, sides)
        
        
def game_play(): 
    monster_score = dice_roller(20,10) 
    
    team_score = dice_roller(8) + dice_roller(12,5) + dice_roller(6)
    
    if monster_score > team_score:
        return ('monster wins', monster_score, 'team loses', team_score)
    else:
        return ('team wins', team_score, 'monster loses', monster_score)


#2 Question List of List / For Loops (25 points: 5+10+10)
#In this task, we need to transpose (switch the rows and the columns if thinking about a table) the dia_list (See below or get here). The transposition of a list of lists (matrix) is a new list of lists (matrix) where the rows of the original become the columns, and the columns become the rows.
#Once you have transposed the matrix, we create a new matrix with the PatientNumber, BMI, and Outcome. However, we also need to change the 1 and 0 integers to strings positive and negative.
#a. Start with creating and copying the dia_list in the exam.py (see below)
#b. In exam.py create a function called transpose_list() that uses a for loop (comprehension not allowed) to transpose items and the subitems from a "9x19" matrix to a "19x9" matrix.
#Name the new list transposed_new
#Remember to make a nested loop for the items and subitems. Use the following names:
#Create a for loop inside another for loop
#For the first loop, the item is the variable.
#For the second loop, use for subitem in...
#From exam_test.py, print out the third, fourth, and fifth items of the transposed_new list.
#c. Create a second function in  exam.py for get_patients() that takes the transposed_new list and extracts PatientNumber, BMI, and Outcome.
#Name this new list age_bmi
#Create the loop with for rows in... for the extraction
#Use a conditional statement that tests if Outcome is an integer of 1 and 0 and converts to positive and negative with 1 being positive.
#d. From exam_test.py call get_patients() and print the result.

import numpy as np

dia_list=[
['PatientNumber',14568,22368,30168,37968,45768,53568,61368,69168,76968,84768,92568,50368,18168,15968,33768,41315,39368,14168,54968],
['Glucose',148,85,183,89,137,116,78,115,197,125,110,168,139,189,166,100,118,107,103],
['BloodPressure',72,66,64,66,40,74,50,0,70,96,92,74,80,60,72,0,84,74,30],
['SkinThickness',35,29,0,23,35,0,32,0,45,0,0,0,0,23,19,0,47,0,38],
['Insulin',0,0,0,94,168,0,88,0,543,0,0,0,0,846,175,0,230,0,83],
['BMI',33.6,26.6,23.3,28.1,43.1,25.6,31,35.3,30.5,0,37.6,38,27.1,30.1,25.8,30,45.8,29.6,43.3],
['DiabetesPedigreeFunction',0.627,0.351,0.672,0.167,2.288,0.201,0.248,0.134,0.158,0.232,0.191,0.537,1.441,0.398,0.587,0.484,0.551,0.254,0.183],
['Age',50,31,32,21,33,30,26,29,53,54,30,34,57,59,51,32,31,31,33],
['Outcome',1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0]]


# b. transpose_list function
def transpose_list(matrix):
    transposed_new = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed_new.append(transposed_row)
    return transposed_new

# c. get_patients function
def get_patients(transposed_matrix):
    age_bmi = []
    for row in transposed_matrix:
        if row[0] in ['PatientNumber', 'BMI', 'Outcome']:
            # Modify Outcome to positive/negative
            if row[0] == 'Outcome':
                row = ['positive' if x == 1 else 'negative' if x == 0 else x for x in row]
            age_bmi.append(row)
    return age_bmi

#4 Data Story with Pandas: 30 pts 10+5+5+5+5
#You will mainly use Pandas to work with the COVID-19 confirmed cases dataset in this problem. The dataset contains the country, province, coordinate and cumulative count of confirmed cases each day.
#The dataset contains the following columns:
#Province/State: The province or state within the country in the next column (can be empty).
#Country/Region: The name of the country/region. Each unique entry is seen as a country.
#Lat: The Latitude of the location (province/state or country) in the GPS coordinates
#Long: The longitude of the location (province/state or country) in the GPS coordinates
#Date: The values are the cumulative numbers of confirmed COVID-19 cases of different countries on this day.
#a. In exam.py. Write a function data_cleaning that i) removes all locations with missing latitude or longitude values, or both latitude and longitude values are zeros. 
# ii) most column names are date times in string format. Convert these columns to datetime format. The function should take a DataFrame variable df as input and returns the cleaned dataframe. 
# The data cleaning needs to be done in Pandas, not with for loops. Hint: pd.to_datetime()
#In exam_test.py, read the raw data into covid_df, and call the data_cleaning function to clean the data. Store the output at the cleaned_covid_df variable.
#b. Within exam.py, write a function get_countries_by_earth_quadrant, which takes a DataFrame variable df, similar to cleaned_covid_df, as input. 
# The function should return a dictionary with each of the Earth Quadrants (NW, NE, SW, SE) as keys and a list of the countries belonging to each quadrant as values. Where 'NW', 'NE', 'SW', and 'SE' are specified as:
#Longitude >= 0 -> E; Longitude < 0 -> W;
#Latitude >= 0 -> N; Latitude < 0 -> S;
#The countries in each quadrant should be ordered alphabetically.
#In exam_test.py, call the get_countries_by_earth_quadrant function to get the dictionary and save it to country_dict.
#c. In exam.py, write a function group_table_by_country to derive country-wise data from the original table using df.groupby function. 
# If a country has more than one location (i.e. provinces) included, its location should be the center of all locations, and its confirmed cases count should be the summation of the per-location values. 
# The function should take a DataFrame variable df as input and return the per-country counts in another dataframe. The indices of the output dataframe should be reset to 0,1,...
#In exam_test.py, call the group_table_by_country function and save the result to country_wise_df.
#d. Plot the total number of cumulative confirmed cases in a whole earth quadrant on every single day in the table.
# In exam.py, write a function plot_new_cases_daily that draws a line plot of the total number of cumulative confirmed cases in the input earth quadrant on each day,
# where the x-axis is the date and y-axis is the corresponding number of cumulative confirmed cases in the whole quadrant.
# Choose a proper title and label for both axes.
# The function should take a DataFrame variable df and a string variable earth_quadrant in {'NW, NE, SW, SE'} as input and return the axes object (plotting area) of the figure.
# In exam_test.py, call the function by plot_new_cases_daily(country_wise_df,'NE') and save the result as ax_ne.
# Hint: You may consider obtaining a Series variable to store the total number of new cases in the earth quadrant; then create a figure with fig, ax = plt.subplots(1,1); 
# and call series.plot() to create the line plot and add ax to the arguments.
# The ax object is returned after plotting.
# e. Write a function get_top_new_case_countries_by_month to compute the top-K countries in terms of new confirmed cases in any specified year and month. 
# If the searched year and month are illegal or not present in the table, print a message 'the input month is not available in the data!' and return None. 
# Otherwise, output the top K countries with the highest number of new cases during the month.
# We may compute the difference between the last day and the first day of the month as the number of new confirmed cases during the month.
# The function should take a DataFrame variable df, an integer year, an integer month, and an integer k_val. For legal input, a dictionary object should be returned, 
# where the keys are top-K country names and values are their new confirmed cases, ordered by the values in descending order.
# In exam_test.py, call the function by get_top_new_case_countries_by_month (country_wise_df, year=2021, month=2, k_val=10) and save the result to top_k_countries_dict.
# Hint: you can visit the year, month, and day of a datetime object dt by dt.year, dt.month, dt.day, respectively.

import pandas as pd
import matplotlib.pyplot as plt

# a. Data Cleaning Function
def data_cleaning(df):
    # Remove missing or zero lat/long values
    df = df[(df['Lat'] != 0) | (df['Long'] != 0)]
    df = df.dropna(subset=['Lat', 'Long'])

    # Convert date columns to datetime
    date_cols = df.columns[4:]  # Assuming the first four columns are not dates
    df[date_cols] = df[date_cols].apply(pd.to_datetime, errors='coerce')

    return df

# b. Function to Get Countries by Earth Quadrant
def get_countries_by_earth_quadrant(df):
    quadrant_dict = {'NW': [], 'NE': [], 'SW': [], 'SE': []}
    for index, row in df.iterrows():
        if row['Long'] >= 0 and row['Lat'] >= 0:
            quadrant = 'NE'
        elif row['Long'] < 0 and row['Lat'] >= 0:
            quadrant = 'NW'
        elif row['Long'] >= 0 and row['Lat'] < 0:
            quadrant = 'SE'
        else:
            quadrant = 'SW'
        country = row['Country/Region']
        if country not in quadrant_dict[quadrant]:
            quadrant_dict[quadrant].append(country)

    # Sort countries alphabetically
    for key in quadrant_dict:
        quadrant_dict[key].sort()

    return quadrant_dict

# c. Function to Group Table by Country
def group_table_by_country(df):
    # Group by country, summing up the confirmed cases and averaging Lat/Long
    grouped_df = df.groupby('Country/Region').agg({'Lat': 'mean', 'Long': 'mean', df.columns[4:]: 'sum'})
    grouped_df = grouped_df.reset_index()
    return grouped_df

# d. Function to Plot New Cases Daily
def plot_new_cases_daily(df, earth_quadrant):
    fig, ax = plt.subplots(1, 1)
    countries = get_countries_by_earth_quadrant(df)[earth_quadrant]
    quadrant_df = df[df['Country/Region'].isin(countries)]
    total_cases = quadrant_df.groupby(quadrant_df.columns[4:]).sum()
    total_cases.plot(ax=ax)
    ax.set_title('Total Cumulative Confirmed Cases in ' + earth_quadrant + ' Quadrant')
    ax.set_xlabel('Date')
    ax.set_ylabel('Cumulative Confirmed Cases')
    return ax

# e. Function to Get Top New Case Countries by Month
def get_top_new_case_countries_by_month(df, year, month, k_val):
    try:
        month_df = df[df.columns[4:]].copy()
        month_df = month_df.filter(regex=f'^{year}-{str(month).zfill(2)}')
        if month_df.empty:
            print('the input month is not available in the data!')
            return None
        df['new_cases'] = month_df.iloc[:, -1] - month_df.iloc[:, 0]
        top_countries = df.nlargest(k_val, 'new_cases')['Country/Region']
        return dict(zip(top_countries, df.loc[top_countries.index, 'new_cases']))
    except Exception as e:
        print(str(e))
        return None


