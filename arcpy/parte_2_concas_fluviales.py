#!/usr/bin/python
# -*- coding: utf-8 -*-

import arcpy 
import os 
import glob 
from datetime import datetime

start_time = datetime.now()


# rutas
dir_raster= "C:/Users/34639/Desktop/curspython/arcgis/Material_arcpy/mdt_200m/"
dir_cuencas = "C:/Users/34639/Desktop/curspython/arcgis/Material_arcpy/cuencas_hidrograficas/"
dir_cuencas_out = "C:/Users/34639/Desktop/curspython/arcgis/resultats/"
carpeta_datos_salida = "C:/Users/34639/Desktop/curspython/arcgis/resultats/"

# Lineas utiles arcpy
arcpy.env.overwriteOutput= "True" # si la capa existe sin esta linia dara error, pero con overwrite ture se sobreescribe
arcpy.CheckOutExtension("Spatial") #activacion licencia "exterior" pk lexecutem desd fuera

# Funciones de crear carpetas
def crear_carpeta(ruta_out):
    if not os.path.exists(ruta_out): # si la ruta no existe la crea
        os.mkdir(ruta_out)
    else:
        pass
crear_carpeta(carpeta_datos_salida) # invoca la funcion

# Archivo seguimiento
archivo_ejecucion = open("%s_Seguimiento_ejecucion.txt"%(carpeta_datos_salida),"w") 


#1 Seleccionar capas de cuenca y copiarlas en otro directorio
# ir a cada subcarpeta y buscar archivos y buscar por hi_cuenca (contains)

carpetas_cuencas = [x[0] for x in os.walk(dir_cuencas)] #loop vamos a quedarnos con la rutas de oswalk
print(carpetas_cuencas)

diccioanrio_cuencas = {}
lista_cuencas=[]
for dir in carpetas_cuencas: #iterar por cada ruta de directorio
    os.chdir(dir)
    for arch in glob.glob("*.shp"): #terminacion shp
        if arch.__contains__("hi_cuenca"):
            r_arch_cuenca = dir + "/" + arch #directorio completo
            nombre_cuenca = dir.split("/")[-1] #split parte texto, en este caso segun /
            id_cuenca = arch.split("_")[-1][0:5] # -1 para acceder al ultimo elemento de una lisata
            lista_cuencas.append(r_arch_cuenca)
            diccioanrio_cuencas[id_cuenca]=nombre_cuenca
            
print(diccioanrio_cuencas)
print(len(diccioanrio_cuencas))      
print(lista_cuencas)

# 2 Mergear capas de cuencas :
#copiar snippet en arcgis
archivo_cuencas_salida = output=carpeta_datos_salida+"Union_Cuencas.shp"

archivo_ejecucion.write("Mergenado:\n %s \n"%(lista_cuencas))

arcpy.Merge_management(inputs=lista_cuencas, output=archivo_cuencas_salida )

# 3 buscar mdts
#hacer lo mismo para los mdt
arch_rasters = [] # crear lista vacia de rasters
os.chdir(dir_raster)# apuntar al directorio que queramos(para el glob)

for raster in glob.glob("*asc"):
    raster = dir_raster +"/"+raster
    arch_rasters.append(raster)

print(arch_rasters)

# Definir proyeccion salida mdt Lambert conica conforme 102014
spatial_reference = 102014 # coordenadas proyectadas esp, Europe Lambert Conformal Conic mas preciso para calgular pendiente
proyeccion = arcpy.SpatialReference(spatial_reference)

archivo_ejecucion.write("Mosaicando MDTs:\n %s \n"%(arch_rasters))

# 4 Mosaicamos mdts No olbidar el FLOAT EN BIT
arcpy.MosaicToNewRaster_management(input_rasters=arch_rasters, output_location=carpeta_datos_salida, raster_dataset_name_with_extension="union_raster_nacional.tif", coordinate_system_for_the_raster= proyeccion , pixel_type="32_BIT_FLOAT", cellsize="200", number_of_bands="1", mosaic_method="LAST", mosaic_colormap_mode="FIRST")

# Creamos layer mdt 
#env.workspace parecido a os.chdir pero no necesita la ruta completa
arcpy.env.workspace = carpeta_datos_salida
#crea a layer
arcpy.MakeRasterLayer_management("union_raster_nacional.tif","union_raster_nacional_lyr")

# 5 Calcular pendientes en porcentaje

archivo_ejecucion.write("Creando raster pendientes  \n")

arcpy.gp.Slope_sa("union_raster_nacional_lyr", carpeta_datos_salida+"pendientes_nacional.tif", "PERCENT_RISE", "1")
# creamos layer pendientes
arcpy.MakeRasterLayer_management("pendientes_nacional.tif","pendientes_nacional_lyr")


# 6 Calcular pendientes mayores a 3 %
archivo_ejecucion.write("Reclasificando raster pendientes  \n") 

arcpy.gp.RasterCalculator_sa('Con( "pendientes_nacional_lyr" < 3, 0,  "pendientes_nacional_lyr") & Con( "pendientes_nacional_lyr" >= 3, 1,  "pendientes_nacional_lyr")', carpeta_datos_salida+"pendientes_nacional_reclas.tif")
# creamos layer pendientes reclasificadas 
arcpy.MakeRasterLayer_management("pendientes_nacional_reclas.tif","pendientes_nacional_reclas_lyr")

archivo_ejecucion.write("Calculando estadisticas de MEDIA MDT Y MEDIA PEN  \n") 

# 7 Calculamos estadisticas zonales 
# de altitud media por cuenca
#anyadir dos nuevos campos a la capa union cuencas
arcpy.gp.ZonalStatisticsAsTable_sa(archivo_cuencas_salida, "id_cuenca", "union_raster_nacional_lyr", r"in_memory/statistics_mdt", "DATA", "MEAN") #guardarla tamporalmente inmemory
arcpy.AlterField_management(r"in_memory/statistics_mdt", "MEAN", 'MEAN_MDT')

# de pendiente media por cuenca
arcpy.gp.ZonalStatisticsAsTable_sa(archivo_cuencas_salida, "id_cuenca", "pendientes_nacional_lyr", r"in_memory/statistics_pen", "DATA", "MEAN")
arcpy.AlterField_management(r"in_memory/statistics_pen", "MEAN", 'MEAN_PEN')

# Unimos las estadisticas a la capa
archivo_ejecucion.write("JOIN DE ESTADISTICOS  \n") 
arcpy.JoinField_management (archivo_cuencas_salida, "id_cuenca", r"in_memory/statistics_mdt", "id_cuenca")
arcpy.JoinField_management (archivo_cuencas_salida, "id_cuenca", r"in_memory/statistics_pen", "id_cuenca")


archivo_ejecucion.write("GENERACION DE CAPAS POR CUENCA  \n")
 

# 8 Recortar todo por cuenca y guardar con el id de la cuenca dentro de la carpeta con el nombre de la CH 
#acceso a datos utilizando cursores https://desktop.arcgis.com/es/arcmap/latest/analyze/python/data-access-using-cursors.htm
with arcpy.da.SearchCursor(archivo_cuencas_salida,["id_demarc","id_cuenca", 'SHAPE@']) as cursor: #campo shape se denine #SHAPE@ 
    for row in cursor:
        
        id_ch = row[0]
        id_c =row[1]
        
        print("ID CONFEDERACION HIDROGRAFICA: %s"%(id_ch))
        if id_ch in diccioanrio_cuencas: # si campo id_demarcacion canvia directorio i accede valor del diccionario
            os.chdir(carpeta_datos_salida) 
            # Acceso al diccionario para obter el nombre de la Confederacion Hidrografica
            nombre_cuenca = diccioanrio_cuencas[id_ch]
            carpeta_salida= carpeta_datos_salida + nombre_cuenca+"_"+id_ch
            crear_carpeta(carpeta_salida)
            
        print("ID Cuenca: ---%s"%(id_c))
        carpeta_salida_cuenca = carpeta_salida+ "/"+id_c
        crear_carpeta(carpeta_salida_cuenca)

        #seleccionamos feature

        archivo_ejecucion.write("----%s  \n"%(id_c)) 
        
        # mdt recortado
        arcpy.gp.ExtractByMask_sa("union_raster_nacional_lyr",row[2],carpeta_salida_cuenca+ "/"+ id_c +"_mdt200.tif" )
        # pendientes recortadas
        arcpy.gp.ExtractByMask_sa("pendientes_nacional_lyr",row[2],carpeta_salida_cuenca+ "/"+ id_c +"_pen200.tif" )
        #pendientes reclasificadas recortadas
        arcpy.gp.ExtractByMask_sa("pendientes_nacional_reclas_lyr",row[2],carpeta_salida_cuenca+ "/"+ id_c +"_pen200_rec.tif" )
        # Superficie cuenca
        where_clause = '"id_cuenca"= \'%s\''%(id_c)
        arcpy.Select_analysis(archivo_cuencas_salida, carpeta_salida_cuenca+"/"+ "Cuenca_%s.shp"%(id_c),where_clause )

    

