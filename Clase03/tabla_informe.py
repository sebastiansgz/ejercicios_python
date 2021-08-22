'''
Este script se puede ejecutar acompañado de dos argumentos que indican la ubicación de camion.csv y precios.csv respectivamente.

En caso de no proveer la ubicacion de dichos archivos este script asume que se trabaja en 'ejercicios_python/Clase03/tabla_filas_tabla.py'
'''
import csv
import sys

# Hago uso de sys.argv para tomar los argumentos que paso al momento de ejecutar el script desde la linea de comandos como el nombre de los archivos que van a ser utilizados.

if len(sys.argv) == 3:
    archivo_camion = sys.argv[1] 
    archivo_precios = sys.argv[2] 
else:
    archivo_camion = '../Data/camion.csv'
    archivo_precios ='../Data/precios.csv'


# ------------------------- Defino las funciones------------------------------------
#Función para manejar el archivo del camion.
def leer_camion(nombre_archivo):
    camion = []                                        # Importante: Definir la lista vacia dentro de la función así inicia vacia siempre.
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)        
        for row in rows:
            lote = dict(zip(headers, row))
            lote['cajones'] = int(lote['cajones'])    
            lote['precio'] = float(lote['precio'])    
            camion.append(lote)            
    return camion

#Función para manejar el archivo de precios.
def leer_precios(archivo_precios):
    precios = []
    with open(archivo_precios, 'rt') as file:        
        rows = csv.reader(file)
        for n_row, row in enumerate(rows, start= 1):
            try:
                nombre = row[0]            
                precio = float(row[1])
                par = (nombre , precio)
                precios.append(par)                
            except IndexError:
                print(f'Alerta: En la linea {n_row} del archivo {archivo_precios} no se encuentran los elementos necesarios para armar un par "key:value"')
    return dict(precios)

# Función para calcular el balance. 

def calcular_balance(camion, precios):    
    costo_total = float()
    venta_total = float()
    for lote in camion:
        costo_total += lote['cajones'] * lote['precio']
        producto = lote['nombre']
        venta_total += precios[producto] * lote['cajones']
    balance = venta_total - costo_total
    if balance >= 0:
        print(f'*BALANCE: \n Costo total: {costo_total} \n Total ventas: {venta_total}\nLa ganacia fue de: {balance}')
    else:
        print(f'*BALANCE: \n Costo total: {costo_total} \n Total ventas: {venta_total}\nLas perdidas fueron de: {balance}')
    return 


def hacer_balance(camion,precios):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')   
    filas_tabla = []   
    for lote in camion:
        producto = lote['nombre']
        cambio = precios[producto]-lote['precio']
        fila = lote['nombre'],int(lote['cajones']),float(lote['precio']), round(cambio,2)
        filas_tabla.append(tuple(fila))        
    return filas_tabla

    
def hacer_tabla_balance(filas_tabla):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    filas_tabla = hacer_balance(camion,precios)
    print(f"{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}")       
    print(f"{'-'*int(10):>10} {'-'*int(10):>10} {'-'*int(10):>10} {'-'*int(10):>10}")     
    for nombre, cajones, precio, cambio in filas_tabla:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
    return




# ------------------------------- Utilizo las funciones----------------------------------

camion = leer_camion(archivo_camion)  # Tengo una lista que contiene diccionarios con las compras por lotes de cada fruta/verdura.
precios = leer_precios(archivo_precios) # Un diccionario con {'nombre' : precio,(...)} Este diccionario contiene la fruta/verdura y su precio de venta.

filas_tabla = hacer_balance(camion,precios) # Tengo una lista con tuplas. Cada tuplas es una fila de la tabla del balanace.
hacer_tabla_balance(filas_tabla)            # Paso la lista con tuplas por esta función y la formateo en una tabla.

#calcular_balance(camion,precios)







