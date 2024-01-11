import time
from handin5 import wordfile_to_list, wordfile_differences_list_search, wordfile_differences_dict_search

wordlist_british = wordfile_to_list('british-english')
wordlist_american = wordfile_to_list('american-english')

start_time = time.time()
differences_list_search = wordfile_differences_list_search('british-english', 'american-english')
time_spent_list_search = time.time() - start_time
print("List Search Differences:", differences_list_search)
print("List Search Execution Time:", time_spent_list_search)

start_time = time.time()
differences_dict_search = wordfile_differences_dict_search('british-english', 'american-english')
time_spent_dict_search = time.time() - start_time

print("List Search Differences:", len(differences_list_search))
print("List Search Execution Time:", time_spent_list_search)
print("Dict Search Differences:", len(differences_dict_search))
print("Dict Search Execution Time:", time_spent_dict_search)
