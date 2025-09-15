# Exercise 3: Temperature Conversion
# Objective: Use map and a lambda function to convert a list of temperatures from Celsius to Fahrenheit

def convert_temperatures(celsius_temperatures):
    """Converts a list of temperatures from Celsius to Fahrenheit using map and lambda"""
    fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius_temperatures))
    return fahrenheit

def temperature_exercise():
    """Temperature conversion demonstration exercise"""
    celsius = [0, 20, 25, 30, 37, 100]
    print(f"Temperatures in Celsius: {celsius}")
    fahrenheit = convert_temperatures(celsius)
    print(f"Temperatures in Fahrenheit: {fahrenheit}")

    print("\nDetailed conversion:")
    for c, f in zip(celsius, fahrenheit):
        print(f"{c}°C = {f:.1f}°F")
