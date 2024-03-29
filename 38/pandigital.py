class Pandigital:
	def is_pandigital(self, test, n):
		first = self.first(test, n)
		remaining = self.remaining(test, n)
		i = 2
		while self.len(remaining) > 0:
			if self.c(first, i, remaining):
				remaining = self.remaining(remaining, self.len(first*i))
				i = i+1
			else:
				return False
		return True

	def c(self, first, n, remaining):
		return str(remaining).find(str(first*n)) == 0
	
	def find_next(self, match, remaning):
		return True
	
	def sub(self, test, offset, i):
		return int(str(test)[offset:offset+i])

	def remaining(self, test, offset):
		if self.len(test) == offset:
			return ''
		return int(str(test)[offset:])

	def first(self, test, n):
		return self.sub(test, 0, n)

	def len(self, i):
		if i == '':
			return 0
		else:
			return len(str(i))
