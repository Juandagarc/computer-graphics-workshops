import os
import numpy as np
from exercises import (
    exercise_1, exercise_2, exercise_3, exercise_4, exercise_5,
    exercise_6, exercise_7, exercise_8, exercise_9, exercise_10,
    run_all_exercises
)


def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    """Display the main workshop menu"""
    print("🐍 WORKSHOP 4: NumPy Array Management 🐍")
    print("=" * 50)
    print("Select an option:")
    print()
    print("1.  Exercise 1: Create a One-Dimensional Array")
    print("2.  Exercise 2: Create a Multidimensional Array")
    print("3.  Exercise 3: Basic Array Operations")
    print("4.  Exercise 4: Mathematical Functions")
    print("5.  Exercise 5: Indexing and Slicing")
    print("6.  Exercise 6: Random Data Generation")
    print("7.  Exercise 7: Aggregation Functions")
    print("8.  Exercise 8: Array Creation with Factory Functions")
    print("9.  Exercise 9: Broadcasting and Alignment Operations")
    print("10. Exercise 10: Transformation and Reshaping Functions")
    print()
    print("11. Run all exercises")
    print("0.  Exit")
    print("=" * 50)


def get_valid_choice():
    """Get a valid option from the user"""
    while True:
        try:
            user_choice = input("\nEnter your option (0-11): ").strip()
            choice_number = int(user_choice)
            if 0 <= choice_number <= 11:
                return choice_number
            else:
                print("❌ Error: You must enter a number between 0 and 11.")
        except ValueError:
            print("❌ Error: You must enter a valid number.")


def execute_exercise(exercise_choice):
    """Execute the selected exercise"""
    exercises = {
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
        11: run_all_exercises
    }

    if exercise_choice in exercises:
        clear_screen()
        print("🚀 Executing exercise...\n")
        try:
            exercises[exercise_choice]()
        except Exception as e:
            print(f"❌ Error executing exercise: {e}")

        input("\n📱 Press Enter to continue...")
    else:
        print("❌ Invalid option.")


def show_numpy_info():
    """Display information about installed NumPy"""
    print(f"📊 NumPy Version: {np.__version__}")
    print(f"🐍 Python Version: {os.sys.version}")
    print()


def main():
    """Main program function"""
    while True:
        clear_screen()
        show_numpy_info()
        show_menu()

        selected_choice = get_valid_choice()

        if selected_choice == 0:
            clear_screen()
            print("🎉 Thank you for using Workshop 4 - NumPy!")
            print("👋 See you later!")
            break
        else:
            execute_exercise(selected_choice)


if __name__ == "__main__":
    main()
