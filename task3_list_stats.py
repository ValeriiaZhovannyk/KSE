def calculate_stats(numbers):
    """
    Calculate min, max, and average from a list of numbers.
    Returns: dictionary with keys 'min', 'max', 'average'
    """
    stats = {"min": min(numbers), "max": max(numbers), "average": sum(numbers)/len(numbers)}
    return stats

result = calculate_stats([10, 20, 30, 40, 50])
print(result)  # {'min': 10, 'max': 50, 'average': 30.0}