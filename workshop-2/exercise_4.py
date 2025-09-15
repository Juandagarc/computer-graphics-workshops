# Exercise 4: Grade Conversion
# Objective: Implement a function that converts a list of numerical grades to their letter equivalent (A, B, C, D, F)

def convert_grades(numerical_grades):
    """Converts numerical grades to letters"""
    letter_grades = []

    for grade in numerical_grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')

    return letter_grades

def grades_exercise():
    """Grade conversion demonstration exercise"""
    scores = [95, 87, 76, 65, 45, 92, 58, 83]
    print(f"Numerical grades: {scores}")
    letters = convert_grades(scores)
    print(f"Letter grades: {letters}")

    # Mostrar la conversión detallada
    print("\nDetailed conversion:")
    for score, letter in zip(scores, letters):
        print(f"{score} → {letter}")
