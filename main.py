from stats import count_words
from stats import count_chars
from stats import sort_dictionary
import sys

def get_book_text(fp):
    with open(fp, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    text = get_book_text(file_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_chars = sort_dictionary(char_count)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

