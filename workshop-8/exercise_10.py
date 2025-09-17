import numpy as np
import matplotlib.pyplot as plt

try:
    img = plt.imread("assets/utp-logo.jpg")
    fig, axs = plt.subplots(1, 9, figsize=(10, 5))
    img_red = np.copy(img)
    img_red[:, :, 1] = img_red[:, :, 2] = 0
    img_green = np.copy(img)
    img_green[:, :, 0] = img_green[:, :, 2] = 0
    img_blue = np.copy(img)
    img_blue[:, :, 0]  = img_blue[:, :, 1]  = 0

    for ax in axs:
        ax.axis('off')

    axs[0].text(0.5, 0.5, '(', fontsize=12, ha='center')
    axs[1].imshow(img_red)
    axs[1].set_title('Canal Rojo')
    axs[2].text(0.5, 0.5, ',', fontsize=12, ha='center')
    axs[3].imshow(img_green)
    axs[3].set_title('Canal Verde')
    axs[4].text(0.5, 0.5, ',', fontsize=12, ha='center')
    axs[5].imshow(img_blue)
    axs[5].set_title('Canal Azul')
    axs[6].text(0.5, 0.5, ')', fontsize=12, ha='center')
    axs[7].text(0.5, 0.5, '=', fontsize=12, ha='center')
    axs[8].imshow(img)
    axs[8].set_title('Logo original')

    plt.subplots_adjust(wspace=0)
    plt.tight_layout()
    plt.show()
except FileNotFoundError:
    print("No se encontró la imagen en la ruta especificada.")