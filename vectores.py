import numpy as np

#Definimos la regla para la operciones de vectores
#Esta regla dice que los vectores tienen que tener la misma logitud
def verificarLongitud(vector1, vector2):
    if len(vector1) == len(vector2):
        return True
    else:
        if len(vector1) > len(vector2):
            print(f"El vector 2 tiene menor longitud que el vector 1 \n {vector1} \n{vector2} \n Los vectores tienen que tener la misma longitud.")
        else:
            print(f"El vector 1 tiene menor longitud que el vector 2 \n {vector1} \n{vector2} \n Los vectores tienen que tener la misma longitud.")
        return False

def sumarVectores():
    #Con input reolectamos los datos
    #Con la funcion .split devidimos el texto ingresado en una lista de subcadenas, utilizando un delimitador
    #text = "1,2,3,4" text.split() = ["1","2","3","4"] 
    #La funcion map aplica la funcion int a cada elemento de la lista ["1","2","3","4"] => 1,2,3,4
    #la funcion list convierte el objeto map en una lista de enteros [1,2,3,4]
    vector1 = np.array(list(map(int, input("Ingresa los números del vector 1 separados por comas: ").split(','))))
    vector2 = np.array(list(map(int, input("Ingresa los números del vector 2 separados por comas: ").split(','))))

    if verificarLongitud(vector1, vector2):
        resultado = vector1 + vector2
        print("Resultado de la suma:", resultado)

def restaVectores():
    vector1 = np.array(list(map(int, input("Ingresa los números del vector 1 separados por comas: ").split(','))))
    vector2 = np.array(list(map(int, input("Ingresa los números del vector 2 separados por comas: ").split(','))))

    if verificarLongitud(vector1, vector2):
        resultado = vector1 - vector2
        print("Resultado de la resta:", resultado)

def multiplicacionVectores():
    vector = np.array(list(map(int, input("Ingresa los números del vector 1 separados por comas: ").split(','))))
    escalar = int(input("Ingresa el escalar: "))

    resultado = vector * escalar
    print("Resultado de la multiplicación por escalar:", resultado)
        
def productoPuntoVectores():
    vector1 = np.array(list(map(int, input("Ingresa los números del vector 1 separados por comas: ").split(','))))
    vector2 = np.array(list(map(int, input("Ingresa los números del vector 2 separados por comas: ").split(','))))

    if verificarLongitud(vector1, vector2):
        resultado = np.dot(vector1, vector2)
        print("Resultado del producto punto:", resultado)

def verificarOrtogonalidad():
    vector1 = np.array(list(map(int, input("Ingresa los números del vector 1 separados por comas: ").split(','))))
    vector2 = np.array(list(map(int, input("Ingresa los números del vector 2 separados por comas: ").split(','))))

    if verificarLongitud(vector1, vector2):
        producto_punto = np.dot(vector1, vector2)
        if producto_punto == 0:
            print("Los vectores son ortogonales.")
        else:
            print("Los vectores no son ortogonales.")
        print("Producto punto:", producto_punto)


def sumaDeMatrices():
    filas1 = int(input("Ingresa el número de filas de la matriz 1: "))
    columnas1 = int(input("Ingresa el número de columnas de la matriz 1: "))
    print("Ingresa los elementos de la matriz 1 fila por fila:")
    #For _in range(filas) hace que cada vez que se ejecuta, solicita al usuario que ingrese una línea de texto , la divide en una lista de enteros y la agrega a una lista más grande.
    #Por ejemplo, si filas1 es 2, el usuario podría ingresar "1,2,3" la primera vez y "4,5,6" la segunda vez. La comprensión de lista producirá [[1, 2, 3], [4, 5, 6]]
    matriz1 = np.array([list(map(int, input().split(','))) for _ in range(filas1)])

    filas2 = int(input("Ingresa el número de filas de la matriz 2: "))
    columnas2 = int(input("Ingresa el número de columnas de la matriz 2: "))
    print("Ingresa los elementos de la matriz 2 fila por fila:")
    matriz2 = np.array([list(map(int, input().split(','))) for _ in range(filas2)])

    #La condicion es que el número de filas de la primera matriz sea igual al número de filas de la segunda matriz
    #Y que el número de columnas de la primera matriz sea igual al número de columnas de la segunda matriz
    if filas1 == filas2 and columnas1 == columnas2: 
        resultado = matriz1 + matriz2 
        print("Resultado de la Suma de matrices:") 
        print(resultado)
    else:
        print("No se pueden sumar las matrices: ambas matrices deben tener el mismo tamaño.")

def multiplicacionEscalarMatrices():
    filas = int(input("Ingresa el número de filas de la matriz: "))
    columnas = int(input("Ingresa el número de columnas de la matriz: "))
    print("Ingresa los elementos de la matriz fila por fila:")
    matriz = np.array([list(map(int, input().split(','))) for _ in range(filas)])

    escalar = int(input("Ingresa escalar: "))

    resultado = matriz * escalar
    print("Resultado de la multiplicación de matrices:")
    print(resultado)

def multiplicacionMatrices():
    filas1 = int(input("Ingresa el número de filas de la matriz 1: "))
    columnas1 = int(input("Ingresa el número de columnas de la matriz 1: "))
    print("Ingresa los elementos de la matriz 1 fila por fila:")
    matriz1 = np.array([list(map(int, input().split(','))) for _ in range(filas1)])

    filas2 = int(input("Ingresa el número de filas de la matriz 2: "))
    columnas2 = int(input("Ingresa el número de columnas de la matriz 2: "))
    print("Ingresa los elementos de la matriz 2 fila por fila:")
    matriz2 = np.array([list(map(int, input().split(','))) for _ in range(filas2)])

    #La condicion nos dice que el numero de columnas de la primera matriz
    #Tiene que se igual a al numero de filas de la segunda matriz 
    if columnas1 == filas2:
        resultado = np.dot(matriz1, matriz2)
        print("Resultado de la multiplicación de matrices:")
        print(resultado)
    else:
        print("No se pueden multiplicar las matrices: el número de columnas de la primera matriz debe ser igual al número de filas de la segunda.")

def menu():
    print("SISTEMA DE OPERACIONES CON VECTORES Y MATRICES")
    print("1. Sumar vectores")
    print("2. Restar vectores")
    print("3. Multiplicar vector por escalar")
    print("4. Producto punto de vectores")
    print("5. Verificar ortogonalidad de vectores")
    print("6. Suma de matrices")
    print("7. Multiplicacion por un escalar matrices")
    print("8. Multiplicar matrices")
    print("9. Salir")

    while True:
            opcion = input("\nElige una opción (1-9): ")
            if opcion == '1':
                print("1. Sumar vectores")
                sumarVectores()
            elif opcion == '2':
                print("2. Restar vectores")
                restaVectores()
            elif opcion == '3':
                print("3. Multiplicar vector por escalar")
                multiplicacionVectores()
            elif opcion == '4':
                print("4. Producto punto de vectores")
                productoPuntoVectores()
            elif opcion == '5':
                print("5. Verificar ortogonalidad de vectores")
                verificarOrtogonalidad()
            elif opcion == '6':
                print("6. Suma de matrices")
                sumaDeMatrices()
            elif opcion == '7':
                print("7. Multiplicacion por un escalar matrices")
                multiplicacionEscalarMatrices()
            elif opcion == '8':
                print("8. Multiplicar matrices")
                multiplicacionMatrices()
            elif opcion == '9':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

menu()