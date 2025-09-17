import numpy as np
import matplotlib.pyplot as plt

# Load and normalize images
image_1 = np.asarray(plt.imread("assets/beach.jpg"), dtype=np.float64) / 255.0
image_2 = np.asarray(plt.imread("assets/boat.jpg"), dtype=np.float64) / 255.0

# Resize to same dimensions
min_height = min(image_1.shape[0], image_2.shape[0])
min_width = min(image_1.shape[1], image_2.shape[1])

image_1_resized = image_1[:min_height, :min_width]
image_2_resized = image_2[:min_height, :min_width]

# Average fusion
image_fusion = (image_1_resized + image_2_resized) / 2.0

# Display results
fig, ax = plt.subplots(1, 3, figsize=(12, 3))

ax[0].imshow(image_1_resized)
ax[0].set_title('Beach Image')
ax[0].axis('off')

ax[1].imshow(image_2_resized)
ax[1].set_title('Boat Image')
ax[1].axis('off')

ax[2].imshow(image_fusion)
ax[2].set_title('Average Fusion')
ax[2].axis('off')

plt.tight_layout()
plt.show()
