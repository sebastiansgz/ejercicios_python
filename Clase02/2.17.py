import csv
import sys

precios = []

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as file:        
        rows = csv.reader(file)
        for row in rows:
            try:
                nombre = row[0]            
                precio = float(row[1])
                par = (nombre , precio)
                precios.append(par)                
            except IndexError:
                print('En alguna/s linea/s del archivo no hay elementos para armar un par "key:value"')
    return dict(precios)
            

if len(sys.argv) == 2:
    nombre_archivo  = sys.argv[1]
else:
    nombre_archivo = '../Data/precios.csv'

print(leer_precios(nombre_archivo))