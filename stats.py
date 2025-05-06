def count_words(text):
    words_list= text.split()
    num_words = len(words_list)
    print(f"{num_words} words found in the document")

def count_chars(text):
    lower_text = text.lower()
    char_count = {}

    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # print(char_count)
    return char_count


