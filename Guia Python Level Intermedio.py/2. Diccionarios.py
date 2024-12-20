
#Diccionarios 2.0

"""
Definición: Aborda el uso avanzado de diccionarios, como la manipulación de diccionarios anidados y comprensión de diccionarios.
Importancia: Mejora la capacidad para almacenar y organizar datos complejos de manera eficiente.
Uso: Ejemplos incluyen:                                     
Creación de diccionarios dentro de diccionarios.
Uso de comprensión de diccionarios para crear nuevos diccionarios de manera concisa.
"""

#creando diccionarios con dic()
diccionario =dict(nombre = "Rosheed", apellido = "Mago")
print(diccionario)


#las listas no pueden ser claves y usamos fronzenset para meter conjuntos
diccionario = {frozenset(["Rosheed","rancio",]):"jajaja"}
print(diccionario)

#creando un diccionario con frontkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando un diccionario con frontkeys() cambiando el valor por defecto: "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"no se")
print(diccionario)

