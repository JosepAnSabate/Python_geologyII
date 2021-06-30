#!/usr/bin/python 

import pandas as pd


alumnos = pd.DataFrame(columns =["Nombre","Edad"])
print(alumnos)


alumnos.loc[1]=["Sylwester",26]
alumnos.loc[2]=["Laura",28]




diccionario_clases_rocas = {"igneas":["pumita","obsidiana","basalto","granito","gabro"],
                            "metamorficas":["pizarra","esquisto","gneis","marmol","cuarcita"],
                            "sedimentarias":["arcilla","arenisca","pudingas","brechas","caliza","sal","carbon"]}


tabla_rocas = pd.DataFrame(columns = ["Tipo roca","roca"])

n = 1
for key, value in diccionario_clases_rocas.items():
    
    for roca in value:
        tabla_rocas.loc[n] = [key,roca]
        n+=1
        
print(tabla_rocas)

tabla_rocas.to_csv("tabla_rocas.csv",";")



        

