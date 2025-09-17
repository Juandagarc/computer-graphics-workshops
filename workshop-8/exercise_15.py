import numpy as np
import matplotlib.pyplot as plt

def convert_to_grayscale_average(image):
    # Convert to grayscale using average of RGB channels
    grayscale_image = (image[:, :, 0] + image[:, :, 1] + image[:, :, 2]) / 3
    return grayscale_image

# Load image
img = plt.imread("assets/utp-logo.jpg")

# Convert to grayscale using the function
img_gray = convert_to_grayscale_average(img)

# Display results
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].imshow(img)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(img_gray, cmap='gray')
ax[1].set_title('Grayscale (Average Method)')
ax[1].axis('off')

plt.tight_layout()
plt.show()

print("Image converted to grayscale using average method")
print(f"Original image shape: {img.shape}")
print(f"Grayscale image shape: {img_gray.shape}")
