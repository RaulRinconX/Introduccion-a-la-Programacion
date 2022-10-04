"""
Ejercicio nivel 2: Cálculo de velocidades en vías colombianas
Modulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

"""

def crear_sector( nombre: str, carriles: int, pendiente: float, 
                   ancho_calzada: float, ancho_berma: float, separador: bool,
                   peatones: bool, control_accesos: str, 
                   zona_recreacional: bool,cuello_de_botella: bool, 
                   zona_escolar: bool ) -> dict:
    """
    Crea un diccionario que representa un sector de la vía con todos sus 
    atributos inicializados.
    
    Parámetros
    ----------
    nombre : str
        Nombre del sector vial.
    carriles : int
        Número de carriles dentro del sector.
    pendiente : float
        Porcentaje de inclinación del sector.
    ancho_calzada : float
        Ancho en metros de la calzada del sector.
    ancho_berma : float
        Ancho en metros de la berma del sector.
    separador : bool
        Existencia de un separador en el sector.
    peatones : bool
        Existencia de concentración de peatones en el sector.
    control_accesos : str
        Tipo de control de accesos que hay en una vía.
        Puede ser “Total”, “Parcial” o “Nulo”
    zona_recreacional : bool
        Existencia de una zona recreacional en el sector.
    cuello_de_botella : bool
        Existencia de un cuello de botella en el sector.
    zona_escolar : bool
        Existencia de una zona escolar en el sector.

    Retorno
    -------
    dict
        Diccionario del sector vial con sus características.

    """

    #TODO: completar y remplazar la siguiente linea por el resultado correcto
    
    sector = {'nombre_sector' : nombre, 'carriles' : carriles, 'pendiente' : pendiente,
               'ancho_calzada' : ancho_calzada, 'ancho_berma': ancho_berma, 
               'separador' : separador, 'concentracion_peatones' : peatones, 'control_accesos' : control_accesos,
               'zona_recreacional' : zona_recreacional, 'cuello_de_botella' : cuello_de_botella,
               'zona_escolar' : zona_escolar }
    
    return sector

def buscar_sector( nombre: str, s1: dict, s2: dict, s3: dict, 
                  s4: dict ) -> dict:
    """
    Busca el sector vial que coincide con el nombre pasado por parámetro.
    Si no se encuentra el sector, se retorna None.
    
    Parámetros
    ----------
    nombre : str
        Nombre del sector vial.
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.
    s3 : dict
        Diccionario con la información del tercer sector vial.
    s4 : dict
        Diccionario con la información del cuarto sector vial.

    Retorno
    -------
    dict
        Diccionario del sector vial con el nombre dado por parámetro.
        Retorna None si no lo encuentra.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    
    if nombre == s1['nombre_sector']:
         return s1 
 
    if nombre == s2["nombre_sector"]:
         return s2
   
    if nombre == s3["nombre_sector"]:
         return s3 
  
    if nombre == s4["nombre_sector"]:
         return s4 
 
     



def clasificar_sector( sector: dict ) -> str:
    """
    Clasifica un sector según sus características geométricas.

    Parámetros
    ----------
    sector : dict
        Diccionario del sector vial a clasificar.

    Retorno
    -------
    str
        Retorna alguna de las 7 clasificaciones viales según características
        geométricas (A1,B1,C1,A2,B2,C2 o D2).

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    p = " "
    if sector['pendiente'] <= 0.05 and sector['ancho_calzada'] == 7.30 and \
        sector['ancho_berma'] == 2.50 and sector['carriles'] > 2:
        p = "A1"
    
    if sector['pendiente'] <= 0.06 and sector['ancho_calzada'] == 7.30 and \
        sector['ancho_berma'] == 1.50 and sector['carriles'] > 2:
        p = "B1"
    
    if sector['pendiente'] <= 0.08 and sector['ancho_calzada'] == 7.0 and \
        sector['ancho_berma'] == 1.30 and sector['carriles'] > 2:
        p = "C1"
    
    if sector['pendiente'] <= 0.06 and sector['ancho_calzada'] == 7.30 and \
        sector['ancho_berma'] == 1.80 and sector['carriles'] == 2:
        p = "A2"
    
    if sector['pendiente'] <= 0.08 and sector['ancho_calzada'] == 7.30 and \
        sector['ancho_berma'] == 1.0 and sector['carriles'] == 2:
        p = "B2"
    
    if sector['pendiente'] <= 0.09 and sector['ancho_calzada'] == 7.0 and \
        sector['ancho_berma'] == 0.50 and sector['carriles'] == 2:
        p = "C2"
    
    if sector['pendiente'] <= 0.09 and sector['ancho_calzada'] == 7.0 and \
        sector['ancho_berma'] == 0.40 and sector['carriles'] == 2:
        p = "D2"
    
    return p
    
    
    
    


def determinar_velocidad_generica( sector: dict ) -> int:
    """
    Determina la velocidad genérica del sector según sus características.

    Parámetros
    ----------
    sector : dict
        Diccionario del sector vial a analizar.

    Retorno
    -------
    int
        Velocidad genérica del sector vial en km/h.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    resultado = 0
    clasificacion = clasificar_sector(sector)
   
    if sector["carriles"] > 2 and sector["separador"] == True:
        if clasificacion == 'A1' and sector["control_accesos"] == "Total" or sector["control_accesos"] == "Parcial" and sector["concentracion_peatones"] == False:
            resultado = 120
        elif clasificacion == 'B1' and sector["control_accesos"] == "Parcial" and sector["concentracion_peatones"] == False:
            resultado = 100
        elif clasificacion == 'B1' and sector["control_accesos"] == "Nulo" and sector["concentracion_peatones"] == False:
            resultado = 90
        elif clasificacion == 'C1' and sector["control_accesos"] == "Nulo" and sector["concentracion_peatones"] == False:
            resultado = 80
        elif clasificacion == 'C1' and sector["control_accesos"] == "Nulo" and sector["concentracion_peatones"] == True:
            resultado = 70
    if sector["carriles"] > 2 and sector["separador"] == False:
        if clasificacion == 'A1' and sector["control_accesos"] == "Total" or sector["control_accesos"] == "Parcial" and sector["concentracion_peatones"] == False:
            resultado = None
        elif clasificacion == 'B1' and sector["control_accesos"] == "Parcial" and sector["concentracion_peatones"] == False:
            resultado = 90
        elif clasificacion == 'B1' and sector["control_accesos"] == "Nulo" and sector["concentracion_peatones"] == False:
            resultado = 80
        elif clasificacion == 'C1' and sector["control_accesos"] == "Nulo" and sector["concentracion_peatones"] == False:
            resultado = 70
        elif clasificacion == 'C1' and sector["control_accesos"] == "Nulo" and sector["concentracion_peatones"] == True:
            resultado = 60
    if sector["carriles"] == 2 and sector["separador"] == False or sector["separador"] == True:
        if sector["concentracion_peatones"] == False and clasificacion == 'A2':
            resultado = 80
        elif sector["concentracion_peatones"] == True and clasificacion == 'A2' or clasificacion == 'B2':
            resultado = 70
        elif sector["concentracion_peatones"] == True and clasificacion == 'C2':
            resultado = 50
        elif sector["concentracion_peatones"] == True and clasificacion == 'D2':
            resultado = 40
    return resultado



def calcular_velocidad_promedio( sector: dict ) -> float:
    """
    Calcula la velocidad promedio de un sector según sus restricciones por
    sitios especiales.

    Parámetros
    ----------
    sector : dict
        Diccionario del sector vial a analizar.

    Retorno
    -------
    float
        Velocidad promedio del sector en km/h redondeada a 2 cifras decimales.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    vel_generica = determinar_velocidad_generica(sector)
    n = 1
    
    if sector["zona_recreacional"] == True:
        vel_generica += 30
        n += 1
    if sector["cuello_de_botella"] == True:
        vel_generica += 40
        n += 1
    if sector["zona_escolar"] == True:
        vel_generica += 30
        n += 1
        
    r = vel_generica/n
       
    return r

def contar_libres_de_restriccion( s1: dict, s2: dict, s3: dict,
                                 s4: dict ) -> int:
    """
    Cuenta los sectores que no tienen sitios especiales.

    Parámetros
    ----------
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.
    s3 : dict
        Diccionario con la información del tercer sector vial.
    s4 : dict
        Diccionario con la información del cuarto sector vial.

    Retorno
    -------
    int
        Número de sectores que no tienen sitios especiales.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    p = 0
    
    if s1["zona_recreacional"] != True and s1["cuello_de_botella"] != True and\
        s1["zona_escolar"] != True:
            p += 1
    elif s2["zona_recreacional"] != True and s2["cuello_de_botella"] != True and\
        s2["zona_escolar"] != True:
            p += 1
    elif s3["zona_recreacional"] != True and s3["cuello_de_botella"] != True and\
        s3["zona_escolar"] != True:
            p += 1
    elif s4["zona_recreacional"] != True and s4["cuello_de_botella"] != True and\
        s4["zona_escolar"] != True:
            p += 1
   

    return p

def determinar_pendiente_menor( pendiente: float, s1: dict, s2: dict, s3: dict,
                               s4: dict ) -> str:
    """
    Determina cuáles sectores tienen una pendiente menor a un número dado.

    Parámetros
    ----------
    pendiente : float
        Conta superior de la pendiente de los sectores a encontrar.
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.
    s3 : dict
        Diccionario con la información del tercer sector vial.
    s4 : dict
        Diccionario con la información del cuarto sector vial.
        
    Retorno
    -------
    str
        Una cadena con todos los nombres de los sectores que tienen una 
        pendiente inferior a la dada por parámetro.
    
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    respuesta = " "
    x = ","
    if s1["pendiente"] < pendiente:
        respuesta += s1["nombre_sector"]
    if s2["pendiente"] < pendiente:
        respuesta += x
        respuesta += s2["nombre_sector"]
    if s3["pendiente"] < pendiente:
        respuesta += x
        respuesta += s3["nombre_sector"]
    if s4["pendiente"] < pendiente:
        respuesta += x
        respuesta += s4["nombre_sector"]

    return respuesta

def velocidad_maxima( s1: dict, s2: dict, s3: dict, s4: dict ) -> dict:
    """
    Retorna el diccionario del sector con la velocidad genérica más alta. En
    caso de encontrar dos sectores con la misma velocidad, se debe mostrar el
    nombre del sector que vaya primero alfabéticamente.

    Parámetros
    ----------
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.
    s3 : dict
        Diccionario con la información del tercer sector vial.
    s4 : dict
        Diccionario con la información del cuarto sector vial.

    Retorno
    -------
    dict
        El diccionario con la velocidad genérica más alta.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    mayor = s1
    max_vel = determinar_velocidad_generica(s1)
    
    max_sec2  = determinar_velocidad_generica(s2)
    max_sec3  = determinar_velocidad_generica(s3)
    max_sec4  = determinar_velocidad_generica(s4)
   
    if max_sec2 > max_vel or max_sec2 == max_vel and s2["nombre_sector"] \
        < mayor["nombre_sector"]:
        mayor = s2
        max_vel = max_sec2
    
    if max_sec3 > max_vel or max_sec3 == max_vel and s3["nombre_sector"] \
        < mayor["nombre_sector"]:
        mayor = s3
        max_vel = max_sec3
    
    if max_sec4 > max_vel or max_sec4 == max_vel and s4["nombre_sector"] \
        < mayor["nombre_sector"]:
        mayor = s4
        max_vel = max_sec4
    
    return mayor


def contar_sitios_especiales( s1: dict, s2: dict, s3: dict, s4: dict ) -> dict:
    """
    Retorna un diccionario con la cantidad de sitios especiales que hay en
    todos los sectores.

    Parámetros
    ----------
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.
    s3 : dict
        Diccionario con la información del tercer sector vial.
    s4 : dict
        Diccionario con la información del cuarto sector vial.

    Retorno
    -------
    dict
        Diccionario que tiene como llaves el nombre del sitio especial y como
        valores la cantidad de sitios especiales que existen de ese sitio.
        Las llaves deben ser "zona_recreacional", "cuello_de_botella" y
        "zona_escolar"

    """
    
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    recreacional = 0
    botella = 0
    escolar = 0
      
    if s1["zona_recreacional"] == True:
        recreacional += 1
    else:
        recreacional += 0
    if s1["cuello_de_botella"] == True:
        botella += 1
    else:
        botella += 0
    if s1["zona_escolar"] == True:
        escolar += 1
    else:
        escolar += 0
        
    if s2["zona_recreacional"] == True:
        recreacional += 1
    else:
        recreacional += 0
    if s2["cuello_de_botella"] == True:
        botella += 1
    else:
        botella += 0
    if s2["zona_escolar"] == True:
        escolar += 1
    else:
        escolar += 0
        
        
    if s3["zona_recreacional"] == True:
        recreacional += 1
    else:
        recreacional += 0
    if s3["cuello_de_botella"] == True:
        botella += 1
    else:
        botella += 0
    if s3["zona_escolar"] == True:
        escolar += 1
    else:
        escolar += 0
        
    if s4["zona_recreacional"] == True:
        recreacional += 1
    else:
        recreacional += 0
    if s4["cuello_de_botella"] == True:
        botella += 1
    else:
        botella += 0
    if s4["zona_escolar"] == True:
        escolar += 1
    else:
        escolar += 0
        
    zonas_esp ={"Recreacional": recreacional, \
                "Cuello_de_botella": botella, \
                  "Zona_escolar": escolar}
    
    
    return zonas_esp