import math

class Number:
	def triangle(self, n):
		return n*(n+1)/2
	def triangle_inverse(self, n):
		return (math.sqrt(8*n+1)-1)/2

	def pentagonal(self, n):
		return n*(3*n-1)/2
	def pentagonal_inverse(self, n):
		return (math.sqrt(24*n+1)+1)/6
	def isPantagonal(self, n):
		return self.isWhole(self.pentagonal_inverse(n))

	def hexagonal(self, n):
		return n*(2*n-1)
	def hexagonal_inverse(self, n):
		return (math.sqrt(8*n+1)+1)/4
	def isHexagonal(self, n):
		return self.isWhole(self.hexagonal_inverse(n))

	def isWhole(self, n):
		return n%1 == 0
