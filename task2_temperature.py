def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: (C × 9/5) + 32
    """
    converted_temperature = ((celsius*9)/5)+32
    return(converted_temperature)

print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0