"""
8. Métodos de Cadenas
Definición: Son funciones predefinidas que se pueden aplicar a objetos de tipo cadena (strings) para manipular texto.
Importancia: Permiten realizar operaciones comunes en cadenas como buscar, modificar y formatear texto de manera sencilla.
Uso: Ejemplos de métodos incluyen:
.lower(): Convierte la cadena a minúsculas.
.upper(): Convierte la cadena a mayúsculas.
.replace(old, new): Reemplaza partes de la cadena.
"""
#1:46:08 - Métodos de cadenas

cadena1 = "hola soy Rosheed"
cadena2 = "Bienvenite"

#lista de algunos metodos:
resultado = dir(cadena1)


#convierten un valor:

#convierte a mayuscula
Mayuscul= cadena1.upper()

#convierte a minuscula
minusc = cadena1.lower()

#primera letra en mayuscula

primer_letra_mayuscula = cadena1.capitalize()
print (primer_letra_mayuscula)

#buscan un valor:

#buscamos una cadena en otra cadena, si no hay coincidencia, me devuelve -1
busqueda_find = cadena1.find("o")

#no aparece -1 pero si excepciones
busqueda_index = cadena1.index("D")

print(busqueda_find)

# Si es numerico, devolvemos True, si no, devolvemos False
es_numerico = cadena1.isnumeric()

#Si es alfanumerico devolvemos true, si no, devolvemos false
es_alfanumerico = cadena1.isalpha("AZ")


#contamos las coincidencias de una cadena  dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")
print(contar_coincidencias)

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)
print(contar_caracteres)

#Verificamos si una cadena empieza con una cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("H")
print(empieza_con)

#Verificamos si una cadena termina con una cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("H")
print(termina_con)

#Si el valor 1, se encuentra en lacadena original, reemplazar el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("la","lu")
print(cadena_nueva)

#ejemplo
#reemplaza un oedazo de la cadena dada por otra dada
cadena_nueva = cadena1.replace(","," ")
cadena_nueva2 = cadena_nueva.capitalize()
print(cadena_nueva2)

#separar cadenas con la cadena que le pasemos (crea una lista)
cadena_separada = cadena1.split(",")
print(cadena_separada)

#2:12:20 - Métodos de listas
#creando una lista con list()
lista = list(["Hola", "Rosheed", 34])

#devuelve la cantidad de elementos que tiene la lista
resultado = len(lista)
print(resultado)

#agregando un elemento a la lista
agregando_con_append = lista.append("JAJAJAJA")
print(lista)

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"Toma mana")
print(lista)

#agregando varios elementos a la lista
lista.extend([False, 2030])

#eliminando un elemento de la lista (por su indice), si se usa el -1 elimina el ultimo elemento
lista.pop(0)
print(lista)     

#removiendo un elemento de la lista por su valor
lista.remove("Toma mana")
print(lista) 

#Ordena de forma ascendente los elementos numericos y booleanos de la lista
lista.sort()

#invierte en forma descendente el orden de elementos de la lista
lista.sort(reverse=True)

print(lista)  

#inviertiendo los elementos de una lista
lista.reverse()

#Eliminando todos los elementos de la lista
lista.clear()

#Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(2030)