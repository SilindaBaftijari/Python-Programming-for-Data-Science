def wordfile_to_list(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            words.append(word)
    return words

def wordfile_to_dict(filename):
    file_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            key = line.strip()
            file_dict[key] = None
    return file_dict

def wordfile_differences_list_search(filename1, filename2):
    wordlist1 = wordfile_to_list(filename1)
    wordlist2 = wordfile_to_list(filename2)

    if len(wordlist1) > len(wordlist2):
        wordlist1, wordlist2 = wordlist2, wordlist1

    differences = [word for word in wordlist1 if word not in wordlist2]
    return differences

def wordfile_differences_dict_search(filename1, filename2):
    word_list = wordfile_to_list(filename1)
    word_dict = wordfile_to_dict(filename2)
    differences = [word for word in word_list if word not in word_dict]
    return differences
