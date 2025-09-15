import os
import numpy as np
from exercises import (
    exercise_1, exercise_2, exercise_3, exercise_4,
    exercise_5, exercise_6, exercise_7,
    create_array, reshape_array, array_properties
)


def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_valid_input(prompt, input_type="float", min_val=None, max_val=None):
    """Function to get valid user input with validation"""
    while True:
        try:
            print(f"\n{prompt}")
            user_input = input("Enter your answer: ").strip()

            value = None  # Initialize value

            if input_type == "int":
                value = int(user_input)
            elif input_type == "float":
                value = float(user_input)
            elif input_type == "string":
                if not user_input:
                    raise ValueError("Input cannot be empty")
                return user_input
            elif input_type == "list":
                if not user_input:
                    raise ValueError("Input cannot be empty")
                try:
                    number_list = [float(x.strip()) for x in user_input.split(',')]
                    if len(number_list) == 0:
                        raise ValueError("List must have at least one element")
                    return number_list
                except ValueError:
                    raise ValueError("Incorrect format. Use numbers separated by commas (e.g.: 1,2,3,4)")
            elif input_type == "matrix":
                if not user_input:
                    raise ValueError("Input cannot be empty")
                try:
                    rows = user_input.split(';')
                    matrix = []
                    for row in rows:
                        row_values = [float(x.strip()) for x in row.split(',')]
                        matrix.append(row_values)
                    return matrix
                except ValueError:
                    raise ValueError("Incorrect format. Use: row1,row2;row3,row4 (e.g.: 1,2;3,4)")

            if value is not None:
                if min_val is not None and value < min_val:
                    raise ValueError(f"Value must be greater than or equal to {min_val}")
                if max_val is not None and value > max_val:
                    raise ValueError(f"Value must be less than or equal to {max_val}")

            return value

        except ValueError as e:
            print(f"\n❌ Error: {str(e)}")
            print("Invalid input. Please try again.")
            input("Press Enter to continue...")


def show_result(message):
    """Function to display results and wait for user input"""
    print(f"\n{'='*60}")
    print("RESULT:")
    print(f"{'='*60}")
    print(message)
    print(f"{'='*60}")
    input("\nPress Enter to return to menu...")


def show_menu():
    """Display the main menu"""
    clear_screen()
    print("╔════════════════════════════════════════════════════════════╗")
    print("║           WORKSHOP 3 - INTRODUCTION TO NUMPY 🐍           ║")
    print("╠════════════════════════════════════════════════════════════╣")
    print("║  1. Array Creation and Properties                          ║")
    print("║  2. Basic Operations                                       ║")
    print("║  3. Indexing and Slicing                                   ║")
    print("║  4. Broadcasting and Universal Functions                   ║")
    print("║  5. Shape Manipulation and Linear Algebra                  ║")
    print("║  6. Working with Missing Data                              ║")
    print("║  7. Save and Load Arrays                                   ║")
    print("║  8. Exit                                                   ║")
    print("╚════════════════════════════════════════════════════════════╝")


def main():
    """Main program function"""
    while True:
        show_menu()

        try:
            user_choice = input("\nSelect an option (1-8): ").strip()

            if not user_choice.isdigit():
                raise ValueError("You must enter a number")

            menu_option = int(user_choice)

            if menu_option < 1 or menu_option > 8:
                raise ValueError("You must enter a number between 1 and 8")

            if menu_option == 1:
                # Exercise 1: Array Creation and Properties
                clear_screen()
                print("🔢 EXERCISE 1: ARRAY CREATION AND PROPERTIES")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    exercise_1()

                    print("\n" + "="*40)
                    print("Do you want to try with your own data? (y/n)")
                    response = input().strip().lower()

                    if response == 'y':
                        data = get_valid_input("Enter numbers separated by commas:", "list")
                        arr = create_array(data)
                        print(f"\nYour array: {arr}")
                        array_properties(arr)

                        if len(data) >= 10:
                            try:
                                reshaped = reshape_array(arr)
                                print(f"\nReshaped array (2x5): {reshaped}")
                                array_properties(reshaped)
                            except:
                                print("Cannot reshape to 2x5 with this array")

                    show_result("Exercise 1 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 2:
                # Exercise 2: Basic Operations
                clear_screen()
                print("➕ EXERCISE 2: BASIC ARRAY OPERATIONS")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    exercise_2()
                    show_result("Exercise 2 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 3:
                # Exercise 3: Indexing and Slicing
                clear_screen()
                print("🔍 EXERCISE 3: INDEXING AND SLICING")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    exercise_3()

                    print("\n" + "="*40)
                    print("Do you want to try custom indexing? (y/n)")
                    response = input().strip().lower()

                    if response == 'y':
                        data = get_valid_input("Enter numbers separated by commas:", "list")
                        arr = np.array(data)
                        print(f"\nYour array: {arr}")

                        index = get_valid_input(f"Enter index to access (0-{len(data)-1}):", "int",
                                              min_val=0, max_val=len(data)-1)
                        print(f"Element at index {index}: {arr[index]}")

                        start_index = get_valid_input(f"Enter start index for slice (0-{len(data)-1}):", "int",
                                              min_val=0, max_val=len(data)-1)
                        end_index = get_valid_input(f"Enter end index for slice ({start_index+1}-{len(data)}):", "int",
                                            min_val=start_index+1, max_val=len(data))
                        print(f"Slice [{start_index}:{end_index}]: {arr[start_index:end_index]}")

                    show_result("Exercise 3 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 4:
                # Exercise 4: Broadcasting
                clear_screen()
                print("📡 EXERCISE 4: BROADCASTING AND UNIVERSAL FUNCTIONS")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    exercise_4()
                    show_result("Exercise 4 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 5:
                # Exercise 5: Linear Algebra
                clear_screen()
                print("🔢 EXERCISE 5: SHAPE MANIPULATION AND LINEAR ALGEBRA")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    exercise_5()
                    show_result("Exercise 5 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 6:
                # Exercise 6: Missing Data
                clear_screen()
                print("❓ EXERCISE 6: WORKING WITH MISSING DATA")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    exercise_6()
                    show_result("Exercise 6 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 7:
                # Exercise 7: Save and Load
                clear_screen()
                print("💾 EXERCISE 7: SAVE AND LOAD ARRAYS")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    exercise_7()
                    show_result("Exercise 7 completed. File 'my_array.npy' created in current directory.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 8:
                # Exit
                clear_screen()
                print("👋 Thank you for using Workshop 3 - NumPy!")
                print("See you later!")
                break

        except ValueError as e:
            print(f"\n❌ Error: {str(e)}")
            input("Press Enter to continue...")
        except KeyboardInterrupt:
            clear_screen()
            print("\n👋 Program interrupted by user.")
            print("See you later!")
            break


if __name__ == "__main__":
    main()
