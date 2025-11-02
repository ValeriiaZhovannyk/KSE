def count_word_frequency(words):
    """
    Count frequency of each word in the list.
    Returns: dictionary with word as key and count as value
    """
    words_counted = dict.fromkeys(words, 0)
    for i in words:
        if i in words_counted.keys():
            words_counted[i] += 1
    
    return(words_counted)


words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(count_word_frequency(words))
# {"apple": 3, "banana": 2, "cherry": 1}