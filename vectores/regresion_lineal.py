import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
pd.set_option('display.max_rows', None)  # Mostrar todas las filas
pd.set_option('display.width', 1000)  # Aumentar el ancho de salida
pd.set_option('display.colheader_justify', 'center')  # Mejor alineación

data = pd.read_csv("Life Expectancy Data.csv")
print(data.shape)
print(data.head(2938))
output_file = "data_filtered.txt"
data.to_csv(output_file, sep="\t", index=False)

print(f"Datos guardados en {output_file}")
# data2=data.query("Year == 2014")
# data2=data.query("Country == 'Argentina'")
# data2=data2.query("GDP < 80000")
# data2=data2.query("`percentage expenditure` != 0")
# data2 = data2.loc[:,["Country","percentage expenditure","GDP"]]
# print(data2.shape)
# print(data2.head(2938))


# gasto = data2.loc[:,"percentage expenditure"]
# pbi = data2.loc[:,"GDP"]
# plt.scatter(pbi,gasto)
# plt.show()
