# Operaciones con Vectores

## Suma de Vectores

La suma de dos vectores u y v se realiza sumando sus componentes correspondientes.

Si u = (u1, u2, …, un) y v = (v1, v2, …, vn), entonces:

u + v = (u1 + v1, u2 + v2…, un + vn)

### Ejemplo:

u = (1, 2, 3), v = (4, 5, 6)

u + v = (1 + 4, 2 + 5, 3 + 6) = (5, 7, 9)

## Resta de Vectores

La resta de dos vectores u y v se realiza restando sus componentes correspondientes.

Si u = (u1, u2, …, un) y v = (v1, v2, …, vn), entonces:

u - v = (u1 - v1, u2 - v2…, un - vn)

### Ejemplo:

u = (1, 2, 3), v = (4, 5, 6)

u - v = (1 - 4, 2 - 5, 3 - 6) = (-3, -3, -3)

## Multiplicación de un Vector por un Escalar

La multiplicación de un vector u por un escalar k se realiza multiplicando cada componente del vector por el escalar.

Si u = (u1, u2, …, un) entonces:

ku = (ku1, ku2, …, kun)

### Ejemplo:

u = (1, 2, 3), k = 3

ku = 3 u = (3 .1, 3 . 2, 3 . 3) = (3, 6, 9)

## Producto Escalar (o Producto Punto)

El producto escalar de dos vectores u y v se calcula multiplicando sus componentes correspondientes y sumando los resultados.

Si u = (u1, u2, …, un) y v = (v1, v2, …, vn), entonces:

u . v = (u1 . v1, u2 . v2…, un .vn)

### Ejemplo:

u = (1, 2, 3), v = (4, 5, 6)

u . v = 1 . 4 + 2 . 5 + 3 . 6 = 4 + 10 + 18 = 32

##Suma de Matrices 
 
Dos matrices A y B de igual tamaño m x n se suman sumando sus elementos 
correspondientes: 

            |a11+b11 a12+b12 ... a1n+b1n|         
            |a21+b21 a12+b22 ... a2n+b2n|  
C = A + B = |   .       .           .   |
            |   .       .           .   |
            |   .       .           .   |
            |am1+bm1 am2+bm2 ... amn+bmn|  

##Multiplicación por un Escalar 
 
Multiplicar una matriz \(A\) por un escalar \(k\) implica multiplicar cada elemento 
de \(A\) por \(k\):

            |K*a11 K*a12 ... K*a1n|         
            |K*a21 K*a22 ... K*a2n| 
    K * A = | .     .         .   |
            | .     .         .   |
            | .     .         .   |
            |K*am1 K*am2 ... K*amn| 


##Multiplicación por un Escalar

El producto de dos matrices A de tamaño m x n y B de tamaño n x p da como 
resultado una matriz C de tamaño m x p, donde cada elemento cij se calcula 
como la suma de los productos de los elementos de la i-ésima fila de A por los 
elementos de la j-ésima columna de B: 

A = |1 2| , B = |2 0| 
    |3 4|       |1 3|


C = AB = |1*2 + 2*1   1*0 + 2*3|  = | 4 6 |
         |3*2 + 4*1   4*0 + 4*3|    |10 12|