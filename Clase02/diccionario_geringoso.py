lista = ['banana', 'manzana', 'mandarina']

def geringoso(palabra):
    cadena = palabra
    capadepenapa = ''
    for c in cadena:   
        if c in ('a', 'e', 'i', 'o', 'u'):           
            capadepenapa = capadepenapa + c + 'p' + c                
        else:
            capadepenapa = capadepenapa + c            
    return capadepenapa


def crear_diccionario(lista):
    diccionario_geringoso = []
    for palabra in lista:
        entrada = (palabra , geringoso(palabra))
        diccionario_geringoso.append(entrada)    
    return dict(diccionario_geringoso)  


print(crear_diccionario(lista))

'''
OUTPUT:

{'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}

'''










