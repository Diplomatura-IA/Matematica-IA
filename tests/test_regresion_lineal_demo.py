import unittest
from vectores.regresion_lineal_demo import regresion_lineal_manual

class TestRegresionLineal(unittest.TestCase):
    def setUp(self):
        # Datos simples con relación lineal perfecta: gasto = 0.01 * PIB
        self.data = {
            "PIB": [1000, 2000, 3000, 4000],
            "Gasto": [10, 20, 30, 40]
        }

    def test_coeficientes(self):
        x, y, y_pred, beta_0, beta_1 = regresion_lineal_manual(self.data, "PIB", "Gasto")
        self.assertAlmostEqual(beta_1, 0.01)
        self.assertAlmostEqual(beta_0, 0.0)

if __name__ == '__main__':
    unittest.main()
