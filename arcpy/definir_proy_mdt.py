#!/usr/bin/python
# -*- coding: utf-8 -*-

import arcpy 
import os 
import glob # permite filtrar por extension de archivo
import time 

# definir la proyeccion de los diferentes mdt de la peninsula 
t1 = time.time()

path = "C:/Users/34639/Desktop/curspython/Material_geoespacial/mdt_200m/"
os.chdir(path)
#archivo de seguimiento w writte
arch_log = open("seguimiento_asginacion_poryeccion.log","w")

for i in glob.glob("*.asc"): #filtrar por extension
    print(i)
    
    if i.__contains__("HU28"): # seleccionar fuso del titulo
        sp= 25828              #  EPSG 
    elif i.__contains__("HU29"):
        sp = 25829
    
    elif i.__contains__("HU30"):
        sp = 25830
    
    elif i.__contains__("HU31"):
        sp = 25831
        
    else: 
        print ("Error")
        break #romper bucle
    
    proyeccion = arcpy.SpatialReference(sp)
    # https://desktop.arcgis.com/es/arcmap/10.3/tools/data-management-toolbox/define-projection.htm
    f = path+ i
    arcpy.DefineProjection_management(in_dataset=f, coor_system=proyeccion)
    
    mnsj= "Se ha asignado la proyeccion de  {0} al archivo: {1}".format(str(sp),i)
    
    arch_log.write(mnsj + "\n") #\n salto de linea t tabular 

t2= time.time()

tiempo_ejecucion= t2-t1

arch_log.write("\n \n \t \t Finalziado en %s segundos"%(tiempo_ejecucion))
