import os
import numpy as np
from exercises import run_all_exercises


def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    """Display the main workshop menu"""
    print("📊 WORKSHOP 6: Numerical Analysis with NumPy and Data Visualization with Matplotlib 📊")
    print("=" * 85)
    print("Welcome to Workshop 6!")
    print()
    print("This workshop covers numerical analysis and data visualization including:")
    print("• Array creation and manipulation")
    print("• Basic arithmetic operations and statistics")
    print("• Element access and boolean indexing")
    print("• Linear algebra operations")
    print("• Data visualization with matplotlib")
    print("• Trigonometric function plotting")
    print("• Scatter plots and histograms")
    print("• Basic image processing")
    print()
    print("Select an option:")
    print()
    print("1. Run all exercises")
    print("0. Exit")
    print("=" * 85)


def get_valid_choice():
    """Get a valid option from the user"""
    while True:
        try:
            user_choice = input("\nEnter your option (0-1): ").strip()
            choice_number = int(user_choice)
            if 0 <= choice_number <= 1:
                return choice_number
            else:
                print("❌ Error: You must enter either 0 or 1.")
        except ValueError:
            print("❌ Error: You must enter a valid number.")


def execute_choice(choice):
    """Execute the selected option"""
    if choice == 1:
        clear_screen()
        try:
            run_all_exercises()
        except Exception as e:
            print(f"❌ Error executing exercises: {e}")
        input("\nPress Enter to return to the main menu...")
    elif choice == 0:
        clear_screen()
        print("🎉 Thank you for using Workshop 6!")
        print("👋 See you later!")
        return False

    return True


def main():
    """Main function to run the workshop"""
    print("Welcome to Workshop 6: Numerical Analysis with NumPy and Data Visualization! 🎉")
    print()
    print("In this workshop, you will explore:")
    print("• Creating and reshaping NumPy arrays")
    print("• Performing arithmetic operations and statistical analysis")
    print("• Working with matrix operations and linear algebra")
    print("• Creating beautiful visualizations with Matplotlib")
    print("• Processing and manipulating image data")
    print()
    input("Press Enter to continue...")

    while True:
        clear_screen()
        show_menu()

        choice = get_valid_choice()

        if not execute_choice(choice):
            break


if __name__ == "__main__":
    main()
