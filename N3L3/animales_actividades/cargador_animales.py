# -*- coding: utf-8 -*-
def cargar_animales(archivo:str)->list:
    animales = []
    
    archivo = open("zoo.csv", "r")
    
    encabezados = archivo.readline()
    linea = archivo.readline()
    
    while len(linea) > 0:
        animales.append(crear_animal(encabezados, linea))
        linea = archivo.readline();
        
    return animales

def crear_animal(encabezados: str, linea:str)->dict:
    animal = {}
    
    encs = encabezados.split(";")
    dat = linea.split(";")
    
    i = 0
    
    while i < len(encs):
        dato = dat[i].replace("\n", "")
        
        try:
            dato = int(dat[i])
            if dato <= 1:
                dato = bool(dato)
        except:
            dato = dat[i].replace("\n", "")

        animal[encs[i].replace("\n","")] = dato
        i+=1
    
    return animal
    