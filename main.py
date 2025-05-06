def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
        print(file_contents)
        
def main():
    get_book_text("./books/frankenstein.txt")

main()