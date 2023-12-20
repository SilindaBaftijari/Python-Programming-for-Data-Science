
def wordfile_to_list(filename):
    words = []  # Initialize an empty list to store words
    with open(filename, 'r') as file:  # Open the file in read mode
        for line in file:  # Iterate over each line in the file
            word = line.strip()  # Remove the newline character at the end
            words.append(word)  # Add the word to the list
    return words

def wordfile_differences_list_search(filename1, filename2):
    # Generate word lists using the wordfile_to_list function
    wordlist_british = wordfile_to_list(filename1)
    wordlist_american = wordfile_to_list(filename2)

    # List to hold words that are in the first file but not in the second
    differences = []

    # Loop through each word in the first list
    for word in wordlist_british:
        # Check if the word is not in the second list
        if word not in wordlist_american:
            differences.append(word)

    # Return the list of words that are only in the first file
    return differences

# call the function with the file paths
differences = wordfile_differences_list_search('/Users/silindabaftijari/Desktop/Python Programming for Data Science/Handin 5/british-english.txt', '/Users/silindabaftijari/Desktop/Python Programming for Data Science/Handin 5/american-english.txt')

#print the differences
print(differences)

def wordfile_to_dict(filename):
    file_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            key = line.strip()
            # Assuming value is not important for this task
            file_dict[key] = None
    return file_dict

def wordfile_differences_dict_search(filename1, filename2):
    word_list = wordfile_to_list(filename1)
    word_dict = wordfile_to_dict(filename2)
    differences = [word for word in word_list if word not in word_dict]
    return differences