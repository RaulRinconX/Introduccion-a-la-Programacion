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
    
    programas = [ ]
    
    archivo = open("Netflix Shows.csv", "r",  encoding="ISO-8859-1")
    archivo.readline()
    
    linea = archivo.readline()
    
    while linea != "":
        datos = linea.split(";")
        programa = { "title": datos[0],
                      "rating": datos[1],
                      "release year": int(datos[4])
                    }     
        
        programas.append(programa)

        linea = archivo.readline()
   
     
    archivo.close()
    
    return programas


#print(cargar())
[]




    
    
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
            
            if (shows[i]["title"] in titulos) == False:
                titulos.append( shows[i]["title"] )
            
        i += 1
      
    return titulos


#print(dar_titulos_anio(cargar(), 2004 ))
















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
    

#print(dar_titulos_clasificacion(cargar(), "PG-13" ))
    

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
    
    titulos = []
    
    i = 0
    
    while i < len(shows):
        
        if int(shows[i]["release year"]) == int(anio) and \
        shows[i]["rating"] == clasificacion:
            titulos.append( shows[i]["title"] )
            
        i += 1
      
    return titulos

#print(dar_titulo_anio_clasificacion(cargar(), 2004, "PG-13" ))


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
    for elem in shows:
        if elem["release year"] > mayor["release year"]:
            mayor = elem
    return mayor

    
#print(dar_show_mayor_anio(cargar() ))   
    
    

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
    
    
def buscar(shows:list, parte_titulo:str)->dict:
    """
    Busca el primer programa que en su nombre
    tiene la parte que llega por parámetro
    y si ninguno lo tiene devuelve None

    Parameters
    ----------
    shows : list
        Lista de diccionarios de programas cargados desde el archivo
    parte_titulo : str
        Texto que se desea buscar entre los títulos de las películas

    Returns
    -------
    dict
        Programa que en su título tenga el texto ingresado por parámetro

    """
    dic = {}
    
    i = 0
    
    while i < len(shows):
        
        if parte_titulo.upper() in shows[i]["title"].upper():
            dic = shows[i]
       
        i += 1
      
    return dic
    
    
       
print(buscar(cargar(), 'Mu'))

def promedio_anio(shows:list)->float:
    """
    Calcula el año promedio de estreno de un programa

    Parameters
    ----------
    shows : list
        Lista de diccionarios de programas cargados desde el archivo

    Returns
    -------
    float
        Promedio de año de estreno

    """
    promedio = 0
    for s in shows: 
        promedio += s["realease year"]
        promedio = promedio/len(shows)

    return promedio
   


#print(promedio_anio(cargar()))









    
def clasificacion_mas_comun(shows:list)->str:
    """
    Busca la clasifación más común entre los
    programas

    Parameters
    ----------
    shows : list
        Lista de diccionarios de programas cargados desde el archivo

    Returns
    -------
    str
        Clasificación más común

    """
    clasificaciones = {}
    for show in shows:
        if show["rating"] not in clasificaciones:
           clasificaciones[show["rating"]] = 0
        else:
           clasificaciones[show["rating"]] += 1
    mayor = 0
    nombre = ""
    for llave in clasificaciones:
        if clasificaciones[llave] > mayor:
            mayor = clasificaciones[llave]
            nombre = llave
    return nombre


    

