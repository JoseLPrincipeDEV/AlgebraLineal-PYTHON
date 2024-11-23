import numpy as np

#funciones con vectores
# Función para calcular la media de un vector
def media_vector(v):
    return np.mean(v)

# Función para calcular la mediana de un vector
def mediana_vector(v):
    return np.median(v)

# Función para calcular la varianza de un vector
def varianza_vector(v):
    return np.var(v)

# Función para calcular la desviación estándar de un vector
def desviacion_estandar_vector(v):
    return np.std(v)

# Función para calcular el valor máximo de un vector
def maximo_vector(v):
    return np.max(v)

# Función para calcular el valor mínimo de un vector
def minimo_vector(v):
    return np.min(v)

# Función para calcular el rango (diferencia entre el máximo y mínimo) de un vector
def rango_vector(v):
    return np.ptp(v)

# Función para calcular la suma de los elementos de un vector
def suma_vector(v):
    return np.sum(v)

# Definir un vector de ejemplo
v = np.array([1, 2, 3, 4, 5])

# Calcular estadísticas del vector
print("Media del vector:", media_vector(v))
print("Mediana del vector:", mediana_vector(v))
print("Varianza del vector:", varianza_vector(v))
print("Desviación estándar del vector:", desviacion_estandar_vector(v))
print("Valor máximo del vector:", maximo_vector(v))
print("Valor mínimo del vector:", minimo_vector(v))
print("Rango del vector:", rango_vector(v))
print("Suma de los elementos del vector:", suma_vector(v))


#funciones con matrices
# Función para calcular la media de cada columna de una matriz
def media_matriz_columna(matriz):
    return np.mean(matriz, axis=0)

# Función para calcular la media de cada fila de una matriz
def media_matriz_fila(matriz):
    return np.mean(matriz, axis=1)

# Función para calcular la mediana de cada columna de una matriz
def mediana_matriz_columna(matriz):
    return np.median(matriz, axis=0)

# Función para calcular la varianza de cada columna de una matriz
def varianza_matriz_columna(matriz):
    return np.var(matriz, axis=0)

# Función para calcular la desviación estándar de cada columna de una matriz
def desviacion_estandar_matriz_columna(matriz):
    return np.std(matriz, axis=0)

# Función para calcular el valor máximo de cada columna de una matriz
def maximo_matriz_columna(matriz):
    return np.max(matriz, axis=0)

# Función para calcular el valor mínimo de cada columna de una matriz
def minimo_matriz_columna(matriz):
    return np.min(matriz, axis=0)

# Función para calcular el rango (diferencia entre el máximo y mínimo) de cada columna de una matriz
def rango_matriz_columna(matriz):
    return np.ptp(matriz, axis=0)

# Función para calcular la suma de los elementos de cada columna de una matriz
def suma_matriz_columna(matriz):
    return np.sum(matriz, axis=0)

# Definir una matriz de ejemplo
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calcular estadísticas por columna
print("Media por columna de la matriz:", media_matriz_columna(matriz))
print("Mediana por columna de la matriz:", mediana_matriz_columna(matriz))
print("Varianza por columna de la matriz:", varianza_matriz_columna(matriz))
print("Desviación estándar por columna de la matriz:", desviacion_estandar_matriz_columna(matriz))
print("Máximo por columna de la matriz:", maximo_matriz_columna(matriz))
print("Mínimo por columna de la matriz:", minimo_matriz_columna(matriz))
print("Rango por columna de la matriz:", rango_matriz_columna(matriz))
print("Suma por columna de la matriz:", suma_matriz_columna(matriz))

# Calcular estadísticas por fila
print("Media por fila de la matriz:", media_matriz_fila(matriz))

# Correlación entre dos matrices
matriz2 = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
print("Correlación entre las dos matrices:", correlacion_matriz(matriz, matriz2))
#funcion con formula cuadratica 

def resolver_ecuacion_cuadratica(a, b, c):
    # Calcular el discriminante (b^2 - 4ac)
    discriminante = b**2 - 4*a*c
    
    # Si el discriminante es mayor o igual a 0, hay soluciones reales
    if discriminante >= 0:
        # Soluciones reales
        x1 = (-b + np.sqrt(discriminante)) / (2 * a)
        x2 = (-b - np.sqrt(discriminante)) / (2 * a)
        return (x1, x2)
    else:
        # Soluciones complejas
        parte_real = -b / (2 * a)
        parte_imaginaria = np.sqrt(-discriminante) / (2 * a)
        x1 = parte_real + parte_imaginaria * 1j
        x2 = parte_real - parte_imaginaria * 1j
        return (x1, x2)

print("el valor de la ecuacion cuadratica es ", resolver_ecuacion_cuadratica(1,-8,15))


# Matriz de coeficientes A y vector B
A = np.array([[2, 3], [4, 1]])
B = np.array([5, 6])

# Resolver el sistema de ecuaciones
solucion = np.linalg.solve(A, B)
print("Solución del sistema de ecuaciones:", solucion)
