import random 

subjects = ["he", "she", "it", "they", "we", "you"]
verbs_1 = ["is", "are", "am"]
objects_1 = ["a student", "a teacher", "a programmer", "a dog", "a cat", "a bird"]
verbs_2 = ["plays", "eats", "sleeps", "drinks", "reads", "writes"]
objects_2 = ["football", "bananas", "bed", "water", "books", "code"]

def generate_sentence():
    result = ""
    
    selected_subject = random.choice(subjects).capitalize() 
    sentence_1 = selected_subject + " " + random.choice(verbs_1) + " " + random.choice(objects_1) + "." + "\n"
    result += sentence_1
    
    selected_subject = random.choice(subjects).capitalize() 
    sentence_2 = selected_subject + " " + random.choice(verbs_2) + " " + random.choice(objects_2) + "."+ "\n"
    result += sentence_2
    
    return (result) 
