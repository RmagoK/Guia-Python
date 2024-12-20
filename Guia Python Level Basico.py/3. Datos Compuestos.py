#56:22 - Datos compuestos

"""
Definición: Estructuras que permiten almacenar múltiples valores en una sola variable, como listas, tuplas y diccionarios.
Importancia: Permiten manejar colecciones de datos de manera organizada y estructurada.
Uso: Se utilizan para agrupar datos relacionados, como una lista de nombres: nombres = ["Ana", "Luis", "Pedro"].
"""


#Matriz Lista
Lista = ["Rosheed Mago","Casado", True, 1.80]
(Lista [0]) = "MODIFICADO"
print (Lista [0]) 

#Matriz Tuplas
Tupla = ("Rosheed Mago", "Casado", False, 1.80)
# (Tupla [0]) = "MODIFICADO" NO SE PUEDE MODIFICAR UNA TUPLA
print (Tupla [0])

#Conjunto (SET) no accede a elementos por indice, no almacena elementos duplicados
Conjunto = {"Rosheed Mago", "Casado", False, 1.80, "si se repite la palabra no aparece = muestra:", False}
Conjunto = {"Se puede redefinir completo el Conjunto pero no individual"}
print (Conjunto)

#Diccionario (dict) (La estructura es key : value y separamos con ",")

Diccionario = {
    "Nombre": "Rosheed",
    "apellido" : "Kassie",
    "Edad" : 22,
    "Se baña" : True
    
}
print (Diccionario ["Nombre"] + " Mago")