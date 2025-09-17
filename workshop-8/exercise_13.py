import numpy as np
import matplotlib.pyplot as plt

def equalize_image(image, factor):
    """
    Equalizes an image using histogram equalization with a given factor.

    Args:
        image: Input image as numpy array (normalized 0-1)
        factor: Equalization factor (0.0 to 1.0)
                0.0 = no equalization (original image)
                1.0 = full histogram equalization

    Returns:
        Equalized image as numpy array
    """
    if len(image.shape) == 3:
        equalized_image = np.zeros_like(image)

        for channel in range(image.shape[2]):
            channel_data = image[:, :, channel]

            hist, bins = np.histogram(channel_data.flatten(), bins=256, range=[0, 1])

            cdf = hist.cumsum()
            cdf_normalized = cdf / cdf.max()

            equalized_channel = np.interp(channel_data.flatten(), bins[:-1], cdf_normalized)
            equalized_channel = equalized_channel.reshape(channel_data.shape)

            equalized_image[:, :, channel] = (1 - factor) * channel_data + factor * equalized_channel
    else:
        hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 1])
        cdf = hist.cumsum()
        cdf_normalized = cdf / cdf.max()
        equalized_gray = np.interp(image.flatten(), bins[:-1], cdf_normalized)
        equalized_gray = equalized_gray.reshape(image.shape)
        equalized_image = (1 - factor) * image + factor * equalized_gray

    return equalized_image

image = np.asarray(plt.imread("assets/beach.jpg"), dtype=np.float64) / 255.0

while True:
    try:
        factor = float(input("Enter equalization factor (0.0 to 1.0): "))
        if 0.0 <= factor <= 1.0:
            break
        else:
            print("Please enter a value between 0.0 and 1.0")
    except ValueError:
        print("Please enter a valid number")

equalized = equalize_image(image, factor)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].imshow(image)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(equalized)
ax[1].set_title(f'Equalized Image (Factor: {factor})')
ax[1].axis('off')

plt.tight_layout()
plt.show()

print(f"Image equalization completed with factor {factor}")
print(f"Original image range: [{np.min(image):.3f}, {np.max(image):.3f}]")
print(f"Equalized image range: [{np.min(equalized):.3f}, {np.max(equalized):.3f}]")
