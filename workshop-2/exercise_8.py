# Exercise 8: Custom Tuple Sorting
# Objective: Implement a function to sort a list of tuples according to multiple criteria

def sort_tuples(tuple_list):
    """Sorts a list of tuples (name, age) by age and then by name"""
    return sorted(tuple_list, key=lambda tuple_item: (tuple_item[1], tuple_item[0]))

def sorting_exercise():
    """Tuple sorting demonstration exercise"""
    people = [
        ("Ana", 25),
        ("Carlos", 30),
        ("Beatriz", 25),
        ("David", 22),
        ("Elena", 30),
        ("Fernando", 28)
    ]

    print("Original list:")
    for person in people:
        print(f"  {person[0]}, {person[1]} years old")

    sorted_people = sort_tuples(people)

    print("\nSorted list (by age, then by name):")
    for person in sorted_people:
        print(f"  {person[0]}, {person[1]} years old")
