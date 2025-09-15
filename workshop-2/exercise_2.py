# Exercise 2: Even Number Filtering
# Objective: Develop a function that filters even numbers from a list

def filter_even_numbers(number_list):
    """Function that filters even numbers from a list"""
    even_numbers = []
    for number in number_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

def filtering_exercise():
    """Even number filtering demonstration exercise"""
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(f"Original list: {numbers_list}")
    even_nums = filter_even_numbers(numbers_list)
    print(f"Even numbers: {even_nums}")
