import matplotlib.pyplot as plt


def desplazar_cuadrilatero(esquinas):
    """
    Desplaza las cuatro esquinas de un cuadrilátero 5 unidades hacia arriba y 7 unidades a la izquierda.
    :param esquinas: Lista de tuplas, cada una representando una esquina (x, y).
    :return: Lista de tuplas con las nuevas coordenadas después del desplazamiento.
    """
    desplazamiento_x = -7  # Mueve hacia la izquierda
    desplazamiento_y = 5  # Mueve hacia arriba
    # Comprención de lista
    nuevas_esquinas = [(x + desplazamiento_x, y + desplazamiento_y) for x, y in esquinas]
    print(nuevas_esquinas)
    return nuevas_esquinas


def plotear_cuadrilatero(original, desplazado):
    """
    Grafica el cuadrilátero antes y después del desplazamiento.
    :param original: Lista de tuplas con las coordenadas originales.
    :param desplazado: Lista de tuplas con las coordenadas desplazadas.
    """
    # Extraer coordenadas originales
    x_orig, y_orig = zip(*original)
    x_orig += (x_orig[0],)  # Cierra el cuadrilátero
    y_orig += (y_orig[0],)

    # Extraer coordenadas desplazadas
    x_despl, y_despl = zip(*desplazado)
    x_despl += (x_despl[0],)
    y_despl += (y_despl[0],)

    # Graficar cuadriláteros
    plt.figure(figsize=(6, 6))
    plt.plot(x_orig, y_orig, "bo-", label="Original")  # Azul para el cuadrilátero original
    plt.plot(x_despl, y_despl, "ro-", label="Desplazado")  # Rojo para el cuadrilátero desplazado
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Desplazamiento de Cuadrilátero")
    plt.legend()
    plt.grid(True)
    plt.show()


# Definir cuadrilátero original
cuadrilatero = [(2, 3), (8, 3), (8, 6), (2, 6)]
print(cuadrilatero)
nuevas_coordenadas = desplazar_cuadrilatero(cuadrilatero)

# Plotear
plotear_cuadrilatero(cuadrilatero, nuevas_coordenadas)
