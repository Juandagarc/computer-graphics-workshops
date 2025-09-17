import numpy as np
import matplotlib.pyplot as plt

def apply_brightness_by_channel(image, factors, channel_indice):
    img_copy = image.copy()
    img_copy[:, :, channel_indice] += factors[channel_indice]
    return img_copy

# input asking how much bright the user wants the image to be
factors = list(map(float, input("Enter brightness factors for R, G, B channels (-1 to 1) separated by spaces: ").split()))

#input asking which channel the user wants to adjust
channel_indice = int(input("Enter the channel index to adjust (0 for Red, 1 for Green, 2 for Blue): "))
if channel_indice not in [0, 1, 2]:
    raise ValueError("Channel index must be 0, 1, or 2.")

# Load the image
image = np.asarray(plt.imread("assets/cartagena.jpg"), dtype=np.float64) / 255.0

# Adjust brightness for each channel
brightened_image = apply_brightness_by_channel(image, factors, channel_indice)

plt.imshow(brightened_image, cmap="gray")
plt.axis('off')
plt.title(f'Brightened Image (factors={factors}, channel={channel_indice})')
plt.show()
