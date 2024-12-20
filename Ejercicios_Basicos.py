
"Ejercicio 12: Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total."

barras = int(input("Introduce el numero de barras vendidas que no son frescas: "))
precio = 3.49
Descuento = 0.6
coste = barras * precio * (1 - Descuento)
calculo_barra_fresca = str(precio)
calculo_barra_Vieja = str(Descuento*100)
calculo_Coste_Final = str(round(coste, 2))

print (f"El coste de una barra fresca es: {calculo_barra_fresca} $")
print(f"El descuento sobre una barra no fresca es: {calculo_barra_Vieja} $")
print(f"el coste final a pagar es: {calculo_Coste_Final} $")


"Ejercicio 10: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."

Peso_Payasos = 112
Peso_Muñeca = 75 

Ventas_de_Payasos = int(input (" Introduce en numero de payasos a enviar: "))
Ventas_de_muñecas = int(input(" Introduce en numero de muñecas a enviar: "))

Peso_Total_Payasos = str(float(Peso_Payasos * Ventas_de_Payasos))

Peso_Total_Muñecas = str(float(Peso_Muñeca * Ventas_de_muñecas)) 

Peso_Final = str(float(Peso_Payasos * Ventas_de_Payasos) + (Peso_Muñeca * Ventas_de_muñecas))

print (f"El peso total del paquete enviado de payasos pesa: {Peso_Total_Payasos} gramos") 
print (f"El peso total del paquete enviado de muñecas pesa: {Peso_Total_Muñecas} gramos") 
print (f"Peso Total de ambos envios: {Peso_Final}")


"Ejercicio 9: Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión."

Cantidad = float(input("¿Cuanto desea invertir de su capital?: "))
Interes = float(input("¿Cuanto desea invertir de forma anual? "))
Años = int(input("¿Por cuantos años? "))
formula_matematica = (str(round(Cantidad * (Interes / 100 + 1)** Años, 2 )))

print(f"El capital obtenido por la inversión es: {formula_matematica}")

"Ejercicio 11: Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales."

Inversion = float(input("Deposite Cantidad: "))
Intereses = 0.04

Balance1 = Inversion * (1 + Intereses)
Redondear_1 =  (str(round(Balance1, 2)))
print (f"Balance tras el primer año: {Redondear_1}")

Balance2 = Balance1 * (1 + Intereses)
Redondear_2 =  (str(round(Balance2, 2)))
print (f"Balance tras el segundo año:{Redondear_2} ")  

Balance3 = Balance2 * (1 + Intereses)
Redondear_3 =  (str(round(Balance3, 2)))
print (f"Balance tras el tercer año: {Redondear_3} ")