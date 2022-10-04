import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.image as mpimg
from matplotlib import pyplot as plt



def cargar_datos(ruta_archivo:str)->pd.DataFrame:
     
    return pd.read_csv(ruta_archivo)

def cargar_coordenadas(nombre_archivo:str)->dict:   
    deptos = {}
    archivo = open(nombre_archivo, encoding="utf8")
    archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        deptos[datos[0]] = (int(datos[1]),int(datos[2]))
        linea = archivo.readline()
    return deptos

def crear_matriz(datos:pd.DataFrame)-> tuple:
    #Creación de los diccionarios con los grupos y departamentos para la matriz
    datos = datos[datos["ExGrupo"]!="SIN DATO"]
    datos = datos[datos["ExGrupo"]!="SIN DATO MINDEFENSA"]
    grupos =sorted(datos["ExGrupo"].unique())
    grupos_dict = dict(list(enumerate(grupos)))
    deptos = sorted(datos["DepartamentoDeResidencia"].unique())
    dept_dict = dict(list(enumerate(deptos)))
    #TODO - Crear la matriz
    matriz = pd.DataFrame(None, index=[deptos], columns=(grupos))
    matriz = []
    for i in range(len(dept_dict)):
        fila = [0]*len(grupos_dict)
        matriz.append(fila)
    
    """

    MATRIZ
                                                 "AUC" "ELN" "FARC" ...
    1.      filas -> departamentos  "AMAZONAS"     10    2     0
             columnas -> grupos     "ANTIOQUIA"     23   12     11
                                    "ARAUCA"        23    12    1 
        

    """
    for i in datos.index:
        grupos = datos["ExGrupo"][i]
        departamento = datos["DepartamentoDeResidencia"][i]
        fila = 0
        columna = 0
        for c in grupos_dict:
            if grupos == grupos_dict[c]:
                columna = c
        for f in dept_dict:
            if departamento == dept_dict[f]:
                fila = f
        matriz[fila][columna] += 1
        
    tupla = (matriz, dept_dict, grupos_dict)
    
    return tupla
 
def grupo_mas_desmovilizados_por_departamento(informacion: tuple, departamento: str)->str:
    """
    Parameters
    ----------
    informacion  : tuple
        Tupla con la informacion de la matriz.
    departamento : str
        Departamento ingresado por el usuario para consultar la tupla.

    Returns
    -------
    str
        Un string con el grupo que tiene mas desmovilizados en ese departamento.

    """
    
    datos = informacion[0]
    filas = informacion[1] 
    columnas = informacion[2] 
    desmovilizados = 0
    contar = 0
    columna_sum = 0
    resultado = None
    
    for i in filas:
        if departamento == filas[i]:
            dato_departamento = i #FILA DONDE ESTA EL DEPARTAMENTO SEGUN LA MATRIZ CREADA
    
    for x in datos[dato_departamento]:
        if x > desmovilizados:
            desmovilizados = x
            columna_sum = contar
        contar += 1
    
    for u in columnas:
        if columna_sum == u:
            resultado = columnas[u]
            
    return resultado


def contar_personas_por_grupo(informacion: tuple, grupo: str)->int:
    """
    

    Parameters
    ----------
    informacion : tuple
        Tupla con la informacion de la matriz
    grupo : str
        Grupo ingresado por el usuario para conocer el número total de desmovilizados.

    Returns
    -------
    int
        Entero que represente el número de desmovilizados que pertenecian al grupo armado.

    """
    datos = informacion[0]
    grupos = informacion[2]
    grupo_escogido = None
    lista_valores = []
    resultado  = 0
    
    for i in grupos:
        if grupo == grupos[i]:
            grupo_escogido = i
            
    for x in datos:
            resultado = x[grupo_escogido]
            lista_valores.append(resultado)
            
    resultado = sum(lista_valores)
        
    return resultado
    

def  departamento_grupo_mayor_desmovilizados(informacion: tuple)->tuple:
    """
    Parameters
    ----------
    informacion : tuple
        Tupla con la informacion de la matriz.

    Returns
    -------
    tuple
        Tupla de la forma (d,g), donde d es el nombre del departamento y g es el nombre del ex grupo armado.


    (Antioquia, AUC)
    
    """  
    datos = informacion[0]
    filas = informacion[1] 
    columnas = informacion[2] 
    valores = []
    d = None
    g = None
    
    for x in datos:
        valores.append(sum(x))
    
    max_value = None
    max_idx = None

    for idx, num in enumerate(valores):
        if (max_value is None or num > max_value):
            max_value = num
            max_idx = idx

    for x in filas:
        if max_idx == x:
            d = filas[max_idx]
            
    max_value = None
    index = None

    for idx, num in enumerate(datos[max_idx]):
        if (max_value is None or num > max_value):
            max_value = num
            index = idx      
            
    for x in columnas:
        if x == index:
            g = columnas[index]
    
    tupla = (d, g)
   
    return tupla
    
#departamento_grupo_mayor_desmovilizados(crear_matriz(cargar_datos("estadisticas.csv")))
    
def desmovilizados_grupo_armado(datos:pd.DataFrame):
    
    nuevo = datos[["ExGrupo"]] #DATAFRAME CON SOLO GRUPOS ARMADOS
    
    nuevo = nuevo["ExGrupo"].value_counts() #SE ORGANIZA Y HACE CONTEO DE LOS GRUPOS
    
    nuevo = nuevo.drop(nuevo.index[[6,7]]) #SE RETIRAN LOS DATOS NO SOLICITADOS EN EL GRAFICO
    
    # GRAFICACION DE LOS DATOS...
    plt.figure(figsize=(6,6))
    nuevo.plot.pie()
    labels = [["AUC", "58.9%"],["FARC", "32,1%"],["ELN", "8.2%"],["ERG", "0.2%"],["ERP","0.3%"],["EPL","0.3%"]]
    
    plt.legend(loc='lower left', fontsize = 'small', labels=labels)
    plt.show()

def numero_desmovilizados_rango_años(datos:pd.DataFrame, anio_menor: int, anio_mayor: int):
    
    nuevo = datos[ ["AnioDesmovilizacion"]]
    nuevo = nuevo["AnioDesmovilizacion"].value_counts().sort_index(ascending=True).tolist()
    df = pd.DataFrame()
    df["Año desmovilización"] = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    df = df.assign(Cantidad = nuevo)
    
    nuevo = df.set_index("Año desmovilización")
    nuevo = nuevo.loc[anio_menor:anio_mayor]
 
    plt.figure()
    nuevo.plot.line(fontsize="small", ylabel="Número de desmovilizados")
    plt.show()
 


def departamentos_mayor_desmovilizados(datos:pd.DataFrame, desmovilizacion: str)->None:
    """
    Parameters
    ----------
    datos : pd.DataFrame
        Se carga el correspondiente DataFrame del Archivo CSV.
    desmovilizacion : str
        Indica en una cadena de caracteres si la desmovilizacion es indidual
        o colectiva.

    Returns
    -------
    None
        Una grafica de lo solicitado.

    """
    nuevo = datos [ ["DepartamentoDeResidencia","TipoDeDesmovilizacion"]]  
    tipo = nuevo[nuevo["TipoDeDesmovilizacion"] == desmovilizacion]
    contador = tipo["DepartamentoDeResidencia"].value_counts().sort_values(ascending=False)
    top = contador.head().sort_values(ascending=True)
     
    plt.figure()
    top.plot.barh(xlabel="Departamento de residencia")
    plt.show()
    

def segun_numero_de_hijos_y_sexo(datos:pd.DataFrame)->None:
    """
    Parameters
    
    NumDeHijos: Número de hijos
    Sexo: MASCULINO/FEMENINO
    ----------
    datos : pd.DataFrame
        Se carga el correspondiente DataFrame del Archivo CSV.

    Returns
    -------
    None
        Una grafica de lo solicitado.
        
        4.
         - dejar solo sexo, hijos.
         - agrupar por el sexo
         - graficar.boxplot()
         "dataframe.boxplot(subplots=False)"

    """
    nuevo = datos.loc[:,["Sexo","NumDeHijos"]]
    nuevo = nuevo[nuevo["NumDeHijos"] != -2] # RETIRO LOS -2 PARA QUE SEA IGUAL AL DOCUMENTO
    
    plt.figure()
    nuevo.boxplot(by="Sexo", showmeans=True)
    plt.xlabel("Sexo")
    plt.ylabel("Número de hijos")
    plt.title("Número de hijos por sexo")
    plt.suptitle("")
    plt.show()


def ocupacion_individuos_beneficio_desembolso(datos:pd.DataFrame)->None:
    """

    Parameters
    ...
    BeneficioTRV
    BeneficioFA
    BeneficioFPT
    BeneficioPDT
    ...
    DesembolsoBIE
    ...
    OcupacionEconomica
    ....
    ----------
    datos : pd.DataFrame
        Se carga el correspondiente DataFrame del Archivo CSV.

    Returns
    -------
    None
        Una grafica de lo solicitado.

    """
    nuevo = datos[["BeneficioTRV","BeneficioFA","BeneficioFPT","BeneficioPDT","DesembolsoBIE","OcupacionEconomica"]]
    
    filtro = nuevo[(nuevo['BeneficioTRV'] == "Sí") | (nuevo['BeneficioFA'] == "Sí")
                   | (nuevo['BeneficioFPT'] == "Sí") | (nuevo['BeneficioPDT'] == "Sí")
                   | (nuevo['DesembolsoBIE'] == "Sí")]
    
    filtro = filtro[["OcupacionEconomica"]]
    
    grafico = filtro.value_counts().sort_index(inplace=False)
    
    plt.figure()
    grafico.plot.bar(xlabel="Ocupacion Economica")
    plt.show()


def grupo_mayor_desmovilizacion_departamento(informacion: tuple)->None:
  
    dict_columns = informacion[2]
    dict_filas = informacion[1]
    matriz = informacion[0]
    resultado = 0
    
    mapa = mpimg.imread("mapa.png").tolist()
       
    colores = {"AUC":[1.0,1.0,0.0], "ELN":[1.0,0.0,0.0], "EPL":[1.0,0.0,1.0],
               "ERG":[0.0,1.0,1.0], "ERP":[0.0,1.0,0.0], "FARC":[1.0, 0.5, 0.50]}
    
    coordenadas = cargar_coordenadas("coordenadas.txt")
    sp = plt.subplot()
    
    for x in range(len(matriz)):
        resultado = grupo_mas_desmovilizados_por_departamento(informacion, dict_filas[x])
        fila, columna = coordenadas[dict_filas[x]]
        rect = mpatches.Rectangle((columna - 6.5,fila - 6.5), 13.0, 13.0, color = colores[resultado])
        sp.add_patch(rect)
        
    legends = []
    for i in range(0, len(matriz[0])):
         legends.append(mpatches.Patch(color = colores[dict_columns[i]], label=dict_columns[i]))
         
    plt.legend(handles = legends)
    plt.imshow(mapa)
    plt.show()
