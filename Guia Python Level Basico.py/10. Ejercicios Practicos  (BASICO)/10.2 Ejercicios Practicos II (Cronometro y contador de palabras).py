
#Le pedimos al usuario que nos diga una frase (o varias)
frase =input("Decime algo master, y te calculo cuanto tardarias si tuvieras que decir ")

#creamos una lista con todas las palabras de la frase )se separan cda vez que haya un espacio en blanco
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde mas de 120 minutos le mandamos un mensaje
if cantidad_de_palabras > 120:
    print("Mira master, tampoco me cuentes tu vida")

#calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f"dijiste {cantidad_de_palabras} palabras, y tardaste {cantidad_de_palabras /2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras * 100 // 2 *1.3 / 100} segundos en decirlo")