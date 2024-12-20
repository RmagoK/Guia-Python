
#Bucle For

"""
Definición: Es una estructura de control que permite iterar sobre una secuencia (como listas, tuplas o cadenas).
Importancia: Facilita la ejecución de un bloque de código repetidamente para cada elemento en una colección.
Uso: Ejemplo de un bucle for:
for i in range(5):
    print(i)
"""

#recorriendo la lista animales

animales = {"gato", "perro", "loro", "cocodrilo"}
numeros = {1,2,3,4}

for animal in animales:
    print(f"ahora la variable animal es igual: {animal}")

#recorriendo la lista numeros y multiplicando cada valor * 10 
for numero in numeros:
    resultado = numero*10
    print(resultado)

#iterar 2 listas del mismo tamaño y al mismo tiempo
for numero, animal in zip (animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
#forma no optima de recorrer una lista  (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros)
    
#forma correcta de recorrer una lista con su indice: 
for num in enumerate (numeros):
    indice = num[0]
    valor = num [1]
    print(f"el indice es: {indice} y el valor es: {valor}")

#Desempaquetar Tupla en un Bucle for (mejor forma)
numeros = [(0, "cero"), (1, "uno",), (2,"dos")]
for num, i in enumerate(numeros):
    index,valor = i
    print(f"El indice es: {num} y el valor es: {valor}")

#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo blucle, el valor actual: {numero}")
else:
    print("el bucle termino")

#todo lo anterior funciona exactamente para tuplas/listas

#Iterar un diccionario

diccionario = {
    "Nombre":"Rosheed",
    "Apellido":"Kassie",
    "Edad": 22
    
}

#recorriendo diccionario obteniendo las claves
print(diccionario)

for key in diccionario.items():
    key
    print(f"el indice es {key}")

#recorriendo diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos [0]
    value = datos [1]
    print(f"el indice es {key} y el valor es: {value}")


#lista de alimentos
frutas = ["banana","manzana", "pera", "ciruela","granada"]
cadena = "Hola mi loco"
numeros = [2,5,8,10]
#evitando que se coma una granada con la sentencia continua
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"me voy a comer una: {fruta}")
    
#evitar que el bucle siga ejecutandose (el else no se ejecuta si hay un break antes)
for fruta in frutas:
    if fruta == "manzana":
        break
    print(f"me voy a comer una: {fruta}")
else:
    print("terminado")
    
#recorrer (iterar) una cadena de texto

for letra in cadena:
    print(letra)

#for en una sola linea de codigo
numeros_duplicados =list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
print(numeros_duplicados)

#otro metodo mas eficiente

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)