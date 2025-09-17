import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en [0,1]
image = np.asarray(plt.imread("assets/cartagena.jpg"), dtype=np.float64) / 255.0

if image.ndim == 3 and image.shape[2] >= 3:
    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs[0, 0].imshow(image)
    axs[0, 0].set_title('Imagen original')
    axs[0, 0].axis('off')

    axs[0, 1].hist(r.ravel(), bins=256, range=(0, 1), color='r', alpha=0.8)
    axs[0, 1].set_title('Histograma - Rojo')
    axs[0, 1].set_xlim(0, 1)

    axs[1, 0].hist(g.ravel(), bins=256, range=(0, 1), color='g', alpha=0.8)
    axs[1, 0].set_title('Histograma - Verde')
    axs[1, 0].set_xlim(0, 1)

    axs[1, 1].hist(b.ravel(), bins=256, range=(0, 1), color='b', alpha=0.8)
    axs[1, 1].set_title('Histograma - Azul')
    axs[1, 1].set_xlim(0, 1)

    plt.tight_layout()
    plt.show()
else:
    # Escala de grises
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(image, cmap='gray')
    axs[0].set_title('Imagen original (Gris)')
    axs[0].axis('off')

    axs[1].hist(image.ravel(), bins=256, range=(0, 1), color='k', alpha=0.9)
    axs[1].set_title('Histograma (Gris)')
    axs[1].set_xlim(0, 1)

    plt.tight_layout()
    plt.show()
