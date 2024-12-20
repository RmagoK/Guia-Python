"""
7. Operadores Lógicos

Definición: Operadores que combinan condiciones booleanas, como and, or y not.
Importancia: Permiten crear expresiones lógicas más complejas y tomar decisiones basadas en múltiples condiciones.
Uso: Se utilizan en condicionales, por ejemplo: if x > 10 and y < 5:
"""
#AND Con que ambas condiciones sean True 

Resultado1 = True & True #Me devuelve True
Resultado2 = False & True # Me devuelve Falso
Resultado3 = True & False # Me devuelve Falso
Resultado4 = False & False# Me devuelve Falso

#OR Con que alguna de las condiciones se cumpla es True, al contrario de AND
Resultado5 = True | True #Me devuelve True
Resultado6 = False | True # Me devuelve True
Resultado7 = True | False # Me devuelve True
Resultado8 = False | False# Me devuelve Falso


#NOT invierte True por False y viceversa
Resultado9 = not True#Me devuelve Falso
Resultado10 = not False#Me devuelve True
Resultado11 = not 2 >= 5 #Me devuelve Falso

print(Resultado11)