import unittest
from vectores.desplazamiento import desplazar_cuadrilatero
class TestDesplazamientoCuadrilatero(unittest.TestCase):
    def test_desplazamiento_correcto(self):
        """
        Verifica que las coordenadas del cuadrilátero se desplacen correctamente
        5 unidades hacia arriba y 7 unidades a la izquierda.
        """
        cuadrilatero_original = [(2, 3), (8, 3), (8, 6), (2, 6)]
        esperado = [(-5, 8), (1, 8), (1, 11), (-5, 11)]
        resultado = desplazar_cuadrilatero(cuadrilatero_original)
        self.assertEqual(resultado, esperado, "El desplazamiento no se realizó correctamente")

    def test_desplazamiento_cero(self):
        """
        Verifica que si un cuadrilátero empieza en (0,0), el desplazamiento funcione correctamente.
        """
        cuadrilatero_original = [(0, 0), (4, 0), (4, 4), (0, 4)]
        esperado = [(-7, 5), (-3, 5), (-3, 9), (-7, 9)]
        resultado = desplazar_cuadrilatero(cuadrilatero_original)
        self.assertEqual(resultado, esperado, "El desplazamiento no funciona con coordenadas en el origen")

    def test_no_modifica_entrada(self):
        """
        Verifica que la lista original no sea modificada.
        """
        cuadrilatero_original = [(2, 3), (8, 3), (8, 6), (2, 6)]
        copia_original = cuadrilatero_original[:]
        _ = desplazar_cuadrilatero(cuadrilatero_original)
        self.assertEqual(cuadrilatero_original, copia_original, "La función modifica la lista original")

if __name__ == "__main__":
    unittest.main()