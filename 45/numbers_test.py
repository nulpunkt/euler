import unittest
from numbers import *

class NumbersTest(unittest.TestCase):
	def test_direct(self):
		n = Number()
		self.assertEquals(40755, n.triangle(285))
		self.assertEquals(40755, n.pentagonal(165))
		self.assertEquals(40755, n.hexagonal(143))

	def test_inverse(self):
		n = Number()
		self.assertEquals(285, n.triangle_inverse(40755))
		self.assertEquals(165, n.pentagonal_inverse(40755))
		self.assertEquals(143, n.hexagonal_inverse(40755))
	
	def test_isX(self):
		n = Number()
		self.assertTrue(n.isPantagonal(40755))
		self.assertFalse(n.isPantagonal(40752))
		
		self.assertTrue(n.isHexagonal(40755))
		self.assertFalse(n.isHexagonal(41755))

if __name__ == '__main__':
	unittest.main()

