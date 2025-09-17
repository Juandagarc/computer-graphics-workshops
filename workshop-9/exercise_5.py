import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(image: np.ndarray) -> np.ndarray:
    if image.ndim == 3 and image.shape[2] >= 3:
        # Coeficientes de luminancia
        r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]
        gray = 0.299 * r + 0.587 * g + 0.114 * b
        return gray
    return image


def binarize(image: np.ndarray, threshold: float) -> np.ndarray:
    gray = to_grayscale(image)
    return (gray >= threshold).astype(np.float64)


# Umbral por consola
threshold = float(input("Ingrese un umbral de binarización (0 a 1): "))

# Cargar imagen
image = np.asarray(plt.imread("assets/cartagena.jpg"), dtype=np.float64) / 255.0

# Binarizar
binary = binarize(image, threshold)

# Mostrar resultados
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(image, cmap="gray")
axs[0].set_title('Imagen original')
axs[0].axis('off')

axs[1].imshow(binary, cmap="gray")
axs[1].set_title(f'Binarizada (umbral={threshold})')
axs[1].axis('off')

plt.tight_layout()
plt.show()
