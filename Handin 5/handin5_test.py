import time
from handin5 import wordfile_differences_list_search, wordfile_differences_dict_search

filename1 = 'Handin 5/british-english.txt'
filename2 = 'Handin 5/american-english.txt'

start_time = time.time()
differences_list_search = wordfile_differences_list_search(filename1, filename2)
time_spent_list_search = time.time() - start_time
print("List Search Differences:", differences_list_search)
print("List Search Execution Time:", time_spent_list_search)

start_time = time.time()
differences_dict_search = wordfile_differences_dict_search(filename1, filename2)
time_spent_dict_search = time.time() - start_time
print("Dict Search Differences:", differences_dict_search)
print("Dict Search Execution Time:", time_spent_dict_search)