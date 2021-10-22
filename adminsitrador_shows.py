# -*- coding: utf-8 -*-

def cargar()->list:
    """
    Carga los shows en una lista a partir del archivo Netflix Shows.csv
    Cada show se carga en un diccionario con la siguiente estructura:
        {title: str con el título del show,
        rating: str con la clasificación del show,
        release year: año de estreno del show
        }
    Returns
    -------
    list
        lista que contiene diccionarios con la información de cada película en el archivo

    """
    #TODO complete siguiendo el paso a paso de la guía
    
    archivo = open("Netflix Shows.csv", "r")
    
    programas = []
    
    archivo.readline()

    linea = archivo.readline()
    
    while linea != "":
        datos = linea.split(";")
        programa = { "title" : datos[0],
                     "rating": datos[1],
                     "release year": datos[4],
                     }
        
        programas.append(programa)
        
        linea = archivo.readline()
    
    archivo.close()
    
    return programas

#print(cargar())

def dar_titulos_anio(shows:list, anio:int)->list:
    """
    Crea y devuelve una lista con los títulos de los shows 
    estrenadas el año que llega por parámetro
    
    Parameters
    ----------
    shows : list
        lista que contiene diccionarios de shows
    anio : int
        año del que se desean conocer los shows

    Returns
    -------
    list
        lista con los títulos de los shows estrenados en el año por 
        parámetro. Lista vacía si ningún show fue estrenado en el año

    """
    #TODO complete siguiendo el paso a paso de la guía
    titulos = []
    
    i = 0
    while i < len(shows):
        if shows[i]["release year"] == anio:
            titulos.append(shows[i]["title"])
            
        i += 1
            
    return titulos 


    

def dar_titulos_clasificacion(shows:list, clasificacion:str)->list:
    """
    Crea y devuelve una lista con los títulos de los shows 
    con la clasificación que llega por parámetro
    
    Parameters
    ----------
    peliculas : list
        lista que contiene diccionarios de shows
    clasificacion : str
        clasificación de la que se desean conocer los shows

    Returns
    -------
    list
        lista con los títulos de los shows con la clasificación por 
        parámetro. Lista vacía si ningún show tiene la clasificación

    """
    #TODO complete de acuerdo a la documentación
    
    lista = []
    
    
    for i in shows:
        if i["rating"] == clasificacion:
            lista.append(i["title"])
            
      
            
    return lista




    

def dar_titulo_anio_clasificacion(shows:list, anio:int, clasificacion: str)->list:
    """
    Crea y devuelve una lista con los títulos de los shows 
    con la clasificación que llega por parámetro estrenadas en el año
    que llega por parámetro
    
    Parameters
    ----------
    peliculas : list
        lista que contiene diccionarios de shows
     anio : int
        año del que se desean conocer los shows
    clasificacion : str
        clasificación de la que se desean conocer los shows

    Returns
    -------
    list
        lista con los títulos de los shows con la clasificación por 
        parámetro estrenados en el año por parámetro.
        Lista vacía si ningún show tiene la clasificación

    """
    #TODO complete de acuerdo a la documentación
    
    lista = []
    
    i = 0
    while i < len(shows):
        if shows[i]["rating"] == clasificacion and int(shows[i]["release year"]) == int(anio):
           lista.append(shows[i]["title"])
    
            
        i += 1
            
    return lista




def dar_show_mayor_anio(shows:list)->dict:
    """
    Busca y devuelve el show de mayor año

    Parameters
    ----------
    peliculas : list
        lista que contiene diccionarios de shows

    Returns
    -------
    dict
        Diccionario del show con mayor año de estreno 
        si hay varios con el máximo año devuelve el 
        primero encontrado

    """
    #TODO complete de acuerdo a la documentación
    mayor = shows[0]
    for s in shows:
        if s["release year"] > mayor["release year"]:
            mayor = s
    return mayor


def dar_show_nombre_corto(shows:list)->dict:
    """
    Busca y devuelve el show con el título mas corto

    Parameters
    ----------
    peliculas : list
        lista que contiene diccionarios de shows

    Returns
    -------
    dict
        Diccionario del show con nombre mas corto
        si hay varios con la misma longitud devuelve el 
        primero encontrado

    """
    #TODO complete de acuerdo a la documentación
    menor = shows[0]
    for s in shows:
        if s["title"] < menor["title"]:
            menor = s
    return menor

print(dar_show_nombre_corto(cargar()))


def dar_shows_nombre_largo(shows:list)->dict:
    """
    Crea y devuelve un diccionario que contiene el nombre del show 
    mas largo de cada año. El diccionario tendra la siguiente
    estrucutra:
        { añio: nombre_show_mas_largo_año, 
          añio: nombre_show_mas_largo_año ...}

    Parameters
    ----------
    shows : list
        lista que contiene diccionarios de shows

    Returns
    -------
    dict
        Diccionario con el nombre del show mas largo de cada año

    """
    #TODO complete de acuerdo a la documentación





    

