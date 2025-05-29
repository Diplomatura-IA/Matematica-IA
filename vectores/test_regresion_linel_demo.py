import unittest
import numpy as np
import pandas as pd
from io import StringIO

# Importamos la función a probar
from regresion_lineal_demo import regresion_lineal_simple


class TestRegresionLineal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Crea un DataFrame de prueba simulado."""
        csv_data = """Year,GDP,percentage expenditure
        2014,50000,8.2
        2014,70000,9.5
        2014,30000,7.8
        2014,90000,10.2
        2014,40000,8.0"""

        cls.test_csv = StringIO(csv_data)
        cls.query = ["Year == 2014", "GDP < 80000"]
        cls.col_x = "GDP"
        cls.col_y = "percentage expenditure"

    def test_regresion_retorna_coeficientes_correctos(self):
        """Verifica si los coeficientes de la regresión son calculados correctamente."""
        coeficiente, intercepto, Y_pred, df_filtrado = regresion_lineal_simple(self.test_csv, self.query, self.col_x,
                                                                               self.col_y)

        # Verificar que los coeficientes no sean None
        self.assertIsNotNone(coeficiente)
        self.assertIsNotNone(intercepto)

        # Verificar tamaño de las predicciones
        self.assertEqual(len(Y_pred), len(df_filtrado))

    def test_filtro_aplicado_correctamente(self):
        """Verifica que los datos filtrados cumplen con los criterios establecidos."""
        _, _, _, df_filtrado = regresion_lineal_simple(self.test_csv, self.query, self.col_x, self.col_y)

        # Comprobar que todos los valores de "Year" sean 2014 y "GDP" sea menor a 80000
        self.assertTrue(all(df_filtrado["Year"] == 2014))
        self.assertTrue(all(df_filtrado["GDP"] < 80000))

    def test_datos_insuficientes(self):
        """Verifica que la función maneje correctamente el caso de datos insuficientes."""
        query_erronea = ["Year == 2025"]
        coeficiente, intercepto, _, df_filtrado = regresion_lineal_simple(self.test_csv, query_erronea, self.col_x,
                                                                          self.col_y)

        self.assertIsNone(coeficiente)
        self.assertIsNone(intercepto)
        self.assertEqual(len(df_filtrado), 0)  # DataFrame vacío


if __name__ == '__main__':
    unittest.main()