#!/usr/bin/python 
# -*- coding: latin-1 -*-

from obspy import read
import matplotlib.pyplot as plt


#Ignore warnings due to python 2 and 3 conflict
import warnings
warnings.filterwarnings("ignore")

stream = read("C:/Users/34639/Desktop/curspython/sismologia/datos_entrada_sismograma/.SRU..Y.D.2013.158.8_8_5.SAC", debug_headers=True)

# Accedemos a los datos
tr = stream[0]
print(tr.stats) #estadisticas

tr.normalize() #normalizacion de los datos
delta = tr.stats.sac.delta #accedemos al valor de metadato delta
print(delta)
print(tr.data)

tiempo = tr.times()
datos =tr.data #datos del sismograma

# Ploteamos
plt.figure(figsize=(10,5)) #tamanyo figura

plt.plot(tiempo,datos,c="k",linewidth=0.5) # x tiempo y datos, grosor linea
plt.ylabel("Amplitud (mV)") #etiquetas
plt.xlabel("Tiempo (s)")
        
plt.ylim(min(datos),max(datos)) #ploteamos los datos
plt.xlim(min(tiempo),max(tiempo))
plt.show()




# Ejemplo de internet similar pro k itera en bucle
"""
plt.figure(figsize=(10,5))
for tr in stream:
    tr.normalize()
    dist = tr.stats.sac.dist
    plt.plot(tr.times(),tr.data+dist*0.01,c="k",linewidth=0.5)
    plt.scatter(tr.stats.sac.t3,dist*0.01,marker="|",color="r")
plt.ylabel("x100 km")    
plt.ylim(84,77)
plt.xlim(650,800)
plt.show()
"""
