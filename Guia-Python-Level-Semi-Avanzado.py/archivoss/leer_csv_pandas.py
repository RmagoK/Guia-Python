import pandas as pd

#Usando la funcion read para leer el archivo csv

df = pd.read_csv("Guia-Python-Level-Semi-Avanzado.py/archivoss/prueba.csv",)
df2 = pd.read_csv("Guia-Python-Level-Semi-Avanzado.py/archivoss/prueba.csv",)
#ordenando dataframe por la edad
df_ordenado = df.sort_values("age")

#ordenando de forma descendente

df_descendente = df.sort_values("age",ascending=False)

#NOTA SOBRE : , permite escoger en un array de un punto a otro o todos los elementos


#concatenando los 2 dataframe

df_concatenado = pd.concat([df,df2])


#accediendo a las primeros 3 filas con head()
primer_fila = df.head(2)

#accediendo a las ultimas 3 filas con tail
ultima_fila = df.tail(3)


#accediendo a la cantidad de filas y columnas con shape
filas_y_columnas_totales = df.shape

#desepaquetando la cantidad de filas y columnas
filas_totales,columnas_totales = df.shape

#obeteniendo data estadistica del dataframe
df_info = df.describe()

#accediendo a un elemento especifico con loc
elemento_especifico_loc = df.loc[1,"name"]

#accediendo desde el indice especifico con iloc
elemento_especifico_iloc = df.iloc[2,1]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con iloc
fila_3 = df.loc[1,:]

#accediendo a filas con edad mayor a 24

fila_mayor = df.loc[df["age"]>= 24,:]
print(fila_mayor)
