import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy.linalg as la

# Cargar los datos
df = pd.read_csv('https://unket.s3-sa-east-1.amazonaws.com/data/mypersonality.csv')
df = df.sample(frac=1).reset_index(drop=True)

# Extraer vectores de personalidad
vectores = np.array([df.loc[k, ['sOPN', 'sCON', 'sEXT', 'sAGR', 'sNEU']].values for k in range(5)])

# Paso 1: Calcular vector promedio
vprom = np.mean(vectores, axis=0)
print("Vector promedio de personalidad:", vprom)

# Paso 2: Función para calcular el ángulo entre vectores
def vector_angle(u, v):
    if np.array_equal(u, v):
        return 0
    else:
        angle = np.arccos(np.dot(u, v) / (la.norm(u) * la.norm(v)))
        return angle

angulo = vector_angle(vectores[0], vectores[2])
print("El ángulo entre los vectores es de:", angulo)

# Paso 3: Calcular todos los ángulos entre los vectores
dimension = len(vectores)
angulos = np.zeros((dimension, dimension))
angulo_menor = (np.pi, 0, 0)

for i in range(dimension):
    for j in range(dimension):
        if i != j:
            angulos[i, j] = vector_angle(vectores[i], vectores[j])
            if angulos[i, j] < angulo_menor[0]:
                angulo_menor = (angulos[i, j], i, j)

print("\nMatriz de ángulos:\n", angulos)
print("\nEl ángulo menor es", angulo_menor[0], "entre los vectores", angulo_menor[1], "y", angulo_menor[2])

# Visualización de la matriz de ángulos
# Gráfico de la matriz de ángulos usando Matplotlib
plt.figure(figsize=(6, 5))
plt.imshow(angulos, cmap="coolwarm", interpolation="nearest")
plt.colorbar(label="Ángulo (radianes)")
plt.xticks(range(len(vectores)), labels=[f"Vec{i}" for i in range(len(vectores))])
plt.yticks(range(len(vectores)), labels=[f"Vec{i}" for i in range(len(vectores))])
plt.title("Ángulos entre vectores de personalidad")

# Anotar valores en la matriz
for i in range(len(vectores)):
    for j in range(len(vectores)):
        plt.text(j, i, f"{angulos[i, j]:.2f}", ha='center', va='center', color="black")

plt.show()
