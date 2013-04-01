import math

class Pentagon:
	def pn(self, n):
		return n*(3*n-1)/2

	def isPentagon(self, n):
		i = self.inverse(n)
		return math.trunc(i) == i

	def inverse(self, n):
		return 1.0/6.0*(math.sqrt(24.0*n+1.0)+1.0)
