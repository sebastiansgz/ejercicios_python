# lista = [0, 100,30,0,-2, -5,-4,200,0]

def buscar_u_elemento(lista, elemento):
    pos = -1
    for i, n in enumerate(lista):
        if n == elemento:
            pos = i
    print(pos)
    return 


def maximo(lista):
    m = 0 
    for e in lista: 
        if e > m:
            m = e
        m = e
    for e in lista:
        if e > m:
            m = e 
    return m


def minimo(lista):
    m = 0 
    for e in lista: 
        if e < m:           
            m = e
    return m





#buscar_u_elemento(lista, 2)
