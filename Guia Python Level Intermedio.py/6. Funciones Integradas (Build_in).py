# Funciones Integradas

"""
Definición: Son funciones predefinidas que están disponibles en Python sin necesidad de importar bibliotecas externas.
Importancia: Proporcionan funcionalidades comunes que simplifican la programación.
Uso: Ejemplos incluyen:
len(): Devuelve la longitud de una colección.
max(): Devuelve el valor máximo de una colección.
"""
#Encontrando el numero mayor de una lista con la funcion max

lista = {11,21,34,42,65}
Numero_mas_alto = max(lista)
print (Numero_mas_alto)

#Encontrando el numero menor de una lista con la funcion min

lista = {11,21,34,42,65}
Numero_mas_bajo = min(lista)
print (Numero_mas_bajo)

#Rendondeamos un numero con la funcion round

numero = round(99.99999999, 2)
print (numero)

#la funcion bool retorna false ---> 0, false, vacio, none | True ---> distinto a 0, True, Cadena, datos no vacios

Resultado_bool = bool(0)
print (Resultado_bool)

#Retona True si todos los valores son verdaderos

resultado_all = all([13131,True, "veinte [59]"])
print (resultado_all)

#suma todos los valores de un iterable

suma_iterables = sum(lista)
print (suma_iterables)

