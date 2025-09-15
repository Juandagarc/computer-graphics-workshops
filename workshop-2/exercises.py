# Solución del Taller: Programación en Python 🐍
# Realizado por: Juan David García Arce

# Ejercicio 1: Calculadora Básica
def suma(a, b):
    """Función para sumar dos números"""
    return a + b

def resta(a, b):
    """Función para restar dos números"""
    return a - b

def multiplicacion(a, b):
    """Función para multiplicar dos números"""
    return a * b

def division(a, b):
    """Función para dividir dos números"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def calculadora():
    """Función principal de la calculadora"""
    print("=== CALCULADORA BÁSICA ===")
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        operacion = input("Seleccione una operación (1-4): ")

        if operacion == "1":
            resultado = suma(num1, num2)
            print(f"\n{num1} + {num2} = {resultado}")
        elif operacion == "2":
            resultado = resta(num1, num2)
            print(f"\n{num1} - {num2} = {resultado}")
        elif operacion == "3":
            resultado = multiplicacion(num1, num2)
            print(f"\n{num1} × {num2} = {resultado}")
        elif operacion == "4":
            resultado = division(num1, num2)
            print(f"\n{num1} ÷ {num2} = {resultado}")
        else:
            print("Operación no válida")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


# Ejercicio 2: Filtrado de Lista de Pares
def filtrar_pares(lista):
    """Función que filtra los números pares de una lista"""
    numeros_pares = []
    for numero in lista:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares

def ejercicio_filtrado():
    """Ejercicio de demostración del filtrado de pares"""
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(f"Lista original: {lista_numeros}")
    pares = filtrar_pares(lista_numeros)
    print(f"Números pares: {pares}")


# Ejercicio 3: Conversión de Temperaturas
def convertir_temperaturas(temperaturas_celsius):
    """Convierte una lista de temperaturas de Celsius a Fahrenheit usando map y lambda"""
    # Fórmula: F = (C × 9/5) + 32
    fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperaturas_celsius))
    return fahrenheit

def ejercicio_temperaturas():
    """Ejercicio de demostración de conversión de temperaturas"""
    celsius = [0, 20, 25, 30, 37, 100]
    print(f"Temperaturas en Celsius: {celsius}")
    fahrenheit = convertir_temperaturas(celsius)
    print(f"Temperaturas en Fahrenheit: {fahrenheit}")

    # Mostrar la conversión detallada
    print("\nConversión detallada:")
    for c, f in zip(celsius, fahrenheit):
        print(f"{c}°C = {f:.1f}°F")


# Ejercicio 4: Conversión de Calificaciones
def convertir_calificaciones(calificaciones_numericas):
    """Convierte calificaciones numéricas a letras"""
    calificaciones_letras = []

    for calificacion in calificaciones_numericas:
        if calificacion >= 90:
            calificaciones_letras.append('A')
        elif calificacion >= 80:
            calificaciones_letras.append('B')
        elif calificacion >= 70:
            calificaciones_letras.append('C')
        elif calificacion >= 60:
            calificaciones_letras.append('D')
        else:
            calificaciones_letras.append('F')

    return calificaciones_letras

def ejercicio_calificaciones():
    """Ejercicio de demostración de conversión de calificaciones"""
    notas = [95, 87, 76, 65, 45, 92, 58, 83]
    print(f"Calificaciones numéricas: {notas}")
    letras = convertir_calificaciones(notas)
    print(f"Calificaciones en letras: {letras}")

    # Mostrar la conversión detallada
    print("\nConversión detallada:")
    for nota, letra in zip(notas, letras):
        print(f"{nota} → {letra}")


# Ejercicio 5: Contador de Frecuencia de Palabras
def contar_palabras(texto):
    """Cuenta la frecuencia de cada palabra en un texto"""
    # Convertir a minúsculas
    texto_lower = texto.lower()

    # Eliminar signos de puntuación básicos
    signos = ".,;:!?¿¡\"'()[]{}+-*/=<>@#$%^&"
    for signo in signos:
        texto_lower = texto_lower.replace(signo, "")

    # Dividir en palabras
    palabras = texto_lower.split()

    # Contar frecuencias
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias

def ejercicio_frecuencia():
    """Ejercicio de demostración del contador de palabras"""
    texto = "Python es un lenguaje de programación. Python es fácil de aprender y Python es poderoso."
    print(f"Texto: {texto}")
    frecuencias = contar_palabras(texto)
    print(f"\nFrecuencia de palabras:")
    for palabra, frecuencia in frecuencias.items():
        print(f"'{palabra}': {frecuencia}")


# Ejercicio 6: Búsqueda Manual en una Lista
def buscar_elemento(lista, elemento):
    """Busca un elemento en una lista y retorna su índice"""
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def ejercicio_busqueda():
    """Ejercicio de demostración de búsqueda manual"""
    lista = ["manzana", "banana", "naranja", "uva", "pera", "kiwi"]
    print(f"Lista: {lista}")

    elementos_buscar = ["naranja", "pera", "mango"]
    for elemento in elementos_buscar:
        indice = buscar_elemento(lista, elemento)
        if indice != -1:
            print(f"'{elemento}' encontrado en el índice {indice}")
        else:
            print(f"'{elemento}' no encontrado en la lista")


# Ejercicio 7: Validación de Paréntesis
def validar_parentesis(cadena):
    """Valida si una cadena de paréntesis está balanceada"""
    contador = 0

    for caracter in cadena:
        if caracter == '(':
            contador += 1
        elif caracter == ')':
            contador -= 1
            # Si el contador es negativo, hay más paréntesis de cierre que de apertura
            if contador < 0:
                return False

    # Al final, el contador debe ser 0 para estar balanceado
    return contador == 0

def ejercicio_parentesis():
    """Ejercicio de demostración de validación de paréntesis"""
    casos_prueba = [
        "()",
        "(())",
        "((()))",
        "()())",
        "(()",
        ")(",
        "()()()",
        "(()(()))"
    ]

    print("Validación de paréntesis:")
    for caso in casos_prueba:
        resultado = validar_parentesis(caso)
        estado = "✓ Balanceado" if resultado else "✗ No balanceado"
        print(f"'{caso}' → {estado}")


# Ejercicio 8: Ordenamiento Personalizado de Tuplas
def ordenar_tuplas(lista_tuplas):
    """Ordena una lista de tuplas (nombre, edad) por edad y luego por nombre"""
    # Ordenar primero por edad (segundo elemento) y luego por nombre (primer elemento)
    return sorted(lista_tuplas, key=lambda tupla: (tupla[1], tupla[0]))

def ejercicio_ordenamiento():
    """Ejercicio de demostración de ordenamiento de tuplas"""
    personas = [
        ("Ana", 25),
        ("Carlos", 30),
        ("Beatriz", 25),
        ("David", 22),
        ("Elena", 30),
        ("Fernando", 28)
    ]

    print("Lista original:")
    for persona in personas:
        print(f"  {persona[0]}, {persona[1]} años")

    personas_ordenadas = ordenar_tuplas(personas)

    print("\nLista ordenada (por edad, luego por nombre):")
    for persona in personas_ordenadas:
        print(f"  {persona[0]}, {persona[1]} años")


# Función para ejecutar todos los ejercicios
def ejecutar_todos_ejercicios():
    """Ejecuta todos los ejercicios de demostración"""
    print("="*60)
    print("EJECUTANDO TODOS LOS EJERCICIOS DE DEMOSTRACIÓN")
    print("="*60)

    print("\n1. FILTRADO DE PARES:")
    ejercicio_filtrado()

    print("\n2. CONVERSIÓN DE TEMPERATURAS:")
    ejercicio_temperaturas()

    print("\n3. CONVERSIÓN DE CALIFICACIONES:")
    ejercicio_calificaciones()

    print("\n4. CONTADOR DE FRECUENCIA:")
    ejercicio_frecuencia()

    print("\n5. BÚSQUEDA MANUAL:")
    ejercicio_busqueda()

    print("\n6. VALIDACIÓN DE PARÉNTESIS:")
    ejercicio_parentesis()

    print("\n7. ORDENAMIENTO DE TUPLAS:")
    ejercicio_ordenamiento()
