#!/usr/bin/python 
# -*- coding: latin-1 -*-
import pandas as pd #leer csv
import numpy as np 
import os 
# Importante para CSV!!!
#les col es poden separar per , o ; exemple: data = pd.read_csv(tabla,sep=";")

# Este script convierte la aceleracion ( (gmv_PGA y gmv_PGV) en intensidad . 
# Mediante el uso de las: Ecuaciones  de Caprio et al. 2015
#-----Si log(gmv_PGA)<=1.6, I=2.27+1.647*log(gmv_PGA)
#-----Si log(gmv_PGA)>1.6, I=-1.361+3.822*log(gmv_PGA)

#-----Si log(gmv_PGV)<=0.3, I=4.424+1.589*log(gmv_PGV)
#-----Si log(gmv_PGV)>0.3, I=4.018+2.671*log(gmv_PGV)

#Ruta directorio
dir = "C:/Users/34639/Desktop/curspython/sismologia/Material_Curso_Calculo_Intensidad/"
os.chdir(dir)
# archivo
tabla = "simulacion_prueba.csv"


data = pd.read_csv(tabla,sep=";")

print ("Cabecera datos")
print(data.head())

# Generamos nuevas columnas de logaritmo de aceleración del suelo , tanto de PGA como PGV
data["log_PGA"] = np.log10(data["gmv_PGA"])
data["log_PGV"] = np.log10(data["gmv_PGV"]) #creamos dos nuevos campos con los calc de los log

print ("\n Cabecera datos despues de calcular los logaritmos")
print(data.head())


# Aplicamos las Ecuaciones de Caprio
# para PGA

#.loc inserta nueva fila
#si el valor del camp es <= 1.6, crea un nuevo campo: I_PGA
#y la eq que le da valor es  2.27 + 1.647 * data["log_PGA"]
data.loc[data["log_PGA"] <= 1.6,  "I_PGA"] = 2.27 + 1.647 * data["log_PGA"]
data.loc[data["log_PGA"] > 1.6,  "I_PGA"] = -1.361 + 3.822 * data["log_PGA"]

# para PGV
data.loc[data["log_PGV"] <= 0.3,  "I_PGV"] = 4.424 + 1.589 * data["log_PGV"]

data.loc[data["log_PGV"] > 0.3, "I_PGV"] = 4.018 + 2.671 * data["log_PGV"]

print ("\n Resultado, cabecera")
print(data.head())


# Guardamos el archivo 
data.to_csv("simulacion_prueba_out.csv",index=False,sep=";")


