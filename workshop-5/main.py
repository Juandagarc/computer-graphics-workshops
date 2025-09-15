import os
import numpy as np
from exercises import (
    exercise_1, exercise_2, exercise_3, exercise_4, exercise_5,
    exercise_6, exercise_7, exercise_8, exercise_9, exercise_10,
    exercise_11, exercise_12, exercise_13, exercise_14, exercise_15,
    exercise_16, exercise_17, exercise_18, run_all_exercises
)


def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    """Display the main workshop menu"""
    print("🐍 WORKSHOP 5: Advanced NumPy Array Manipulation 🐍")
    print("=" * 60)
    print("Select an option:")
    print()
    print("1.  Exercise 1: Create a Specific Vector")
    print("2.  Exercise 2: Create a Vector with a Range")
    print("3.  Exercise 3: Vector Concatenation")
    print("4.  Exercise 4: Find Minimum Value")
    print("5.  Exercise 5: Find Maximum Value")
    print("6.  Exercise 6: Determine Vector Length")
    print("7.  Exercise 7: Calculate Average Manually")
    print("8.  Exercise 8: Calculate Average with NumPy")
    print("9.  Exercise 9: Calculate Mean with NumPy")
    print("10. Exercise 10: Sum of All Elements")
    print("11. Exercise 11: Boolean Indexing Filtering (Simple)")
    print("12. Exercise 12: Boolean Indexing Filtering (Compound)")
    print("13. Exercise 13: Element Modification by Index")
    print("14. Exercise 14: Calculate Mode")
    print("15. Exercise 15: Vector Sorting")
    print("16. Exercise 16: Scalar Operation (Multiplication)")
    print("17. Exercise 17: Range Element Modification")
    print("18. Exercise 18: Another Range Element Modification")
    print()
    print("19. Run all exercises")
    print("0.  Exit")
    print("=" * 60)


def get_valid_choice():
    """Get a valid option from the user"""
    while True:
        try:
            user_choice = input("\nEnter your option (0-19): ").strip()
            choice_number = int(user_choice)
            if 0 <= choice_number <= 19:
                return choice_number
            else:
                print("❌ Error: You must enter a number between 0 and 19.")
        except ValueError:
            print("❌ Error: You must enter a valid number.")


def execute_exercise(exercise_choice):
    """Execute the selected exercise"""
    clear_screen()

    exercise_functions = {
        1: exercise_1,
        2: exercise_2,
        3: exercise_3,
        4: exercise_4,
        5: exercise_5,
        6: exercise_6,
        7: exercise_7,
        8: exercise_8,
        9: exercise_9,
        10: exercise_10,
        11: exercise_11,
        12: exercise_12,
        13: exercise_13,
        14: exercise_14,
        15: exercise_15,
        16: exercise_16,
        17: exercise_17,
        18: exercise_18,
        19: run_all_exercises
    }

    if exercise_choice in exercise_functions:
        try:
            exercise_functions[exercise_choice]()
        except Exception as e:
            print(f"❌ Error executing exercise: {e}")
    else:
        print("❌ Invalid exercise number")

    if exercise_choice != 19:  # Don't pause after running all exercises
        input("\nPress Enter to return to the main menu...")


def main():
    """Main function to run the workshop"""
    print("Welcome to Workshop 5: Advanced NumPy Array Manipulation! 🎉")
    print()
    print("This workshop covers:")
    print("• Vector creation and manipulation")
    print("• Statistical operations (min, max, mean, mode)")
    print("• Boolean indexing and filtering")
    print("• Element modification and sorting")
    print("• Scalar operations and array transformations")
    print()
    input("Press Enter to continue...")

    while True:
        clear_screen()
        show_menu()

        choice = get_valid_choice()

        if choice == 0:
            clear_screen()
            print("🎉 Thank you for using Workshop 5!")
            print("👋 See you later!")
            break
        else:
            execute_exercise(choice)


if __name__ == "__main__":
    main()
