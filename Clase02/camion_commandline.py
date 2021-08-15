import csv
import sys

def costo_camion(archivo):
    with open(archivo, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)    
        costo_total = float()
        for row in rows:
            try:
                costo_por_fruta = float(row[1]) * float(row[2])
                costo_total += costo_por_fruta
            except ValueError:
                print('warning')
    return costo_total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv' 

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)