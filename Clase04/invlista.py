def invertir_lista(lista):
    i = 0
    invertida = []
    for n in range(len(lista)):
        i -= 1
        invertida.append(lista[i])
    return invertida

l1 = [1, 2, 3, 4, 5]
l2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']

invertida = invertir_lista(l2)

print(invertida)