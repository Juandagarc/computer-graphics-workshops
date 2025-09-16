# Workshop 7: Function Approximation with Taylor Series 🐍

This document contains the solution to the exercises proposed in Workshop 7 on function approximation using Taylor Series in Python.

**Created by:** Juan David García Arce

---

## 📝 Solved Exercises

The workshop consists of developing custom versions of various mathematical functions using their Taylor series expansions and then visualizing them.

### **Exercise 1: Exponential Function Approximation**

**Objective:** Implement a Python function that approximates the value of e^x using its Taylor series expansion: e^x = 1 + x + x²/2! + x³/3! + ...

---

### **Exercise 2: Sine Function Approximation**

**Objective:** Implement a Python function that approximates the value of sin(x) using its Taylor series expansion: sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...

---

### **Exercise 3: Cosine Function Approximation**

**Objective:** Implement a Python function that approximates the value of cos(x) using its Taylor series expansion: cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...

---

### **Exercise 4: Natural Logarithm Approximation**

**Objective:** Implement a Python function that approximates the value of ln(1+x) for |x|<1 using its Taylor series expansion: ln(1+x) = x - x²/2 + x³/3 - x⁴/4 + ...

---

### **Exercise 5: Tangent Function Approximation**

**Objective:** Implement a Python function that approximates the value of the tangent function, using the relation tan(x) = sin(x) / cos(x) with the previously developed series.

---

### **Exercise 6: Comparative Visualization of Functions**

**Objective:** Use Matplotlib to plot all implemented functions in the same subplot, facilitating a direct visual comparison between them.

---

## How to Run

1. Navigate to the workshop-7 directory
2. Run the main script:
   ```bash
   python main.py
   ```
3. Choose option 1 to run all exercises
4. Follow the prompts and press Enter to progress through exercises

## Key Features

- **Simplified Menu**: Only "Run all exercises" and "Exit" options
- **Complete English Translation**: All code, comments, and output in English
- **Mathematical Accuracy**: Precise Taylor series implementations with error analysis
- **Comprehensive Visualizations**: Side-by-side comparisons of custom vs NumPy functions
- **Educational Value**: Detailed explanations of mathematical concepts

## Learning Objectives

By completing this workshop, you will:
- Understand Taylor series mathematical foundations
- Implement mathematical functions from first principles
- Analyze convergence and accuracy of infinite series
- Compare custom implementations with optimized library functions
- Create professional mathematical visualizations

## Mathematical Concepts Covered

- **Taylor Series Expansions**: Understanding infinite series representations
- **Factorial Calculations**: Implementing factorial functions efficiently
- **Convergence Analysis**: Studying how series approximate true values
- **Error Analysis**: Measuring approximation accuracy
- **Function Visualization**: Creating comparative plots

## Prerequisites

- Python 3.x
- NumPy library
- Matplotlib library
- Basic understanding of calculus and infinite series
