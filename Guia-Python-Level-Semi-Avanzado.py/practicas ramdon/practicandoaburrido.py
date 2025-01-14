
# crearemos una funcion el cual permita saludar a una persona retornamos el nombre para guardarlo
def saludar(name):
    return name

#Creamos una funcion para contar la cantidad de letras que posee la variable saludo utilizando el metodo len, nos permitira hacer el conteo de las palabras a ingresar en la variable saludo retornamos y guardamos los valores en cantidad

def Palabras(cantidad):
    cantidad = len(saludo)
    return cantidad

#creamos una funcion el cual asigna al nombre de la persona un sexo, cuyo sexo puede tener un adjetivo predeterminado por la funcion

def Hola(nombre,sexo):
    sexo = sexo.lower()

    if (sexo == "mujer"):
        adjetivo = "preciosa"
    elif (sexo == "hombre"):
        adjetivo = "guapo"
    else:
        adjetivo = "una vaina rara"
    print(f"hola, {nombre}, veo que eres {adjetivo}")

def es_palindromo():
    #solicitamos al usuario un texto
    usuario = input("Agrega una palabra: ")

    #eliminamos el espacio y lo convertimos a minuscula
    usuario = usuario.replace(" ", "").lower()

    #detectamos si es palindromo
    if usuario == usuario[::-1]:
        print(f"La cadena de texto {usuario}, es palindromo")
    else:
        print(f"La cadena de texto {usuario}, no es palindromo")

es_palindromo()

#llamamos la funcion hola, y le agregamos los nombres y los sexos de los usuarios
Hola("Rosheed","hombre")
Hola("Emperatriz","Mujer")
Hola("Carlos","gei")





#input almacenara en formato string la palabra que ingresara el usuario
saludo = input (str("Por favor, ingrese un nombre: "))

#Variable saludando, el cual contiene la funcion "saludar" con el nombre a llamar e imprimimos agregando un f string
saludando = saludar(saludo)
print (f"Hola, {saludando}, como estas")

#llamamos la funcion Palabras el cual contara las palabras de la variable saludo e imprimimos la variable cantidad
cantidad = Palabras(saludo)
print (f"La cantidad de palabras que tienes en total son: {cantidad}")
    


