import csv

def costo_camion(archivo):
    with open(archivo, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        costo_total = float()
        for row in rows:
            costo_por_fruta = float(row[1]) * float(row[2])
            costo_total += costo_por_fruta
    return costo_total

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
