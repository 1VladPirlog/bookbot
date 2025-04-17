

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

from stats import get_word_count
from stats import get_char_count

def main():
    filename = "books/frankenstein.txt"
    content = get_book_text(filename)
    
    if content is not None:
        word_count = get_word_count(content)
        print(f"{word_count} words found in the document")
        
    if content:
        char_count = get_char_count(content)
        for char, count in char_count.items():
            print(f"{char_count}")

if __name__ == "__main__":
    main()