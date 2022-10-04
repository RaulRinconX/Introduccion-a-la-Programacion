# -*- coding: utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt

def cargar()->pd.DataFrame:
    
    df = pd.read_csv('inscritos_p.csv')
    return df

def dar_inscripciones_periodo(datos: pd.DataFrame, periodo:int)->pd.DataFrame:
    """
    Crea y devuelve un nuevo DataFrame que solo contenga 
    las isncripciones de un periodo dado

    Parameters
    ----------
    datos : pd.DataFrame
        datos originales
    periodo : int
        Periodo de interés

    Returns
    -------
    nuevo : TYPE
        DAtos resultantes

    """
    #TODO completar siguiendo la guía del profesor
    nuevo = datos[ datos["PERIODO"] == periodo]
    
    
    return nuevo 
	
	
#print(dar_inscripciones_periodo(cargar(), 201610))

def dar_inscripciones_periodo_programa(datos: pd.DataFrame, periodo:int, programa:str)->int:
    """
    Devuelve la cantidad de isncritos para el programa y periodo dados

    Parameters
    ----------
    datos : pd.DataFrame
        Datos de inscritos
    periodo : int
        Periodo de interés
    programa : str
        Programa de interés

    Returns
    -------
    int
        inscritos al programa en el periodo

    """
    #TODO completar siguiendo la guía del profesor
    
    nuevo = datos[ (datos["PERIODO"] == periodo) & 
                  (datos["PROGRAMA"] == programa)]
    
    
    return nuevo.values.tolist() #[0][2] se pueden sacar los valores para manipulalrlos
                                 #ESTO VUELVE EL DATAFRAME EN UNA LISTA 

    
    
print(dar_inscripciones_periodo_programa(cargar(), 201710, 'ISIS'))

def graficar_inscritos_por_periodo(datos: pd.DataFrame)->None:
    """
    Grafica la cantidad de inscritos para cada periodo en un gráfico de barras

    Parameters
    ----------
    datos : pd.DataFrame
        Datos de inscripciones

    """
    #TODO completar siguiendo la guía del profesor
    
    nuevo = datos.groupby("PERIODO").sum()
    
    plt.figure()
    nuevo.plot.bar()
    nuevo.plot(kind="bar")
    
    plt.show
    
graficar_inscritos_por_periodo(cargar())
    
def graficar_inscritos_programa(datos: pd.DataFrame, prog:str)->None:
    """
    Grafica una torta con el porcentaje de inscritos obtenido en cada
    periodo para le programa indicado

    Parameters
    ----------
    datos : pd.DataFrame
        Datos de inscripciones
    prog : str
       Programa de interés


    """
    #TODO completar siguiendo la guía del profesor
	
    nuevo = datos[ datos["PROGRAMA"] == prog]

    nuevo = nuevo.groupby("PERIODO")["INSCRITOS"].sum()
    
    plt.figure()
    nuevo.plot.pie()
    plt.show()
    
graficar_inscritos_programa(cargar(), 'ISIS')
    

def dar_isncritos_anio(datos: pd.DataFrame, anio: int)->list:
    """
    Crea una lista de tuplas que contiene la 
    cantidad de isncritos para el año dado. Por ejemplo:
        [(201910, 8127), (201920, 6131)]
        
    cada año tiene dos periodos 10 y 20

    Parameters
    ----------
    datos : pd.DataFrame
        Datos de inscripciones
    anio : int
        Año de interpes

    Returns
    -------
    list
        Lista de tuplas

    """
    
    #TODO completar siguiendo la guía del profesor
        
    
#print(dar_isncritos_anio(cargar(), 2019))
