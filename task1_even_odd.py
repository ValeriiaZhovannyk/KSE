def check_even_odd(number):
    """
    Check if a number is even or odd.
    Returns: "even" or "odd"
    """
    if int(number) % 2 == 0:
        return ('even')
    else:
        return ('odd')

print(check_even_odd(5))
print(check_even_odd(4))