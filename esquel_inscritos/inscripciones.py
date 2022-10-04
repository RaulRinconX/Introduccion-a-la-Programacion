# -*- coding: utf-8 -*-

def cargar()->list:
    """Crea una matriz que contiene la cantidad de inscritos Masculino y Femenino
    a cada programa en cada semestre.
        |           |201510    |201520    |....
        |ADMI       |(M,F)     |(8,7)    |....
        |CONT       |(4,4)     |(1,2)    |....
        ....
    """
    matriz = []
    
    arch = open('inscritos.csv', 'r')
    
    linea = arch.readline()
    
    while linea != "":
        datos = linea.split(";")
        
        if matriz == []:
            matriz.append( [ "", datos[0]] )
            matriz.append( [ datos[1], (int(datos[2]), int(datos[3]))   ])
        else:
            
            if datos[0] not in matriz[0]:
                matriz[0].append(datos[0])
                for f in matriz[1:]:
                    f.append( (0, 0) )
            col = matriz[0].index(datos[0])
            
            fila = -1
            f = 1
            while f < len(matriz) and fila == -1:
                if matriz[f][0].strip() == datos[1].strip():
                    fila = f
                    
                f += 1
            
            if fila == -1:
                n_fila = [datos[1]]
                
                for c in matriz[0][1:]:
                    n_fila.append( (0,0) )
                matriz.append(n_fila)
                fila = len(matriz) -1
                
            
            matriz[fila][col] = (int(datos[2]), int(datos[3]))
            
          
            
                
        linea = arch.readline()
    
    arch.close()
    
    return matriz


def matriz_inscritos(matriz:list)->list:
    """Devuelve una matriz que indica cuantos inscritos hubo para cada programa 
    en cada semestre.
        |           |201510|201520|....
        |ADMI       |10    |15    |....
        |CONT       |8     |3     |....
        ...
    """
    matriz_i = []
    
    #TODO completar
    matriz.append(matriz[0])
    
    for f in matriz[1:]:
        nueva_fila = [ f[0]]
        
        for t in range(1, len(f)):
            nueva_fila.append(f[t][0] + f[t][1])
        matriz_i.append(nueva_fila)
        
    
        

        
    return matriz_i

print(matriz_inscritos(cargar()))


def femenino_x_programa(matriz:list, programa:str)->int:
    """
    Indica la cantidad total de inscritos femeninos al programa

    Parameters
    ----------
    matriz : list
        Matriz de isncritos discriminada por inscritos masculinos y femeninos
    programa : str
        El programa para el que se desea conocer los inscritos

    Returns
    -------
    int
        Inscritos femeninos al programa

    """
    insc = 0
    
    #TODO completar
    for f in matriz[1:]:
        if f[0] == programa:
            for t in f[1:]:
                insc += t[1]
                
    return insc

#print(femenino_x_programa(cargar(), 'GEOC'))


def masculino_x_periodo(matriz:list, periodo:str)->int:
    """
    Indica la cantidad total de inscritos masculinos al periodo

    Parameters
    ----------
    matriz : list
        Matriz de isncritos discriminada por inscritos masculinos y femeninos
    programa : str
        El periodo para el que se desea conocer los inscritos

    Returns
    -------
    int
        Inscritos masculinos al periodo

    """
    #TODO completar
    insc = 0
    
    col = matriz[0].index(periodo)
    
    for f in matriz[1:]:
        insc += f[col][0]
        
    return insc

#print(masculino_x_periodo(cargar(), '201910'))
    
def lista_prog_mas_porc_femenino_x_periodo(matriz:list)->list:
    """
    Crea y devuelve una lista de tuplas con el programa con 
    mayor porcentaje de inscritos femeninos para cada semestre.
    Las tuplas tendran la siguiente estructura:
        (periodo, programa, porcentaje_inscritos_femeninos)
        
    OJO con la division por cero.
        
    Parameters
    ----------
    matriz : list
        Matriz de isncritos discriminada por inscritos masculinos y femeninos

    Returns
    -------
    list
        Lista de tuplas con el programa con mayor porcentaje de inscritos femeninos
        por semestre.

    """
    tuplas = []
    
    #TODO completar
    
    
    return tuplas

#print(lista_prog_mas_porc_femenino_x_periodo(cargar()))



from matplotlib import pyplot as plt

def graficar_inscritos_periodo(matriz:list)->None:
    
    


