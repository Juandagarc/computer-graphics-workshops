import os
from exercise_1 import calculator
from exercise_2 import filtering_exercise, filter_even_numbers
from exercise_3 import temperature_exercise, convert_temperatures
from exercise_4 import grades_exercise, convert_grades
from exercise_5 import frequency_exercise, count_words
from exercise_6 import search_exercise, search_element
from exercise_7 import parentheses_exercise, validate_parentheses
from exercise_8 import sorting_exercise, sort_tuples
from exercise_9 import password_exercise, generate_password, generate_secure_password, evaluate_strength
from exercise_10 import phone_book_exercise, interactive_phone_book_menu, PhoneBook


def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_valid_input(prompt, input_type="float", min_val=None, max_val=None):
    """Function to get valid user input with validation"""
    while True:
        try:
            print(f"\n{prompt}")
            user_input = input("Enter your answer: ").strip()

            value = None  # Initialize value to avoid warning

            if input_type == "int":
                value = int(user_input)
            elif input_type == "float":
                value = float(user_input)
            elif input_type == "string":
                if not user_input:
                    raise ValueError("Input cannot be empty")
                return user_input
            elif input_type == "list_int":
                if not user_input:
                    raise ValueError("Input cannot be empty")
                try:
                    number_list = [int(x.strip()) for x in user_input.split(',')]
                    if len(number_list) == 0:
                        raise ValueError("List must have at least one element")
                    return number_list
                except ValueError:
                    raise ValueError("Incorrect format. Use integers separated by commas (e.g.: 1,2,3,4)")
            elif input_type == "list_float":
                if not user_input:
                    raise ValueError("Input cannot be empty")
                try:
                    number_list = [float(x.strip()) for x in user_input.split(',')]
                    if len(number_list) == 0:
                        raise ValueError("List must have at least one element")
                    return number_list
                except ValueError:
                    raise ValueError("Incorrect format. Use numbers separated by commas (e.g.: 1.5,2.3,3.7)")
            elif input_type == "list_string":
                if not user_input:
                    raise ValueError("Input cannot be empty")
                string_list = [x.strip() for x in user_input.split(',')]
                if len(string_list) == 0:
                    raise ValueError("List must have at least one element")
                return string_list

            # Validate range if specified for numbers
            if input_type in ["int", "float"] and value is not None:
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
    print("║           WORKSHOP 2 - PYTHON PROGRAMMING 🐍              ║")
    print("╠════════════════════════════════════════════════════════════╣")
    print("║  1. Basic Calculator                                       ║")
    print("║  2. Even Number List Filtering                             ║")
    print("║  3. Temperature Conversion                                 ║")
    print("║  4. Grade Conversion                                       ║")
    print("║  5. Word Frequency Counter                                 ║")
    print("║  6. Manual List Search                                     ║")
    print("║  7. Parentheses Validation                                 ║")
    print("║  8. Custom Tuple Sorting                                   ║")
    print("║  9. Random Password Generator                              ║")
    print("║ 10. Phone Book Management                                  ║")
    print("║ 11. Exit                                                   ║")
    print("╚════════════════════════════════════════════════════════════╝")


def main():
    """Main program function"""
    while True:
        show_menu()

        try:
            user_choice = input("\nSelect an option (1-11): ").strip()

            if not user_choice.isdigit():
                raise ValueError("You must enter a number")

            menu_option = int(user_choice)

            if menu_option < 1 or menu_option > 11:
                raise ValueError("You must enter a number between 1 and 11")

            if menu_option == 1:
                # Exercise 1: Basic Calculator
                clear_screen()
                print("🔢 EXERCISE 1: BASIC CALCULATOR")
                print("-" * 50)
                try:
                    calculator()
                    show_result("Exercise 1 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 2:
                # Exercise 2: Even Number Filtering
                clear_screen()
                print("📊 EXERCISE 2: EVEN NUMBER LIST FILTERING")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    filtering_exercise()

                    print("\n" + "="*40)
                    print("Do you want to try with your own list? (y/n)")
                    response = input().strip().lower()

                    if response == 'y':
                        numbers = get_valid_input("Enter numbers separated by commas:", "list_int")
                        even_nums = filter_even_numbers(numbers)
                        print(f"\nYour list: {numbers}")
                        print(f"Even numbers: {even_nums}")

                    show_result("Exercise 2 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 3:
                # Exercise 3: Temperature Conversion
                clear_screen()
                print("🌡️ EXERCISE 3: TEMPERATURE CONVERSION")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    temperature_exercise()

                    print("\n" + "="*40)
                    print("Do you want to try with your own temperatures? (y/n)")
                    response = input().strip().lower()

                    if response == 'y':
                        celsius_temps = get_valid_input("Enter Celsius temperatures separated by commas:", "list_float")
                        fahrenheit_temps = convert_temperatures(celsius_temps)
                        print(f"\nCelsius: {celsius_temps}")
                        print(f"Fahrenheit: {fahrenheit_temps}")

                    show_result("Exercise 3 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 4:
                # Exercise 4: Grade Conversion
                clear_screen()
                print("📝 EXERCISE 4: GRADE CONVERSION")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    grades_exercise()

                    print("\n" + "="*40)
                    print("Do you want to try with your own grades? (y/n)")
                    response = input().strip().lower()

                    if response == 'y':
                        numerical_scores = get_valid_input("Enter numerical grades separated by commas:", "list_float")
                        letter_grades = convert_grades(numerical_scores)
                        print(f"\nNumerical grades: {numerical_scores}")
                        print(f"Letter grades: {letter_grades}")

                    show_result("Exercise 4 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 5:
                # Exercise 5: Word Frequency Counter
                clear_screen()
                print("📖 EXERCISE 5: WORD FREQUENCY COUNTER")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    frequency_exercise()

                    print("\n" + "="*40)
                    print("Do you want to try with your own text? (y/n)")
                    response = input().strip().lower()

                    if response == 'y':
                        custom_text = get_valid_input("Enter your text:", "string")
                        word_frequencies = count_words(custom_text)
                        print(f"\nText: {custom_text}")
                        print("Word frequencies:")
                        for word, frequency in word_frequencies.items():
                            print(f"  '{word}': {frequency}")

                    show_result("Exercise 5 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 6:
                # Exercise 6: Manual List Search
                clear_screen()
                print("🔍 EXERCISE 6: MANUAL LIST SEARCH")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    search_exercise()

                    print("\n" + "="*40)
                    print("Do you want to try with your own list? (y/n)")
                    response = input().strip().lower()

                    if response == 'y':
                        custom_list = get_valid_input("Enter list elements separated by commas:", "list_string")
                        search_element_input = get_valid_input("Enter element to search:", "string")
                        found_index = search_element(custom_list, search_element_input)

                        if found_index != -1:
                            print(f"'{search_element_input}' found at index {found_index}")
                        else:
                            print(f"'{search_element_input}' not found in the list")

                    show_result("Exercise 6 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 7:
                # Exercise 7: Parentheses Validation
                clear_screen()
                print("🔗 EXERCISE 7: PARENTHESES VALIDATION")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    parentheses_exercise()

                    print("\n" + "="*40)
                    print("Do you want to try with your own parentheses string? (y/n)")
                    response = input().strip().lower()

                    if response == 'y':
                        parentheses_string = get_valid_input("Enter parentheses string:", "string")
                        is_balanced = validate_parentheses(parentheses_string)
                        status = "✓ Balanced" if is_balanced else "✗ Not balanced"
                        print(f"'{parentheses_string}' → {status}")

                    show_result("Exercise 7 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 8:
                # Exercise 8: Custom Tuple Sorting
                clear_screen()
                print("📋 EXERCISE 8: CUSTOM TUPLE SORTING")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    sorting_exercise()
                    show_result("Exercise 8 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 9:
                # Exercise 9: Random Password Generator
                clear_screen()
                print("🔒 EXERCISE 9: RANDOM PASSWORD GENERATOR")
                print("-" * 50)
                try:
                    print("Running predefined exercise...")
                    password_exercise()

                    print("\n" + "="*40)
                    print("Do you want to generate a custom password? (y/n)")
                    response = input().strip().lower()

                    if response == 'y':
                        password_length = get_valid_input("Enter password length:", "int", min_val=4, max_val=50)
                        custom_password = generate_secure_password(password_length)
                        strength_level, criteria, score = evaluate_strength(custom_password)

                        print(f"\nGenerated password: {custom_password}")
                        print(f"Strength: {strength_level} ({score}/5)")

                    show_result("Exercise 9 completed.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 10:
                # Exercise 10: Phone Book Management
                clear_screen()
                print("📞 EXERCISE 10: PHONE BOOK MANAGEMENT")
                print("-" * 50)
                try:
                    print("Choose an option:")
                    print("1. Run demonstration")
                    print("2. Interactive phone book")

                    sub_choice = input("Select (1-2): ").strip()

                    if sub_choice == "1":
                        phone_book_exercise()
                        show_result("Exercise 10 demonstration completed.")
                    elif sub_choice == "2":
                        interactive_phone_book_menu()
                        show_result("Interactive phone book session completed.")
                    else:
                        show_result("Invalid option selected.")

                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 11:
                # Exit
                clear_screen()
                print("👋 Thank you for using Workshop 2!")
                print("See you later!")
                break

        except ValueError as e:
            print(f"\n❌ Error: {str(e)}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
