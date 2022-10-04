import time

def cargar_blockchain_cupicoin(nombre_archivo: str)->list:

    """
    ESTA FUNCIÓN ES PARA PODER CARGAR
    LOS ARCHIVOS DENTRO DE DICCIONARIOS SEGUN
    COMO FUNCIONA Y TRABAJA CUPICOIN
    """
    bloques = []
    bloque_temporal = []

    archivo = open(nombre_archivo, "r",  encoding="ISO-8859-1")
    archivo.readline()
    linea = archivo.readline()
    

    bloque_actual = 0
    sentinela = False
    while True:
        
        datos = linea.split(",")
        datos.append(-1)

        if int(datos[1])==bloque_actual:
            bloque_temporal.append(datos)
            linea = archivo.readline()
        else:
            timestamp = int(time.time())
            if bloque_actual==0:
                hash_anterior = ''
            else:
                hash_anterior = bloques[-1]["hash"]

            bloque = {
                "numero_bloque": bloque_actual,
                "cantidad_transacciones": len(bloque_temporal),
                "timestamp": timestamp,
                "abierto": False,
                "hash": calcular_el_hash(bloque_temporal, timestamp),
                "hash_anterior": hash_anterior
            }
            
            for i in range(len(bloque_temporal)):
                if bloque_temporal[i][3]=="":
                    operacion = "contrato"
                else:
                    operacion = "transferencia"
                bloque[i]= {
                    "codigo_transaccion": bloque_temporal[i][0],
                    "remitente":bloque_temporal[i][2],
                    "destinatario":bloque_temporal[i][3],
                    "valor":bloque_temporal[i][4],
                    "operacion": operacion
                }

            bloque_actual+=1
            bloque_temporal = []
            bloques.append(bloque)
        
        if linea == '':
            sentinela = True
            
        if sentinela is True:
            break
        
   
    bloques[-1]["timestamp"]  = None
    bloques[-1]["hash"]  = None
    bloques[-1]["abierto"]  = True
    

     
    archivo.close()
    
    return bloques


def hashh (SumaASCII: int, timestamp: int) -> int:
 return SumaASCII % timestamp

def calcular_el_hash(bloque_temporal, timestamp):
    sumaASCII = ""
    for a in bloque_temporal:
        a=[str(x) for x in a]
        sumaASCII += "".join(a)
    
    valor = 0
    for x in range(len(sumaASCII)):
        valor += ord(sumaASCII[x])
    
    return hashh(valor, timestamp)
    



def agregar_transaccion(bloques: list, transaccion: dict)-> dict:
    dic = {}
    
    if bloques == []:
        dic["numero_bloque"] = 0
        dic["cantidad_transacciones"] = 0
        dic["timestamp"] = None
        dic["abierto"] = True
        dic["hash"] = None
        dic["hash_anterior"] = None
        bloques.append(dic)
        new = bloques[-1]
        TransaccionNueva = new["cantidad_transacciones"]
        new[TransaccionNueva] = transaccion
        new["cantidad_transacciones"] += 1
    else:
        ult = bloques[-1]
        TransaccionNueva = ult["cantidad_transacciones"]
        ult[TransaccionNueva] = transaccion
        ult["cantidad_transacciones"] += 1
        
    return bloques

def agregar_nuevo_bloque(blockchain: list, timestamp: int)->None:
    
    blockchain[-1]["timestamp"]= timestamp
    blockchain[-1]["abierto"]= False
    blockchain[-1]["hash"]= calcular_el_hash(blockchain[-1])
    
    blockchain.append({
                "numero_bloque": blockchain[-1]["numero_bloque"]+1,
                "cantidad_transacciones": 0,
                "timestamp": None,
                "abierto": True,
                "hash": None,
                "hash_anterior": blockchain[-1]["hash"]
            })
    
def contar_veces_aparece_cuenta(bloques: list, direccion: str)->dict:
    cuenta = {}
    remitente = 0
    destinatario = 0
    
    for i in bloques:
        transacciones = bloques["cantidad_transacciones"]
        for i in transacciones:
            a = bloques[i]
            if a["remitente"] is direccion:
                remitente += 1
            if a["destinatario"] is direccion:
                destinatario += 1
            
    remitente = cuenta["remitente"] 
    destinatario = cuenta["destinatario"] 
    return cuenta
                
def buscar_transaccion(blockchain: list, codigo: str)->dict:
    
    buscar = {}
    for bloque in blockchain:
        transacciones = bloque["cantidad_transacciones"]
        for i in transacciones:
            
            if blockchain[bloque][i]["codigo_transacciones"] == codigo:
                
                buscar = blockchain[bloque][i] #REVISAR
    return buscar 
    
    
def validar_bloque(blockchain: list, remitente: int, destinatario: int)->list:
    validar = []
    for bloque in blockchain:
        transacciones = bloque["cantidad_transacciones"]
        for i in range(0, transacciones):
            if bloque[i]["remitente"] == remitente and bloque[i]["destinatario"] == destinatario:
                validar.append(bloque[i])
    return validar


def dar_transferencia_mayor_valor(blockchain: list)->dict:
    maximo = {}
    mayor = 0
    for bloque in blockchain:
        transacciones = bloque["cantidad_transacciones"]
        for i in range(0, transacciones):
            if [bloque][i]["valor"] > mayor:
                maximo = bloque[i]
    return maximo

def calcular_saldo_cuenta(blockchain: list, direccion: str)->float:
    suma = 0
    for bloque in blockchain:
        transacciones = bloque["cantidad_transacciones"]
        for i in range(0, transacciones):
            transaccion = bloque[i]
            if transaccion["destinatario"] == direccion:
                suma += transaccion["valor"]
            elif transaccion["remitente"] == direccion:
                if transaccion["operacion"] == "contrato":
                    suma += transaccion["valor"]
                else:
                    suma -= transaccion["valor"]
    return suma

def integridad_blockchain(blockchain: list)-> bool:
    validacion = True

    for x in range(len(blockchain)):
        bloque = blockchain[x]
        bloque_anterior = blockchain[x-1]
        tiempo  = bloque["timestamp"]
        if bloque is not blockchain[-1]:
            jash = calcular_el_hash(bloque, tiempo)
            if bloque["hash"] != jash:
                validacion = False 
        if bloque != blockchain[0]:
            validacion = False
        if bloque_anterior["hash"] != bloque["hash_anterior"]:
            validacion = False
        if bloque != blockchain[-1] and bloque["abierto"] is True:
            validacion = False
    if blockchain[-1]["abierto"] == False:
        validacion = False
    return validacion

           
    
    