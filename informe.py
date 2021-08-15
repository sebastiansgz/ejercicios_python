'''
Este script se puede ejecutar acompañado de dos argumentos que indican la ubicación de camion.csv y precios.csv respectivamente.

En caso de no proveer la ubicacion de dichos archivos este script asume que se trabaja en 'ejercicios_python/informe.py'
'''
import csv
import sys

camion = []
precios = []

def leer_camion(archivo_camion):
    with open(archivo_camion, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)        
        for row in rows:
            lote = {
                headers[0] : row[0],
                headers[1] : int(row[1]), 
                headers[2] : float(row[2])
            }
            camion.append(lote)
    return camion


def leer_precios(archivo_precios):
    with open(archivo_precios, 'rt') as file:        
        rows = csv.reader(file)
        for row in rows:
            try:
                nombre = row[0]            
                precio = float(row[1])
                par = (nombre , precio)
                precios.append(par)                
            except IndexError:
                print(f'Alerta: En alguna/s linea/s del archivo {archivo_precios} no se encuentran los elementos necesarios para armar un par "key:value"')
    return dict(precios)


if len(sys.argv) == 3:
    archivo_camion = sys.argv[1] 
    archivo_precios = sys.argv[2] 
else:
    archivo_camion = 'Data/camion.csv'
    archivo_precios ='Data/precios.csv'


camion = leer_camion(archivo_camion)  # Tengo una lsta que contiene diccionarios
precios = leer_precios(archivo_precios) # Un diccionario con {'nombre' : precio,(...)}
costo_total = float()
venta_total = float()

for lote in camion:
    costo_total += lote['cajones'] * lote['precio']
    producto = lote['nombre']
    venta_total += precios[producto] * lote['cajones']    

balance = venta_total - costo_total


print(f'BALANCE: \n Costo total: {costo_total} \n Total ventas: {venta_total} \n Diferencia: {balance}')

'''
OUTPUT

Alerta: En alguna/s linea/s del archivo Data/precios.csv no se encuentran los elementos necesarios para armar un par "key:value"
BALANCE: 
 Costo total: 47671.15 
 Total ventas:62986.1 
 Diferencia: 15314.949999999997

'''