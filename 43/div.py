class Divisible:
	def isDivisible (self, n):
		return self.is2D(n) and self.is3D(n) and self.is5D(n) and self.is7D(n) and self.is11D(n) and self.is13D(n) and self.is17D(n)

	def is2D(self, n):
		return int(n[1:4]) % 2 == 0
	
	def is3D(self, n):
		return int(n[2:5]) % 3 == 0
	
	def is5D(self, n):
		return int(n[3:6]) % 5 == 0
	
	def is7D(self, n):
		return int(n[4:7]) % 7 == 0
	
	def is11D(self, n):
		return int(n[5:8]) % 11 == 0
	
	def is13D(self, n):
		return int(n[6:9]) % 13 == 0
	
	def is17D(self, n):
		return int(n[7:10]) % 17 == 0
