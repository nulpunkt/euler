import unittest
from pandigital import *

class PandigitalTest(unittest.TestCase):
	def test_findnext(self):
		p = Pandigital()
		print p.find_next(192384576, 3)

	def test_is_pandigital(self):
		p = Pandigital()
		self.assertTrue(p.is_pandigital(192384576, 3))
		self.assertFalse(p.is_pandigital(192384576, 2))
		self.assertTrue(p.is_pandigital(918273645, 1))
	
if __name__ == '__main__':
	unittest.main()
