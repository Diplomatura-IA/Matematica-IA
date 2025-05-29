import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
pd.set_option('display.max_rows', None)  # Mostrar todas las filas
pd.set_option('display.width', 1000)  # Aumentar el ancho de salida
pd.set_option('display.colheader_justify', 'center')  # Mejor alineación

data = pd.read_csv("Life Expectancy Data.csv")
# print(data.shape)
# print(data.head())
# output_file = "data_filtered_mypersonality.txt"
# data.to_csv(output_file, sep="\t", index=False)
# print(f"Datos guardados en {output_file}")

data2=data.query("Year == 2014")
# data2=data.query("Country == 'Argentina'")
data2=data2.query("GDP < 80000")
data2=data2.query("`percentage expenditure` != 0")
data2 = data2.loc[:,["Country","percentage expenditure","GDP"]]
print(data2.shape)
print(data2.head())


gasto = data2.loc[:,"percentage expenditure"]
pbi = data2.loc[:,"GDP"]
plt.scatter(pbi,gasto)
plt.show()


# PASO 1
# Transformar las variables "pbi" y "gasto" en los array de numpy "x" e "y" respectivamente.

# PASO 2
# Calcular los valores óptimos de las variables β1 y β0 siguiendo las fórmulas vistas en clase.
# Nota: recordá que el uso del broadcasting de numpy puede ayudarte.

# PASO 3
# Calcular las predicciones del gasto usando los coeficientes obtenidos en la regresión con la fórmula y^=β0+β1x.
# Nota: recordá que el uso del broadcasting de numpy puede ayudarte.

#PASO 4
# Grafica los puntos (x,y) y la recta obtenida en el mismo plot para verificar su desempeño.
