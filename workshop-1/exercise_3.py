import numpy as np

class MRUA:
    def __init__(self, initial_velocity, time, acceleration):
        self.initial_velocity = initial_velocity
        self.time = time
        self.acceleration = acceleration

    def get_distance(self):
        return self.initial_velocity * self.time + (1/2 * self.acceleration * np.sqrt(self.time))