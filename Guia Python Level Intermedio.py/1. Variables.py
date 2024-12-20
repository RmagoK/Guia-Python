"""
1. Variables 2.0
Definición: Se refiere a la gestión avanzada y el uso de variables, incluyendo tipos de datos más complejos.
Importancia: Permite un mejor manejo de los datos y la creación de estructuras más eficientes en los programas.
Uso: Incluye el uso de variables globales y locales, así como la conversión de tipos de datos.

"""
#Desempaquetado

#creando una tupla
datos_en_tupla = ("Rosheed", "Mago", 22)
datos_en_lista = ["Rosheed", "Mago", 22] 
#el desempaquetado
nombre,apellido, edad = datos_en_lista

#mostrando resultado
print(apellido)

#creando tuplas con tuples

tuplaas = tuple(["dato1","dato2","dato3"])

print(tuplaas)

#creando una tupla sin parentesis
tuplaz = "dato1","dato2","dato3"

#creando una tupla sin parentesis de un solo dato
tuplaz = "dato1",
print(tuplaz)

# SETS (Conjuntos)
#creando un conjunto con sets
conjunto = set(["dato1", "dato2"])
print(conjunto)

conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

#TEORIA DE CONJUNTOS
#agregando un conjunto dentro de otro conjunto
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto con #otra forma de verificarlo
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)



print(resultado)
