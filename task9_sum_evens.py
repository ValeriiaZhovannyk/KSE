def sum_even_numbers(start, end):
    """
    Calculate sum of all even numbers from start to end (inclusive).
    Use a loop and if statement.
    """
    result = 0
    for i in range(int(start), int(end+1)):
        if i % 2 == 0:
            result += i
            # print(i)

    return result

print(sum_even_numbers(1, 10))   # 30 (2+4+6+8+10)
print(sum_even_numbers(5, 15))   # 50 (6+8+10+12+14)