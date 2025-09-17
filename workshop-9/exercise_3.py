import numpy as np
import matplotlib.pyplot as plt


def adjust_contrast_gamma(image: np.ndarray, gamma: float) -> np.ndarray:
    """
    Ajusta el contraste en las zonas claras usando corrección gamma.
    Valores de gamma > 1.0 aumentan el contraste en las luces.
    """
    x = np.clip(image, 0.0, 1.0)
    # Fórmula de corrección gamma
    return x ** gamma


def main(image_path: str, gamma_val: float):
    """Carga una imagen, aplica el ajuste gamma y muestra el original vs. el resultado."""
    try:
        original_image = plt.imread(image_path) / 255.0
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar la imagen en la ruta: {image_path}")
        return

    # Aplicar únicamente la transformación gamma
    gamma_contrast_image = adjust_contrast_gamma(original_image, gamma_val)

    # Crear una figura con 2 subplots (1 fila, 2 columnas) para mostrar lado a lado
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle("Comparación de Contraste (Gamma)", fontsize=16)

    # 1. Mostrar la imagen original
    axs[0].imshow(original_image)
    axs[0].set_title('Imagen Original')
    axs[0].axis('off')

    # 2. Mostrar la imagen con contraste gamma
    axs[1].imshow(gamma_contrast_image)
    axs[1].set_title(f'Contraste Zonas Claras (gamma={gamma_val})')
    axs[1].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    IMAGE_FILE = 'assets/cartagena.jpg'
    # Un valor típico de gamma para aumentar contraste en luces es entre 1.5 y 2.5
    GAMMA_VALUE = 2.2

    main(image_path=IMAGE_FILE, gamma_val=GAMMA_VALUE)