def buscar_precio(fruta):
    is_there = False          
    with open('../Data/precios.csv', 'rt') as file:            
        for line in file:            
            row = line.split(',') 
            if row[0].lower() == fruta.lower():
                is_there = True
                if is_there:
                    precio_fruta = float(row[1])
                print(f'El precio de la {fruta} es: {precio_fruta}')         
        if is_there == False:
            print(f'{fruta} no figura en el listado de precios')


fruta = input('Ingrese la fruta (o verdura) para consultar su precio: ')
precio = buscar_precio(fruta)