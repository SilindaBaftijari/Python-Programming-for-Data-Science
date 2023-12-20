
#Creating the variable 
message = "hello world" 
message_length = len(message) 

# Print the length of the string to the console
print(message_length)

# Open the file 'message.txt' in write mode ('w')
with open('message.txt', 'w') as file:
    file.write(message)

print("The string has been written to 'message.txt'")