# Creando Funciones Propias
"""
Definición: Se refiere a la creación de funciones personalizadas para encapsular bloques de código reutilizables.
Importancia: Mejora la modularidad y la legibilidad del código.
Uso: Ejemplo de una función propia:
def saludar(nombre):
    return f"Hola, {nombre}!"
"""

#creando una funcion simple
def saludar():
    print ("Hello, !Como estas!")

#Ejecutando la funcion simple

saludar()

#Creando una funcion con parametros (una variable)

def saludando(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "Reina"

    elif (sexo == "hombre"):
        adjetivo = "lider"

    else:
        adjetivo = "amor"
    
    print (f"Hola {nombre}, mi {adjetivo}, espero que estes bien")

    
saludando("Rosheed","hombre")
saludando("Emperatriz","muJeR")
saludando("Carlos","no BInarIo")

#Creando una funcion que me retorne valores

# Se define una función llamada crear_contrasena_random que recibe un argumento llamado num.
def crear_contrasena_random(num):

# Se crea una variable llamada chars que contiene un conjunto de caracteres alfabéticos.
    
    chars= "abcdefghij"
    #Se convierte el número num a una cadena de texto y se guarda en la variable numero_entero.
    
    numero_entero = str(num)
    #Se extrae el primer dígito del número original (numero_entero) y se convierte a un entero, almacenándolo nuevamente en la variable num.
    
    num = int(numero_entero [0])
    # Se calculan tres índices (c1, c2, c3) utilizando el valor del primer dígito del número.
    c1 = num -2
    c2 = num
    c3 = num -5

    """
    Se construye la contraseña utilizando la interpolación de cadenas (f-strings):
    Se seleccionan los caracteres de la cadena chars según los índices c1, c2 y c3.
    Se duplica el número original convertido a cadena (numero_entero * 2).
     """
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{numero_entero *2}"
    
    
    return (contrasena)

# Se llama a la función crear_contrasena_random con el argumento 98, lo que inicia la ejecución del código.
password = crear_contrasena_random(98)
valor = (f"Su  nueva contrasena es: {password}")
print (valor)