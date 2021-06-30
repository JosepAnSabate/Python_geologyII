from PyQt5.QtCore import * #importar todos los modulos QTCore
from qgis.core import *      # a diferencia de arcpy qgis te moltissimes llibreries
from qgis.gui import *
import os
import sys

ruta_in = "C:/Users/34639/Desktop/curspython/arcgis/Material_arcpy/mdt_200m/"
os.chdir(ruta_in)
ruta_out = "C:/Users/34639/Desktop/curspython/qgis/0_pryecc_definida"

if not os.path.exists(ruta_out):
    os.mkdir(ruta_out)


#iterar sobre las layers seleccionadas  respuesta 2 https://gis.stackexchange.com/questions/36937/how-to-iterate-over-selected-layers
layers = iface.layerTreeView().selectedLayers() 
# seleccionar las capas a proyectar en qgis

print(layers)

# Por cada layer dentro de la interfaz
for layer in layers:
    
    nombre_layer= str(layer.name())
    print(nombre_layer)
    
    if nombre_layer.__contains__("PNOA"):
    
        if nombre_layer.__contains__("HU28"):
            src_id= 25828
        elif nombre_layer.__contains__("HU29"):
            src_id= 25829
        
        elif nombre_layer.__contains__("HU30"):
            src_id= 25830
            
        elif nombre_layer.__contains__("HU31"):
            src_id= 25831
        else:
            src_id=0
        
        print ("La %s pertenece al src: %s"%(nombre_layer, src_id))
        
        if src_id !=0:
            crs =layer.crs()
            crs.createFromId(src_id) #crear crs a partir de un id
            print(crs)

            file_name = ruta_out +"/"+ nombre_layer + '.tif' #capa resultado
            
            file_writer = QgsRasterFileWriter(file_name) #crear arch vacio y
            pipe = QgsRasterPipe() #anyade al arch vacio los datos de la layer(arc temp)
            provider = layer.dataProvider()  #anyade al arch vacio los datos de la layer(arc temp)


            if not pipe.set(provider.clone()):
                print ("Cannot set pipe provider")

            
            
            #Escribimos las propiedades del raster
            file_writer.writeRaster(
            pipe,
            provider.xSize(),
            provider.ySize(),
            provider.extent(),
            crs)
        else: 
            print ("El nombre de la layer no contiene en su nombre el huso al que pertenece")
            print (nombre_layer)
    else:
        print("La capa %s no es un mdt"%(nombre_layer))


