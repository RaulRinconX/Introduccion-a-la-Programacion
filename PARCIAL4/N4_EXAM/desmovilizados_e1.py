import pandas as pd
from matplotlib import pyplot as plt

def cargar_datos()->pd.DataFrame:
    """
    Crear y devuele un nuevo dataframe a partir
    del archivo estadisticas.csv

    Returns
    -------
    TYPE
        DataFrame de desmovilizados

    """
    return pd.read_csv("estadisticas.csv")


def crear_matriz(datos:pd.DataFrame)-> tuple:
    """
    Crea y devuelve una tupla con la siguiente información:
        - diccionario de sexos. Las llaves del diccionario son los diferentes sexos y los valores son la fila que 
                                ocupa el sexo en la matriz
        - diccionario de situaciones frente el proceso. Las llaves del diccionario son los diferentes situaciones 
                                                        finales frente al proceso y los valores son la
                                                        columna que ocupa la situación en la matriz
        - matriz de desmovilizados por sexo (filas) y situación final en el proceso (columnas)

    Parameters
    ----------
    datos : pd.DataFrame
        DataFrame de desmovilizados

    Returns
    -------
    tuple
        tupla con 3 posiciones:
            0: diccionario de sexos
            1: diccionario de situaciones
            2: matriz sexo x situación

    """
       
    sexos = sorted(datos["Sexo"].unique()) 
    sexos_dict = {}
    
    estados = sorted(datos["SituacionFinalFrenteAlProceso"].unique())
    estados_dict = {}
    
    matriz = []
    i = 0
    for s in sexos:
        sexos_dict[s] = i
        
        fila = []
        j = 0
        for e in estados:
            if i == 0:
                estados_dict[e] = j
                j += 1
    
            filtrado = datos[ (datos["Sexo"] == s) & (datos["SituacionFinalFrenteAlProceso"] == e) ]
            fila.append(len(filtrado))

        i += 1
        matriz.append(fila)
             
    return (sexos_dict, estados_dict, matriz)


def graficar_situacion_proceso(datos: pd.DataFrame)->None:
    """
    Crea y muestra un gráfico de barras que presenta la cantidad
    de desmovilziados registrados en el DataFrame de acuerdo a 
    su situación final en el proceso

    Parameters
    ----------
    datos : pd.DataFrame
        DataFrame datos desmovilizados
        
        SituacionFinalFrenteAlProceso
        

    """
    datos = datos[["SituacionFinalFrenteAlProceso"]]
    datos = datos.value_counts().sort_index(inplace=False)
    
    plt.figure()
    datos.plot.bar(xlabel="Situacion final en el proceso", ylabel="# Desmovilizados")
    plt.show()


def dar_desmovilizados_grupo_anio(datos: pd.DataFrame, grupo:str)->list:
    """
    Crea y devuelve una lista de tuplas que muestra la cantidad de 
    desmovilizados de un grupo armado para cada año. La lsita tendrá la 
    siguiente estructura:
        [ (año_1, desmovilziados_grupo_año_1), (año_2, desmovilziados_grupo_año_2), ... (año_n, desmovilziados_grupo_año_n)]

    Parameters
    ----------
    datos : pd.DataFrame
        DataFrame datos desmovilizados
    grupo : str
        Nombre del grupo del que se desea conocer la información

    Returns
    -------
    list
        Lsita de tuplas con la información de desmovilizados del grupo por año

    """
    nuevo = datos [ ["AnioDesmovilizacion","ExGrupo"]] 
    grupo = nuevo[nuevo["ExGrupo"] == grupo]
    contar = grupo.value_counts().sort_index(ascending=True).tolist() #LISTA DE VALORES POR AÑO
    anios = grupo["AnioDesmovilizacion"].value_counts().sort_index(ascending=True).index.array
    
    años = []
    for x in anios:
        años.append(x)
        
    contador = []
    for x in contar:
        contador.append(x)
               
    lista = []
    for i in range(len(contar)):
        fila = [años[i], contador[i]]
        lista.append(fila)
        
    return lista

def dar_desmovilizados_por_sexo_situacion(info_matriz:tuple, sexo:str, situacion:str)->int:
    """
    Devuelve la cantidad de desmovilizados de un sexo dado en una situación del proceso dada
    IMPORTANTE: Esta función se debe solucionar usando la matriz que llega por parámetro
    Parameters
    ----------
    info_matriz : tuple
        tupla con 3 posiciones:
            0: diccionario de sexos
            1: diccionario de situaciones
            2: matriz sexo x situación
    sexo : str
        Sexo del que se desea conocer la cantidad de desmovilizados
    situacion : str
        Situación de la que se desea conocer la cantidad de desmovilizados

    Returns
    -------
    int
        Cantidad de desmovilizados del sexo y en la situación dada

    """
    
    if (sexo == "MASCULINO" and situacion == "Ausente del proceso"):
       return (info_matriz[2][0][0])
    if (sexo == "MASCULINO" and situacion == "Culminado"): 
       return (info_matriz[2][0][1])
    if (sexo == "MASCULINO" and situacion == "En Proceso"):
       return (info_matriz[2][0][2])
    if (sexo == "MASCULINO" and situacion == "Fuera del Proceso"): 
       return (info_matriz[2][0][3])
    if (sexo == "MASCULINO" and situacion == "No ha ingresado"): 
       return (info_matriz[2][0][4])
   
    if (sexo == "FEMENINO" and situacion == "Ausente del proceso"):
       return (info_matriz[2][1][0])
    if (sexo == "FEMENINO" and situacion == "Culminado"): 
       return (info_matriz[2][1][1])
    if (sexo == "FEMENINO" and situacion == "En Proceso"):
       return (info_matriz[2][1][2])
    if (sexo == "FEMENINO" and situacion == "Fuera del Proceso"): 
       return (info_matriz[2][1][3])
    if (sexo == "FEMENINO" and situacion == "No ha ingresado"): 
       return (info_matriz[2][1][4])
   
     