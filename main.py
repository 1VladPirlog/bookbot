

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

from stats import get_word_count
from stats import get_char_count
from stats import sort_char_counts

def main():
    filename = "books/frankenstein.txt"
    text = get_book_text(filename)
    
    if text:
        word_count = get_word_count(text)
        char_count = get_char_count(text)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filename}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for char, count in sorted(char_count.items()):
            print(f"'{char}: {count}'")
        print("============= END ===============")

if __name__ == "__main__":
    main()