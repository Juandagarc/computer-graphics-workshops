# -*- coding: utf-8 -*-
"""
Script para el análisis por lotes de imágenes termográficas.

Este módulo carga y procesa una lista de archivos de imagen (.tiff),
realizando un análisis completo para cada uno y mostrando los resultados
de forma secuencial.
"""
import numpy as np
import matplotlib.pyplot as plt

def analizar_imagen_termografica(nombre_archivo):
    """
    Carga, analiza y visualiza una única imagen termográfica.

    Args:
        nombre_archivo (str): La ruta al archivo de imagen .tiff.
    """
    print(f"\n{'='*20} ANÁLISIS DE: {nombre_archivo} {'='*20}")

    try:
        # --- ETAPA 1: Ingesta y Calibración de Datos ---
        ImagenTiff = plt.imread(nombre_archivo)
        D = np.double(ImagenTiff)
    except FileNotFoundError:
        print(f"ERROR: No se pudo encontrar el archivo '{nombre_archivo}'. Saltando al siguiente.")
        return # Termina la ejecución para este archivo si no se encuentra

    # Constantes de calibración del sensor
    TEM_MIN = -40
    TEM_MAX = 160
    NBits = 14

    # Transformación lineal de datos crudos a grados Celsius
    raw_range = 2**NBits
    temp_range = TEM_MAX - TEM_MIN
    MatrizCenti = (D / raw_range) * temp_range + TEM_MIN

    # --- ETAPA 2: Análisis Estadístico ---
    print("--- Analíticas de la Imagen Térmica ---")
    temp_promedio = np.mean(MatrizCenti)
    temp_mediana = np.median(MatrizCenti)
    hist, bin_edges = np.histogram(MatrizCenti, bins=100)
    modal_bin_index = np.argmax(hist)
    temp_moda = (bin_edges[modal_bin_index] + bin_edges[modal_bin_index + 1]) / 2
    temp_max = np.max(MatrizCenti)
    temp_min = np.min(MatrizCenti)
    max_y, max_x = np.unravel_index(np.argmax(MatrizCenti), MatrizCenti.shape)
    min_y, min_x = np.unravel_index(np.argmin(MatrizCenti), MatrizCenti.shape)

    print(f"Temperatura Media: {temp_promedio:.2f} °C")
    print(f"Temperatura Mediana: {temp_mediana:.2f} °C")
    print(f"Temperatura Modal (Estimada): {temp_moda:.2f} °C")
    print(f"Anomalía Caliente (Máx): {temp_max:.2f} °C en coordenadas ({max_x}, {max_y})")
    print(f"Anomalía Fría (Mín): {temp_min:.2f} °C en coordenadas ({min_x}, {min_y})")
    print("-" * 40)


    # --- ETAPA 3: Visualización de Datos ---
    fig, axs = plt.subplots(1, 2, figsize=(15, 7))
    fig.suptitle(f"Reporte Termográfico: {nombre_archivo}", fontsize=16)

    # Subplot 1: Mapa de Calor (cmap invertido para calor oscuro y frío claro)
    im = axs[0].imshow(MatrizCenti, cmap='hot_r', origin='upper')
    axs[0].set_title("Mapa de Calor Térmico")
    axs[0].set_xlabel("Coordenada X (píxeles)")
    axs[0].set_ylabel("Coordenada Y (píxeles)")
    fig.colorbar(im, ax=axs[0], shrink=0.85, label="Temperatura (°C)")
    axs[0].plot(max_x, max_y, 'o', color='magenta', markersize=8, label=f'Máxima: {temp_max:.2f}°C')
    axs[0].plot(min_x, min_y, 'D', color='cyan', markersize=8, label=f'Mínima: {temp_min:.2f}°C')
    axs[0].legend()

    # Subplot 2: Histograma
    axs[1].hist(MatrizCenti.flatten(), bins=75, color='green', alpha=0.75)
    axs[1].set_title("Distribución de Temperaturas")
    axs[1].set_xlabel("Temperatura (°C)")
    axs[1].set_ylabel("Conteo de Píxeles (Frecuencia)")
    axs[1].grid(axis='y', linestyle='--', alpha=0.7)

    # --- ETAPA 4: Presentación Final ---
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# --- Proceso Principal ---
# Lista de los archivos que subiste para ser procesados.
archivos_a_procesar = [
    "FLIR_00088.tiff",
    "FLIR_00641.tiff",
    "FLIR_02399.tiff",
    "FLIR_06983.tiff"
]

# Itera sobre la lista y ejecuta el análisis para cada archivo.
for archivo in archivos_a_procesar:
    analizar_imagen_termografica(archivo)

print("\nAnálisis de todas las imágenes completado. ✅")