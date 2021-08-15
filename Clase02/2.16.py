import csv
import sys

camion = []

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as file:
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



if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1] 
else:
    nombre_archivo = '../Data/camion.csv'

