def main():
    path_to_book = "books/frankenstein.txt"
    create_report(path_to_book)

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path_to_text):
    with open(path_to_text) as f:
        return f.read()
    
def count_each_char(text):
    counts = {}
    for char in text:
        if char.lower() not in counts:
            counts[char.lower()] = 1
        else:
            counts[char.lower()] += 1
    return counts

def create_report(path_to_book):
    text = get_book_text(path_to_book)
    word_count = count_words(text)
    char_counts = count_each_char(text)
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in char_counts:
        if char.isalpha():
            print(f"The '{char}' character was found {char_counts[char]} times")
    print("--- End report ---")

main()