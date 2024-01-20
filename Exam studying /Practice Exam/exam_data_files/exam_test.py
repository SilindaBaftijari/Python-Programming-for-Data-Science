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