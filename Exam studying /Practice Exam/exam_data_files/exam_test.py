from exam import game_play

# Calling game_play and printing the result
result = game_play()
print(result)


from exam import transpose_list, get_patients, dia_list

# Transpose the matrix and print out the specified rows
transposed_new = transpose_list(dia_list)
print(transposed_new[2])  # Third item
print(transposed_new[3])  # Fourth item
print(transposed_new[4])  # Fifth item

# Call get_patients and print the result
age_bmi = get_patients(transposed_new)
print(age_bmi)

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
