import unittest

from vectores.ortogonalidad import son_ortogonales


class TestOrtogonalidad(unittest.TestCase):

    def test_ortogonales_en_2d(self):
        u = [1, 0]
        v = [0, 1]
        t = 1e-10
        self.assertTrue(son_ortogonales(u, v, t))

    def test_no_ortogonales(self):
        u = [1, 2]
        v = [3, 4]
        t = 1e-10
        self.assertFalse(son_ortogonales(u, v, t))

    def test_casi_ortogonales_con_tolerancia(self):
        u = [1, 0.00000000001]
        v = [0, 1]
        t = 1e-10
        self.assertTrue(son_ortogonales(u, v, t))  # porque el producto punto ≈ 1e-11

    def test_casi_ortogonales_fuera_de_tolerancia(self):
        u = [1, 0.001]
        v = [0, 1]
        t = 1e-10
        self.assertFalse(son_ortogonales(u, v, t))  # porque 0.001 > tolerancia
