from collections import Counter
def sort_on(items):
    return items["num"]

def get_num_words(file_text):
    words_list= file_text.split()
    return len(words_list)

def get_num_characters(file_text):
    characters = {}
    for c in file_text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] +=1
        else:
            characters[lowered] = 1
    character_list = []
    for key in characters:
        character_list.append({"char": key , "num":characters[key]})
    character_list.sort(reverse=True, key=sort_on)   
    return character_list