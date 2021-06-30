#!/usr/bin/python 
# -*- coding: latin-1 -*-
import numpy as np 


# 1 Introduccion a los array de numpy 

zero_vector = np.zeros(5) #matriz de 5 0

print(zero_vector)

zero_matriz= np.zeros((5,3)) #matriz 5 filas 3 col

print(zero_matriz) 


A = np.array([[3,6],[5,7]]) #matriz ordenada en filas

print (A)
print (A.transpose()) #transponer matriz

# Ejercicio 1: ¿La longitud de array de numpy se puede modificar? 
# - No 

# Ejercicio 2: ¿Como generar el siguiente resultado en numpy¿?
#  numpy.array([0.,0.,0.,0.])


# Ejercicio 3: considerando el siguiente codigo 
#x = numpy.array([[3,6],[5,7]])
#y = x.transpose()
# print(y)
# ¿Cuál crees que será el resultado?
# [[3 5]
# [6 7]]


# 2 Cortar los array de numpy 

# 2.1 Matrices unidimensionales

x = np.array([1,2,3])
y = np.array([2,4,6])

print(x[2])

print(x[0:2])

z = x+y #suma de matrices
print(z)

# 2.2 Matrices bidimensionales

X = np.array([[1,2,3],[4,5,6]])

Y = np.array([[3,4,5],[9,10,11]])

print(X[:,1])
print(Y[:,1])
#suma 2 y 4 y 5 con 10
suma = X[:,1] + Y[:,1]  # Las listas de python se concatenan mientras que las numpy array operan entre si
print(suma)

# Ejercicio 1 : teniendo en cunta la siguientes lineas 
j = np.array([1,2,5])
print('Ej1')
# como llegar al siguiente resultado:  array([2]) ¿? 
# Consejo , acceder mediante fila y columna.
print(j[1])#no
#asi
indi = [1]
print(j[indi])

# Ejercicio 2: Teniendo en cuenta las siguientes lineas 
# Piensa antes en el resultado y confirma si es el que esperabas.
 #a = np.array([1,2])
 #b= np.array([3,4,5])
 #print (a+ b)

#Resultado esperado, error. Para sumar matrices deben tener mismo num de filas y col

# 3 Indexado de numpy arays 

z = np.array([1,4,5,8,9,11,15])

ind= [0,2,4]

print(z[ind])

ind = np.array([0,2,4])

print(z[ind])


# Se pueden utilizar indices logicos  (True, False)
print(z > 5) #valors inf a 5 null


# 4 Mutabilidad e Inmutabilidad
# Si son vistas son mutables 
# p.e 
z = np.array([1,3,5,7,9])

x = z[0:3] # No es una copia , es una seleccion, mutable:

print(x)#acced al el x i z tambien

x[0]=3

print(x)
print (z)

# Si son copias son inmutables
z = np.array([1,3,5,7,9])

ind = np.array([0,1,2]) # Crea un nuevo objeto 

print(z)
print(ind)

x = z[ind] # Seleccion mediante un nuevo objeto, realzia una copia de valores z segun los valores de ind.

print(x) 
x[0] = 3

print (x)
print (z)

# No hay que utilziar vistas sino copias de objetos si no queremos modificar el objeto original.


# 5 Generacion de numeros aleatorios 

x = np.random.random(10)

print(np.any(x>0.8)) #condicional boolean

print(np.all(x>=0.1)) #otro condicional boolean

print(x)


# 6 Creacion y exploracion de numpy arrays 

# Creacion de una matriz de valores lineales
print("Ejercicio 6")
lineal = np.linspace(0,100,10)
print(lineal)

logaritmicos1 = np.logspace(1,2,10)
print( "log1",logaritmicos1)

logaritmicos2 = np.logspace(np.log10(10),np.log10(100),10)
print("log2", logaritmicos2)



# 7 Info de numpy
# De numero de listas y longitud de cada una --> mediante shape (forma)
# De longitud total --> size

X = np.array([[1,2,3],[4,5,6]])

print("Shape = ", X.shape)
print("Size= ", X.size)

