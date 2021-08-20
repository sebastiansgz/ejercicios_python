import csv

def costo_camion(archivo):
    with open(archivo, 'rt') as file:
        filas = csv.reader(file)
        encabezados = next(filas)
        costo_total = float()
        for n_fila, fila in enumerate(filas, start = 1):
            record = dict(zip(encabezados ,fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            except ValueError:
                print(f'Fila {n_fila} No puede interpretar: {fila}')

    return costo_total

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)