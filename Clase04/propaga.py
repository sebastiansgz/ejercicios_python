def propagar(vector):
    # Recorro la lista de izq a derecha cada 0 a la derecha de un 1 es tranformado por otro 1 en una nueva lista
    izq_der = [0] 
    for fosforo in vector:
        if (fosforo == 0) and (izq_der[-1]) == 1:
            fosforo = 1
            izq_der.append(fosforo)
        else:
            izq_der.append(fosforo)
    izq_der.remove(0)
 # Recorro la lista de derecha a izquierda, cada 0 a la izq de un 1 es convertido a 1 en una nueva lista que invierte el orden de la lista original.       
    i = 0
    der_izq = []
    for _ in range(len(izq_der)):
        i -=1
        if (izq_der[i] == 0) and (der_izq[-1] ==1):
            fosforo = izq_der[i] 
            fosforo = 1
            der_izq.append(fosforo)
        else:
            fosforo = izq_der[i]
            der_izq.append(fosforo)
# Vuelvo a invertir la lista para tenerla en el orden original.
    i = 0
    invertida = []
    for n in range(len(der_izq)):
        i -= 1
        invertida.append(der_izq[i])    
    return invertida               
    
        
            
print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))