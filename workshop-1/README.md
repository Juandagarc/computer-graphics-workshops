# Solución del Taller:️

Este documento contiene la guía y pistas para la solución de los ejercicios propuestos en el taller de física y programación.

**Realizado por:** Juan David García Arce

---

## 📝 Puntos del Taller

A continuación se presentan los ejercicios del taller con pistas para su resolución.

### **1. Cálculo de la Caída Libre**

**Objetivo:** Escribir un programa que calcule y muestre el tiempo que tarda un objeto en caer desde una altura determinada sin resistencia del aire.

**Pistas:**
* Importa el módulo `math` para usar la función de raíz cuadrada: `math.sqrt()`.
* Define la gravedad `g` como una constante (`g = 9.81`).
* La fórmula a implementar es $t = \sqrt{\frac{2h}{g}}$.

---

### **2. Conversión de Unidades de Velocidad**

**Objetivo:** Crear una función que convierta la velocidad de km/h a m/s y viceversa.

**Pistas:**
* Recuerda los factores de conversión:
    * Para convertir de **km/h a m/s**, multiplica por `5/18`.
    * Para convertir de **m/s a km/h**, multiplica por `18/5`.
* Puedes usar una declaración `if/elif/else` dentro de la función para decidir qué conversión realizar según el argumento de entrada.

---

### **3. Cálculo del Desplazamiento**

**Objetivo:** Desarrollar un script que calcule el desplazamiento de un objeto en movimiento rectilíneo uniformemente acelerado.

**Pistas:**
* La fórmula $s = ut + \frac{1}{2}at^2$ se traduce directamente a Python.
* Asegúrate de manejar el exponente correctamente: `t**2`.
* El término $\frac{1}{2}$ se puede escribir como `0.5` para asegurar una operación de punto flotante.

---

### **4. Suma de Vectores**

**Objetivo:** Implementar una función que tome dos vectores representados como listas y devuelva su suma vectorial.

**Pistas:**
* Si los vectores son `v1 = [x1, y1]` y `v2 = [x2, y2]`, el vector resultante es `[x1 + x2, y1 + y2]`.
* Puedes acceder a los elementos por su índice (`v1[0]`, `v1[1]`) para realizar la suma.

---

### **5. Producto Escalar de Vectores**

**Objetivo:** Escribir un programa que calcule el producto escalar de dos vectores y determine el ángulo entre ellos.

**Pistas:**
* El **producto escalar** de `v1 = [x1, y1]` y `v2 = [x2, y2]` es `(x1*x2) + (y1*y2)`.
* Para el **ángulo**, necesitarás la fórmula $\theta = \arccos\left(\frac{v_1 \cdot v_2}{|v_1||v_2|}\right)$.
* Importa `math` para usar `math.acos()` (arcocoseno), `math.sqrt()` (para la magnitud $|v|$) y `math.degrees()` para convertir el resultado de radianes a grados.

---

### **6. Lanzamiento de Proyectil**

**Objetivo:** Crear un script para calcular el alcance máximo ($R$) y la altura máxima ($H$) de un proyectil.

**Pistas:**
* Necesitarás las siguientes fórmulas:
    * Altura Máxima: $H = \frac{v_0^2 \sin^2(\theta)}{2g}$
    * Alcance Máximo: $R = \frac{v_0^2 \sin(2\theta)}{g}$
* Importa el módulo `math` para usar `math.sin()` y `math.radians()`, ya que las funciones trigonométricas en Python esperan el ángulo en radianes.
* No olvides definir la constante de gravedad `g = 9.81`.