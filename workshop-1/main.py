import os
from exercise_1 import Object
from exercise_2 import Distance
from exercise_3 import MRUA
from exercise_4 import sum_of_vectors
from exercise_5 import scalar_product
from exercise_6 import ProjectileMotion


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
            elif input_type == "vector":
                # For comma-separated vectors
                if not user_input:
                    raise ValueError("Input cannot be empty")
                vector = [float(x.strip()) for x in user_input.split(',')]
                if len(vector) == 0:
                    raise ValueError("Vector must have at least one element")
                return vector

            # Validate range if specified
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
    print(f"\n{'='*50}")
    print("RESULT:")
    print(f"{'='*50}")
    print(message)
    print(f"{'='*50}")
    input("\nPress Enter to return to menu...")


def show_menu():
    """Display the main menu"""
    clear_screen()
    print("╔══════════════════════════════════════════════════╗")
    print("║                MAIN MENU                         ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  1. Object Falling                               ║")
    print("║  2. Distance Conversion                          ║") 
    print("║  3. MRUA (Uniform Acceleration)                  ║")
    print("║  4. Sum of Vectors                               ║")
    print("║  5. Scalar Product of Vectors                    ║")
    print("║  6. Projectile Motion                            ║")
    print("║  7. Exit                                         ║")
    print("╚══════════════════════════════════════════════════╝")


def main():
    """Main program function"""
    while True:
        show_menu()
        
        try:
            user_choice = input("\nSelect an option (1-7): ").strip()

            if not user_choice.isdigit():
                raise ValueError("You must enter a number")

            menu_option = int(user_choice)

            if menu_option < 1 or menu_option > 7:
                raise ValueError("You must enter a number between 1 and 7")

            if menu_option == 1:
                # Exercise 1: Object Falling
                clear_screen()
                print("🏀 EXERCISE 1: OBJECT FALLING")
                print("-" * 40)
                try:
                    object_weight = get_valid_input("Enter object weight (kg):", "float", min_val=0.1)
                    falling_ball = Object('ball', object_weight)
                    falling_time = falling_ball.get_time_of_falling(10)
                    result_message = f"The falling time for a {falling_ball.name} of {falling_ball.weight}kg from 10m is: {falling_time:.2f} seconds."
                    show_result(result_message)
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 2:
                # Exercise 2: Distance Conversion
                clear_screen()
                print("📏 EXERCISE 2: DISTANCE CONVERSION")
                print("-" * 40)
                try:
                    distance_input = get_valid_input("Enter distance (value + unit, e.g.: '30 km/h'):", "string")
                    input_parts = distance_input.split()
                    if len(input_parts) != 2:
                        raise ValueError("Incorrect format. Use: value unit (e.g.: '30 km/h')")

                    distance_value = float(input_parts[0])
                    distance_unit = input_parts[1]
                    distance_converter = Distance(distance_value, distance_unit)
                    print("\n🔄 Converting...")
                    distance_converter.convert()
                    show_result("Conversion completed. Results are shown above.")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 3:
                # Exercise 3: MRUA
                clear_screen()
                print("🚗 EXERCISE 3: MRUA (UNIFORM ACCELERATION)")
                print("-" * 40)
                try:
                    initial_velocity = get_valid_input("Enter initial velocity (m/s):", "float")
                    motion_time = get_valid_input("Enter time (s):", "float", min_val=0)
                    motion_acceleration = get_valid_input("Enter acceleration (m/s²):", "float")

                    moving_car = MRUA(initial_velocity, motion_time, motion_acceleration)
                    calculated_distance = moving_car.get_distance()
                    result_message = f"The distance for a car moving at {moving_car.initial_velocity} m/s, with acceleration of {moving_car.acceleration} m/s² for {moving_car.time} seconds is: {calculated_distance:.2f} meters."
                    show_result(result_message)
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 4:
                # Exercise 4: Sum of Vectors
                clear_screen()
                print("➕ EXERCISE 4: VECTOR ADDITION")
                print("-" * 40)
                try:
                    first_vector = get_valid_input("Enter vector 1 (comma separated, e.g.: 1,2,3):", "vector")
                    second_vector = get_valid_input("Enter vector 2 (comma separated, e.g.: 4,5,6):", "vector")

                    if len(first_vector) != len(second_vector):
                        raise ValueError("Vectors must have the same dimension")

                    vector_sum = sum_of_vectors(first_vector, second_vector)
                    show_result(f"The vector sum is: {vector_sum}")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 5:
                # Exercise 5: Scalar Product
                clear_screen()
                print("✖️ EXERCISE 5: SCALAR PRODUCT")
                print("-" * 40)
                try:
                    first_vector = get_valid_input("Enter vector 1 (comma separated, e.g.: 1,2,3):", "vector")
                    second_vector = get_valid_input("Enter vector 2 (comma separated, e.g.: 4,5,6):", "vector")

                    if len(first_vector) != len(second_vector):
                        raise ValueError("Vectors must have the same dimension")

                    dot_product_result = scalar_product(first_vector, second_vector)
                    show_result(f"The scalar product is: {dot_product_result}")
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 6:
                # Exercise 6: Projectile Motion
                clear_screen()
                print("🎯 EXERCISE 6: PROJECTILE MOTION")
                print("-" * 40)
                try:
                    initial_velocity = get_valid_input("Enter initial velocity (m/s):", "float", min_val=0)
                    launch_angle = get_valid_input("Enter launch angle (degrees):", "float", min_val=0, max_val=90)

                    projectile_motion = ProjectileMotion(initial_velocity=initial_velocity, launch_angle_degrees=launch_angle)
                    max_range = projectile_motion.get_max_range()
                    max_height = projectile_motion.get_max_height()
                    result_message = f"Maximum range: {max_range:.2f} meters\nMaximum height: {max_height:.2f} meters"
                    show_result(result_message)
                except Exception as e:
                    show_result(f"Error in exercise: {str(e)}")

            elif menu_option == 7:
                # Exit
                clear_screen()
                print("👋 Thank you for using the program!")
                print("See you later!")
                break

        except ValueError as e:
            print(f"\n❌ Error: {str(e)}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
