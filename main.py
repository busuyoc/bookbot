from stats import count_words

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
        count_words(file_contents)
        
def main():
    get_book_text("./books/frankenstein.txt")
    

main()