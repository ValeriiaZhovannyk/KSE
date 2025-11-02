def count_words_in_file(filename):
    """
    Count total number of words in a file.
    Handle FileNotFoundError - return 0 if file doesn't exist.
    """
    try:   
        with open(filename, 'r') as file:
            content = file.read()
            words_count = len(content.split())
            return words_count
    except FileNotFoundError:
        return(0)


# If file contains: "Hello world from Python"
print(count_words_in_file("sample.txt"))  # 4
print(count_words_in_file("missing.txt")) # 0