import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("assets/utp-logo.jpg")/255

img_gray = (0.299*img[:, :, 0] + 0.587*img[:, :, 1] + 0.144*img[:, :, 2])
plt.imshow(img_gray)
plt.show()
