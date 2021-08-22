def suma_tuplas(tupla1, tupla2):                            # Tengo una funcion que le doy dos tuplas de numeros y las suma.
    return tuple(a + b for a, b in zip(tupla1, tupla2))


def obtener_filas(nums_1,nums_n):                           #Obtengo las filas para DESPUES armar la tabla
    filas_tabla = []
    filas_tabla.append(nums_0)
    filas_tabla.append(nums_n)    
    for i in range(0,8):                                           
        nums_n = suma_tuplas(nums_1, nums_n)
        filas_tabla.append(nums_n)
    return filas_tabla

def crear_tabla(filas_tabla): 
    i = 1
    print()
    for n_fila, fila in enumerate(filas_tabla, start= 0):
        print(f'{n_fila}:', end=' ')
        for x in fila:                
            if i <= (len(fila)):
                print(f"{x} ", end=' ')
                i += 1
        print('\n') 
        i = 1
    return

nums_0 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)                              # Estado inical
nums_1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)                              # Esto debe ser una constante que se suma.

                              
nums_n = suma_tuplas(nums_0, nums_1)
filas_tabla = obtener_filas(nums_1,nums_n)
crear_tabla(filas_tabla)




