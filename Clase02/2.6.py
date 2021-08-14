def costo_camion(archivo):
    with open(archivo, 'rt') as file:
        headers = next(file).split()
        costo_total = float()
        for line in file:
            row = line.split(',')
            costo_por_fruta = float(row[1]) * float(row[2])
            costo_total += costo_por_fruta
    return costo_total

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
