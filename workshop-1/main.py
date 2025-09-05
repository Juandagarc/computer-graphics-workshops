import curses
from exercise_1 import Object
from exercise_2 import Distance
from exercise_3 import MRUA
from exercise_4 import sum_of_vectors
from exercise_5 import scalar_product
from exercise_6 import ProjectileMotion


# Function to display the menu
def menu(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()  # Clear the screen
    options = [
        "1. Object Falling",
        "2. Distance Conversion",
        "3. MRUA (Uniform Acceleration)",
        "4. Sum of Vectors",
        "5. Scalar Product of Vectors",
        "6. Projectile Motion",
        "7. Exit"
    ]
    current_option = 0
    while True:
        stdscr.clear()  # Clear the screen before rendering
        height, width = stdscr.getmaxyx()

        for i, option in enumerate(options):
            x = width // 2 - len(option) // 2
            y = height // 2 - len(options) // 2 + i
            if i == current_option:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, option)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, option)

        stdscr.refresh()

        key = stdscr.getch()

        # Navigate through the options using arrow keys
        if key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == 10:  # Enter key pressed
            if current_option == 0:
                # Exercise 1: Object Falling
                stdscr.clear()
                stdscr.addstr(0, 0, "Enter the weight of the object (kg): ")
                stdscr.refresh()
                weight = int(stdscr.getstr().decode())
                ball = Object('ball', weight)
                stdscr.addstr(1, 0,
                              f"The falling time for a {ball.name} of {ball.weight}kg from 10m is: {ball.get_time_of_falling(10)} seconds.")
                stdscr.refresh()
                stdscr.getch()  # Wait for user to press a key before going back to menu

            elif current_option == 1:
                # Exercise 2: Distance Conversion
                stdscr.clear()
                stdscr.addstr(0, 0, "Enter distance (value + unit, e.g., 30 km/h): ")
                stdscr.refresh()
                distance_input = stdscr.getstr().decode()
                distance = Distance(*distance_input.split())
                distance.convert()
                stdscr.refresh()
                stdscr.getch()  # Wait for user to press a key before going back to menu

            elif current_option == 2:
                # Exercise 3: MRUA
                stdscr.clear()
                stdscr.addstr(0, 0, "Enter initial velocity (m/s): ")
                stdscr.refresh()
                velocity = int(stdscr.getstr().decode())
                stdscr.addstr(1, 0, "Enter time (s): ")
                stdscr.refresh()
                time = int(stdscr.getstr().decode())
                stdscr.addstr(2, 0, "Enter acceleration (m/s^2): ")
                stdscr.refresh()
                acceleration = int(stdscr.getstr().decode())
                car = MRUA(velocity, time, acceleration)
                stdscr.addstr(3, 0,
                              f"The distance for a car moving at {car.initial_velocity} m/s, with an acceleration of {car.acceleration} m/s² over {car.time} seconds is: {car.get_distance()} meters.")
                stdscr.refresh()
                stdscr.getch()  # Wait for user to press a key before going back to menu

            elif current_option == 3:
                # Exercise 4: Sum of Vectors
                stdscr.clear()
                stdscr.addstr(0, 0, "Enter vector 1 (comma-separated, e.g., 1,2,3): ")
                stdscr.refresh()
                vector_1 = list(map(int, stdscr.getstr().decode().split(',')))
                stdscr.addstr(1, 0, "Enter vector 2 (comma-separated, e.g., 4,5,6): ")
                stdscr.refresh()
                vector_2 = list(map(int, stdscr.getstr().decode().split(',')))
                result = sum_of_vectors(vector_1, vector_2)
                stdscr.addstr(2, 0, f"The sum of vectors is: {result}")
                stdscr.refresh()
                stdscr.getch()  # Wait for user to press a key before going back to menu

            elif current_option == 4:
                # Exercise 5: Scalar Product
                stdscr.clear()
                stdscr.addstr(0, 0, "Enter vector 1 (comma-separated, e.g., 1,2,3): ")
                stdscr.refresh()
                vector_1 = list(map(int, stdscr.getstr().decode().split(',')))
                stdscr.addstr(1, 0, "Enter vector 2 (comma-separated, e.g., 4,5,6): ")
                stdscr.refresh()
                vector_2 = list(map(int, stdscr.getstr().decode().split(',')))
                result = scalar_product(vector_1, vector_2)
                stdscr.addstr(2, 0, f"The scalar product is: {result}")
                stdscr.refresh()
                stdscr.getch()  # Wait for user to press a key before going back to menu

            elif current_option == 5:
                # Exercise 6: Projectile Motion
                stdscr.clear()
                stdscr.addstr(0, 0, "Enter initial velocity (m/s): ")
                stdscr.refresh()
                velocity = int(stdscr.getstr().decode())
                stdscr.addstr(1, 0, "Enter launch angle (degrees): ")
                stdscr.refresh()
                angle = int(stdscr.getstr().decode())
                projectile = ProjectileMotion(initial_velocity=velocity, launch_angle_degrees=angle)
                stdscr.addstr(2, 0, f"Maximum Range: {projectile.get_max_range()} meters")
                stdscr.addstr(3, 0, f"Maximum Height: {projectile.get_max_height()} meters")
                stdscr.refresh()
                stdscr.getch()  # Wait for user to press a key before going back to menu

            elif current_option == 6:
                # Exit
                break

        stdscr.refresh()


# Start the curses application
curses.wrapper(menu)







