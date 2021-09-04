def invertir_lista(lista):
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append(lista[i]) 
    return invertida

l = [1, 2, 3, 4, 5]    
l2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
m = invertir_lista(l2)
print(m)
