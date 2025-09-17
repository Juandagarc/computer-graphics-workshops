import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

matrix = np.array([
    [[0, 1, 1],   [1, 1, 1],   [1, 0, 0]],  # Cian, White, Red,
    [[1, 0, 1],   [0.5, 0.5, 0.5], [0, 1, 0]],  # Magenta, Gray, Green
    [[1, 1, 0],   [0, 0, 0],   [0, 0, 1]]   # yellow, Black, Blue
])

plt.imshow(matrix)
plt.show()