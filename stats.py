def get_word_count(text):
    if text is None:
        return 0
    words = text.split()
    return len(words)