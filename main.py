from stats import count_words
from stats import count_chars

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_chars(file_contents)
        print(char_count)
        return word_count, char_count
        
def main():
    get_book_text("./books/frankenstein.txt")
    

main()