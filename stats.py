def get_word_count(text):
    if text is None:
        return 0
    words = text.split()
    return len(words)

def get_char_count(text):
    
    content_lower = text.lower()
    char_dict = {}
    for char in content_lower:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_char_counts(char_dict):
    # Step 1: Create empty list to hold our dictionaries
    sorted_list = []
    
    # Step 2: Convert dictionary to list of dictionaries
    for character, count in char_dict.items():
        # Create a new dictionary for each character-count pair
        char_entry = {
            "char": character,
            "count": count
        }
        # Append to our list
        sorted_list.append(char_entry)
    
    # Step 3: Define sorting logic using lambda
    # Sort by count descending first, then character ascending
    def sort_key(item):
        # Primary key: negative count for descending order
        # Secondary key: character itself for alphabetical
        return (-item["count"], item["char"])
    
    # Step 4: Perform the actual sorting
    sorted_list.sort(key=sort_key)  # Could also use lambda directly
    
    return sorted_list