import unittest

from vectores.ortogonalidad import son_ortogonales


class TestOrtogonalidad(unittest.TestCase):

    def test_ortogonales_en_2d(self):
        """
        Verifica verdadero para ortogonal [0, 1] y [1, 0]
        """
        u = [1, 0]
        v = [0, 1]
        t = 1e-10
        self.assertTrue(son_ortogonales(u, v, t,), "Verdadero")

    def test_no_ortogonales(self):
        """
        Verifica falso para ortogonal [1, 2] y [3, 4]
        """
        u = [1, 2]
        v = [3, 4]
        t = 1e-10
        self.assertFalse(son_ortogonales(u, v, t), "Falso")

    def test_casi_ortogonales_con_tolerancia(self):
        """
        Verífica verdadero para casi ortogonal con tolerancia [1, 0.00000000001] y [0, 1]
        """
        u = [1, 0.00000000001]
        v = [0, 1]
        t = 1e-10
        self.assertTrue(son_ortogonales(u, v, t), "Verdadero porque el producto punto ≈ 1e-11")

    def test_casi_ortogonales_fuera_de_tolerancia(self):
        """
        Verífica verdadero para casi ortogonal con tolerancia [1, 0.001] y [0, 1]
        """
        u = [1, 0.001]
        v = [0, 1]
        t = 1e-10
        self.assertFalse(son_ortogonales(u, v, t), "Falso porque 0.001 > tolerancia")
