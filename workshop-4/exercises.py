import numpy as np


def exercise_1():
    """Ejercicio 1: Crear un Array Unidimensional
    Objetivo: Crear e imprimir un array unidimensional que contenga los números del 1 al 10.
    """
    print("=== Ejercicio 1: Crear un Array Unidimensional ===")
    array_1d = np.arange(1, 11)
    print(f"Array unidimensional del 1 al 10: {array_1d}")
    print(f"Tipo de dato: {array_1d.dtype}")
    print(f"Forma del array: {array_1d.shape}")
    print()


def exercise_2():
    """Ejercicio 2: Crear un Array Multidimensional
    Objetivo: Crear e imprimir una matriz 2D de 3x3 que contenga los números del 1 al 9.
    """
    print("=== Ejercicio 2: Crear un Array Multidimensional ===")
    array_2d = np.arange(1, 10).reshape(3, 3)
    print("Matriz 2D de 3x3 con números del 1 al 9:")
    print(array_2d)
    print(f"Forma del array: {array_2d.shape}")
    print(f"Número de dimensiones: {array_2d.ndim}")
    print()


def exercise_3():
    """Ejercicio 3: Operaciones Básicas con Arrays
    Objetivo: Crear dos arrays unidimensionales, sumarlos y mostrar el resultado en un nuevo array.
    """
    print("=== Ejercicio 3: Operaciones Básicas con Arrays ===")
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([10, 20, 30, 40, 50])
    suma = array1 + array2

    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")
    print(f"Suma de arrays: {suma}")
    print(f"Multiplicación de arrays: {array1 * array2}")
    print(f"Resta (array2 - array1): {array2 - array1}")
    print()


def exercise_4():
    """Ejercicio 4: Funciones Matemáticas
    Objetivo: Calcular la exponencial de cada elemento en un array de números del 1 al 5 y mostrar el resultado.
    """
    print("=== Ejercicio 4: Funciones Matemáticas ===")
    array = np.arange(1, 6)
    exponential = np.exp(array)

    print(f"Array original: {array}")
    print(f"Exponencial de cada elemento: {exponential}")
    print(f"Logaritmo natural: {np.log(array)}")
    print(f"Raíz cuadrada: {np.sqrt(array)}")
    print(f"Potencia al cuadrado: {np.power(array, 2)}")
    print()


def exercise_5():
    """Ejercicio 5: Indexación y Segmentación
    Objetivo: Seleccionar e imprimir únicamente los elementos pares de un array que contiene los números del 1 al 10.
    """
    print("=== Ejercicio 5: Indexación y Segmentación ===")
    array = np.arange(1, 11)
    elementos_pares = array[array % 2 == 0]

    print(f"Array original: {array}")
    print(f"Elementos pares: {elementos_pares}")
    print(f"Primeros 5 elementos: {array[:5]}")
    print(f"Últimos 3 elementos: {array[-3:]}")
    print(f"Elementos del índice 2 al 7: {array[2:8]}")
    print()


def exercise_6():
    """Ejercicio 6: Generación de Datos Aleatorios
    Objetivo: Generar e imprimir un array que contenga 10 números aleatorios con valores entre 0 y 1.
    """
    print("=== Ejercicio 6: Generación de Datos Aleatorios ===")
    # Establecer semilla para reproducibilidad
    np.random.seed(42)

    random_array = np.random.random(10)
    random_integers = np.random.randint(1, 100, 5)
    normal_distribution = np.random.normal(0, 1, 8)

    print(f"10 números aleatorios entre 0 y 1: {random_array}")
    print(f"5 enteros aleatorios entre 1 y 100: {random_integers}")
    print(f"8 números de distribución normal (μ=0, σ=1): {normal_distribution}")
    print()


def exercise_7():
    """Ejercicio 7: Funciones de Agregación
    Objetivo: Crear un array con los números del 1 al 5 y calcular e imprimir la media de sus elementos.
    """
    print("=== Ejercicio 7: Funciones de Agregación ===")
    array = np.arange(1, 6)

    media = np.mean(array)
    suma = np.sum(array)
    maximo = np.max(array)
    minimo = np.min(array)
    desviacion = np.std(array)
    mediana = np.median(array)

    print(f"Array: {array}")
    print(f"Media: {media}")
    print(f"Suma: {suma}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")
    print(f"Desviación estándar: {desviacion:.4f}")
    print(f"Mediana: {mediana}")
    print()


def exercise_8():
    """Ejercicio 8: Creación de Arrays con Funciones de Fábrica
    Objetivo: Crear e imprimir un array que contenga 5 elementos, donde cada elemento sea el número 7.
    """
    print("=== Ejercicio 8: Creación de Arrays con Funciones de Fábrica ===")

    # Diferentes maneras de crear arrays con valores específicos
    array_sevens = np.full(5, 7)
    array_zeros = np.zeros(5)
    array_ones = np.ones(8)
    array_empty = np.empty(3)
    identity_matrix = np.eye(4)
    linspace_array = np.linspace(0, 10, 6)

    print(f"Array de 5 elementos con valor 7: {array_sevens}")
    print(f"Array de 5 ceros: {array_zeros}")
    print(f"Array de 8 unos: {array_ones}")
    print(f"Matriz identidad 4x4:")
    print(identity_matrix)
    print(f"6 números igualmente espaciados de 0 a 10: {linspace_array}")
    print()


def exercise_9():
    """Ejercicio 9: Operaciones de Alineación y Broadcasting
    Objetivo: Sumar dos arrays unidimensionales diferentes utilizando broadcasting y mostrar el resultado.
    """
    print("=== Ejercicio 9: Operaciones de Alineación y Broadcasting ===")

    # Arrays de diferentes tamaños para demostrar broadcasting
    array1 = np.array([1, 2, 3, 4])
    array2 = np.array([10])  # Se puede hacer broadcasting
    array3 = np.array([[1], [2], [3]])  # Array 2D para broadcasting
    array4 = np.array([10, 20, 30, 40])

    # Broadcasting examples
    result1 = array1 + array2
    result2 = array3 + array4
    result3 = array1 * 2  # Broadcasting con escalar

    print(f"Array1: {array1}")
    print(f"Array2 (escalar en array): {array2}")
    print(f"Broadcasting array1 + array2: {result1}")
    print()
    print(f"Array3 (columna): \n{array3}")
    print(f"Array4 (fila): {array4}")
    print(f"Broadcasting array3 + array4: \n{result2}")
    print()
    print(f"Broadcasting con escalar (array1 * 2): {result3}")
    print()


def exercise_10():
    """Ejercicio 10: Funciones de Transformación y Redimensionamiento
    Objetivo: Crear un array con los números del 1 al 6 y transformarlo en una matriz de 2x3.
    """
    print("=== Ejercicio 10: Funciones de Transformación y Redimensionamiento ===")

    array_original = np.arange(1, 7)
    matriz_2x3 = array_original.reshape(2, 3)
    matriz_3x2 = array_original.reshape(3, 2)
    matriz_1x6 = array_original.reshape(1, 6)
    array_flatten = matriz_2x3.flatten()
    array_transpose = matriz_2x3.T

    print(f"Array original: {array_original}")
    print(f"Forma original: {array_original.shape}")
    print()
    print(f"Matriz 2x3:")
    print(matriz_2x3)
    print(f"Forma: {matriz_2x3.shape}")
    print()
    print(f"Matriz 3x2:")
    print(matriz_3x2)
    print()
    print(f"Matriz 1x6:")
    print(matriz_1x6)
    print()
    print(f"Array aplanado desde 2x3: {array_flatten}")
    print(f"Transpuesta de matriz 2x3:")
    print(array_transpose)
    print()


def run_all_exercises():
    """Ejecutar todos los ejercicios del taller"""
    print("🐍 TALLER 4: Manejo de Arrays con NumPy 🐍")
    print("=" * 60)
    print()

    exercises = [
        exercise_1, exercise_2, exercise_3, exercise_4, exercise_5,
        exercise_6, exercise_7, exercise_8, exercise_9, exercise_10
    ]

    for i, exercise in enumerate(exercises, 1):
        exercise()
        if i < len(exercises):
            print("-" * 60)
            print()
