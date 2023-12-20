import time
from handin5 import wordfile_differences_dict_search

# Replace with your actual file paths
filename1 = '/Users/silindabaftijari/Desktop/Python Programming for Data Science/Handin 5/british-english.txt'
filename2 = '/Users/silindabaftijari/Desktop/Python Programming for Data Science/Handin 5/american-english.txt'

start_time = time.time()
differences = wordfile_differences_dict_search(filename1, filename2)
end_time = time.time()

print("Differences:", differences)
print("Execution Time:", end_time - start_time)