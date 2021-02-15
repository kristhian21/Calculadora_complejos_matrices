import unittest
import math
import Complex_Vector_Spaces as cL


class TestComplex(unittest.TestCase):

	def test_suma(self):
		c1 = (-7, -4)
		c2 = (3, -5)

		self.assertEqual(cL.sumaComplejos(c1, c2), (-4, -9))

	def test_resta(self):
		c1 = (-3, 4)
		c2 = (3, 8)

		self.assertEqual(cL.restaComplejos(c1, c2), (-6, -4))

	def test_producto(self):
		c1 = (3, -2)
		c2 = (1, 2)

		self.assertEqual(cL.productoComplejos(c1, c2), (7, 4))

	def test_division(self):
		c1 = (-2, 1)
		c2 = (1, 2)

		self.assertEqual(cL.divisionComplejos(c1, c2), 5)

	def test_modulo(self):
		c = (-7, 2)

		self.assertEqual(cL.moduloComplejos(c), 7.28)

	def test_conjugado(self):
		c = (2, 4)

		self.assertEqual(cL.conjugadoComplejos(c), (2, -4))

	def test_cart_polar(self):
		c = (1, 1)

		self.assertEqual(cL.cartesiano_polar(c), (1.414, 45.000))

	def test_polar_cart(self):
		p = (math.sqrt(3), 80)

		self.assertEqual(cL.polar_cartesiano(p), (0.301, 1.706))

	def test_sumaVectores(self):
		v1 = [(-3, 4), (-5, 0), (-6, 8)]
		v2 = [(-1, -1), (3, 5), (-5, 7)]

		self.assertEqual(cL.sumaVectores(v1, v2), [(-4, 3), (-2, 5), (-11, 15)])

	def test_inversoAditivo(self):
		v = [(-3, 4), (-5, 0), (-6, 8)]

		self.assertEqual(cL.inversoAditivo(v), [(3, -4), (5, 0), (6, -8)])

	def test_multiplicacionE(self):
		escalar = (3, 2)
		v1 = [(6, -4), (7, 3), (4.2, -8.1), (0, -3)]

		self.assertEqual(cL.multiplicacionEscalar(escalar, v1), [(26, 0), (15, 23), (28.8, -15.899999999999997), (6, -9)])

	def test_adicionMatrices(self):
		m1 = [[(1, -2), (6, 4), (-8, -1)],
			  [(4, 6), (-2, -4), (9, 8)],
			  [(-10, -5), (2, -3), (2, 7)]]

		m2 = [[(6, 3), (0, 0), (5, 1)],
			  [(2, 4), (-5, 6), (1, 6)],
			  [(4, -4), (-3, -5), (2, 8)]]

		self.assertEqual(cL.adicionMatrices(m1, m2), [[(7, 1), (6, 4), (-3, 0)], [(6, 10), (-7, 2), (10, 14)], [(-6, -9), (-1, -8), (4, 15)]])

	def test_inversoAMatriz(self):
		m1 = [[(1, -2), (6, 4), (-8, -1)],
			  [(4, 6), (-2, -4), (9, 8)],
			  [(-10, -5), (2, -3), (2, 7)]]

		self.assertEqual(cL.inversoAditivo_M(m1), [[(-1, 2), (-6, -4), (8, 1)], [(-4, -6), (2, 4), (-9, -8)], [(10, 5), (-2, 3), (-2, -7)]])

	def test_M_escalarMatriz(self):
		escalar = (3, 2)
		m1 = [[(1, -2), (6, 4), (-8, -1)],
			  [(4, 6), (-2, -4), (9, 8)],
			  [(-10, -5), (2, -3), (2, 7)]]

		self.assertEqual(cL.multiplicacionEscalar_M(escalar, m1), [[(7, -4), (10, 24), (-22, -19)], [(0, 26), (2, -16), (11, 42)], [(-20, -35), (12, -5), (-8, 25)]])

	def test_transpuesta(self):
		m1 = [[(1, -2), (6, 4), (-8, -1)],
			  [(4, 6), (-2, -4), (9, 8)],
			  [(-10, -5), (2, -3), (2, 7)]]

		self.assertEqual(cL.transpuesta(m1), [[(1, -2), (4, 6), (-10, -5)], [(6, 4), (-2, -4), (2, -3)], [(-8, -1), (9, 8), (2, 7)]])

	def test_conjugada(self):
		m1 = [[(1, -2), (6, 4), (-8, -1)],
			  [(4, 6), (-2, -4), (9, 8)],
			  [(-10, -5), (2, -3), (2, 7)]]

		self.assertEqual(cL.conjugada(m1), [[(1, 2), (6, -4), (-8, 1)], [(4, -6), (-2, 4), (9, -8)], [(-10, 5), (2, 3), (2, -7)]])

	def test_adjunta(self):
		m3 = [[(5, 7), (-4, 5), (-7, -8)],
			  [(0, 0), (4, 1), (-1, 8)]]

		self.assertEqual(cL.adjunta(m3), [[(5, -7), (0, 0)], [(-4, -5), (4, -1)], [(-7, 8), (-1, -8)]])

	def test_productoMatrices(self):
		m3 = [[(5, 7), (-4, 5), (-7, -8)],
			  [(0, 0), (4, 1), (-1, 8)]]
		m2 = [[(6, 3), (0, 0), (5, 1)],
			  [(2, 4), (-5, 6), (1, 6)],
			  [(4, -4), (-3, -5), (2, 8)]]

		self.assertEqual(cL.productoMatrices(m3, m2), [[(-79, 47), (-29, 10), (34, -51)], [(32, 54), (17, 0), (-68, 33)]])

	def test_accionMatriz(self):
		m1 = [[(1, -2), (6, 4), (-8, -1)],
			  [(4, 6), (-2, -4), (9, 8)],
			  [(-10, -5), (2, -3), (2, 7)]]
		v2 = [(6, 3), (0, 0), (5, 1)]

		self.assertEqual(cL.accionMatrizVector(m1, v2), [[(-27, -22)], [(43, 97)], [(-42, -23)]])

	def test_productoInterno(self):
		v1 = [(-2, 0), (-6, 4), (4, 8), (-3, -1)]
		v2 = [(0, 0), (-1, 5), (9, -4), (3, 3)]

		self.assertEqual(cL.productoInternoVectores(v1, v2), (18, -120))

	def test_norma(self):
		v = [(-2, 0), (-6, 4), (4, 8), (-3, -1)]

		self.assertEqual(cL.normaVector(v), 12.083045973594572)

	def test_distancia(self):
		v1 = [(-2, 0), (-6, 4), (4, 8), (-3, -1)]
		v2 = [(0, 0), (-1, 5), (9, -4), (3, 3)]

		self.assertEqual(cL.distanciaVectores(v1, v2), 15.84297951775486)

	def test_esUnitaria(self):
		m = [[(1, 3), (0, 5 / 15 ** (1 / 2)), (12, 1)],
			 [(-5, 0), (0, 6), (2 / 2 * (19 ** (1 / 2)), -8 / 2 * (19 ** (1 / 2)))], [(0, -4.5), (20, 0), (2, 1)]]
		self.assertFalse(cL.esUnitaria(m))

	def test_esHermitiana(self):
		m = [[(5, 0), (4, 5), (6, -16)], [(4, -5), (13, 0), (7, 0)], [(6, 16), (7, 0), (-2.1, 0)]]

		self.assertTrue(m)

	def test_productoTensor(self):
		m1 = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
		m2 = [[(1, 0), (3, 4)], [(0, 0), (1, 0)]]

		self.assertEqual(cL.productoTensor(m1, m2), [[(0, 0), (0, 0), (1, 0), (3, 4)],
												  [(0, 0), (0, 0), (0, 0), (1, 0)],
												  [(1, 0), (3, 4), (0, 0), (0, 0)],
												  [(0, 0), (1, 0), (0, 0), (0, 0)]])


if __name__ == '__main__':
	unittest.main()
