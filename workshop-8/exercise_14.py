import numpy as np
import matplotlib.pyplot as plt

def equalize_image_average(image):
    if image.max() > 1:
        image = image.astype(np.float64) / 255.0

    if len(image.shape) == 3:
        equalized_image = np.zeros_like(image)

        for channel in range(image.shape[2]):
            channel_data = image[:, :, channel]

            hist, bins = np.histogram(channel_data.flatten(), bins=256, range=[0, 1])

            cdf = hist.cumsum()
            cdf_normalized = cdf / cdf.max()

            equalized_channel = np.interp(channel_data.flatten(), bins[:-1], cdf_normalized)
            equalized_image[:, :, channel] = equalized_channel.reshape(channel_data.shape)
    else:
        hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 1])
        cdf = hist.cumsum()
        cdf_normalized = cdf / cdf.max()
        equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized)
        equalized_image = equalized_image.reshape(image.shape)

    return equalized_image

img = plt.imread("assets/beach.jpg")

img_equalized = equalize_image_average(img)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].imshow(img)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(img_equalized)
ax[1].set_title('Equalized Image (Average Technique)')
ax[1].axis('off')

plt.tight_layout()
plt.show()

print("Image equalization completed using average technique")
print(f"Original image range: [{np.min(img):.3f}, {np.max(img):.3f}]")
print(f"Equalized image range: [{np.min(img_equalized):.3f}, {np.max(img_equalized):.3f}]")
