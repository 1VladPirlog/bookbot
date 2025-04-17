

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

from stats import get_word_count

def main():
    filename = "books/frankenstein.txt"
    content = get_book_text(filename)
    if content is not None:
        word_count = get_word_count(content)
        print(f"{word_count} words found in the document")

if __name__ == "__main__":
    main()