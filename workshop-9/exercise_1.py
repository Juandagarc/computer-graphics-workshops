import numpy as np
import matplotlib.pyplot as plt

def adjust_brightness(image, factor):
    return image + factor

# input asking how much bright the user wants the image to be
factor = float(input("Enter a brightness factor(-1 to 1): "))

# Load the image
image = np.asarray(plt.imread("assets/cartagena.jpg"), dtype=np.float64) / 255.0

# Adjust brightness
brightened_image = adjust_brightness(image, factor)

plt.imshow(brightened_image, cmap="gray")
plt.axis('off')
plt.title(f'Brightened Image (factor={factor})')
plt.show()