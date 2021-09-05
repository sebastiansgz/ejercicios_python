import csv
import sys
from collections import Counter
from pprint import pprint


if sys.argv == 2:
    archivo_arboles = sys.argv[1]
else:
    archivo_arboles = '../Data/arbolado-en-espacios-verdes.csv'


def leer_parque(archivo_arboles, parque):                  # 3.18 Devuelve una lista con diccionarios. [{'header':valor, 'header':valor,...},{'header':valor,'header':valor,...}] 
    filas_arboles =[]
    lista_arboles =[]
    with open(archivo_arboles, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for info_arbol in rows:
            dict_arbol = dict(zip(headers,info_arbol))
            filas_arboles.append(dict_arbol)
        for dict_arbol in filas_arboles:
            if dict_arbol['espacio_ve'] == parque:
                lista_arboles.append(dict_arbol)
    # pprint(lista_arboles)
    # print(f'Hay {len(lista_arboles)} en el espacio verde {parque}')
    return lista_arboles
        
        
def especies(lista_arboles):                                       # 3.19 Devuelve un conjunto con las especies.
    lista_especies =[]
    for arbol in lista_arboles:
        lista_especies.append(arbol['nombre_com'])
    especies = set(lista_especies)
    # pprint(especies)
    return especies


def contar_ejemplares(lista_arboles):                              # 3.20 Devuelve un diccionario con pares: 'especie' : cant.
    cant_por_especie = Counter()
    lista_pares =[]
    for arbol in lista_arboles:
        cant_por_especie[arbol['nombre_com']] += 1
    for especie in cant_por_especie:
        par = (especie, cant_por_especie[especie])
        lista_pares.append(par)
    # print(dict(lista_pares))
    cantidad_ejemplares = (dict(lista_pares)) 
    return cantidad_ejemplares
    

def obtener_alturas(lista_arboles, especie):                      # 3.21 Devuelve una lista con las alturas.
    lista_alturas = []             
    for arbol in lista_arboles:
            if arbol['nombre_com'] == especie:
                lista_alturas.append(float(arbol['altura_tot']))
    return lista_alturas 
   

def obtener_inclinaciones(lista_arboles, especie):                # 3.22 Duvuelve una lista con las inclinaciones.
    lista_inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista_inclinaciones.append(int(arbol['inclinacio']))
    return lista_inclinaciones


def especimen_mas_inclinado(lista_arboles):
    pares = []
    conjunto = especies(lista_arboles)
    for especie in conjunto:
       lista_inclinaciones = obtener_inclinaciones(lista_arboles, especie)
       par = (max(lista_inclinaciones), especie)
       pares.append(par)
    mas_inclinado = max(pares)
    return mas_inclinado
    


def especie_promedio_mas_inclinada(lista_arboles):
    promedios = []
    conjunto = especies(lista_arboles)
    for especie in conjunto:
       lista_inclinaciones = obtener_inclinaciones(lista_arboles, especie)
       par = (sum(tuple(lista_inclinaciones))/len(lista_inclinaciones), especie)
       promedios.append(par)
    mas_inclinado_promedio = max(promedios)
    return mas_inclinado_promedio


def leer_parque2(archivo_arboles):
    with open(archivo_arboles, 'rt') as file:
        rows = csv.reader(file)
        headers =  next(rows)
        row = next(rows)
        arboleda = [ dict(zip(headers,row)) for row in rows ]
    return arboleda






parques =["GENERAL PAZ","ANDES, LOS","CENTENARIO"]

#-------------------------- 3.20 MÁS COMÚN ----------------------------------------------
print('3.20 MÁS COMÚN\n')
for parque in parques:
    lista_arboles = leer_parque(archivo_arboles, parque)
    cantidad = contar_ejemplares(lista_arboles)
    mas_comun = Counter(cantidad).most_common(5)
    print(f'Las cinco especies más comunes del parque {parque} son: {mas_comun}') 

#------------------ 3.21 ALTURA ----------------------------------------------------------
print('\n \n3.21 ALTURA\n')

for parque in parques:
    lista_arboles = leer_parque(archivo_arboles, parque)
    lista_alturas = obtener_alturas(lista_arboles, 'Jacarandá')
    altura_promedio = print(f'La altura promedio del Jacarandá en {parque} es: {sum(tuple(lista_alturas))/ len(lista_alturas):.2f}')
    altura_max = print(f'La altura maxima del Jacarandá en {parque} es: {max(tuple(lista_alturas))}m\n')

#-----------------3.23 INCLINACIÓN --------------------------------------------------------
print('\n \n3.22 INCLINACIÓN\n')

for parque in parques:
    lista_arboles = leer_parque(archivo_arboles, parque)
    mas_inclinado = especimen_mas_inclinado(lista_arboles)
    print(f'En el parque {parque} el árbol más inclinado pertenece a la especie {mas_inclinado[1]} y tiene una inclinación de: {mas_inclinado[0]}°')
    
#-----------------3.24 INCLINACIÓN PROMEDIO  --------------------------------------------------------
print('\n \n3.24 INCLINACIÓN PROMEDIO \n')

for parque in parques:
    lista_arboles = leer_parque(archivo_arboles, parque)
    mas_inclinado_promedio = especie_promedio_mas_inclinada(lista_arboles)
    print(f'En el parque {parque} la especie más inclinada en promedio es {mas_inclinado_promedio[1]} con una inclinación promedio de: {mas_inclinado_promedio[0]}°')

#--------------4.16 ALTURAS JACARANDÁ LIST COMPRESSION------------------------------------------------
arboleda =  leer_parque2(archivo_arboles)

H = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    
 #-------------4.17 ALTURAS Y DIAMETROS---------------------------------------------------------------

H_d = [(float(arbol['diametro']),float(arbol['altura_tot'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
   



    


  


