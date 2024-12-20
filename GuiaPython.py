
"""""
                                        --------  FUNDAMENTOS  --------

1. Datos Simples

Definición: Son los tipos de datos más básicos en Python, como enteros, flotantes, cadenas y booleanos.
Importancia: Permiten almacenar y manipular información fundamental de manera eficiente.
Uso: Se utilizan en cálculos, operaciones de texto y decisiones lógicas.




2. Variables
Definición: Son espacios en la memoria que se utilizan para almacenar datos y permiten su manipulación durante la ejecución del programa.
Importancia: Facilitan la reutilización y el manejo de datos en el código.
Uso: Se declaran asignando un valor, por ejemplo: x = 10.




3. Datos Compuestos
Definición: Estructuras que permiten almacenar múltiples valores en una sola variable, como listas, tuplas y diccionarios.
Importancia: Permiten manejar colecciones de datos de manera organizada y estructurada.
Uso: Se utilizan para agrupar datos relacionados, como una lista de nombres: nombres = ["Ana", "Luis", "Pedro"].




4. Operadores Aritméticos
Definición: Son símbolos que realizan operaciones matemáticas en los operandos, como suma (+), resta (-), multiplicación (*), división (/), etc.
Importancia: Permiten realizar cálculos y manipular datos numéricos de manera efectiva.
Uso: Se utilizan en expresiones matemáticas, por ejemplo: resultado = a + b.





5. Operadores de Comparación
Definición: Son operadores que comparan dos valores y devuelven un valor booleano (True o False), como igual (==), diferente (!=), mayor que (>), etc.
Importancia: Son esenciales para tomar decisiones en el flujo del programa.
Uso: Se utilizan en condicionales, por ejemplo: if a > b:.






6. Condicionales
Definición: Estructuras de control que permiten ejecutar diferentes bloques de código según si una condición es verdadera o falsa.
Importancia: Permiten la toma de decisiones en el código, haciendo que el programa sea dinámico.
Uso: Se utilizan con if, elif y else, por ejemplo:
if x > 10:
    print("Mayor que 10")
else:
    print("Menor o igual a 10")
    
    
    
    
    
7. Operadores Lógicos
Definición: Operadores que combinan condiciones booleanas, como and, or y not.
Importancia: Permiten crear expresiones lógicas más complejas y tomar decisiones basadas en múltiples condiciones.
Uso: Se utilizan en condicionales, por ejemplo: if x > 10 and y < 5:.






                                    ------- SECCIÓN BÁSICA -------

1. Métodos de Cadenas
Definición: Son funciones predefinidas que se pueden aplicar a objetos de tipo cadena (strings) para manipular texto.
Importancia: Permiten realizar operaciones comunes en cadenas como buscar, modificar y formatear texto de manera sencilla.
Uso: Ejemplos de métodos incluyen:
.lower(): Convierte la cadena a minúsculas.
.upper(): Convierte la cadena a mayúsculas.
.replace(old, new): Reemplaza partes de la cadena.





2. Métodos de Listas
Definición: Son funciones que se aplican a listas para realizar diversas operaciones como añadir, eliminar o modificar elementos.
Importancia: Facilitan la manipulación de colecciones de datos de manera eficiente.
Uso: Ejemplos de métodos incluyen:
.append(item): Añade un elemento al final de la lista.
.remove(item): Elimina el primer elemento que coincide con el valor.
.sort(): Ordena los elementos de la lista.





3. Métodos de Diccionarios
Definición: Son funciones específicas que se utilizan para manipular diccionarios, que son estructuras de datos que almacenan pares clave-valor.
Importancia: Permiten acceder y modificar datos de manera eficiente y organizada.
Uso: Ejemplos de métodos incluyen:
.keys(): Devuelve una vista de todas las claves en el diccionario.
.values(): Devuelve una vista de todos los valores en el diccionario.
.get(key): Devuelve el valor asociado a una clave específica.





4. Entrada de Datos (Inputs)
Definición: Es el proceso de recoger información del usuario a través de la función input().
Importancia: Permite a los programas interactuar con los usuarios, haciendo que sean más dinámicos y personalizados.
Uso: Se utiliza para solicitar datos, por ejemplo:
nombre = input("Ingresa tu nombre: ")







5. Ejercicios Prácticos 1
Definición: Son actividades o problemas diseñados para aplicar los conceptos aprendidos en programación.
Importancia: Fortalecen la comprensión y la habilidad de resolver problemas mediante la práctica.
Uso: Consisten en tareas como crear funciones, manipular listas o cadenas, o implementar lógica condicional.




                              ------ SECCIÓN INTERMEDIA -------

1. Variables 2.0
Definición: Se refiere a la gestión avanzada y el uso de variables, incluyendo tipos de datos más complejos.
Importancia: Permite un mejor manejo de los datos y la creación de estructuras más eficientes en los programas.
Uso: Incluye el uso de variables globales y locales, así como la conversión de tipos de datos.




2. Diccionarios 2.0
Definición: Aborda el uso avanzado de diccionarios, como la manipulación de diccionarios anidados y comprensión de diccionarios.
Importancia: Mejora la capacidad para almacenar y organizar datos complejos de manera eficiente.
Uso: Ejemplos incluyen:
Creación de diccionarios dentro de diccionarios.
Uso de comprensión de diccionarios para crear nuevos diccionarios de manera concisa.





3. Bucle For
Definición: Es una estructura de control que permite iterar sobre una secuencia (como listas, tuplas o cadenas).
Importancia: Facilita la ejecución de un bloque de código repetidamente para cada elemento en una colección.
Uso: Ejemplo de un bucle for:
for i in range(5):
    print(i)
    
    
    
    
    
4. Bucle While
Definición: Es una estructura de control que repite un bloque de código mientras una condición sea verdadera.
Importancia: Permite crear bucles que pueden continuar indefinidamente hasta que se cumpla una condición de salida.
Uso: Ejemplo de un bucle while:
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    
    
    
    
    
5. Funciones Integradas
Definición: Son funciones predefinidas que están disponibles en Python sin necesidad de importar bibliotecas externas.
Importancia: Proporcionan funcionalidades comunes que simplifican la programación.
Uso: Ejemplos incluyen:
len(): Devuelve la longitud de una colección.
max(): Devuelve el valor máximo de una colección.





6. Creando Funciones Propias
Definición: Se refiere a la creación de funciones personalizadas para encapsular bloques de código reutilizables.
Importancia: Mejora la modularidad y la legibilidad del código.
Uso: Ejemplo de una función propia:
def saludar(nombre):
    return f"Hola, {nombre}!"
    
    
    
    
    
    
7. Funciones Lambda
Definición: Son funciones anónimas y pequeñas que se definen usando la palabra clave lambda.
Importancia: Permiten crear funciones rápidas y simples sin necesidad de definirlas formalmente.
Uso: Ejemplo de una función lambda:
suma = lambda x, y: x + y
print(suma(2, 3))  # Salida: 5





8. Ejercicios Prácticos 2
Definición: Son ejercicios diseñados para aplicar los conceptos aprendidos en la programación de Python.
Importancia: Refuerzan el aprendizaje a través de la práctica y la resolución de problemas.
Uso: Consisten en actividades como implementar bucles, crear funciones y trabajar con diccionarios.

                                ------- SECCIÓN SEMI-AVANZADA -------

1. Módulos
Definición: Son archivos que contienen definiciones y declaraciones de Python. Un módulo permite organizar el código en partes reutilizables.
Importancia: Facilita la modularización del código, promoviendo la reutilización y el mantenimiento.
Uso: Se utiliza la palabra clave import para incluir módulos, por ejemplo:
import math
print(math.sqrt(16))  # Salida: 4.0





2. Enrutamiento de Módulos
Definición: Se refiere a la forma en que se importan y utilizan módulos desde diferentes ubicaciones dentro de un proyecto.
Importancia: Permite organizar el código de manera efectiva y acceder a funcionalidades específicas de diferentes módulos.
Uso: Ejemplo de enrutamiento:
from paquete import modulo







3. Paquetes
Definición: Son colecciones de módulos organizados en directorios que permiten agrupar funcionalidades relacionadas.
Importancia: Facilitan la organización de proyectos más grandes y complejos, permitiendo una estructura jerárquica.
Uso: Se crea un paquete mediante un directorio que contiene un archivo __init__.py.





4. Archivos TXT
Definición: Son archivos de texto plano utilizados para almacenar información de manera sencilla.
Importancia: Son fáciles de crear y manipular, y se utilizan comúnmente para almacenamiento de datos.
Uso: Para leer y escribir en archivos TXT, se utilizan las funciones open(), read(), y write(), por ejemplo:
with open('archivo.txt', 'w') as f:
    f.write('Hola, mundo!')
    
    
    
    
    
5. Archivos CSV
Definición: Son archivos de valores separados por comas, utilizados para almacenar datos tabulares.
Importancia: Permiten el intercambio de datos entre programas que no pueden leer nativamente los mismos formatos de archivo.
Uso: Se pueden manejar con el módulo csv, por ejemplo:
import csv
with open('archivo.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Nombre', 'Edad'])
    writer.writerow(['Alice', 30])
    
    
    
    
    
6. Trabajando con Archivos
Definición: Se refiere a la manipulación de archivos en Python, incluyendo la lectura, escritura y cierre adecuado de archivos.
Importancia: Es fundamental para la persistencia de datos y la interacción con el sistema de archivos.
Uso: Incluye el manejo de excepciones para asegurar que los archivos se manejen correctamente.





7. Trabajando con Gráficos
Definición: Se refiere a la visualización de datos en forma gráfica utilizando bibliotecas de Python.
Importancia: Facilita la interpretación de datos complejos y la presentación de resultados de manera visual.
Uso: Bibliotecas como matplotlib o seaborn son comúnmente utilizadas para crear gráficos, por ejemplo:
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()



------- SECCIÓN AVANZADA -------

1. Excepciones
Definición: Son errores que ocurren durante la ejecución de un programa, interrumpiendo su flujo normal.
Importancia: Permiten manejar errores de manera controlada, mejorando la robustez y estabilidad del programa.
Uso: Se utilizan bloques try, except, finally para manejar excepciones. Ejemplo:
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero.")
    
    
    
    
    
    
2. Expresiones Regulares
Definición: Son secuencias de caracteres que forman un patrón de búsqueda, utilizado para realizar coincidencias en cadenas de texto.
Importancia: Son herramientas poderosas para la validación, búsqueda y manipulación de texto.
Uso: Se utilizan con el módulo re. Ejemplo de uso básico:
import re
patron = r'\d+'  # Busca uno o más dígitos
coincidencias = re.findall(patron, 'Hay 12 manzanas y 5 peras.')
print(coincidencias)  # Salida: ['12', '5']







3. Analizando Expresiones Regulares
Definición: Implica descomponer y entender patrones de expresiones regulares para aplicar correctamente en diferentes escenarios.
Importancia: Permite ajustar los patrones para obtener coincidencias específicas y resolver problemas complejos de búsqueda.
Uso: Puede incluir la explicación de componentes de una expresión regular, como:
\d: Coincide con cualquier dígito.
\w: Coincide con cualquier carácter alfanumérico.
.: Coincide con cualquier carácter excepto el salto de línea.





4. Ejercicio de Expresiones Regulares
Definición: Se refiere a la práctica de aplicar expresiones regulares en problemas concretos.
Importancia: Refuerza el aprendizaje mediante la práctica, ayudando a entender mejor su funcionamiento.
Uso: Puede incluir tareas como validar correos electrónicos, extraer números de un texto o encontrar patrones específicos. Ejemplo de un ejercicio simple:
# Validar un correo electrónico
correo = 'ejemplo@dominio.com'
patron_correo = r'^[\w\.-]+@[\w\.-]+$'
if re.match(patron_correo, correo):
    print("Correo válido.")
else:
    print("Correo inválido.")


"""