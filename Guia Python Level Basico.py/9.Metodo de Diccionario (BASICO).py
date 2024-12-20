"""
9. Métodos de Diccionarios
Definición: Son funciones específicas que se utilizan para manipular diccionarios, que son estructuras de datos que almacenan pares clave-valor.
Importancia: Permiten acceder y modificar datos de manera eficiente y organizada.
Uso: Ejemplos de métodos incluyen:
.keys(): Devuelve una vista de todas las claves en el diccionario.
.values(): Devuelve una vista de todos los valores en el diccionario.
.get(key): Devuelve el valor asociado a una clave específica.
"""

#keys devuelve las claves (tambien nos sirve para iterar) nos devuelve un ejemplo dict_item
diccionario = {
    "nombre": "Rosheed",
    "apellido":"Kassie",
    "Edad": 20
}

claves = diccionario.keys()
print(claves)

#obteniendo un objeto con get (no me lanza una excepción y si no encunetra nada el programa continua )
diccionario = {
    "nombre": "Rosheed",
    "apellido":"Kassie",
    "Edad": 20
}

claves = diccionario.get("Hola mi loco")
print("El programa continua")
print(claves)

# clear elimina todo del diccionario

diccionario.clear()


# pop elimina un elemento del diccionario
diccionario.pop("nombre")


# item para iterar el dict (obteniendo un elemento dict_item iterable)
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

#2:39:23 - Entrada de datos (inputs)
#pedirle un dato al usuario
nombre = input("master, dame tu nombre: ")
print(nombre)

resultado = int(nombre)*2
print(resultado)

resultado = float(nombre)*2
print(resultado)