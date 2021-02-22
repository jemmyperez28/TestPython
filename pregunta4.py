""" Hacer un programa que tenga la funcion de listar las carpetas y archivos y ordenar por tamaño o fecha, y que muestre"""
import os 
import glob 
ruta = 'C:\\Users\\User\\Desktop\\test'
respuestas = ""
lista=[]
archivos = os.listdir(ruta)
archivos.sort(key=os.path.getmtime) #Ordenar por fecha de creacion.

ordenados = ("\n".join(archivos))
print("Archivos ordenados por fecha de creacion: \n" + ordenados)
"""
for i in ordenados :
    if i == "\n":
        lista.append(respuestas)
        respuestas=""
    else :
        respuestas = respuestas + i
lista.append(respuestas)
"""
for i in archivos:
    with open(i,'r') as file: 
        data1 = file.read().replace('\n','')
        for x in archivos:
            with open(x,'r') as file :
                data2 = file.read().replace('\n','')
                if x == i :
                    pass
                else: 
                    if data1==data2:
                        print("Se encontro archivo con contenido duplicado " + x )

