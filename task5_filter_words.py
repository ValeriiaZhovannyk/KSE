def filter_long_words(words, min_length):
    """
    Return list of words longer than min_length.
    """
    filtered_words = []
    for i in words:
        if len(i) > min_length:
            filtered_words.append(i)
    return filtered_words

words = ["cat", "elephant", "dog", "butterfly"]
print(filter_long_words(words, 5))  
# ["elephant", "butterfly"]