# Exercise 6: Manual List Search
# Objective: Develop a function to find the index of an element in a list without using built-in methods like .index()

def search_element(element_list, element):
    """Searches for an element in a list and returns its index"""
    for i in range(len(element_list)):
        if element_list[i] == element:
            return i
    return -1

def search_exercise():
    """Manual search demonstration exercise"""
    fruit_list = ["apple", "banana", "orange", "grape", "pear", "kiwi"]
    print(f"List: {fruit_list}")

    elements_to_search = ["orange", "pear", "mango"]
    for element in elements_to_search:
        index = search_element(fruit_list, element)
        if index != -1:
            print(f"'{element}' found at index {index}")
        else:
            print(f"'{element}' not found in the list")
