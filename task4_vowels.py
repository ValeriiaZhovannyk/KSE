def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in text.
    Case-insensitive.
    """
    vowels = ["a", "e", "i", "o", "u"]
    vowels_counter = 0
    for i in text.lower():
        if i in vowels:
            vowels_counter += 1
    return vowels_counter

print(count_vowels("Hello World"))  # 3
print(count_vowels("Python"))       # 1