def get_word_count(text):
    if text is None:
        return 0
    words = text.split()
    return len(words)

def get_char_count(text):
    
    content_lower = text.lower()
    char_dict = {}
    for char in content_lower:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict