
# Funciones Lambda

"""
Definición: Son funciones anónimas y pequeñas que se definen usando la palabra clave lambda.
Importancia: Permiten crear funciones rápidas y simples sin necesidad de definirlas formalmente.
Uso: Ejemplo de una función lambda:
suma = lambda x, y: x + y
print(suma(2, 3))  # Salida: 5
"""

numeros= [1,2,3,4,5,6,7,8,9,10]

#creando funcion si un numero es par
#def es_par (num):
 #   if (num%2 == 0):
 #       return True
    
#usando filter con una funcion comun

#numero_par = filter(es_par, numeros)

#print (list (numero_par))

#creando la misma funcion pero usando lambda

numero_par = filter(lambda numero : numero%2 == 0, numeros)

print (list (numero_par))

#creando una funcion lambda que multiplica x2


multiplicar_por_2 = lambda x : x*2

#print (multiplicar_por_2 (5))