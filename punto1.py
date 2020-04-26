# Se supone:
# El dominio es un local del estilo cafeteria tipico, donde se encuentran clientes que atender, pedidos que realizar y cobrar; tambien habran insumos que limpiar por pedido.
# La organizacion a simular es pequeña, por lo que normalmente no tienen personal para realizar multiples actividades en simultaneo, como conclusion de esto, se debera simular de 
# manera continua la realizacion de actividades e ignorando la posibilidad de realizar actividades en simultaneo.
# El valor que representa cada posicion del arreglo de clientes representa la cantidad de minutos; por ejemplo; 2.95 serian 2 minutos y el 95% de otro minuto (practicamente 3 minutos).


import numpy as np


def calcular_costo_higienizar_elementos(pedidos):
    acumulador = 0
    for pedido in pedidos:
        acumulador+=5
    return acumulador


# Funcion que dada una lista de tiempo utilizado en pedidos devuelve la sumatoria de los valores en la lista.
def calcular_costo_atender_pedidos(pedidos):
    acumulador = 0
    for pedido in pedidos:
        acumulador+=pedido
    return acumulador

# Funcion que dado un tamaño "cantidad" devuelve una lista de dicho tamaño compuesta por tiempos utilizados en pedidos que sigue una distribucion exponencial.
def obtener_pedidos(cantidad):
    return np.random.exponential(2,cantidad)

# Funcion que dado un tamaño "cantidad" devuelve una lista de dicho tamaño compuesta por tiempos de atencion a clientes que sigue una distribucion normal.
def obtener_clientes(cantidad):
    media = 5 # Significa que cada cliente en promedio tardara <media> minutos en ser atendido.
    desvio = 3 # Significa que para cada atención se tendra una variacion +- <desvio> de la <media>.
    clientes = np.random.normal(media,desvio,cantidad)
    return clientes


# Funcion para calcular el tiempo de atender los clientes a partir de una lista de clientes
def calcular_costo_atender_clientes(clientes,productividad):
    if productividad == 0:
        return 0
    else:
        acumulador = 0
        i = 0
        # Sumamos los valores del arreglo de tiempos de atenciones a clientes.
        for cliente in clientes:
            i+=1
            #print("DEBUG --- Tiempo de atencion del cliente"+i+": "+cliente)
            acumulador += cliente
        return acumulador / productividad


# Funcion principal.
def __main__():
    PRODUCTIVIDAD = 1 # Valor que varìa entre 0 y 1 indicando la productividad de los empleados (no esta limitado, si se incrementa la productividad al 1000% lo soluciona). Verlo de este modo provee escalabilidad.
    CANT_CLIENTES = 10 # Valor que representa la cantidad de clientes a atender.
    CANT_PEDIDOS = 10 # Valor que representa la cantidad de pedidos (independientemente del estado del mismo{en realizacion, entregado, cobrado})
    
    tiempoSimulacion = 0

    print("DEBUG --- cantidad de clientes: ",CANT_CLIENTES)
    print("DEBUG --- cantidad de pedidos: ",CANT_PEDIDOS)
    
    # Veo cuantos clientes fueron atendidos, calculo el costo temporal asociado y actualizo el tiempo de la simulacion.
    clientes = obtener_clientes(CANT_CLIENTES)
    tiempoUsadoEnAtenderClientes = calcular_costo_atender_clientes(clientes,PRODUCTIVIDAD)
    tiempoSimulacion+=tiempoUsadoEnAtenderClientes
    print("DEBUG --- el tiempo usado en atender a todos los clientes fue de: "+tiempoUsadoEnAtenderClientes.__str__()+" minutos.")
    
    # Veo cuantos pedidos fueron realizados,calculo el costo temporal asociado y actualizo el tiempo de la simulacion.
    pedidos = obtener_pedidos(CANT_PEDIDOS)
    tiempoUsadoEnAtenderPedidos = calcular_costo_atender_pedidos(pedidos)
    tiempoSimulacion+=tiempoUsadoEnAtenderPedidos
    print("DEBUG --- el tiempo usado en atender a todos los pedidos fue de: "+tiempoUsadoEnAtenderPedidos.__str__()+" minutos.")
    
    # Calculo cuanto tiempo se gasta en higienizar los elementos y actualizo el tiempo de la simulacion.
    tiempoHigienizacionDeElementos = calcular_costo_higienizar_elementos(pedidos)
    tiempoSimulacion+=tiempoHigienizacionDeElementos
    print("DEBUG --- el tiempo usado en higienizar los elementos fue de: "+tiempoHigienizacionDeElementos.__str__()+" minutos.")

    print("DEBUG --- el tiempo usado en toda la simulacion fue de: "+tiempoSimulacion.__str__()+" minutos.")
    return 0



# Funcion de inicio.
def __init__():
    __main__()# Iniciamos la secuencia principal de ejecucion.
    return 0


# Primer linea en ejecutarse.
__init__()
