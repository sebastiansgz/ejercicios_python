import csv

def costo_camion(archivo):
    with open(archivo, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        costo_total = float()
        for i, row in enumerate(rows, start = 1):
            try:
                costo_por_fruta = float(row[1]) * float(row[2])
                costo_total += costo_por_fruta
            except ValueError:
                print(f'Fila {i} No puede interpretar: {row}')

    return costo_total

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)