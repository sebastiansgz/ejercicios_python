#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Semántica

#Comentario: Detecté 2 errores:
#   1. El programa estaba preparado sólo para encontrar la letra "a" minúscula. Arreglé esto usando el método lower() en la linea 16.
#   2. El programa no terminaba de evaluar cada elemento de la cadena asignada a  "expresion".
#      Al evaluar la primera letra si esta no es 'a' (como se espera segun la linea 21) devolvería False y saldría del loop while sin terminar de evaluar el resto de elementos de la cadena.

# Lo corregí usando un booleano 'is_there'.
# También coloqué incremento de la variable 'i' dentro del else, así sigue evaluando cada elemento de la cadena y al terminar sale del loop y devuelve el valor de is_there.
# Si la letra 'a' no se encuentra el valor de is_there nunca cambia y al salir del loop sigue siendo False. 
#    A continuación va el código corregido:

def tiene_a(expresion):
    expresion = expresion.lower()
    n = len(expresion)
    i = 0
    is_there = False
    while i < n:        
        if expresion[i] == 'a':
            is_there = True
            return is_there
        else: 
            i += 1
    return is_there    
        
        

tiene_a('UNSAM 2020')

#%%
#Ejercicio 3.2. Sintaxis

#Comentario: Los errores estaban en:
#   1. Faltaban los dos puntos ':' al final al definir la función tiene_a()
#   2. Al crear el while faltaban también los dos puntos al final.
#   3. En la condición if también falatabn los dos puntos al final y el operador correcto para igualdad es '=='
#   4. El programa estaba preparado sólo para detecatr minusculas lo solucioné con el metodo lower()
# #  tipo y estaba ubicado en TAL lugar.


def tiene_a(expresion):
    expresion = expresion.lower()
    n = len(expresion)
    i = 0
    while i < n :
        if expresion[i] == 'a':
            return True
        i += 1    
    return False


tiene_a('UNSAM 2020')

#%%
#Ejercicio 3.3. Tipos

#Comentario: El programa no estaba preparado para recibir otro tipo diferente de las strings. Ahora cualquier expresion se convierte a string para que el programa pueda ejecturarse, para esto usé str().

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno(1984)

# %%

#Ejercicio 3.4 Alcances

#Comentario: Es necesario el 'return' para que pueda devolvernos el resultdo después de haberse ejecutado la función.

def suma(a,b):
    return a + b
    

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
# %%

# Ejercicio 3.5 Pisando memoria

# Comentario:El error consiste en que dentro de for al escribir algo como  'registro[encabezado[0]]' estaría reasignando el valor de cada key que sea igual a registro[encabezado[0]]. Es decir que todas las keys que  sean iguales a 'nombre' van a tomar como valor el nombre de la fruta en cada iteración. Lo mismo ocurre con las otras keys 'cajones'  y 'precio'.
# por esto, al llegar a la ultima fila todas las keys toman como valor los valores de esta ultima fila de la iteración.
# Solucioné el problema creando cada diccionario dentro del for.
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
   
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {
                encabezado[0] : fila[0],
                encabezado[1] : int(fila[1]),
                encabezado[2] : float(fila[2])
                }
            camion.append(registro)
        return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
