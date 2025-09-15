import numpy as np

# 1. Creation and properties of numpy arrays

def create_array(input_list):
    return np.array(input_list)

def reshape_array(arr):
    return arr.reshape(2, 5)

def array_properties(arr):
    print('Array properties:')
    print('Shape:', arr.shape)
    print('Size:', arr.size)
    print('Number of dimensions:', arr.ndim)
    return arr.shape, arr.size, arr.ndim

def exercise_1():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr = create_array(input_list)
    array_properties(arr)
    reshaped_arr = reshape_array(arr)
    array_properties(reshaped_arr)

# 2. Basic operations with numpy arrays
def exercise_2():
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([10, 20, 30, 40, 50])
    print("Array 1:", array1)
    print("Array 2:", array2)
    print("Addition:", array1 + array2)
    print("Subtraction:", array2 - array1)
    print("Multiplication:", array1 * array2)
    print("Division:", array2 / array1)
    print("Exponentiation:", array1 ** 2)
    print("Square root of Array 2:", np.sqrt(array2))

# 3. Indexing and Slicing
def exercise_3():
    data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    print("Fifth element:", data[4])
    print("Subsection (indices 2 to 6):", data[2:7])

# 4. Broadcasting and Universal Functions
def exercise_4():
    matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("A + 10:", matrix_a + 10)
    print("Square root of A:", np.sqrt(matrix_a))

# 5. Shape Manipulation and Linear Algebra
def exercise_5():
    matrix_m = np.array([[1, 2, 3, 4, 5, 6]])
    reshaped_matrix = matrix_m.reshape(3, 2)
    print("M reshape (3,2):", reshaped_matrix)
    print("Dot product M and M.T:", np.dot(reshaped_matrix, reshaped_matrix.T))

# 6. Working with Missing Data
def exercise_6():
    data = np.array([1, 2, np.nan, 4, 5])
    clean_data = np.nan_to_num(data, nan=0)
    print("Array without NaN:", clean_data)
    print("Array mean:", np.mean(clean_data))

# 7. Save and Load Arrays
def exercise_7():
    data = np.array([100, 200, 300])
    np.save('my_array.npy', data)
    loaded_array = np.load('my_array.npy')
    print("Loaded array:", loaded_array)
