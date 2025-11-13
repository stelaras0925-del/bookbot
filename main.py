from stats import get_num_words,get_num_characters
import sys


if len(sys.argv) == 2:
    def get_book_text(filepath):
        with open(filepath) as f:
        # do something with f (the file) here
        # f is a file object
            file_contents = f.read()
            return(f"{file_contents}")
else:
    print("Usage: python3 main.py <path_to_book>")
        
def main():
    file_text = get_book_text(f"{sys.argv[1]}")
    num_words = get_num_words(file_text)
    num_characters = get_num_characters(file_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")    
    characters_list = []
    for chars in num_characters:
        characters_list.append(f"{chars['char']}: " + f"{chars['num']}")
    for i in range(len(characters_list)):
        print(characters_list[i])
main()    