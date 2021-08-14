with open('../Data/precios.csv', 'rt') as file:    
    for line in file:
        row = line.split(',')
        if str(row[0]).lower() == 'naranja':
            precio_naranja = float(row[1])

print(f'El precio de la naranaja es: {precio_naranja}')

