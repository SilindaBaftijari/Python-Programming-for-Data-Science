
#Task 1
from exam import game_play

# Calling game_play and printing the result
result = game_play()
print(result)


#Task 2 
from exam import transpose_list, get_patients, dia_list

# Transpose the matrix and print out the specified rows
transposed_new = transpose_list(dia_list)
print(transposed_new[2])  # Third item
print(transposed_new[3])  # Fourth item
print(transposed_new[4])  # Fifth item

# Call get_patients and print the result
age_bmi = get_patients(transposed_new)
print(age_bmi)


#Task 3
#3 Question Numpy + Plots (25 points: 5+5+5+5+5)
#In this task, we will work with a dataset of child obesity that contains age, exercise, height, and obesity. We will use NumPy and Matplotlib to investigate the relationships between them.
#a. Use import numpy as np and import matplotlib.pyplot as plt in exam_test.py.
#In exam_test.py load the health dataset into a NumPy array using the genfromtxt function with the skip_header parameter enabled.
#Print the shape of the dataset (number of rows and columns) from exam_test.py
#b. Extract columns into variables for age, weight, height, exercise, and obesity columns.
#c. Create a scatter plot from exam_test.py of weight vs. age, with exercise level represented by color.
#X-axis label "Age (years)"
#Y-axis label "Weight (lbs)"
#Title "Weight vs. Age with Exercise Level"
#Colorbar "Exercise Level (hours per week)"
#d. Create a bar chart of children aged 10 for obesity vs. normal in exam_test.py.
#Use the variable age_counts to perform the np operations to get the age group and to plot the obesity. Obesity is 1, and Not Obese is 0.
#The bar legends (x coordinates) should read "Not Obese", "Obese"
#X-axis "Obesity"
#Y-axis "Age 10 count"
#e. Using NumPy to print in the terminal the correlation between weight and exercise from exam_test.py.  Hint: search for the NumPy function for calculating the correlation coefficient.
import numpy as np
import matplotlib.pyplot as plt

# a. Load the dataset
dataset = np.genfromtxt('/Users/silindabaftijari/Desktop/Python Programming for Data Science/Exam studying /Practice Exam/exam_data_files/health_data2.csv', delimiter=',', skip_header=1)
print("Shape of the dataset:", dataset.shape)

# b. Extract columns
age = dataset[:, 0]  # Assuming age is the first column
weight = dataset[:, 1]  # Replace with the correct column index for weight
height = dataset[:, 2]  # Replace with the correct column index for height
exercise = dataset[:, 3]  # Replace with the correct column index for exercise
obesity = dataset[:, 4]  # Replace with the correct column index for obesity

# c. Scatter plot of weight vs. age
plt.scatter(age, weight, c=exercise)
plt.xlabel("Age (years)")
plt.ylabel("Weight (lbs)")
plt.title("Weight vs. Age with Exercise Level")
cbar = plt.colorbar()
cbar.set_label("Exercise Level (hours per week)")
plt.show()

# d. Bar chart for children aged 10
age_10 = dataset[age == 10]
obese_count = np.sum(age_10[:, 4] == 1)  # Assuming obesity is marked as 1
not_obese_count = len(age_10) - obese_count

plt.bar(["Not Obese", "Obese"], [not_obese_count, obese_count])
plt.xlabel("Obesity")
plt.ylabel("Age 10 count")
plt.show()

# e. Print correlation between weight and exercise
correlation = np.corrcoef(weight, exercise)[0, 1]
print("Correlation between weight and exercise:", correlation)



#Task 4 
# Import necessary libraries
import pandas as pd

# Read the dataset
covid_df = pd.read_csv('covid_data.csv')  # Replace 'covid_data.csv' with your file path

# a. Clean the data
cleaned_covid_df = data_cleaning(covid_df)

# b. Get countries by earth quadrant
country_dict = get_countries_by_earth_quadrant(cleaned_covid_df)

# c. Group table by country
country_wise_df = group_table_by_country(cleaned_covid_df)

# d. Plot new cases daily
ax_ne = plot_new_cases_daily(country_wise_df, 'NE')

# e. Get top new case countries by month
top_k_countries_dict = get_top_new_case_countries_by_month(country_wise_df, year=2021, month=2, k_val=10)
