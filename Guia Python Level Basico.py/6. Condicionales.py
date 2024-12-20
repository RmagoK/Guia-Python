"""
6. Condicionales

Definición: Estructuras de control que permiten ejecutar diferentes bloques de código según si una condición es verdadera o falsa.
Importancia: Permiten la toma de decisiones en el código, haciendo que el programa sea dinámico.
Uso: Se utilizan con if, elif y else, por ejemplo:
if x > 10:
    print("Mayor que 10")
else:
    print("Menor o igual a 10")

"""
#1:26:59 - Condicionales

#if True: 
    #La accion se ejecuta
    
#if False:
    #La accion no se ejecuta
    
Edad = 18
if Edad <= 18:
    print("Es menor o igual a 18")
else:
    print("Es mayor a 18 años")

Base_de_datos_contraseña = "Rosheed123"
contraseña = "Rosheed123"
if Base_de_datos_contraseña == contraseña:
    print("Iniciando Sección...")
else:
    print("Contraseña Invalida")
    
Ingresos = 100
Gastos = 1

# if anidados y else if (elif)
if Ingresos > 400:
    if Gastos - Ingresos < 10:
        print("Estas en la pobreza")
    else:
        print("bajale a la gastadera, no hay rial")
    
elif Ingresos > 300:
    print("Puedes vivir algo comodo")
    
elif Ingresos > 100:
    print("solo te alcanza para luz y agua y comida")
    
elif Ingresos >= 50:
    print("ve ahorrando plata")
    
elif Ingresos >= 10:
    print("mi loco ta mos en crisis")
    
else:
    print("empieza a pelar las nalgas")