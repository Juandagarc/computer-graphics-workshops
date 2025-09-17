import numpy as np
import matplotlib.pyplot as plt


def zoom_region(image: np.ndarray, top: int, left: int, height: int, width: int, scale: int) -> np.ndarray:
    if scale < 1:
        raise ValueError("El factor de escala debe ser un entero >= 1")
    h, w = image.shape[:2]
    top = max(0, min(top, h - 1))
    left = max(0, min(left, w - 1))
    bottom = max(top + 1, min(top + height, h))
    right = max(left + 1, min(left + width, w))
    crop = image[top:bottom, left:right]
    # Ampliar por repetición (vecino más cercano)
    zoomed = np.repeat(np.repeat(crop, scale, axis=0), scale, axis=1)
    return zoomed


# Entradas del usuario
print("Ingrese la región a recortar (top, left, height, width) y un factor de escala entero (>=1)")
vals = list(map(int, input("Valores separados por espacios: ").split()))
if len(vals) != 5:
    raise ValueError("Debe ingresar exactamente 5 valores: top left height width scale")

top, left, height, width, scale = vals

# Cargar imagen
image = np.asarray(plt.imread("assets/cartagena.jpg"), dtype=np.float64) / 255.0

# Aplicar zoom
zoomed = zoom_region(image, top, left, height, width, scale)

# Mostrar
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(image)
axs[0].set_title('Imagen original')
axs[0].axis('off')

axs[1].imshow(zoomed)
axs[1].set_title(f'Zoom región ({top},{left},{height},{width}) x{scale}')
axs[1].axis('off')

plt.tight_layout()
plt.show()
