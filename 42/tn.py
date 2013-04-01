import math

class TriangleNumber:
	def number(self, word):
		n = 0
		for i in range(0, len(word)):
			n += ord(word[i]) - 64
		return n

	def inverse (self, t):
		return 0.5*(math.sqrt(8*t+1)-1)
	
	def isTN (self, n):
		i = self.inverse(n)
		return math.trunc(i) == i
	
