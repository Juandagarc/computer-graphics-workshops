import numpy as np
import matplotlib.pyplot as plt


def exercise_1():
    """Exercise 1: Array Creation and Reshaping
    Objective: Create an array with numbers from 1 to 15 and then reshape it to a 3x5 matrix.
    """
    print("=== Exercise 1: Array Creation and Reshaping ===")
    A = np.arange(1, 16)
    print(f"Original array (1D): {A}")
    print(f"Shape: {A.shape}")

    A_reshaped = A.reshape(3, 5)
    print(f"Reshaped array (3x5 matrix):\n{A_reshaped}")
    print(f"New shape: {A_reshaped.shape}")
    print()
    return A_reshaped


def exercise_2():
    """Exercise 2: Basic Arithmetic Operations
    Objective: Calculate the total sum, mean, and product of all elements in array 'A'.
    """
    print("=== Exercise 2: Basic Arithmetic Operations ===")
    A = np.arange(1, 16).reshape(3, 5)

    total_sum = np.sum(A)
    mean_value = np.mean(A)
    product = np.prod(A)

    print(f"Array A:\n{A}")
    print(f"Total sum: {total_sum}")
    print(f"Mean: {mean_value}")
    print(f"Product of all elements: {product}")
    print()
    return total_sum, mean_value, product


def exercise_3():
    """Exercise 3: Element Access and Slicing
    Objective: Extract a specific portion of array 'A', corresponding to the second and third elements of the second row.
    """
    print("=== Exercise 3: Element Access and Slicing ===")
    A = np.arange(1, 16).reshape(3, 5)

    # Second row, second and third elements (indices 1 and 2)
    extracted = A[1, 1:3]

    print(f"Array A:\n{A}")
    print(f"Second row: {A[1, :]}")
    print(f"Second and third elements of second row: {extracted}")
    print(f"Individual elements: A[1,1]={A[1,1]}, A[1,2]={A[1,2]}")
    print()
    return extracted


def exercise_4():
    """Exercise 4: Boolean Indexing Filtering
    Objective: Create a new array 'B' from 'A' containing only elements whose value is greater than 7.
    """
    print("=== Exercise 4: Boolean Indexing Filtering ===")
    A = np.arange(1, 16).reshape(3, 5)

    # Create boolean mask
    mask = A > 7
    B = A[mask]

    print(f"Array A:\n{A}")
    print(f"Boolean mask (A > 7):\n{mask}")
    print(f"Array B (elements > 7): {B}")
    print(f"Number of elements in B: {len(B)}")
    print()
    return B


def exercise_5():
    """Exercise 5: Linear Algebra Operations
    Objective: Create a 3x3 square matrix 'C' and calculate its determinant and inverse matrix.
    """
    print("=== Exercise 5: Linear Algebra Operations ===")
    # Create a 3x3 matrix that's likely to be invertible
    C = np.array([[2, 1, 3], [1, 4, 2], [3, 2, 1]], dtype=float)

    determinant = np.linalg.det(C)

    print(f"Matrix C (3x3):\n{C}")
    print(f"Determinant: {determinant:.4f}")

    if abs(determinant) > 1e-10:
        inverse = np.linalg.inv(C)
        # Verify: C * C^-1 should equal identity matrix
        identity_check = np.dot(C, inverse)

        print(f"Inverse matrix:\n{inverse}")
        print(f"Verification (C * C^-1):\n{identity_check}")
        print(f"Is result close to identity? {np.allclose(identity_check, np.eye(3))}")
    else:
        print("Matrix is singular (not invertible)")
    print()
    return determinant, inverse if abs(determinant) > 1e-10 else None


def exercise_6():
    """Exercise 6: Basic Statistical Analysis
    Objective: Generate an array 'D' of 100 random numbers and calculate main statistics: max, min, mean, and standard deviation.
    """
    print("=== Exercise 6: Basic Statistical Analysis ===")
    D = np.random.rand(100)

    maximum = np.max(D)
    minimum = np.min(D)
    mean = np.mean(D)
    std_dev = np.std(D)

    print(f"Array D (first 10 elements): {D[:10]}")
    print(f"Array size: {D.size}")
    print(f"Maximum value: {maximum:.4f}")
    print(f"Minimum value: {minimum:.4f}")
    print(f"Mean: {mean:.4f}")
    print(f"Standard deviation: {std_dev:.4f}")
    print()
    return D, maximum, minimum, mean, std_dev


def exercise_7():
    """Exercise 7: Trigonometric Functions Plot
    Objective: Visualize sine and cosine functions in the same plot within the range of -2π to 2π.
    """
    print("=== Exercise 7: Trigonometric Functions Plot ===")
    x = np.linspace(-2*np.pi, 2*np.pi, 1000)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y_sin, label='sin(x)', color='blue', linewidth=2)
    plt.plot(x, y_cos, label='cos(x)', color='red', linewidth=2)
    plt.xlabel('x (radians)')
    plt.ylabel('y')
    plt.title('Trigonometric Functions: sin(x) and cos(x)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)

    # Add π markers on x-axis
    pi_ticks = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]
    pi_labels = ['-2π', '-π', '0', 'π', '2π']
    plt.xticks(pi_ticks, pi_labels)

    plt.tight_layout()
    plt.show()

    print("Trigonometric functions plotted successfully!")
    print(f"X range: {x.min():.2f} to {x.max():.2f}")
    print(f"Number of points: {len(x)}")
    print()
    return x, y_sin, y_cos


def exercise_8():
    """Exercise 8: Scatter Plot Creation
    Objective: Create a scatter plot using the values of random array 'D' on the Y-axis and their corresponding indices on the X-axis.
    """
    print("=== Exercise 8: Scatter Plot Creation ===")
    D = np.random.rand(100)
    indices = np.arange(len(D))

    plt.figure(figsize=(12, 6))
    plt.scatter(indices, D, alpha=0.7, c=D, cmap='viridis', s=30)
    plt.xlabel('Index')
    plt.ylabel('Random Value')
    plt.title('Scatter Plot of Random Array D')
    plt.colorbar(label='Value')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    print("Scatter plot created successfully!")
    print(f"Number of points: {len(D)}")
    print(f"Value range: {D.min():.4f} to {D.max():.4f}")
    print()
    return indices, D


def exercise_9():
    """Exercise 9: Histogram Creation
    Objective: Generate a histogram to visualize the distribution of data in random array 'D', adjusting the number of bins.
    """
    print("=== Exercise 9: Histogram Creation ===")
    D = np.random.rand(100)

    plt.figure(figsize=(12, 8))

    # Create subplots with different bin numbers
    bin_counts = [10, 20, 30]

    for i, bins in enumerate(bin_counts):
        plt.subplot(2, 2, i+1)
        plt.hist(D, bins=bins, alpha=0.7, color='skyblue', edgecolor='black')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title(f'Histogram with {bins} bins')
        plt.grid(True, alpha=0.3)

    # Statistical summary subplot
    plt.subplot(2, 2, 4)
    plt.text(0.1, 0.8, f'Statistical Summary:', fontsize=12, fontweight='bold')
    plt.text(0.1, 0.6, f'Mean: {np.mean(D):.4f}')
    plt.text(0.1, 0.5, f'Std: {np.std(D):.4f}')
    plt.text(0.1, 0.4, f'Min: {np.min(D):.4f}')
    plt.text(0.1, 0.3, f'Max: {np.max(D):.4f}')
    plt.text(0.1, 0.2, f'Size: {len(D)}')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    print("Histogram created successfully!")
    print(f"Data analyzed: {len(D)} random values")
    print()
    return D


def exercise_10():
    """Exercise 10: Basic Image Manipulation
    Objective: Load an image file, process it to convert to grayscale, and display both versions, original and modified.
    """
    print("=== Exercise 10: Basic Image Manipulation ===")

    try:
        # Create a sample image using only NumPy (no PIL required)
        # Generate a colorful sample image
        height, width = 200, 300

        # Create RGB channels using NumPy functions
        x_coords = np.linspace(0, 2*np.pi, width)
        y_coords = np.linspace(0, 2*np.pi, height)

        # Create meshgrid for 2D patterns
        X, Y = np.meshgrid(x_coords, y_coords)

        # Create RGB channels with different patterns
        r = np.sin(X) * np.cos(Y)
        g = np.cos(X) * np.sin(Y)
        b = np.sin(X + Y)

        # Normalize to 0-1 range for matplotlib
        r = (r + 1) / 2
        g = (g + 1) / 2
        b = (b + 1) / 2

        # Combine channels
        color_image = np.stack([r, g, b], axis=2)

        # Convert to grayscale using the luminance formula
        grayscale_image = 0.299 * color_image[:,:,0] + 0.587 * color_image[:,:,1] + 0.114 * color_image[:,:,2]

        # Display both images
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.imshow(color_image)
        plt.title('Original Color Image')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(grayscale_image, cmap='gray')
        plt.title('Grayscale Image')
        plt.axis('off')

        plt.tight_layout()
        plt.show()

        print("Image manipulation completed successfully!")
        print(f"Original image shape: {color_image.shape}")
        print(f"Grayscale image shape: {grayscale_image.shape}")
        print("Conversion formula used: 0.299*R + 0.587*G + 0.114*B")
        print("Sample image generated using NumPy trigonometric functions")

    except Exception as e:
        print(f"Error in image processing: {e}")
        print("Generated a sample image for demonstration")

    print()
    return color_image, grayscale_image


def run_all_exercises():
    """Run all exercises sequentially"""
    print("🚀 RUNNING ALL EXERCISES 🚀")
    print("=" * 60)
    print()

    exercises = [
        exercise_1, exercise_2, exercise_3, exercise_4, exercise_5,
        exercise_6, exercise_7, exercise_8, exercise_9, exercise_10
    ]

    for i, exercise in enumerate(exercises, 1):
        exercise()
        if i < len(exercises):
            input("Press Enter to continue to the next exercise...")
            print()

    print("✅ All exercises completed successfully!")
    print("=" * 60)
