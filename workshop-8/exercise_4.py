import numpy as np
import matplotlib.pyplot as plt

try:
    img = plt.imread("assets/utp-logo.jpg")
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    img_red = np.copy(img)
    img_red[:, :, 1] = img_red[:, :, 2] = 0


    axs[0].imshow(img)
    axs[0].set_title('Logo original')
    axs[0].axis('off')

    axs[1].imshow(img_red)
    axs[1].set_title('Canal Rojo')
    axs[1].axis('off')

    plt.tight_layout()
    plt.show()
except FileNotFoundError:
    print("No se encontró la imagen en la ruta especificada.")