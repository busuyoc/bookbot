def count_words(text):
    words_list= text.split()
    num_words = len(words_list)
    # print(f"{num_words} words found in the document")
    return num_words

def count_chars(text):
    lower_text = text.lower()
    char_count = {}

    for char in lower_text:
        if char.isalpha():   
            char_count[char] = char_count.get(char, 0) + 1

    
    return char_count

def sort_dictionary(char_count):
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(key=lambda d: d["num"], reverse=True)
    return char_list


