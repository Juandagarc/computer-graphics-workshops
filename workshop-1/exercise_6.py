import numpy as np

class ProjectileMotion:
    def __init__(self, initial_velocity, launch_angle_degrees):
        self.v0 = initial_velocity
        self.angle_rad = np.radians(launch_angle_degrees)  # Convert degrees to radians
        self.g = 9.81  # Acceleration due to gravity in m/s²

    def get_max_range(self):
        return (self.v0 ** 2) * np.sin(2 * self.angle_rad) / self.g

    def get_max_height(self):
        return (self.v0 ** 2) * (np.sin(self.angle_rad) ** 2) / (2 * self.g)
