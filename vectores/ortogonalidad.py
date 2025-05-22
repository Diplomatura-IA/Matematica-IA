import numpy as np


# Definir una función en python que detecte si dos vectores son ortogonales
def son_ortogonales(u, v, t):
    """
    Determina si dos vectores son ortogonales. se agrega la
    tolerancia (0.0000000001)
    :param u: List o tuple con los componentes del primer vector.
    :param v: List o tuple con los componentes del segundo vector.
    :param t: Tolerancia (0.0000000001) para redondear lo más cercano a cero
    :return: True si son ortogonales, False en caso contrario.
    """
    # Calculo el producto punto
    producto_punto = np.dot(u, v)
    print(f"Producto punto = {producto_punto}")
    # Verifico si el producto escalar es cercano a cero dentro del margen de tolerancia
    result = np.abs(producto_punto) < t
    return result


tolerancia = 1e-10
vector_u = [1, 2, -1]
vector_v = [2, -1, 1]

print(son_ortogonales(vector_u, vector_v, tolerancia))
