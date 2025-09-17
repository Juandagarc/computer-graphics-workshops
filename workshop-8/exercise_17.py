import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("assets/utp-logo.jpg")/255

img_gray = (np.maximum(img[:, :, 0], img[:, :, 1], img[:, :, 2]) + np.minimum(img[:, :, 0], img[:, :, 1], img[:, :, 2]))
plt.imshow(img_gray)
plt.show()
