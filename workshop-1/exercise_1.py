import numpy as np

class Object:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_time_of_falling(self, height):
        return np.sqrt((2 * height) / self.weight)