valor=0
texto=""
print (f'{texto:>6s}',end="")
for cabecera in range(10):
    print (f'{cabecera:>5d}',end="")
print("")
linea="-"
linea=linea*5*11+"-"
print (linea)
for filas in range(10):
    contador=0
    print (f'{filas:>5d}:{valor:>5d}',end="")
    
    for columnas in range(9):
        valor+=filas
        print (f'{valor:>5d}',end="")
        if contador==8:
            print("")        
        contador+=1
    valor=0
    