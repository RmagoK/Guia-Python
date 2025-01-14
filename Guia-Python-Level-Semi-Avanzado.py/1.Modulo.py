#1. Módulos Definición: Son archivos que contienen definiciones y declaraciones de Python. Un módulo permite organizar el código en partes reutilizables.
#Importancia: Facilita la modularización del código, promoviendo la reutilización y el mantenimiento.
#Uso: Se utiliza la palabra clave import para incluir módulos, por ejemplo:
#import math
#print(math.sqrt(16))  # Salida: 4.0

#Importando un modulo y asignandole un nombre "M_Saludar"
#import Modulo_saludar as M_Saludar

#creando una variable que use el modulo y su respectiva funcion (.saludar) mientras asignamos el nombre de usuario
#saludando = M_Saludar.saludar("Emperatriz")

#imprimimos la variable salundando
#print (saludando)

# Importamos el modulo, modulo_saludar y usamos sus dos funciones el cual usando "as" le asignamos otro nombre al metodo
from funciones_buenas.Modulo_saludar import saludar as saludar_Normal, saludar_raro as saludo_rarisimo

#creamos dos variables con las respectivas funciones y usuarios
saludando = saludar_Normal("Emperatriz")
saludarraro = saludo_rarisimo("Rosheed")

# imprimimos
print (saludando)
print (saludarraro)

#para ver las propiedades y metodos del namespace
print(dir(saludar_Normal))

print(__name__)
