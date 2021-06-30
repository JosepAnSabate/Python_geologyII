#!/usr/bin/python 

import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0,10,20) #numpy entre 0 y 10 20 valores espaciado lineal

print (x)

y = x ** 2.0
print(y)

y2 = x ** 1.5
print(y2)
#Tamanyo de la figura
plt.figure(figsize=(9, 3))
#dibujar tramas tam linea 2 tamanyo circulo 12
plt.plot(x,y,"bo-",linewidth=2,markersize=12,label="Elevado a 2")
# anyade los otros val de y en gs- green quadrados
plt.plot(x,y2,"gs-",linewidth=2,markersize=12, label = "Elevado a 1.5")


plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc = "upper left")#leyenda arriba izq

plt.show() #mostrar grafica

plt.savefig("figura_ejemplo.png")
plt.close()