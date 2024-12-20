#39:27 - Variables

"""
Definición: Son espacios en la memoria que se utilizan para almacenar datos y permiten su manipulación durante la ejecución del programa.
Importancia: Facilitan la reutilización y el manejo de datos en el código.
Uso: Se declaran asignando un valor, por ejemplo: x = 10.
"""

#Numero
a = 2
b = 3
c = a + b
numero = 10
numero += 5

#Palabras
Nombre = "Lucas"
print (Nombre)

#Concatenar con el simbolo +
Nombre = "Lucas"
Bienvenida = "Hola " + Nombre + " ¿Como estas?"

#Concatenar (mas recomendable) con f {string}

Bienvenido = "fHola {Nombre} ¿como estas?"

#Operadores de pertenencia (in / not in)

Nombre = True
Bienvenido_Pertenencia = "FHOLA {Nombre} ¿Como estas?"
print ("Hola" in Bienvenida)
print ("Hola" not in Bienvenida)
