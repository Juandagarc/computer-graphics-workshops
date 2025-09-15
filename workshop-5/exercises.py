import numpy as np
from collections import Counter


def exercise_1():
    """Exercise 1: Create a Specific Vector
    Objective: Create a NumPy vector called 'A' with values [2, 3, 5, 1, 4, 79, 8, 6, 10].
    """
    print("=== Exercise 1: Create a Specific Vector ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    print(f"Vector A: {A}")
    print(f"Shape: {A.shape}")
    print(f"Data type: {A.dtype}")
    print()
    return A


def exercise_2():
    """Exercise 2: Create a Vector with a Range
    Objective: Create a NumPy vector called 'B' containing a sequence of numbers from 11 to 20.
    """
    print("=== Exercise 2: Create a Vector with a Range ===")
    B = np.arange(11, 21)
    print(f"Vector B: {B}")
    print(f"Shape: {B.shape}")
    print(f"Data type: {B.dtype}")
    print()
    return B


def exercise_3():
    """Exercise 3: Vector Concatenation
    Objective: Combine vectors 'A' and 'B' to form a new vector 'C' in a single row.
    """
    print("=== Exercise 3: Vector Concatenation ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    print(f"Vector A: {A}")
    print(f"Vector B: {B}")
    print(f"Vector C (concatenated): {C}")
    print(f"Shape of C: {C.shape}")
    print()
    return C


def exercise_4():
    """Exercise 4: Find Minimum Value
    Objective: Find the element with the lowest value in vector 'C' using a NumPy function.
    """
    print("=== Exercise 4: Find Minimum Value ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    min_value = np.min(C)
    min_index = np.argmin(C)
    print(f"Vector C: {C}")
    print(f"Minimum value: {min_value}")
    print(f"Index of minimum value: {min_index}")
    print()
    return min_value


def exercise_5():
    """Exercise 5: Find Maximum Value
    Objective: Find the element with the highest value in vector 'C' using a NumPy function.
    """
    print("=== Exercise 5: Find Maximum Value ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    max_value = np.max(C)
    max_index = np.argmax(C)
    print(f"Vector C: {C}")
    print(f"Maximum value: {max_value}")
    print(f"Index of maximum value: {max_index}")
    print()
    return max_value


def exercise_6():
    """Exercise 6: Determine Vector Length
    Objective: Calculate the total number of elements present in vector 'C' using a NumPy function.
    """
    print("=== Exercise 6: Determine Vector Length ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    length = np.size(C)
    print(f"Vector C: {C}")
    print(f"Total number of elements: {length}")
    print(f"Alternative using len(): {len(C)}")
    print()
    return length


def exercise_7():
    """Exercise 7: Calculate Average Manually
    Objective: Calculate the average of vector 'C' elements using only sum and division operations.
    """
    print("=== Exercise 7: Calculate Average Manually ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    total_sum = np.sum(C)
    total_elements = len(C)
    manual_average = total_sum / total_elements
    print(f"Vector C: {C}")
    print(f"Sum of all elements: {total_sum}")
    print(f"Number of elements: {total_elements}")
    print(f"Manual average (sum/count): {manual_average}")
    print()
    return manual_average


def exercise_8():
    """Exercise 8: Calculate Average with NumPy
    Objective: Find the average of vector 'C' elements using NumPy's specific function.
    """
    print("=== Exercise 8: Calculate Average with NumPy ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    numpy_average = np.average(C)
    print(f"Vector C: {C}")
    print(f"Average using np.average(): {numpy_average}")
    print()
    return numpy_average


def exercise_9():
    """Exercise 9: Calculate Mean with NumPy
    Objective: Find the arithmetic mean of vector 'C' elements using NumPy's own function.
    """
    print("=== Exercise 9: Calculate Mean with NumPy ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    numpy_mean = np.mean(C)
    print(f"Vector C: {C}")
    print(f"Mean using np.mean(): {numpy_mean}")
    print()
    return numpy_mean


def exercise_10():
    """Exercise 10: Sum of All Elements
    Objective: Calculate the sum of all elements contained in vector 'C' using a NumPy function.
    """
    print("=== Exercise 10: Sum of All Elements ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    total_sum = np.sum(C)
    print(f"Vector C: {C}")
    print(f"Sum of all elements: {total_sum}")
    print(f"Alternative using np.add.reduce(): {np.add.reduce(C)}")
    print()
    return total_sum


def exercise_11():
    """Exercise 11: Boolean Indexing Filtering (Simple)
    Objective: Create a new vector 'D' containing only elements from vector 'C' that are greater than 5.
    """
    print("=== Exercise 11: Boolean Indexing Filtering (Simple) ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    D = C[C > 5]
    print(f"Vector C: {C}")
    print(f"Boolean mask (C > 5): {C > 5}")
    print(f"Vector D (elements > 5): {D}")
    print(f"Number of elements in D: {len(D)}")
    print()
    return D


def exercise_12():
    """Exercise 12: Boolean Indexing Filtering (Compound)
    Objective: Create a new vector 'E' filtering 'C' to include only elements greater than 5 and less than 15.
    """
    print("=== Exercise 12: Boolean Indexing Filtering (Compound) ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    mask = (C > 5) & (C < 15)
    E = C[mask]
    print(f"Vector C: {C}")
    print(f"Boolean mask ((C > 5) & (C < 15)): {mask}")
    print(f"Vector E (5 < elements < 15): {E}")
    print(f"Number of elements in E: {len(E)}")
    print()
    return E


def exercise_13():
    """Exercise 13: Element Modification by Index
    Objective: Replace values at the fifth and fifteenth position of vector 'C' with the number 7.
    """
    print("=== Exercise 13: Element Modification by Index ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    C_modified = C.copy()  # Create a copy to preserve original
    print(f"Original Vector C: {C}")
    print(f"Original values at positions 5 and 15: C[4]={C[4]}, C[14]={C[14]}")
    C_modified[4] = 7   # Fifth position (0-indexed)
    C_modified[14] = 7  # Fifteenth position (0-indexed)
    print(f"Modified Vector C: {C_modified}")
    print(f"New values at positions 5 and 15: C[4]={C_modified[4]}, C[14]={C_modified[14]}")
    print()
    return C_modified


def exercise_14():
    """Exercise 14: Calculate Mode
    Objective: Determine which value appears most frequently within vector 'C'.
    """
    print("=== Exercise 14: Calculate Mode ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])

    # Count frequency of each element
    unique_elements, counts = np.unique(C, return_counts=True)
    max_count = np.max(counts)
    mode_indices = np.where(counts == max_count)[0]
    modes = unique_elements[mode_indices]

    print(f"Vector C: {C}")
    print(f"Unique elements: {unique_elements}")
    print(f"Counts: {counts}")
    print(f"Maximum frequency: {max_count}")
    print(f"Mode(s): {modes}")

    if len(modes) == len(unique_elements):
        print("All elements appear with the same frequency (no mode)")
    else:
        print(f"The most frequent value(s): {modes}")
    print()
    return modes


def exercise_15():
    """Exercise 15: Vector Sorting
    Objective: Sort all elements of vector 'C' in ascending order, from lowest to highest value.
    """
    print("=== Exercise 15: Vector Sorting ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    C_sorted = np.sort(C)
    print(f"Original Vector C: {C}")
    print(f"Sorted Vector C (ascending): {C_sorted}")
    print(f"Sorted indices: {np.argsort(C)}")
    print()
    return C_sorted


def exercise_16():
    """Exercise 16: Scalar Operation (Multiplication)
    Objective: Multiply each element of vector 'C' by the scalar 10.
    """
    print("=== Exercise 16: Scalar Operation (Multiplication) ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    C_multiplied = C * 10
    print(f"Original Vector C: {C}")
    print(f"Vector C multiplied by 10: {C_multiplied}")
    print(f"Data type of result: {C_multiplied.dtype}")
    print()
    return C_multiplied


def exercise_17():
    """Exercise 17: Range Element Modification
    Objective: Replace elements from sixth to eighth in vector 'C' with values 60, 70, and 80, respectively.
    """
    print("=== Exercise 17: Range Element Modification ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    C_modified = C.copy()  # Create a copy to preserve original
    print(f"Original Vector C: {C}")
    print(f"Original values at positions 6-8: {C[5:8]}")  # 0-indexed: 5, 6, 7
    C_modified[5:8] = [60, 70, 80]  # Sixth to eighth positions (0-indexed: 5, 6, 7)
    print(f"Modified Vector C: {C_modified}")
    print(f"New values at positions 6-8: {C_modified[5:8]}")
    print()
    return C_modified


def exercise_18():
    """Exercise 18: Another Range Element Modification
    Objective: Replace elements from fourteenth to sixteenth in vector 'C' with values 140, 150, and 160.
    """
    print("=== Exercise 18: Another Range Element Modification ===")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.arange(11, 21)
    C = np.concatenate([A, B])
    C_modified = C.copy()  # Create a copy to preserve original
    print(f"Original Vector C: {C}")
    print(f"Original values at positions 14-16: {C[13:16]}")  # 0-indexed: 13, 14, 15
    C_modified[13:16] = [140, 150, 160]  # Fourteenth to sixteenth positions (0-indexed: 13, 14, 15)
    print(f"Modified Vector C: {C_modified}")
    print(f"New values at positions 14-16: {C_modified[13:16]}")
    print()
    return C_modified


def run_all_exercises():
    """Run all exercises sequentially"""
    print("🚀 RUNNING ALL EXERCISES 🚀")
    print("=" * 60)
    print()

    exercises = [
        exercise_1, exercise_2, exercise_3, exercise_4, exercise_5,
        exercise_6, exercise_7, exercise_8, exercise_9, exercise_10,
        exercise_11, exercise_12, exercise_13, exercise_14, exercise_15,
        exercise_16, exercise_17, exercise_18
    ]

    for i, exercise in enumerate(exercises, 1):
        exercise()
        if i < len(exercises):
            input("Press Enter to continue to the next exercise...")
            print()

    print("✅ All exercises completed successfully!")
    print("=" * 60)
