
import time as t


def cargar_blockchain_cupicoin(nombre_archivo:str)->list:
    
    control = []
    bloques = []
    
    arch = open(nombre_archivo, "r")
    
    arch.readline() 
    
    linea = arch.readline()
    ultimo_ts = t.time()
    while linea != "":
        
        datos = linea.replace("\n","").split(",")
        
        if datos[1] not in control:
            control.append(datos[1])
            f3_agregar_bloque(bloques, float(datos[5]))
     
            
        operacion = "transferencia"
        if datos[3].strip() == '':
            operacion = "contrato"
            
        dicc_transaccion = { "codigo_transaccion": datos[0],
                             "remitente": datos[2],
                             "destinatario": datos[3],
                             "valor": float(datos[4]),
                             "operacion": operacion
            
                            }
        f2_agregar_transaccion(bloques, dicc_transaccion)
        
        ultimo_ts = float(datos[5])
        linea = arch.readline()
        
    arch.close()
    
    f3_agregar_bloque(bloques, ultimo_ts)
    
    return bloques




def f2_agregar_transaccion(bloques:list, transaccion:dict)->None:
    """
    Agrega una transacción en el último bloque 
    Aumenta la cantidad de transacciones del último bloque en 1

    Parameters
    ----------
    bloques : list
        Lista de bloques que forman el blockchain
    transaccion : dict
        Transacción que se desea agregar

    """
    bloques[-1][bloques[-1]["cantidad_transacciones"]] = transaccion
    bloques[-1]["cantidad_transacciones"] += 1
    
    
    
def f3_agregar_bloque(bloques:list, timestap:float)->None:
    """
    Agrega un nuevo bloque al final del blockchain
    Cierra el último bloque y le asigna el timestamp
    Parameters
    ----------
    bloques : list
        Lista de bloques que forman el blockchain
    timestap : float
        Timestamp en que se está cerrando se está agregando el nuevo bloque
        y se cierra el anterior.
    """
    
    if len(bloques) == 0:
        nuevo = {"numero_bloque": 0,
             "cantidad_transacciones": 0,
             "abierto": True
            }
        bloques.append(nuevo)
    else:
        ultimo = bloques[-1]
        ultimo["timestamp"] = timestap
        ultimo["abierto"] = False
    
    
    
        nuevo = {"numero_bloque": ultimo["numero_bloque"] + 1,
                 "cantidad_transacciones": 0,
                 "abierto": True
                }
        bloques.append(nuevo)
      
        
        
def contar_menos_de_en_segmento(bloques:list, b_inicial:int, b_final:int, valor:float)->int:
    """
    Cuenta e informa la cantidad de transacciones (de tpo transferencia) registradas entre 
    el bloque inicial (incluido) el bloque final (no incluido) que tienen un valor inferior al indicado por
    parámetro

    Parameters
    ----------
    bloques : list
        Lista de bloques que forman el blockchain
    b_inicial : int
        número del bloque inicial a revisar (se debe incluir en la revisión).
    b_final : int
        número del bloque final a revisar (no se debe incluir en la revisión).
    valor : float
        valor que se desea revisar entre las transacciones

    Returns
    -------
    int
        Cantidad de transacciones (tipo transferencia) en el segmento de bloques dado con un valor
        inferior al indicado.

    """
    #TODO complete de acuerdo a la documentación
    cantidad_transacciones = 0
    for tr in bloques:
        for i in range(b_inicial, b_final):
            if [i]["operacion"] == "transferencia" and [i]["valor"] < valor:
                cantidad_transacciones += 1
        
    return cantidad_transacciones
    


      
def existe_contrato_en_segmento (bloques:list, b_inicial:int, b_final:int)->bool:
    """
    Indica si en un segmento de bloques dado existe al menos un contrato.
    Su solución debe ser eficiente y si encuentra un contrato no debe 
    revisar mas transacciones

    Parameters
    ----------
    bloques : list
        Lista de bloques que forman el blockchain
    b_inicial : int
        número del bloque inicial a revisar (se debe incluir en la revisión).
    b_final : int
        número del bloque final a revisar (no se debe incluir en la revisión).

    Returns
    -------
    bool
        True si existe al menos un contrato en el segmento de bloques dados
        o False en caso contrario

    """
    #TODO complete de acuerdo a la documentación
    contrato = False
    for i in bloques:
        for i in range(b_inicial, b_final - 1):
            operaciones = bloques[i]
            if operaciones == "contrato":
                contrato = True
                
                
        
    return contrato
        

    



