'''
Este script se puede ejecutar acompañado de dos argumentos que indican la ubicación de camion.csv y precios.csv respectivamente.

En caso de no proveer la ubicacion de dichos archivos este script asume que se trabaja en 'ejercicios_python/informe.py'
'''
import csv
import sys

# Hago uso de sys.argv para tomar los argumentos que paso al momento de ejecutar el script desde la linea de comandos como el nombre de los archivos que van a ser utilizados.

if len(sys.argv) == 3:
    archivo_camion = sys.argv[1] 
    archivo_precios = sys.argv[2] 
else:
    archivo_camion = '../Data/fecha_camion.csv'
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
def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo) as file:        
        rows = csv.reader(file)
        for n_row, row in enumerate(rows, start=0):
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print(f'Alerta: En la linea {n_row} del archivo "{nombre_archivo}" no hay elementos para armar un par "key:value"')
    return precios

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
        print(f'BALANCE: \n Costo total: {costo_total} \n Total ventas: {venta_total}\nLa ganacia fue de: {balance}')
    else:
        print(f'BALANCE: \n Costo total: {costo_total} \n Total ventas: {venta_total}\nLas perdidas fueron de: {balance}')
    return 

# ------------------------------- Utilizo las funciones----------------------------------
camion = leer_camion(archivo_camion)  # Tengo una lista que contiene diccionarios
precios = leer_precios(archivo_precios) # Un diccionario con {'nombre' : precio,(...)}

calcular_balance(camion,precios)

'''
OUTPUT

Alerta: En la linea 30 del archivo "Data/precios.csv" no hay elementos para armar un par "key:value"
BALANCE: 
 Costo total: 47671.15 
 Total ventas: 62986.1
La ganacia fue de: 15314.949999999997

'''