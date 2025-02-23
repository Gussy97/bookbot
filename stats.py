def count_words(text):
    words = text.split()
    return len(words)

def count_each_char(text):
    counts = {}
    for char in text:
        if char.lower() not in counts:
            counts[char.lower()] = 1
        else:
            counts[char.lower()] += 1
    return counts

def get_book_text(path_to_text):
    with open(path_to_text) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]
    
def get_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    return sorted_list

def create_report(path_to_book):
    text = get_book_text(path_to_book)
    word_count = count_words(text)
    char_counts = count_each_char(text)
    sorted_list = get_sorted_list(char_counts)
    sorted_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for obj in sorted_list:
        if obj["char"].isalpha():
            print(f"{obj["char"]}: {obj["num"]}")
    print("============= END ===============")