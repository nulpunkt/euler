import unittest
from pandigital import *

class PandigitalTest(unittest.TestCase):
	def test_findnext(self):
		p = Pandigital()
		print p.find_next(192384576, 3)

if __name__ == '__main__':
	unittest.main()
