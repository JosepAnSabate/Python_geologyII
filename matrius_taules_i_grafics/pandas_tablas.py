#!/usr/bin/python 

#Pandas is used to analyze data.

import pandas as pd


alumnos = pd.DataFrame(columns =["Nombre","Edad"]) #crear columnas
print(alumnos)

#crear filas
alumnos.loc[1]=["Sylwester",26]
alumnos.loc[2]=["Laura",28]

print(alumnos)


diccionario_clases_rocas = {"igneas":["pumita","obsidiana","basalto","granito","gabro"],
                            "metamorficas":["pizarra","esquisto","gneis","marmol","cuarcita"],
                            "sedimentarias":["arcilla","arenisca","pudingas","brechas","caliza","sal","carbon"]}


tabla_rocas = pd.DataFrame(columns = ["Tipo roca","roca"])

n = 1 #fila 1
for key, value in diccionario_clases_rocas.items(): #iteramos x el diccionario
    #print(key)
    #print(value)
    for roca in value:
        tabla_rocas.loc[n] = [key,roca] #n num de fila corresponent
        n+=1 #x cada fila
        
print(tabla_rocas)

tabla_rocas.to_csv("tabla_rocas.csv",";") #guardar como csv igua dir k el script
