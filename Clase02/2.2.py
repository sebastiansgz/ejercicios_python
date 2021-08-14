costo_total = float()

with open('../Data/camion.csv', 'rt') as file:
    headers = next(file).split()
    for line in file:
        row = line.split(',')
        costo_por_fruta = float(row[1]) * float(row[2])
        costo_total += costo_por_fruta

print(costo_total) 

