import os
import numpy as np
from exercises import run_all_exercises


def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    """Display the main workshop menu"""
    print("📐 WORKSHOP 7: Function Approximation with Taylor Series 📐")
    print("=" * 70)
    print("Welcome to Workshop 7!")
    print()
    print("This workshop covers function approximation using Taylor series including:")
    print("• Exponential function approximation (e^x)")
    print("• Trigonometric functions (sin, cos, tan)")
    print("• Natural logarithm approximation ln(1+x)")
    print("• Mathematical series convergence analysis")
    print("• Comparative visualization of approximations")
    print("• Error analysis between Taylor series and built-in functions")
    print()
    print("Select an option:")
    print()
    print("1. Run all exercises")
    print("0. Exit")
    print("=" * 70)


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
        print("🎉 Thank you for using Workshop 7!")
        print("👋 Hope you enjoyed learning about Taylor series approximations!")
        return False

    return True


def main():
    """Main function to run the workshop"""
    print("Welcome to Workshop 7: Function Approximation with Taylor Series! 🎉")
    print()
    print("In this workshop, you will explore:")
    print("• Understanding Taylor series mathematical foundations")
    print("• Implementing custom mathematical functions from scratch")
    print("• Analyzing convergence and accuracy of series approximations")
    print("• Comparing custom implementations with NumPy built-in functions")
    print("• Creating comprehensive visualizations of mathematical functions")
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
