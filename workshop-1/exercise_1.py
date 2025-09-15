import numpy as np

class Object:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.gravity = 9.81  # m/s² - acceleration due to gravity

    def get_time_of_falling(self, height):
        # Correct formula: t = sqrt(2h/g)
        return np.sqrt((2 * height) / self.gravity)
