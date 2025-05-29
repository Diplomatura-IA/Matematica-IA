import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def regresion_lineal_simple(csv_file, query, col_x, col_y):
    """
    Lee un archivo CSV como data frame, aplica filtros y calcula la regresión lineal entre dos columnas.
    Parámetros:
    - csv_file: STR Ruta del archivo CSV.
    - filtros: Lista de condiciones en formato string para `query()`. Ejemplo: ["Year == 2014", "GDP < 80000"]
    - columna_x: Nombre de la columna independiente.
    - columna_y: Nombre de la columna dependiente.

    Retorna:
    - Coeficiente de regresión, intercepto y DataFrame filtrado.
    """
    # Cargar datos
    data_frame = pd.read_csv(csv_file)

    # Aplicar filtros dinámicos
    for condicion in query:
        data_frame = data_frame.query(condicion)

    # Eliminar valores nulos
    data_frame = data_frame.dropna(subset=[col_x, col_y])

    # Verificar tamaño de datos después de filtrado
    if data_frame.shape[0] == 0:
        print("Error: No hay suficientes datos después de aplicar los filtros.")
        return None, None, data_frame

    # Transformar en arrays de numpy
    x = data_frame[col_x].values
    y = data_frame[col_y].values
    # print(x,y)

    # Calcular la regresión lineal usando numpy
    x_media, y_media = np.mean(x), np.mean(y)
    print(x_media, y_media)
    b1 = np.sum((x - x_media) * (y - y_media)) / np.sum((x - x_media) ** 2)
    b0 = y_media - b1 * x_media

    # Calcular las predicciones
    y_pred = b0 + b1 * x

    return b1, b0, y_pred, data_frame


def graficar_regresion(df, col_x, col_y, y_pred):
    """
    Grafica los datos filtrados y la línea de regresión lineal.
    Parámetros:
    - df: DataFrame filtrado.
    - columna_x: Nombre de la columna independiente.
    - columna_y: Nombre de la columna dependiente.
    - coef: Coeficiente de la regresión.
    - intercepto: Intercepto de la regresión.
    - Y_pred: Predicciones de la regresión lineal.
    """
    x = df[col_x].values
    y = df[col_y].values

    # Creo el gráfico
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.7, edgecolors="k", label="Datos originales")
    plt.plot(x, y_pred, color='red', label="Regresión Lineal")

    # Etiquetas y título del grafico
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.title(f"Regresión Lineal de {col_y} vs {col_x}")
    plt.legend()
    plt.grid()
    plt.show()


# Ejemplo del Colab (buscar otros ejemplos)
csv_path = "Life Expectancy Data.csv"
filtros = ["Year == 2014", "GDP < 80000", "`percentage expenditure` != 0"]
columna_x = "GDP"
columna_y = "percentage expenditure"

# Ejecuto la regresión
coeficiente, intercepto, Y_pred, df_filtrado = regresion_lineal_simple(csv_path, filtros, columna_x, columna_y)

# Verifico que el coeficiente no devuelva none
if coeficiente is not None:
    print(f"Coeficiente β1: {coeficiente}, Intercepto β0: {intercepto}")
    graficar_regresion(df_filtrado, columna_x, columna_y, Y_pred)
else:
    print(coeficiente)
