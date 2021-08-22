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
    print('   ', end= '')  
    for x in nums_1:                   
        print(f"{x:>2} ", end=' ')
    print(f"\n{'-'*42}")
    for n_fila, fila in enumerate(filas_tabla, start= 0):
        print(f'{n_fila}:', end=' ')
        for x in fila:              
            print(f"{x:>2} ", end=' ')                
        print('\n')        
    return

nums_0 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)                              # Estado inical
nums_1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)                              # Esto debe ser una constante que se suma.

                              
nums_n = suma_tuplas(nums_0, nums_1)

filas_tabla = obtener_filas(nums_1,nums_n)
crear_tabla(filas_tabla)

'''
    0   1   2   3   4   5   6   7   8   9  
------------------------------------------
0:  0   0   0   0   0   0   0   0   0   0  

1:  0   1   2   3   4   5   6   7   8   9  

2:  0   2   4   6   8  10  12  14  16  18  

3:  0   3   6   9  12  15  18  21  24  27  

4:  0   4   8  12  16  20  24  28  32  36  

5:  0   5  10  15  20  25  30  35  40  45  

6:  0   6  12  18  24  30  36  42  48  54  

7:  0   7  14  21  28  35  42  49  56  63  

8:  0   8  16  24  32  40  48  56  64  72  

9:  0   9  18  27  36  45  54  63  72  81 

'''           
    
