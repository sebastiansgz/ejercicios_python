frase = 'Todos somos programadores'  
palabras = frase.split()    # Creo uan list que contiene las palabras
sublist = []                                    # Necesito una lista vacia para llenarla después.
for palabra in palabras:                        # itero sobre cada elemepto de la lista, es decir, sobre cada palabra.
        if palabra.endswith('o'):               # pregunto por la terminacion masculino sigunlar.
            palabra_t = palabra[:-1] + 'e'      # Creo una nueva palabra que recorta la termanción del masc. sing. y le agrego "e"

        elif palabra.endswith('os'):            # Pregunto por la terminación masculino plural
             palabra_t = palabra[:-2] + 'es'    # Creo una nueva palabra que recorta la termanción del masc. plural y le agrego "es"
        else:
            palabra_t = palabra
        
        sublist.append(palabra_t)               # Agrego la nueva palabra a la lista  sublist
        
frase_t = ' '.join(sublist)                     # Convierto la lista en una string con los elementos unidos por un espacio ' '
print(frase_t)                                  

### OUTPUT: Todes somes programadores

