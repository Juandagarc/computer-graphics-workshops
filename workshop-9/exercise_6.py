import numpy as np
import matplotlib.pyplot as plt


def rotate_image_nn(image: np.ndarray, degrees: float) -> np.ndarray:
    radians = np.deg2rad(degrees)
    cos_t, sin_t = np.cos(radians), np.sin(radians)

    h, w = image.shape[:2]
    cx, cy = (w - 1) / 2.0, (h - 1) / 2.0

    # Coordenadas de salida
    x = np.arange(w)
    y = np.arange(h)
    Xo, Yo = np.meshgrid(x, y)
    Xc = Xo - cx
    Yc = Yo - cy

    # Mapeo inverso (R^T)
    Xi = cos_t * Xc + sin_t * Yc + cx
    Yi = -sin_t * Xc + cos_t * Yc + cy

    Xi_r = np.rint(Xi).astype(int)
    Yi_r = np.rint(Yi).astype(int)

    # Imagen destino
    if image.ndim == 3:
        out = np.zeros_like(image)
    else:
        out = np.zeros((h, w), dtype=image.dtype)

    # Máscara de válidos
    mask = (Xi_r >= 0) & (Xi_r < w) & (Yi_r >= 0) & (Yi_r < h)

    if image.ndim == 3:
        out[Yo[mask], Xo[mask], :] = image[Yi_r[mask], Xi_r[mask], :]
    else:
        out[Yo[mask], Xo[mask]] = image[Yi_r[mask], Xi_r[mask]]

    return out


# Entrada de ángulo
angle = float(input("Ingrese el ángulo de rotación en grados (positivo antihorario): "))

# Cargar imagen
image = np.asarray(plt.imread("assets/cartagena.jpg"), dtype=np.float64) / 255.0

# Rotar
rotated = rotate_image_nn(image, angle)

# Mostrar resultados
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(image)
axs[0].set_title('Imagen original')
axs[0].axis('off')

axs[1].imshow(rotated)
axs[1].set_title(f'Rotada {angle}° (NN)')
axs[1].axis('off')

plt.tight_layout()
plt.show()
