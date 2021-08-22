import csv
import sys



def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo) as file:        
        rows = csv.reader(file)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print('En alguna/s linea/s del archivo no hay elementos para armar un par "key:value"')
    return precios
            

if len(sys.argv) == 2:
    nombre_archivo  = sys.argv[1]
else:
    nombre_archivo = '../Data/precios.csv'

print(leer_precios(nombre_archivo))