import numpy as np
import matplotlib.pyplot as plt


def factorial(n):
    """Calculate factorial of n"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def exercise_1():
    """Exercise 1: Exponential Function Approximation
    Objective: Implement a Python function that approximates the value of e^x using its Taylor series expansion:
    e^x = 1 + x + x²/2! + x³/3! + ...
    """
    print("=== Exercise 1: Exponential Function Approximation ===")

    def taylor_exp(x, terms=10):
        """Approximate e^x using Taylor series"""
        result = 0
        for n in range(terms):
            result += (x ** n) / factorial(n)
        return result

    # Test values
    test_values = [-2, -1, 0, 1, 2]

    print("Comparing Taylor approximation vs NumPy exp:")
    print(f"{'x':<5} {'Taylor (10 terms)':<15} {'NumPy exp':<12} {'Error':<10}")
    print("-" * 50)

    for x in test_values:
        taylor_val = taylor_exp(x, 10)
        numpy_val = np.exp(x)
        error = abs(taylor_val - numpy_val)
        print(f"{x:<5} {taylor_val:<15.6f} {numpy_val:<12.6f} {error:<10.2e}")

    # Plot comparison
    x_range = np.linspace(-3, 3, 100)
    taylor_values = [taylor_exp(x, 15) for x in x_range]
    numpy_values = np.exp(x_range)

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, numpy_values, 'b-', label='NumPy exp(x)', linewidth=2)
    plt.plot(x_range, taylor_values, 'r--', label='Taylor approximation (15 terms)', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('e^x')
    plt.title('Exponential Function: Taylor Series vs NumPy')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    print("Exponential function approximation completed!")
    print()
    return taylor_exp


def exercise_2():
    """Exercise 2: Sine Function Approximation
    Objective: Implement a Python function that approximates the value of sin(x) using its Taylor series expansion:
    sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...
    """
    print("=== Exercise 2: Sine Function Approximation ===")

    def taylor_sin(x, terms=10):
        """Approximate sin(x) using Taylor series"""
        result = 0
        for n in range(terms):
            # Only odd powers with alternating signs
            power = 2 * n + 1
            sign = (-1) ** n
            result += sign * (x ** power) / factorial(power)
        return result

    # Test values (in radians)
    test_values = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]

    print("Comparing Taylor approximation vs NumPy sin:")
    print(f"{'x (rad)':<8} {'Taylor (10 terms)':<15} {'NumPy sin':<12} {'Error':<10}")
    print("-" * 55)

    for x in test_values:
        taylor_val = taylor_sin(x, 10)
        numpy_val = np.sin(x)
        error = abs(taylor_val - numpy_val)
        print(f"{x:<8.3f} {taylor_val:<15.6f} {numpy_val:<12.6f} {error:<10.2e}")

    # Plot comparison
    x_range = np.linspace(-2*np.pi, 2*np.pi, 200)
    taylor_values = [taylor_sin(x, 15) for x in x_range]
    numpy_values = np.sin(x_range)

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, numpy_values, 'b-', label='NumPy sin(x)', linewidth=2)
    plt.plot(x_range, taylor_values, 'r--', label='Taylor approximation (15 terms)', linewidth=2)
    plt.xlabel('x (radians)')
    plt.ylabel('sin(x)')
    plt.title('Sine Function: Taylor Series vs NumPy')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)
    plt.tight_layout()
    plt.show()

    print("Sine function approximation completed!")
    print()
    return taylor_sin


def exercise_3():
    """Exercise 3: Cosine Function Approximation
    Objective: Implement a Python function that approximates the value of cos(x) using its Taylor series expansion:
    cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...
    """
    print("=== Exercise 3: Cosine Function Approximation ===")

    def taylor_cos(x, terms=10):
        """Approximate cos(x) using Taylor series"""
        result = 0
        for n in range(terms):
            # Only even powers with alternating signs
            power = 2 * n
            sign = (-1) ** n
            result += sign * (x ** power) / factorial(power)
        return result

    # Test values (in radians)
    test_values = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]

    print("Comparing Taylor approximation vs NumPy cos:")
    print(f"{'x (rad)':<8} {'Taylor (10 terms)':<15} {'NumPy cos':<12} {'Error':<10}")
    print("-" * 55)

    for x in test_values:
        taylor_val = taylor_cos(x, 10)
        numpy_val = np.cos(x)
        error = abs(taylor_val - numpy_val)
        print(f"{x:<8.3f} {taylor_val:<15.6f} {numpy_val:<12.6f} {error:<10.2e}")

    # Plot comparison
    x_range = np.linspace(-2*np.pi, 2*np.pi, 200)
    taylor_values = [taylor_cos(x, 15) for x in x_range]
    numpy_values = np.cos(x_range)

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, numpy_values, 'b-', label='NumPy cos(x)', linewidth=2)
    plt.plot(x_range, taylor_values, 'r--', label='Taylor approximation (15 terms)', linewidth=2)
    plt.xlabel('x (radians)')
    plt.ylabel('cos(x)')
    plt.title('Cosine Function: Taylor Series vs NumPy')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)
    plt.tight_layout()
    plt.show()

    print("Cosine function approximation completed!")
    print()
    return taylor_cos


def exercise_4():
    """Exercise 4: Natural Logarithm Approximation
    Objective: Implement a Python function that approximates the value of ln(1+x) for |x|<1 using its Taylor series expansion:
    ln(1+x) = x - x²/2 + x³/3 - x⁴/4 + ...
    """
    print("=== Exercise 4: Natural Logarithm Approximation ===")

    def taylor_ln(x, terms=20):
        """Approximate ln(1+x) using Taylor series for |x| < 1"""
        if abs(x) >= 1:
            print(f"Warning: |x| = {abs(x)} >= 1, series may not converge")

        result = 0
        for n in range(1, terms + 1):
            sign = (-1) ** (n + 1)
            result += sign * (x ** n) / n
        return result

    # Test values (|x| < 1)
    test_values = [-0.9, -0.5, 0, 0.5, 0.9]

    print("Comparing Taylor approximation vs NumPy log:")
    print(f"{'x':<5} {'1+x':<8} {'Taylor (20 terms)':<16} {'NumPy log':<12} {'Error':<10}")
    print("-" * 65)

    for x in test_values:
        taylor_val = taylor_ln(x, 20)
        numpy_val = np.log(1 + x)
        error = abs(taylor_val - numpy_val)
        print(f"{x:<5} {1+x:<8.2f} {taylor_val:<16.6f} {numpy_val:<12.6f} {error:<10.2e}")

    # Plot comparison
    x_range = np.linspace(-0.99, 0.99, 200)
    taylor_values = [taylor_ln(x, 25) for x in x_range]
    numpy_values = np.log(1 + x_range)

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, numpy_values, 'b-', label='NumPy log(1+x)', linewidth=2)
    plt.plot(x_range, taylor_values, 'r--', label='Taylor approximation (25 terms)', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('ln(1+x)')
    plt.title('Natural Logarithm: Taylor Series vs NumPy')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)
    plt.tight_layout()
    plt.show()

    print("Natural logarithm approximation completed!")
    print()
    return taylor_ln


def exercise_5():
    """Exercise 5: Tangent Function Approximation
    Objective: Implement a Python function that approximates the value of the tangent function,
    using the relation tan(x) = sin(x) / cos(x) with the previously developed series.
    """
    print("=== Exercise 5: Tangent Function Approximation ===")

    def taylor_sin(x, terms=15):
        """Approximate sin(x) using Taylor series"""
        result = 0
        for n in range(terms):
            power = 2 * n + 1
            sign = (-1) ** n
            result += sign * (x ** power) / factorial(power)
        return result

    def taylor_cos(x, terms=15):
        """Approximate cos(x) using Taylor series"""
        result = 0
        for n in range(terms):
            power = 2 * n
            sign = (-1) ** n
            result += sign * (x ** power) / factorial(power)
        return result

    def taylor_tan(x, terms=15):
        """Approximate tan(x) using sin(x)/cos(x) with Taylor series"""
        sin_val = taylor_sin(x, terms)
        cos_val = taylor_cos(x, terms)

        if abs(cos_val) < 1e-10:
            return float('inf') if sin_val > 0 else float('-inf')

        return sin_val / cos_val

    # Test values (avoiding points where tan is undefined)
    test_values = [-np.pi/3, -np.pi/6, 0, np.pi/6, np.pi/3]

    print("Comparing Taylor approximation vs NumPy tan:")
    print(f"{'x (rad)':<8} {'Taylor (15 terms)':<16} {'NumPy tan':<12} {'Error':<10}")
    print("-" * 56)

    for x in test_values:
        taylor_val = taylor_tan(x, 15)
        numpy_val = np.tan(x)
        error = abs(taylor_val - numpy_val)
        print(f"{x:<8.3f} {taylor_val:<16.6f} {numpy_val:<12.6f} {error:<10.2e}")

    # Plot comparison (avoiding singularities)
    x_range = np.linspace(-np.pi/3, np.pi/3, 200)
    taylor_values = [taylor_tan(x, 15) for x in x_range]
    numpy_values = np.tan(x_range)

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, numpy_values, 'b-', label='NumPy tan(x)', linewidth=2)
    plt.plot(x_range, taylor_values, 'r--', label='Taylor approximation (15 terms)', linewidth=2)
    plt.xlabel('x (radians)')
    plt.ylabel('tan(x)')
    plt.title('Tangent Function: Taylor Series vs NumPy')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)
    plt.ylim(-5, 5)  # Limit y-axis to avoid plotting large values near singularities
    plt.tight_layout()
    plt.show()

    print("Tangent function approximation completed!")
    print()
    return taylor_tan


def exercise_6():
    """Exercise 6: Comparative Visualization of Functions
    Objective: Use Matplotlib to plot all implemented functions in the same subplot,
    facilitating a direct visual comparison between them.
    """
    print("=== Exercise 6: Comparative Visualization of Functions ===")

    # Define Taylor series functions
    def taylor_exp(x, terms=15):
        result = 0
        for n in range(terms):
            result += (x ** n) / factorial(n)
        return result

    def taylor_sin(x, terms=15):
        result = 0
        for n in range(terms):
            power = 2 * n + 1
            sign = (-1) ** n
            result += sign * (x ** power) / factorial(power)
        return result

    def taylor_cos(x, terms=15):
        result = 0
        for n in range(terms):
            power = 2 * n
            sign = (-1) ** n
            result += sign * (x ** power) / factorial(power)
        return result

    def taylor_ln(x, terms=20):
        if abs(x) >= 1:
            return float('nan')
        result = 0
        for n in range(1, terms + 1):
            sign = (-1) ** (n + 1)
            result += sign * (x ** n) / n
        return result

    def taylor_tan(x, terms=15):
        sin_val = taylor_sin(x, terms)
        cos_val = taylor_cos(x, terms)
        if abs(cos_val) < 1e-10:
            return float('nan')
        return sin_val / cos_val

    # Create comprehensive comparison plot - FIX: Correct subplot unpacking
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    ax1, ax2, ax3 = axes[0]
    ax4, ax5, ax6 = axes[1]

    # 1. Exponential function
    x_exp = np.linspace(-2, 2, 200)
    taylor_exp_vals = [taylor_exp(x, 15) for x in x_exp]
    numpy_exp_vals = np.exp(x_exp)

    ax1.plot(x_exp, numpy_exp_vals, 'b-', label='NumPy exp(x)', linewidth=2)
    ax1.plot(x_exp, taylor_exp_vals, 'r--', label='Taylor (15 terms)', linewidth=2)
    ax1.set_xlabel('x')
    ax1.set_ylabel('e^x')
    ax1.set_title('Exponential Function')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2. Sine function
    x_trig = np.linspace(-2*np.pi, 2*np.pi, 200)
    taylor_sin_vals = [taylor_sin(x, 15) for x in x_trig]
    numpy_sin_vals = np.sin(x_trig)

    ax2.plot(x_trig, numpy_sin_vals, 'b-', label='NumPy sin(x)', linewidth=2)
    ax2.plot(x_trig, taylor_sin_vals, 'r--', label='Taylor (15 terms)', linewidth=2)
    ax2.set_xlabel('x (radians)')
    ax2.set_ylabel('sin(x)')
    ax2.set_title('Sine Function')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # 3. Cosine function
    taylor_cos_vals = [taylor_cos(x, 15) for x in x_trig]
    numpy_cos_vals = np.cos(x_trig)

    ax3.plot(x_trig, numpy_cos_vals, 'b-', label='NumPy cos(x)', linewidth=2)
    ax3.plot(x_trig, taylor_cos_vals, 'r--', label='Taylor (15 terms)', linewidth=2)
    ax3.set_xlabel('x (radians)')
    ax3.set_ylabel('cos(x)')
    ax3.set_title('Cosine Function')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # 4. Natural logarithm
    x_ln = np.linspace(-0.95, 0.95, 200)
    taylor_ln_vals = [taylor_ln(x, 25) for x in x_ln]
    numpy_ln_vals = np.log(1 + x_ln)

    ax4.plot(x_ln, numpy_ln_vals, 'b-', label='NumPy log(1+x)', linewidth=2)
    ax4.plot(x_ln, taylor_ln_vals, 'r--', label='Taylor (25 terms)', linewidth=2)
    ax4.set_xlabel('x')
    ax4.set_ylabel('ln(1+x)')
    ax4.set_title('Natural Logarithm')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # 5. Tangent function
    x_tan = np.linspace(-np.pi/3, np.pi/3, 200)
    taylor_tan_vals = [taylor_tan(x, 15) for x in x_tan]
    numpy_tan_vals = np.tan(x_tan)

    ax5.plot(x_tan, numpy_tan_vals, 'b-', label='NumPy tan(x)', linewidth=2)
    ax5.plot(x_tan, taylor_tan_vals, 'r--', label='Taylor (15 terms)', linewidth=2)
    ax5.set_xlabel('x (radians)')
    ax5.set_ylabel('tan(x)')
    ax5.set_title('Tangent Function')
    ax5.legend()
    ax5.grid(True, alpha=0.3)
    ax5.set_ylim(-3, 3)

    # 6. All functions together (normalized view)
    x_all = np.linspace(-1, 1, 200)

    # Normalize functions to similar scales for comparison
    exp_norm = np.exp(x_all) / np.exp(1)  # Normalize by e
    sin_norm = np.sin(x_all)
    cos_norm = np.cos(x_all)
    ln_norm = np.log(1 + x_all * 0.5)  # Scale x to avoid domain issues

    ax6.plot(x_all, exp_norm, label='e^x (normalized)', linewidth=2)
    ax6.plot(x_all, sin_norm, label='sin(x)', linewidth=2)
    ax6.plot(x_all, cos_norm, label='cos(x)', linewidth=2)
    ax6.plot(x_all, ln_norm, label='ln(1+0.5x)', linewidth=2)
    ax6.set_xlabel('x')
    ax6.set_ylabel('Function value')
    ax6.set_title('All Functions Comparison')
    ax6.legend()
    ax6.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    print("Comparative visualization completed!")
    print("Summary of Taylor series implementations:")
    print("• Exponential: e^x = Σ(x^n/n!) for n=0 to ∞")
    print("• Sine: sin(x) = Σ((-1)^n * x^(2n+1)/(2n+1)!) for n=0 to ∞")
    print("• Cosine: cos(x) = Σ((-1)^n * x^(2n)/(2n)!) for n=0 to ∞")
    print("• Natural log: ln(1+x) = Σ((-1)^(n+1) * x^n/n) for n=1 to ∞, |x|<1")
    print("• Tangent: tan(x) = sin(x)/cos(x) using Taylor approximations")
    print()


def run_all_exercises():
    """Run all exercises sequentially"""
    print("🚀 RUNNING ALL EXERCISES 🚀")
    print("=" * 60)
    print()

    exercises = [
        exercise_1, exercise_2, exercise_3, exercise_4, exercise_5, exercise_6
    ]

    for i, exercise in enumerate(exercises, 1):
        exercise()
        if i < len(exercises):
            input("Press Enter to continue to the next exercise...")
            print()

    print("✅ All exercises completed successfully!")
    print("📊 All Taylor series approximations have been implemented and visualized!")
    print("=" * 60)
